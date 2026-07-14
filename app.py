import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


st.set_page_config(
    page_title="Dashboard Analítica Universitaria",
    page_icon="📊",
    layout="wide"
)


st.title("📊 Plataforma Integral de Analítica Universitaria")

st.subheader(
    "Predicción de Congestión de Trámites Administrativos mediante BI, Big Data e IA Ética"
)


# Cargar dataset
df = pd.read_csv("dataset_personal_ETL.csv")


# Vista previa
st.header("Vista previa del dataset")

st.dataframe(df.head())


# ==========================
# KPI
# ==========================

st.header("Indicador KPI")


total_tramites = len(df)

total_congestion = df["Congestion"].sum()

porcentaje = (total_congestion / total_tramites) * 100


col1, col2 = st.columns(2)


with col1:
    st.metric(
        "Total de trámites",
        total_tramites
    )


with col2:
    st.metric(
        "Porcentaje de congestión",
        f"{porcentaje:.2f}%"
    )



# ==========================
# GRAFICO DE BARRAS
# ==========================

st.header("Congestión por Tipo de Trámite")


fig, ax = plt.subplots(figsize=(10,5))


sns.countplot(
    data=df,
    x="Tipo_Tramite",
    hue="Congestion",
    ax=ax
)


plt.xticks(rotation=45)

st.pyplot(fig)



# ==========================
# HISTOGRAMA
# ==========================

st.header("Distribución del Número de Solicitudes")


fig, ax = plt.subplots(figsize=(10,5))


sns.histplot(
    data=df,
    x="Numero_Solicitudes",
    bins=20,
    kde=True,
    ax=ax
)


st.pyplot(fig)



# ==========================
# HEATMAP
# ==========================

st.header("Correlación de Variables")


fig, ax = plt.subplots(figsize=(12,8))


sns.heatmap(
    df.select_dtypes(include="number").corr(),
    annot=True,
    cmap="coolwarm",
    ax=ax
)


st.pyplot(fig)



# ==========================
# STORYTELLING
# ==========================

st.header("📌 Hallazgos Principales")


st.write("""
**Hallazgo 1:**  
El aumento del número de solicitudes incrementa la probabilidad de congestión administrativa.
""")


st.write("""
**Hallazgo 2:**  
La disponibilidad de personal influye directamente en los tiempos de atención.
""")


st.write("""
**Hallazgo 3:**  
Los periodos de alta demanda requieren una planificación anticipada de recursos.
""")


st.header("💡 Recomendaciones")


st.write("""
**Recomendación 1:**  
Asignar mayor personal en temporadas de alta demanda.
""")


st.write("""
**Recomendación 2:**  
Optimizar los canales digitales de atención universitaria.
""")


st.write("""
**Recomendación 3:**  
Utilizar modelos predictivos para anticipar congestiones.
""")
