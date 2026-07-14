
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


st.set_page_config(
    page_title="Dashboard Analítico Universitario",
    page_icon="📊",
    layout="wide"
)


st.title("📊 Plataforma Integral de Analítica Universitaria")

st.subheader(
    "Predicción de Congestión de Trámites Administrativos"
)


# Cargar datos
df = pd.read_csv("dataset_personal_ETL.csv")

st.write("Columnas del dataset:")
st.write(df.columns.tolist())


st.header("Vista del Dataset")

st.dataframe(df.head())
