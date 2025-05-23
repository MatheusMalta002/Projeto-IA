from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import xgboost as xgb
import pandas as pd

app = FastAPI()

# Carrega o modelo treinado
model = xgb.Booster()
model.load_model("../model/fraud_detection_model_v1.model")

# Define os atributos esperados
predictors = ['Time', 'V1', 'V2', 'V3', 'V4', 'V5', 'V6', 'V7', 'V8', 'V9', 'V10',
              'V11', 'V12', 'V13', 'V14', 'V15', 'V16', 'V17', 'V18', 'V19',
              'V20', 'V21', 'V22', 'V23', 'V24', 'V25', 'V26', 'V27', 'V28',
              'Amount']

class Transacao(BaseModel):
    Time: float
    V1: float
    V2: float
    V3: float
    V4: float
    V5: float
    V6: float
    V7: float
    V8: float
    V9: float
    V10: float
    V11: float
    V12: float
    V13: float
    V14: float
    V15: float
    V16: float
    V17: float
    V18: float
    V19: float
    V20: float
    V21: float
    V22: float
    V23: float
    V24: float
    V25: float
    V26: float
    V27: float
    V28: float
    Amount: float

@app.post("/predict")
def predict(transacoes: List[Transacao]):
    df = pd.DataFrame([t.dict() for t in transacoes])
    dmatrix = xgb.DMatrix(df[predictors])
    preds = model.predict(dmatrix)

    df["probabilidade_fraude"] = preds
    df["classificacao"] = df["probabilidade_fraude"].apply(lambda x: "fraude" if x >= 0.5 else "normal")

    return df.to_dict(orient="records")
