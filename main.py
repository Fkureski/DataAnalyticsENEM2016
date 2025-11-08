import logging
from src.utils import setup_logging
from src import etl, univariate, multivariate, visualizations
from src.config import OUT_DIR

def main():
    setup_logging()
    logging.info("==== ENEM 2016 — Pipeline de Análise ====")

    # ETL: Carregar e limpar os dados
    df = etl.run_etl()

    # 1) Análise Univariada: Estatísticas e histogramas para 10 variáveis
    univ = univariate.run_univariate(df)
    logging.info(f"Univariada (amostra):\n{univ.head(3)}")

    # 2) Análise Multivariada: Correlação de Pearson
    corr = multivariate.run_pearson(df)
    multivariate.top_correlations_with_targets(
        corr, targets=[c for c in ["NU_NOTA_MT","NU_NOTA_REDACAO","NU_NOTA_HISTORIA","NU_NOTA_CH"] if c in corr.columns]
    )

    # 3) Visualizações: Gráficos exploratórios e explicativos
    visualizations.run_visuals(df)

    # Exibir mensagens finais
    logging.info(f"Arquivos prontos em: {OUT_DIR.resolve()}")

if __name__ == "__main__":
    main()
