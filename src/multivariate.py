import logging
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from .config import FIG_DIR, REP_DIR

def run_pearson(df: pd.DataFrame, focus_cols=None) -> pd.DataFrame:
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

def top_correlations_with_targets(corr: pd.DataFrame, targets: list, k: int = 8) -> pd.DataFrame:
    rows = []
    for t in targets:
        if t not in corr.columns:
            continue
        s = corr[t].drop(index=t, errors="ignore").dropna().sort_values(key=lambda x: x.abs(), ascending=False)
        topk = s.head(k)
        for feat, val in topk.items():
            rows.append({"target": t, "feature": feat, "pearson": float(val)})
    out = pd.DataFrame(rows)
    out.to_csv(REP_DIR / "top_correlations.csv", index=False)
    return out
