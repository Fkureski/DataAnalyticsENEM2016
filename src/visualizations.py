import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from .config import FIG_DIR

def box_by_category(df: pd.DataFrame, value_col: str, cat_col: str, title: str):
    data = [df.loc[df[cat_col]==cat, value_col].dropna().values for cat in df[cat_col].dropna().unique()]
    labels = [str(c) for c in df[cat_col].dropna().unique()]
    plt.figure(figsize=(7,5))
    plt.boxplot(data, labels=labels, showmeans=True)
    plt.title(title)
    plt.xlabel(cat_col)
    plt.ylabel(value_col)
    plt.tight_layout()
    plt.savefig(FIG_DIR / f"box_{value_col}_by_{cat_col}.png", dpi=160)
    plt.close()

def scatter_with_trend(df: pd.DataFrame, xcol: str, ycol: str, title: str):
    x = df[xcol].dropna()
    y = df[ycol].dropna()
    df_xy = pd.concat([x,y], axis=1).dropna()
    xv = df_xy[xcol].values
    yv = df_xy[ycol].values
    # reta de tendência (OLS simples)
    b1, b0 = np.polyfit(xv, yv, 1)
    yhat = b1*xv + b0
    plt.figure(figsize=(6,5))
    plt.scatter(xv, yv, s=8, alpha=0.4)
    plt.plot(xv, yhat, linewidth=2)
    plt.title(title)
    plt.xlabel(xcol)
    plt.ylabel(ycol)
    plt.tight_layout()
    plt.savefig(FIG_DIR / f"scatter_{xcol}_vs_{ycol}.png", dpi=160)
    plt.close()

def bar_mean_by_category(df: pd.DataFrame, value_col: str, cat_col: str, title: str):
    mean_table = df.groupby(cat_col, dropna=True)[value_col].mean().sort_values(ascending=False)
    plt.figure(figsize=(7,5))
    plt.bar(mean_table.index.astype(str), mean_table.values)
    plt.title(title)
    plt.xlabel(cat_col)
    plt.ylabel(f"Média de {value_col}")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig(FIG_DIR / f"bar_mean_{value_col}_by_{cat_col}.png", dpi=160)
    plt.close()

def run_visuals(df: pd.DataFrame):
    # 1) exploratória (distribuição por categoria)
    if {"NU_NOTA_MT","Q006"}.issubset(df.columns):
        box_by_category(df, "NU_NOTA_MT", "Q006", "Exploratória: NU_NOTA_MT por faixas de renda (Q006)")
    # 2) explicativa (relação forte entre duas notas)
    if {"NU_NOTA_MT","NU_NOTA_LC"}.issubset(df.columns):
        scatter_with_trend(df, "NU_NOTA_MT", "NU_NOTA_LC", "Explicativa: Relação NU_NOTA_MT vs NU_NOTA_LC")
    # 3) extra (barras da média por tipo de escola)
    if {"NU_NOTA_REDACAO","TP_DEPENDENCIA_ADM_ESC"}.issubset(df.columns):
        bar_mean_by_category(df, "NU_NOTA_REDACAO", "TP_DEPENDENCIA_ADM_ESC",
                             "Média de Redação por Dependência Administrativa")
