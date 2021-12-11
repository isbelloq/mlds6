from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import MinMaxScaler, OneHotEncoder, FunctionTransformer, Normalizer

def generate_feature_extractor() -> ColumnTransformer:
    """Generates the feature extractor object for the secop dataset.

    Returns
    -------
    ColumnTransformer : ColumnTransformer
        Sklearn object to extract features.
    """ 
    column_transformer = ColumnTransformer([
        ("OneHot",
         OneHotEncoder(), 
         ['tipo_identifi_del_contratista', 
          'objeto_a_contratar',
          'departamento_entidad',
          'origen_de_los_recursos']),
        ('Scaler', Normalizer(), ['cuantia_contrato'])
    ])