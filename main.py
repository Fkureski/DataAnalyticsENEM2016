import logging
from src.utils import setup_logging
from src import etl, univariate, multivariate, visualizations, modeling
from src.config import OUT_DIR

def main():
    setup_logging()
    logging.info("==== ENEM 2016 — Pipeline de Análise ====")
    df = etl.run_etl()

    # 1) Univariada (10 variáveis + histogramas)
    univ = univariate.run_univariate(df)
    logging.info(f"Univariada (amostra):\n{univ.head(3)}")

    # 2) Multivariada (correlação de Pearson + top relações)
    corr = multivariate.run_pearson(df)
    multivariate.top_correlations_with_targets(
        corr, targets=[c for c in ["NU_NOTA_MT","NU_NOTA_REDACAO","NU_NOTA_HISTORIA","NU_NOTA_CH"] if c in corr.columns]
    )

    # 3) Visualizações (exploratória + explicativa + extra)
    visualizations.run_visuals(df)

    # 4) Regressão (3 modelos)
    modeling.run_modeling(df)

    logging.info(f"Arquivos prontos em: {OUT_DIR.resolve()}")

if __name__ == "__main__":
    main()
