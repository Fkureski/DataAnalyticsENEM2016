from pathlib import Path

# Caminhos
DATA_PATH = Path("data/microdados_enem_2016.csv")
OUT_DIR = Path("outputs")
FIG_DIR = OUT_DIR / "figures"
REP_DIR = OUT_DIR / "reports"

# Colunas de interesse
NUM_COLS_BASE = [
    "NU_IDADE",
    "NU_NOTA_CN", "NU_NOTA_CH", "NU_NOTA_LC",
    "NU_NOTA_MT", "NU_NOTA_REDACAO"
]

CAT_COLS_BASE = [
    "TP_SEXO", "TP_COR_RACA",
    "TP_ESCOLA", "TP_DEPENDENCIA_ADM_ESC",
    "Q001", "Q002", "Q006"
]

# “Target” principais (se não houver História específica, usamos CH como proxy)
TARGETS = {
    "matematica": "NU_NOTA_MT",
    "redacao": "NU_NOTA_REDACAO",
    # algumas versões não têm NU_NOTA_HISTORIA; caímos para CH
    "historia_ou_ch": "NU_NOTA_HISTORIA"
}

# Quantas variáveis usar na Univariada (rubrica pede 10)
UNIVARIATE_COLUMNS = [
    "NU_IDADE","NU_NOTA_MT","NU_NOTA_REDACAO","NU_NOTA_CH","NU_NOTA_CN",
    "NU_NOTA_LC","Q006","Q001","Q002","TP_DEPENDENCIA_ADM_ESC"
]
