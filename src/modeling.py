import json
import logging
import numpy as np
import pandas as pd
from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.neighbors import KNeighborsRegressor

from .config import REP_DIR, CAT_COLS_BASE, NUM_COLS_BASE

def _build_preprocessor(num_cols, cat_cols):
    num_pipe = Pipeline([
        ("imputer", SimpleImputer(strategy="median"))
    ])
    cat_pipe = Pipeline([
        ("imputer", SimpleImputer(strategy="most_frequent")),
        ("onehot", OneHotEncoder(handle_unknown="ignore", sparse_output=False))
    ])
    return ColumnTransformer([
        ("num", num_pipe, num_cols),
        ("cat", cat_pipe, cat_cols)
    ])

def _metrics(y_true, y_pred):
    r2 = r2_score(y_true, y_pred)
    mae = mean_absolute_error(y_true, y_pred)
    rmse = mean_squared_error(y_true, y_pred, squared=False)
    return {"r2": float(r2), "mae": float(mae), "rmse": float(rmse)}

def _fit_and_eval(df: pd.DataFrame, target: str, models: dict) -> pd.DataFrame:
    # garante que target exista; se não, usa CH para "história"
    ycol = target
    if target == "NU_NOTA_HISTORIA" and "NU_NOTA_HISTORIA" not in df.columns:
        ycol = "NU_NOTA_CH"
    use_cols = list({*(NUM_COLS_BASE+CAT_COLS_BASE)})  # evita repetidos
    use_cols = [c for c in use_cols if c in df.columns and c != ycol]
    X = df[use_cols].copy()
    y = pd.to_numeric(df[ycol], errors="coerce")
    Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.2, random_state=42)

    num_cols = Xtr.select_dtypes(include=[np.number]).columns.tolist()
    cat_cols = [c for c in Xtr.columns if c not in num_cols]
    pre = _build_preprocessor(num_cols, cat_cols)

    rows = []
    for name, model in models.items():
        pipe = Pipeline([("prep", pre), ("model", model)])
        pipe.fit(Xtr, ytr)
        pred = pipe.predict(Xte)
        m = _metrics(yte, pred)
        m.update({"model": name, "target": ycol})
        rows.append(m)
    return pd.DataFrame(rows)

def run_modeling(df: pd.DataFrame):
    models = {
        "LinearRegression": LinearRegression(n_jobs=None),  # simples e transparente
        "RandomForest": RandomForestRegressor(n_estimators=200, random_state=42),
        "KNN": KNeighborsRegressor(n_neighbors=7)
    }
    targets = ["NU_NOTA_MT", "NU_NOTA_REDACAO", "NU_NOTA_HISTORIA"]  # CH caso HIST não exista

    all_results = []
    for t in targets:
        res = _fit_and_eval(df, t, models)
        all_results.append(res)

    out = pd.concat(all_results, ignore_index=True)
    REP_DIR.mkdir(parents=True, exist_ok=True)
    out.to_csv(REP_DIR / "modeling_results.csv", index=False)
    logging.info("Modelagem finalizada; métricas salvas em reports/modeling_results.csv")
    # Também salva um JSON resumido por target -> melhor nota
    best = (out.sort_values(["target","r2"], ascending=[True, False])
               .groupby("target").head(1))
    (REP_DIR / "best_models.json").write_text(json.dumps(best.to_dict(orient="records"), indent=2, ensure_ascii=False))
    return out
