# ENEM 2016 – Análise de Dados e Modelagem

## 1. Descrição do Dataset

O dataset utilizado neste projeto é referente ao **ENEM 2016** e foi obtido na plataforma Kaggle. Ele contém informações de todos os participantes da prova, incluindo dados sociodemográficos, desempenho nas provas e respostas a um questionário socioeconômico.

### Principais Grupos de Variáveis:
- **Dados sociodemográficos:**
  - Idade (`NU_IDADE`)
  - Sexo (`TP_SEXO`)
  - Cor/Raça (`TP_COR_RACA`)
  - Escolaridade dos pais (`Q001`, `Q002`)
  - Renda familiar (`Q006`)

- **Informações escolares:**
  - Tipo de escola de ensino médio (`TP_ESCOLA`)
  - Dependência administrativa da escola (`TP_DEPENDENCIA_ADM_ESC`)
  
- **Notas nas provas:**
  - Nota de Ciências da Natureza (`NU_NOTA_CN`)
  - Nota de Ciências Humanas (`NU_NOTA_CH`)
  - Nota de Linguagens e Códigos (`NU_NOTA_LC`)
  - Nota de Matemática (`NU_NOTA_MT`)
  - Nota de Redação (`NU_NOTA_REDACAO`)
  - Nota de História (`NU_NOTA_HISTORIA`)

- **Questionário socioeconômico:**
  - Várias perguntas sobre as condições socioeconômicas dos participantes (variáveis de Q001 a Q050).

## 2. Problema

O objetivo deste projeto é investigar quais fatores influenciam as notas nas provas de **História**, **Matemática** e **Redação** no ENEM 2016. Para isso, será analisado o impacto de variáveis sociodemográficas, informações escolares e desempenho nas outras provas (Ciências da Natureza, Linguagens e Códigos) no desempenho nessas disciplinas.

### Questões principais:
- Quais variáveis mais impactam a nota de **Matemática**, **História** e **Redação**?
- Existe correlação entre as notas de diferentes matérias?
- Podemos construir modelos preditivos para essas notas a partir das variáveis disponíveis?

## 3. ETL / ELT

### Passos principais:
- **Leitura do dataset bruto**: O dataset será carregado e inspecionado.
- **Seleção de colunas relevantes**: Será realizada uma seleção de variáveis de interesse (como idade, sexo, notas e questionário socioeconômico).
- **Filtragem de candidatos presentes em todas as provas**: Apenas participantes com notas nas 3 provas de interesse (Matemática, História e Redação) serão selecionados.
- **Tratamento de valores ausentes**: Valores ausentes nas variáveis relevantes serão tratados.
- **Criação de variáveis numéricas**: Variáveis categóricas (como escolaridade dos pais e renda) serão convertidas para formato numérico, quando necessário.

## 4. Análise Univariada

Será realizada uma análise descritiva das variáveis numéricas e categóricas selecionadas. Para isso, serão calculadas as seguintes estatísticas para **10 variáveis**:
- **Média, Mediana, Moda**
- **Desvio Padrão**
- **Percentis (25, 50, 75)**
- **Histogramas / distribuições** para variáveis como idade, notas e renda.

## 5. Análise Multivariada

### Passos principais:
- **Codificação de variáveis categóricas**: Variáveis como a escolaridade dos pais e tipo de escola serão codificadas para facilitar a análise.
- **Matriz de correlação de Pearson**: A correlação entre as variáveis numéricas será analisada, com foco nas notas de **Matemática**, **História** e **Redação**.
- **Interpretação das principais relações**: Serão destacadas as relações mais significativas, como a correlação entre notas e variáveis sociodemográficas.

## 6. Visualizações

Serão gerados gráficos para facilitar a interpretação dos dados e das correlações encontradas:
- **Gráficos exploratórios**: Explorando as distribuições de notas e variáveis sociodemográficas.
- **Gráficos explicativos**: Mostrando relações entre as variáveis, como o impacto da renda e da escolaridade dos pais nas notas de **Matemática**, **História** e **Redação**.

## 7. Modelagem (Regressão)

### Passos principais:
- **Definição do target**: O objetivo será prever a nota de **Matemática**, **História** e **Redação** com base nas variáveis disponíveis.
- **Engenharia de atributos**: Serão criados novos atributos para melhorar a previsão.
- **Aplicação de modelos de regressão**: Serão aplicados pelo menos 3 modelos de regressão, como **Regressão Linear**, **Random Forest** e **K-Nearest Neighbors (KNN)**.
- **Comparação de métricas**: Serão comparadas as métricas de desempenho (R², MAE, RMSE) dos modelos aplicados.

## 8. Conclusão

- **Principais achados descritivos**: Resumo dos resultados da análise univariada e multivariada.
- **Principais relações multivariadas**: Conclusões sobre as correlações encontradas entre as variáveis.
- **Desempenho dos modelos de regressão**: Comparação entre os modelos preditivos.
- **Limitações e possíveis extensões**: Considerações sobre as limitações do modelo e possíveis melhorias para um futuro trabalho.
