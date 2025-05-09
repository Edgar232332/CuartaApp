import pandas as pd
import plotly.express as px
import streamlit as st
import pickle
import numpy as np

gpa = pd.read_csv("GPA1.csv")

st.title("Aplicación 5")
tab1, tab2, tab3 = st.tabs(["Análisis univariado", "Análisis bivariado", "Modelo"])
with tab1:
    fig1 = px.histogram ( gpa, x = "Promedio" )
    fig2 = px.histogram ( gpa, x = "Genero")
    fig3 = px.histogram ( gpa, x = "Vive en Campus")
    fig4 = px.histogram ( gpa, x = "Promedio alcohol")
    st.plotly_chart(fig1)
    st.plotly_chart(fig2)
    st.plotly_chart(fig3)
    st.plotly_chart(fig4)
with tab2:
    fig5  =  px.box(gpa,  x = "Genero" ,  y = "Promedio" ,  title = 'Promedio de notas respecto al género' )
    fig6  =  px.box(gpa,  x = "Vive en Campus" ,  y = "Promedio" ,  title = "Promedio de notas respecto a si vive en el campus" ) 
    fig7  =  px.scatter(gpa,  x = "Promedio alcohol" ,  y = "Promedio" ,  title = 'Promedio de notas respecto al promedio de alcohol ingerido semanalmente' ) 
    st.plotly_chart(fig5)
    st.plotly_chart(fig6)
    st.plotly_chart(fig7)
with tab3:
    with open("model (1).pickle", "rb") as m:
        modelo = pickle.load(m)
    alcohol = st.slider("Seleccione su promedio semanal de consumo alcohol ", 0, 7)
    gender = st.selectbox("Seleccione genero", ["Mujer", "Hombre"])
    if gender == "Hombre":
            gender = 1
    else:
            gender = 0
    
    campus = st.selectbox("Seleccione si reside en el campus", ["Reside","No Reside"])
    if campus == "Reside":
            campus = 1
    else:
            campus = 0


    if st.button("Predecir"):
        pred = modelo.predict(np.array([[alcohol, gender, campus]]))
        predre = round(pred[0], 2)
        st.write("Su promedio es de:", predre)
