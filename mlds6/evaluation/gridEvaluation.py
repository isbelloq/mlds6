import json 
import os

from pandas import DataFrame

from sklearn.base import ClassifierMixin
from sklearn.model_selection import GridSearchCV

from mlds6.database.io import export_table
from mlds6.environment.base import get_data_paths
from mlds6.datamodels.training import ModelType
from mlds6.models.feature_extraction import generate_feature_extractor
from mlds6.models.model import generate_model_pipeline,save_model

def train_search_model(X_train, y_train,
                  model: ClassifierMixin, 
                  hiperparams: dict,
                  scoring='f1')->GridSearchCV:
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
    search.fit(X_train,y_train)
    return search
    
def save_model_report(grid_model:GridSearchCV, 
                      model_type:ModelType 
                      ):
    """Save a cv_results_ file from grid_model

    Parameters
    ----------
    grid_model : GridSearchCV
        A trained GridSearch model
    model_type : ModelType
        kind of estimator used in GridSearch
    """
    paths = get_data_paths()
    report_model = DataFrame(grid_model.cv_results_)
    export_table(paths.features, model_type.name, 'parquet', report_model)
    
def save_evaluation_model(grid_model: GridSearchCV,
                          model_type:ModelType):
    """Save model evaluation

    Parameters
    ----------
    grid_model : GridSearchCV
        the model to save
    model_type : ModelType
        kind of base estimator aplied
    """
    save_model(grid_model, f'{model_type.name}_grid')
    
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