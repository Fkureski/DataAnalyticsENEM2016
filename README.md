# ENEM 2016 – Análise de Dados e Modelagem

## 1. Descrição do Dataset

O dataset utilizado neste projeto é referente ao **ENEM 2016** e foi obtido na plataforma Kaggle. Ele contém informações de todos os participantes da prova, incluindo dados sociodemográficos, desempenho nas provas e respostas a um questionário socioeconômico.

Após um processo de **ETL/ELT**, o arquivo original (~5.6 GB) foi reduzido para um arquivo filtrado (~1 GB), contendo apenas as colunas relevantes para este estudo.

### Principais grupos de variáveis utilizadas

- **Dados sociodemográficos:**
  - Idade (`NU_IDADE`)
  - Sexo (`TP_SEXO`)
  - Cor/Raça (`TP_COR_RACA`)
  - Estado de residência (`SG_UF_RESIDENCIA`)
  - Escolaridade do pai (`Q001`)
  - Escolaridade da mãe (`Q002`)
  - Renda familiar (`Q006`)

- **Informações escolares:**
  - Tipo de escola de ensino médio (`TP_ESCOLA`)
  - Dependência administrativa da escola (`TP_DEPENDENCIA_ADM_ESC`)

- **Notas nas provas:**
  - Nota de Ciências da Natureza (`NU_NOTA_CN`)
  - Nota de Ciências Humanas (`NU_NOTA_CH`) – área que inclui História
  - Nota de Linguagens e Códigos (`NU_NOTA_LC`)
  - Nota de Matemática (`NU_NOTA_MT`)
  - Nota de Redação (`NU_NOTA_REDACAO`)

- **Questionário socioeconômico:**
  - Variáveis de contexto familiar e econômico (`Q001`, `Q002`, `Q006`).

---

## 2. Problema

O objetivo deste projeto é investigar quais fatores influenciam as notas nas provas de **Matemática**, **Redação** e **Ciências Humanas** (que engloba História, Geografia, Sociologia, etc.) no ENEM 2016.

Além disso, busca-se entender como o desempenho varia de acordo com:
- **Região/estado de residência** (`SG_UF_RESIDENCIA`)
- **Sexo** (`TP_SEXO`)
- **Tipo de escola** (`TP_ESCOLA`)
- **Idade** (`NU_IDADE`)
- **Variáveis socioeconômicas** (escolaridade dos pais e renda familiar).

### Questões principais

- Quais variáveis mais impactam a nota de **Matemática**, **Redação** e **Ciências Humanas (NU_NOTA_CH)**?
- Existe correlação entre as notas de diferentes matérias?
- Há diferenças de desempenho entre:
  - alunos de escolas públicas e privadas?
  - homens e mulheres?
  - estados/regiões diferentes?
- Podemos construir modelos preditivos para essas notas a partir das variáveis disponíveis?

---

## 3. ETL / ELT

### Passos principais

1. **Leitura do dataset bruto**  
   - Leitura do arquivo original do ENEM 2016 em chunks, devido ao tamanho (~5.6 GB).

2. **Seleção de colunas relevantes**  
   - Manutenção apenas das colunas necessárias para o escopo definido:
     - Identificação e residência: `NU_INSCRICAO`, `SG_UF_RESIDENCIA`
     - Perfil sociodemográfico: `NU_IDADE`, `TP_SEXO`, `TP_COR_RACA`
     - Escola: `TP_ESCOLA`, `TP_DEPENDENCIA_ADM_ESC`
     - Notas das provas: `NU_NOTA_CN`, `NU_NOTA_CH`, `NU_NOTA_LC`, `NU_NOTA_MT`, `NU_NOTA_REDACAO`
     - Socioeconômicas: `Q001`, `Q002`, `Q006`

3. **Filtragem de candidatos presentes nas provas de interesse**  
   - Manter apenas participantes com notas em:
     - `NU_NOTA_MT` (Matemática),
     - `NU_NOTA_REDACAO` (Redação),
     - `NU_NOTA_CH` (Ciências Humanas).

4. **Tratamento de valores ausentes**
   - Remoção de linhas com valores nulos nas notas-chave.
   - Verificação de valores ausentes em variáveis explicativas (idade, renda, escolaridade dos pais).

5. **Criação/ajuste de variáveis numéricas**
   - Conversão de variáveis categóricas em numéricas para análise estatística e modelos:
     - `TP_SEXO`, `TP_ESCOLA`, `TP_DEPENDENCIA_ADM_ESC`, `TP_COR_RACA`
     - Codificação de `Q001`, `Q002` e `Q006` como ordinais (níveis de escolaridade e faixas de renda).
   - Possível criação de faixas de idade (ex.: 15–17, 18–20, 21+).

6. **Salvamento do dataset tratado**
   - Geração do arquivo final: `enem2016_socioeconomico.csv`, usado nas análises seguintes.

---

## 4. Análise Univariada

Será realizada uma análise descritiva das variáveis selecionadas.

Para **pelo menos 10 variáveis numéricas/ordenadas**, serão calculadas:

- **Medidas de tendência central:** média, mediana, moda  
- **Medidas de dispersão:** desvio padrão  
- **Percentis:** 25, 50 e 75  
- **Visualização:** histogramas ou gráficos de barras.

### Exemplos de variáveis analisadas

- **Notas:** `NU_NOTA_CN`, `NU_NOTA_CH`, `NU_NOTA_LC`, `NU_NOTA_MT`, `NU_NOTA_REDACAO`
- **Perfil/condições:**
  - Idade (`NU_IDADE`)
  - Escolaridade do pai (`Q001_num`)
  - Escolaridade da mãe (`Q002_num`)
  - Renda familiar (`Q006_num`)
  - Tipo de escola (`TP_ESCOLA_num`)

