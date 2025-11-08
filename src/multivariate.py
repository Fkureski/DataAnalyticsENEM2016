import logging
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from .config import FIG_DIR, REP_DIR

def run_pearson(df: pd.DataFrame) -> pd.DataFrame:
    num_df = df.select_dtypes(include=[np.number]).copy()
    corr = num_df.corr(method="pearson")
    corr.to_csv(REP_DIR / "pearson_corr.csv")
    # Heatmap simples (matplotlib puro)
    plt.figure(figsize=(8,6))
    im = plt.imshow(corr.values, aspect="auto")
    plt.colorbar(im, fraction=0.046, pad=0.04)
    plt.xticks(range(corr.shape[1]), corr.columns, rotation=90)
    plt.yticks(range(corr.shape[0]), corr.index)
    plt.title("Matriz de Correlação de Pearson")
    plt.tight_layout()
    plt.savefig(FIG_DIR / "pearson_heatmap.png", dpi=160)
    plt.close()
    logging.info("Correlação de Pearson calculada e salva.")
    return corr
