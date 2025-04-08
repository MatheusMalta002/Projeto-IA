# 💳 Credit Card Fraud Detector

Este projeto tem como objetivo detectar transações fraudulentas com cartão de crédito utilizando aprendizado de máquina. A aplicação possui um modelo treinado com XGBoost e uma interface web simples para uso interativo.

## 📂 Estrutura do Projeto

```
.
├── backend/
│   └── main (1).py         # Código do FastAPI que serve o modelo
├── frontend/
│   └── main.py             # Interface em Streamlit para enviar e classificar arquivos
├── notebooks/
│   ├── treino_modelo.ipynb # Notebook com análise exploratória, pré-processamento e treino inicial
│   └── treino_modelo_v2.ipynb # (Adicionar aqui outro arquivo de treinamento, se houver)
└── model/
    └── fraud_detection_model_v1.model # Modelo XGBoost salvo
```

## 🚀 Como Executar

### 1. Clonar o repositório
```bash
git clone https://github.com/seu-usuario/credit-card-fraud-detector.git
cd credit-card-fraud-detector
```

### 2. Instalar as dependências
Recomenda-se o uso de um ambiente virtual (como `venv` ou `conda`).

```bash
pip install -r requirements.txt
```

### 3. Iniciar o Back-end (API FastAPI)
```bash
uvicorn backend.main:app --reload
```

> A API estará disponível em `http://localhost:8000/predict`

### 4. Iniciar o Front-end (Streamlit)
```bash
streamlit run frontend/main.py
```

> A interface estará disponível em `http://localhost:8501`

## 📊 Funcionalidades

- Upload de arquivos CSV, XLSX ou JSON com transações.
- Classificação das transações como "fraude" ou "normal".
- Probabilidade de fraude calculada para cada entrada.
- Download dos resultados em CSV.

## 🧠 Modelo Utilizado

- Algoritmo: XGBoost Classifier
- Dataset: Credit Card Fraud Detection (Kaggle)
- Estratégia: Treinamento com dados desbalanceados, análise estatística, separação de treino/teste.

## 📌 Requisitos

- Python 3.8+
- FastAPI
- Streamlit
- xgboost
- pandas
- scikit-learn
- uvicorn
- requests

## 📄 Licença

Este projeto é de uso educacional e livre para estudos e adaptações.
