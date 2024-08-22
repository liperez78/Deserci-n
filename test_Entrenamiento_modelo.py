
import pytest
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.tree import DecisionTreeClassifier

from Entrenamiento_modelo import Extraer_Dividir_Datos, modelopipeline

def test_Extraer_Dividir_Datos(monkeypatch):
    # Mock para pandas.read_excel
    def mock_read_excel(file):
        data = {
            "ID": [1, 2, 3],
            "feature1": [10, 20, 30],
            "feature2": [0.1, 0.2, 0.3],
            "DESERTOR": [0, 1, 0]
        }
        return pd.DataFrame(data)
    
    monkeypatch.setattr(pd, 'read_excel', mock_read_excel)
    
    X, y = Extraer_Dividir_Datos()
    
    # Verificar que X y y sean del tipo esperado
    assert isinstance(X, pd.DataFrame)
    assert isinstance(y, pd.Series)
    
    # Verificar las dimensiones
    assert X.shape == (3, 2)
    assert y.shape == (3,)

