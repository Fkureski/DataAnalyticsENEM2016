import logging
import pandas as pd
from .config import DATA_PATH, NUM_COLS_BASE, CAT_COLS_BASE, OUT_DIR
from .utils import ensure_dirs

def read_raw_csv(path=DATA_PATH) -> pd.DataFrame:
    logging.info(f"Lendo dataset de: {path}")
    # engine=python permite sep=None (detecção heurística)
    df = pd.read_csv(
        path,
        sep=None, engine="python",
        thousands=".", decimal=",",
        na_values=["", "NA", "NaN", "nan", "NULL", "None"]
    )
    logging.info(f"Linhas: {len(df):,}  |  Colunas: {len(df.columns):,}")
    return df

def basic_select_and_types(df: pd.DataFrame) -> pd.DataFrame:
    cols = [c for c in NUM_COLS_BASE + CAT_COLS_BASE if c in df.columns]
    sub = df[cols].copy()
    # Coerção numérica nas notas/idade (erros -> NaN)
    numeric_cols = [c for c in NUM_COLS_BASE if c in sub.columns]
    for c in numeric_cols:
        sub[c] = pd.to_numeric(sub[c], errors="coerce")
    return sub

def filter_present_in_main_targets(df: pd.DataFrame) -> pd.DataFrame:
    # precisamos de notas válidas em MT e REDAÇÃO; em História usamos NU_NOTA_HISTORIA se existir,
    # senão usamos CH como substituto.
    need = ["NU_NOTA_MT","NU_NOTA_REDACAO"]
    for c in need:
        if c in df.columns:
            df = df[df[c].notna()]
    # História
    hist_col = "NU_NOTA_HISTORIA" if "NU_NOTA_HISTORIA" in df.columns else "NU_NOTA_CH"
    df = df[df[hist_col].notna()]
    df = df.assign(NOTA_HISTORIA_REF=df.get("NU_NOTA_HISTORIA", df["NU_NOTA_CH"]))
    return df

def filter_valid_candidates(df: pd.DataFrame) -> pd.DataFrame:
    df = df[df["IN_TREINEIRO"] == 0]
    df = df[df["TP_PRESENCA_MT"] == 1]
    df = df[df["TP_PRESENCA_CH"] == 1]
    df = df[df["TP_STATUS_REDACAO"] == 1]
    return df

def run_etl() -> pd.DataFrame:
    ensure_dirs(OUT_DIR)
    df = read_raw_csv()
    df = basic_select_and_types(df)
    df = filter_present_in_main_targets(df)
    df = filter_valid_candidates(df)
    logging.info(f"Após ETL: {df.shape[0]:,} linhas e {df.shape[1]} colunas.")
    return df
