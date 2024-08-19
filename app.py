import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import streamlit as st

# Crear un DataFrame con los datos
data = {
    "ESTRATO": [1000000, 9028, -14413, 233543, 131355, 2831],
    "GRADO": [0.009028, 1.0, 961004, 129205, None, 18173],
    "EDAD": [-14413, 61004, 1.0, 86182, 13697, -51215],
    "PUNTAJE": [233543, 129205, 86182, 1.0, None, 44992],
    "ingresos_promedio": [131355, 11742, -13697, 261148, 1.0, -29565],
    "DESERTOR": [2831, 18173, -20319, 14173, 51215, -44992]
}

df = pd.DataFrame(data)

# Eliminar filas con valores nulos
df = df.dropna()

# Dividir los datos en características (X) y variable objetivo (y)
X = df.drop("DESERTOR", axis=1)
y = df["DESERTOR"]

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear el modelo de Árbol de Decisión
model = DecisionTreeClassifier()

# Entrenar el modelo
model.fit(X_train, y_train)

# Predecir en el conjunto de prueba
y_pred = model.predict(X_test)

# Calcular la precisión del modelo
accuracy = accuracy_score(y_test, y_pred)

# Streamlit UI
st.title("Predicción de Deserción Escolar")

st.write(f"Precisión del modelo: {accuracy:.2f}")

st.write("Estudiantes que desertaron:")
desertores = df[df["DESERTOR"] > 0]
st.dataframe(desertores)

st.write("Predicción en nuevos datos")
estrato = st.number_input("Estrato", value=0)
grado = st.number_input("Grado", value=0.0)
edad = st.number_input("Edad", value=0)
puntaje = st.number_input("Puntaje", value=0.0)
ingresos = st.number_input("Ingresos promedio", value=0)

if st.button("Predecir"):
    nuevo_estudiante = pd.DataFrame({
        "ESTRATO": [estrato],
        "GRADO": [grado],
        "EDAD": [edad],
        "PUNTAJE": [puntaje],
        "ingresos_promedio": [ingresos]
    })
    prediccion = model.predict(nuevo_estudiante)
    st.write("Predicción de deserción:", prediccion[0])
