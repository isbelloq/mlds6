from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.base import TransformerMixin, ClassifierMixin
from mlds6.environment.base import get_data_paths
from joblib import dump, load
import os

def generate_model_pipeline(
    extractor: ColumnTransformer,
    classifier: ClassifierMixin
) -> Pipeline:
    """Defines the model pipeline.

    Parameters
    ----------
    extractor : ColumnTransformer
        Extracts features from a dataframe.
    classifier : ClassifierMixin
        Classification model.

    Returns
    -------
    Pipeline
        model pipeline
    """
    pipe = Pipeline([
        ("extractor", extractor),
        ("classifier", classifier)
    ])
    return pipe

def save_model_pipeline(model :Pipeline, path: str ,filename = "model"):
    """Save model pipeline

    Parameters
    ----------
    model : Pipeline
        model to save
    path: str
        path to save the model
    filename : str, optional
        output filename, by default "model"
    """
    data_paths = get_data_paths()
    dump(model, os.path.join(data_paths.models, f"{filename}.joblib"))
    
def load_model_pipeline(path: str, filename="model")->Pipeline:
    """Load model from disk

    Parameters
    ----------
    path : str, 
        path of the model 
    filename : str, optional
        input filename, by default "model"

    Returns
    -------
    Pipeline
        output pipeline model
    """
    
    return load(os.path.join(path , f"{filename}.joblib"))
    