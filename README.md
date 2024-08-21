el proyecto presentado tendrá como objeto principal desplegar un modelode inteligencia artificial que permite clasificar los posibles casos de deserciónescolar, 
esto a través de la evaluación de diversos factores socioeconómicos ydemográficos.
1. ##Proyecto prevención de la deserción estudiantil en etapa escolar

Genera el contexto de los factores principales que promueven la deserción escolar se encuentran las condiciones geográficas y sociales de los entornos de desarrollo, el
acceso a la educación, las condiciones socioeconómicas del contexto familiar y local, entre otros.

2. ##Modelo entrenado desercciòn_escolar.ipynb
Entrenar y evaluar un modelo de clasificación usando un Árbol de Decisión en Python para predecir la deserción escola
3. Ejecución del programa app.py

Es una aplicación de predicción de deserción escolar utilizando Streamlit para la interfaz de usuario, pandas para la manipulación de datos y scikit-learn para construir y evaluar un modelo de clasificación con un Árbol de Decisión, Es decir:
Construye un modelo de Árbol de Decisión para predecir la deserción escolar basado en características como "ESTRATO", "GRADO", "EDAD", "PUNTAJE" y "ingresos_promedio". Después de entrenar el modelo y calcular su precisión, el código también identifica e imprime los estudiantes que han desertado según los datos proporcionados.
se debe ejecutar con streamlit run app.py, el aplicativo devuelve la url para ejecutarlo en el local y la url para generarlo por la web

##Interfaz de usuario con Streamlit:

Título: Muestra el título "Predicción de Deserción Escolar".
Precisión: Muestra la precisión del modelo entrenado.
Visualización de datos: Muestra un subconjunto del DataFrame que contiene solo a los estudiantes que desertaron.
Entrada de nuevos datos: Proporciona entradas de número para que el usuario ingrese valores para las características de un nuevo estudiante.
Predicción: Cuando se hace clic en el botón "Predecir", se crea un nuevo DataFrame con los valores ingresados y el modelo predice si ese estudiante deserta o no.
4. ## Salida:
Muestra la predicción sobre la deserción basada en los valores ingresados por el usuario en la interfaz.
Crea una url para que el usuario navegue sobre los datos y genere la predicción
