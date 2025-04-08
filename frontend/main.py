import streamlit as st
import pandas as pd
import requests
import json

API_URL = "http://localhost:8000/predict"

st.title("Detector de Fraudes")
st.write("Envie um arquivo com as transações (CSV, XLSX ou JSON) para ver a classificação: normal ou fraude.")

arquivo = st.file_uploader("Envie o arquivo", type=["csv", "xlsx", "json"])

if "df_resultado" not in st.session_state:
    st.session_state.df_resultado = None

if arquivo is not None:
    try:
        if arquivo.name.endswith(".csv"):
            df = pd.read_csv(arquivo)
        elif arquivo.name.endswith(".xlsx"):
            df = pd.read_excel(arquivo)
        elif arquivo.name.endswith(".json"):
            conteudo = arquivo.read()
            dados_json = json.loads(conteudo)
            df = pd.DataFrame(dados_json)
        else:
            st.error("Formato de arquivo não suportado.")
            st.stop()

        df = df.drop(columns=["Class"], errors="ignore")

        with st.spinner("Analisando transações..."):
            response = requests.post(API_URL, json=df.to_dict(orient="records"))

        if response.status_code != 200:
            st.error(f"Erro da API: {response.status_code} - {response.text}")
        else:
            st.session_state.df_resultado = pd.DataFrame(response.json())

    except Exception as e:
        st.error(f"Erro ao processar o arquivo: {e}")

# Mostra os resultados se já tiverem sido processados
if st.session_state.df_resultado is not None:
    df_resultado = st.session_state.df_resultado

    total = len(df_resultado)
    qtd_fraude = (df_resultado["classificacao"] == "fraude").sum()
    qtd_normal = (df_resultado["classificacao"] == "normal").sum()

    st.success("Análise concluída!")
    st.markdown(f"""
    ### Resumo da Análise:
    - **Total de transações:** {total}
    - **Transações fraudulentas:** {qtd_fraude}
    - **Transações normais:** {qtd_normal}
    """)
    st.dataframe(df_resultado[["Time", "Amount", "probabilidade_fraude", "classificacao"]])

    # Botão de download separado
    csv = df_resultado.to_csv(index=False).encode("utf-8")
    st.download_button(
        label="📥 Baixar resultado como CSV",
        data=csv,
        file_name="resultado_fraudes.csv",
        mime="text/csv"
    )