Além disso, serão exploradas as distribuições de:

- **Sexo (`TP_SEXO`)** – proporção de participantes por sexo  
- **Tipo de escola (`TP_ESCOLA`)** – distribuição entre tipos de escola  
- **Estado de residência (`SG_UF_RESIDENCIA`)** – quantidade de participantes por UF

Nesses casos, serão utilizados principalmente **gráficos de barras** e tabelas de frequência.

---

## 5. Análise Multivariada

### Codificação de variáveis categóricas

- Transformação de `TP_SEXO`, `TP_ESCOLA`, `TP_DEPENDENCIA_ADM_ESC`, `TP_COR_RACA`, `SG_UF_RESIDENCIA` em representações numéricas (por exemplo, one-hot encoding ou códigos inteiros).
- Manutenção de `Q001`, `Q002`, `Q006` como variáveis ordinais.

### Correlação de Pearson

- Construção de uma **matriz de correlação de Pearson** com as variáveis numéricas e codificadas.
- Foco nas correlações com as notas de:
  - `NU_NOTA_MT` (Matemática)
  - `NU_NOTA_CH` (Ciências Humanas)
  - `NU_NOTA_REDACAO` (Redação)

### Interpretação das relações

Serão destacadas e interpretadas:

- Correlações entre as notas das diferentes áreas (ex.: Matemática × Ciências da Natureza).
- Impacto de:
  - Idade (`NU_IDADE`)
  - Tipo de escola (`TP_ESCOLA`)
  - Sexo (`TP_SEXO`)
  - Renda familiar (`Q006_num`)
  - Escolaridade dos pais (`Q001_num`, `Q002_num`)
  - UF de residência (`SG_UF_RESIDENCIA`, via médias por estado)

A interpretação será feita em linguagem simples, comentando, por exemplo, se determinado grupo tende a ter notas mais altas ou baixas.

---

## 6. Visualizações

Serão gerados **pelo menos 3 gráficos de alta qualidade**, incluindo exemplos de análises:

### Gráficos exploratórios

- Histogramas das notas de:
  - Matemática (`NU_NOTA_MT`)
  - Redação (`NU_NOTA_REDACAO`)
  - Ciências Humanas (`NU_NOTA_CH`)
  - Idade (`NU_IDADE`)

- Gráfico de barras:
  - Distribuição de participantes por sexo (`TP_SEXO`)
  - Distribuição por tipo de escola (`TP_ESCOLA`)
  - Distribuição por estado (`SG_UF_RESIDENCIA`)

### Gráficos explicativos

- **Boxplots**:
  - Nota de Matemática por tipo de escola (`NU_NOTA_MT` × `TP_ESCOLA`)
  - Nota de Redação por sexo (`NU_NOTA_REDACAO` × `TP_SEXO`)

- **Scatterplot**:
  - Matemática × Ciências da Natureza (`NU_NOTA_MT` × `NU_NOTA_CN`) com linha de tendência

- **Gráfico de médias por UF**:
  - Média de Matemática ou Redação por `SG_UF_RESIDENCIA` (barras).

---

## 7. Modelagem (Regressão)

### Definição do target

O foco principal será prever a nota de **Matemática** (`NU_NOTA_MT`). Opcionalmente, a mesma abordagem pode ser repetida para **Redação** ou **Ciências Humanas** (`NU_NOTA_CH`).

### Engenharia de atributos

Serão utilizados como variáveis explicativas:

- Idade (`NU_IDADE`)
- Sexo (`TP_SEXO`)
- Tipo de escola (`TP_ESCOLA`)
- Dependência administrativa (`TP_DEPENDENCIA_ADM_ESC`)
- UF de residência (codificada, `SG_UF_RESIDENCIA`)
- Escolaridade dos pais (`Q001_num`, `Q002_num`)
- Renda familiar (`Q006_num`)
- Notas de outras áreas:
  - `NU_NOTA_CN`, `NU_NOTA_CH`, `NU_NOTA_LC`

### Modelos de regressão aplicados

Serão aplicados pelo menos **3 modelos**:

1. **Regressão Linear**
2. **Random Forest Regressor**
3. **K-Nearest Neighbors (KNN) Regressor**

### Métricas de avaliação

- **R²** (coeficiente de determinação)
- **MAE** (erro médio absoluto)
- **RMSE** (raiz do erro quadrático médio)

Os resultados serão comparados e interpretados de forma clara (por exemplo, “o modelo X explica cerca de Y% da variação das notas de Matemática”).

---

## 8. Conclusão

Na conclusão, serão apresentados:

- **Principais achados descritivos**:
  - Distribuição das notas
  - Perfil dos participantes (idade, sexo, tipo de escola, renda e escolaridade dos pais)
  - Diferenças entre estados (`SG_UF_RESIDENCIA`)

- **Relações multivariadas**:
  - Correlações entre notas
  - Impacto de sexo, tipo de escola, renda e escolaridade dos pais no desempenho
  - Diferenças regionais, quando relevantes

- **Desempenho dos modelos de regressão**:
  - Comparação entre os modelos testados
  - Discussão sobre o quão bem é possível prever a nota de Matemática com as variáveis disponíveis

- **Limitações e possíveis extensões**:
  - Limitações do uso de dados de um único ano
  - Simplificações nas codificações de variáveis categóricas
  - Sugestões para trabalhos futuros (ex.: uso de outros anos do ENEM, modelos mais complexos, análise mais detalhada por região ou grupo específico).
