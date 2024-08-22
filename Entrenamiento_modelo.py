import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix

from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
import seaborn as sns
import matplotlib.pyplot as plt

def Extraer_Dividir_Datos():
    #importar datos en un datafram
    df = pd.read_excel('Datos_deserción.xlsx')

    # Eliminar filas con valores nulos

    df = df.dropna()

    # Dividir los datos en características (X) y variable objetivo (y)
    X = df.drop(["DESERTOR",'ID'], axis=1) #se elimina la variable de respuesta y el Id consecutivo de la fila
    y = df["DESERTOR"]

    return X,y

def modelopipeline():

    
    X,y=Extraer_Dividir_Datos()
    
    # Dividir los datos en conjuntos de entrenamiento y prueba
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


    # Definir transformaciones para datos numéricos
    numeric_features = X.select_dtypes(include=['int64', 'float64']).columns
    numeric_transformer = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='mean')),
        ('scaler', StandardScaler())
    ])

    # Combinar transformaciones
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', numeric_transformer, numeric_features)
        ])

    # Crear el modelo de Árbol de Decisión
    model = DecisionTreeClassifier()

    # Crear el pipeline
    pipeline = Pipeline(steps=[('preprocessor', preprocessor),
                            ('classifier', model)])

    # Entrenar el modelo
    modelo=pipeline.fit(X_train, y_train)

    datos_entregados=[modelo,X_test,y_test]
    return datos_entregados
    



