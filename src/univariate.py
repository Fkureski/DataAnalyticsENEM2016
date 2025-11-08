import logging
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from .config import UNIVARIATE_COLUMNS, FIG_DIR, REP_DIR
from .utils import ensure_dirs

def describe_series(s: pd.Series) -> dict:
    s_clean = s.dropna()
    mode_vals = s_clean.mode(dropna=True)
    mode = mode_vals.iloc[0] if not mode_vals.empty else np.nan
    return {
        "mean": float(s_clean.mean()),         # média
        "median": float(s_clean.median()),     # mediana
        "mode": float(mode),                   # moda
        "std": float(s_clean.std(ddof=1)),     # desvio padrão
        "p25": float(s_clean.quantile(0.25)),  # percentis
        "p50": float(s_clean.quantile(0.50)),
        "p75": float(s_clean.quantile(0.75)),
        "min": float(s_clean.min()),
        "max": float(s_clean.max())
    }

def plot_histogram(s: pd.Series, name: str):
    plt.figure()
    plt.hist(s.dropna().values, bins=30)
    plt.title(f"Histograma - {name}")
    plt.xlabel(name)
    plt.ylabel("Frequência")
    plt.tight_layout()
    plt.savefig(FIG_DIR / f"hist_{name}.png", dpi=150)
    plt.close()

def run_univariate(df: pd.DataFrame) -> pd.DataFrame:
    ensure_dirs(FIG_DIR, REP_DIR)
    cols = [c for c in UNIVARIATE_COLUMNS if c in df.columns]
    logging.info(f"Univariada em {len(cols)} variáveis: {cols}")
    rows = []
    for c in cols:
        d = describe_series(df[c])
        d["variable"] = c
        rows.append(d)
        if pd.api.types.is_numeric_dtype(df[c]):
            plot_histogram(df[c], c)
    out = pd.DataFrame(rows).set_index("variable")
    out.to_csv(REP_DIR / "univariate_stats.csv", index=True)
    logging.info("Univariada finalizada (estatísticas + histogramas).")
    return out
