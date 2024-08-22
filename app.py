import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import streamlit as st
import Entrenamiento_modelo
import numpy as np


def GUI():
    #recibir los datos entrenamos del modelo 
    datos_recibidos=Entrenamiento_modelo.modelopipeline()
    model=datos_recibidos[0]
    X_test=datos_recibidos[1]
    y_test=datos_recibidos[2]

    # Predecir en el conjunto de prueba
    y_pred = model.predict(X_test)

    # Calcular la precisión del modelo
    accuracy = accuracy_score(y_test, y_pred)



    # Streamlit UI
    #titulo
    st.title("Predicción de Deserción Escolar")
    st.subheader('Entrada de datos:')


    st.write("Predicción en nuevos datos")
    estrato = st.selectbox(
        "Estrato:",
        (0,1,2,3,4,5,6,"No indica"),
        )
    #st.selectbox('pr',options=np.arange(1.0,7.1,0.1))
    grado =st.selectbox("Grado:",options=np.arange(1,12))
    edad = st.number_input("Edad:", value=0, min_value=0, step=1)
    puntaje = st.number_input("Nota promedio año:", value=1.0, step=0.1, min_value=1.0, max_value=10.0)
    ingresos = st.number_input("Promedio de ingresos économicos (anual):", value=0, min_value=0)

    #convertir valores para la evaluación
    if estrato=="No indica":
        estrato=7

    #Evaluación del modelo
    if st.button("Predecir"):
        nuevo_estudiante = pd.DataFrame({
            "ESTRATO": [estrato],
            "GRADO": [grado],
            "EDAD": [edad],
            "PUNTAJE": [puntaje],
            "ingresos_promedio": [ingresos]
        })
        prediccion = model.predict(nuevo_estudiante)
        st.write("Predicción de deserción:", "El estudiante deserto" if prediccion[0]==1 else "El estudiante se mantiene en el sistema educativo")

        st.write(f"Precisión del modelo: {accuracy:.2f}")

  



def main():
    my_app = GUI()
    return 0

if __name__ == "__main__":
    main()
