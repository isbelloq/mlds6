import json
import os

from pandas import DataFrame
from joblib import dump, load

from sklearn.base import ClassifierMixin
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import classification_report

from mlds6.database.io import export_table
from mlds6.environment.base import get_data_paths
from mlds6.datamodels.training import ModelType
from mlds6.models.feature_extraction import generate_feature_extractor
from mlds6.models.model import generate_model_pipeline, save_model


def train_search_model(X_train, y_train,
                  model: ClassifierMixin,
                  hiperparams: dict,
                  scoring='f1') -> GridSearchCV:
    """Create and train a GridSearchCV model

    Parameters
    ----------
    X_train :
        X input features
    y_train :
        y target features
    model : ClassifierMixin
        model that will aply grid search
    hiperparams : dict
        parameter settings to try as hiperparams model values
    scoring : str, optional
        Strategy to evaluate the performance, by default 'f1'

    Returns
    -------
    GridSearchCV
        Trained GridSearch
    """
    extractor = generate_feature_extractor()
    pipe = generate_model_pipeline(extractor, model)
    search = GridSearchCV(pipe, hiperparams, scoring=scoring, n_jobs=4)
    search.fit(X_train, y_train)
    return search


def save_model_report(grid_model: GridSearchCV,
                      filename: str
                      ):
    """Save a cv_results_ file from grid_model

    Parameters
    ----------
    grid_model : GridSearchCV
        A trained GridSearch model
    filename : str
        name of the output file
    """
    paths = get_data_paths()
    report_model = DataFrame(grid_model.cv_results_)
    export_table(paths.features, f'{filename}_report', 'parquet', report_model)


def save_scoring_report(X_test, y_test, grid_model: GridSearchCV, filename: str):
    """Save scoring report file from grid_model
    Parameters
    ----------
    X_test: {array-like, sparse matrix} of shape (n_samples, n_features)
        input data
    y_test: 1d array-like of shape (n_samples,)
        test target values.
    grid_model : GridSearchCV
        A trained GridSearch model
    filename : str
        name of the output file
    """
    paths = get_data_paths()
    y_pred = grid_model.predict(X_test)
    scoring = classification_report(y_test, y_pred, output_dict=True)
    dump(scoring, os.path.join(paths.features, f'{filename}_score.joblib'))
    
def get_hiperparams(model_type: ModelType)->dict:
    """load model hiperparams

    Parameters
    ----------
    model_type : ModelType
        Kind of model aplied

    Returns
    -------
    dict
        Hiperparams to aply a gridsearch
    """
    paths = get_data_paths()
    file = os.path.join(paths.param_hiperparams, 'model_hiperparams.json')
    with open(file) as f:
        params = json.load(f)
    return params[model_type.name]

def save_grid_model(model: GridSearchCV, filename='model_grid'):
    """Save model pipeline

    Parameters
    ----------
    model : GridSearchCV
        model to save
    filename : str, optional
        output filename, by default "model"
    """
    data_paths = get_data_paths()
    dump(model, os.path.join(data_paths.models, f"{filename}_grid.joblib"))
    
def load_grid_model(path: str, filename="model")->GridSearchCV:
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
    return load(os.path.join(path , f"{filename}_grid.joblib"))
    