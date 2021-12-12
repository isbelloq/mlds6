from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, FunctionTransformer
from numpy import log10, power
from typing import Tuple
from pandas import DataFrame

_features =['objeto_a_contratar',
          'departamento_entidad',
          'Tipo_persona',
          'origen_de_los_recursos']
_target_features = 'sobrecosto'

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
         _features
         )
    ])
    return column_transformer

def select_features(secop_i : DataFrame) -> Tuple[DataFrame]:
    """Select the features to train the model

    Parameters
    ----------
    secop_i : DataFrame
        

    Returns
    -------
    Tuple[DataFrame]
        X and y features df that will apply to the model
    """
    X_df = secop_i[_features]
    y_df = secop_i[_target_features]
    return (X_df, y_df)