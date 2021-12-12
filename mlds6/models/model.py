from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.base import TransformerMixin, ClassifierMixin
from mlds6.environment.base import get_data_paths
from joblib import dump, load
import os

def generate_model_pipeline(
    extractor: ColumnTransformer,
    selector: TransformerMixin,
    classifier: ClassifierMixin
) -> Pipeline:
    """Defines the model pipeline.

    Parameters
    ----------
    extractor : ColumnTransformer
        Extracts features from a dataframe.
    selector : TransformerMixin
        Selects the most important features.
    classifier : ClassifierMixin
        Classification model.

    Returns
    -------
    Pipeline
        model pipeline
    """
    pipe = Pipeline([
        ("extractor", extractor),
        ("selector", selector),
        ("classifier", classifier)
    ])
    return pipe

def save_model_pipelin(model :Pipeline, filename = "model"):
    """Save model pipeline

    Parameters
    ----------
    model : Pipeline
        model to save
    filename : str, optional
        output filename, by default "model"
    """
    data_paths = get_data_paths()
    dump(model, os.path.join(data_paths.models, f"{filename}.joblib"))
    
def load_model_pipeline(filename="model")->Pipeline:
    """Load model from disk

    Parameters
    ----------
    filename : str, optional
        input filename, by default "model"

    Returns
    -------
    Pipeline
        output pipeline model
    """
    
    data_paths = get_data_paths()
    return load(os.path.join(data_paths.models , f"{filename}.joblib"))
    