from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from mlds6.database.io import load_table
from imblearn.over_sampling import RandomOverSampler
from typing import Tuple
from pandas import DataFrame
from mlds6.environment.base import get_data_paths
import json
import os

def generate_feature_extractor() -> ColumnTransformer:
    """Generates the feature extractor object for the secop dataset.

    Returns
    -------
    ColumnTransformer : ColumnTransformer
        Sklearn object to extract features.
    """
    params = get_features_params()
    column_transformer = ColumnTransformer([
        ("OneHot",
         OneHotEncoder(),
         params['features']
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
    params = get_features_params()
    X_df = secop_i[params['features']]
    y_df = secop_i[params['target_features']]
    return (X_df, y_df)

def get_features_params():
    """Get the features params

    Returns
    -------
    params: Dict
        Features params
    """
    data_path = get_data_paths()
    file = os.path.join(data_path.param_features, 'featureparams.json')
    with open(file) as f:
        params = json.load(f)
    return params

def get_train_data(train_size=0.8):
    """split data in train and test sets

    Parameters
    ----------
    train_size : float, optional
        train size proportion, by default 0.8

    Returns
    -------
        X, y train and test datasets
    """
    paths = get_data_paths()
    data = load_table(paths.preprocessed_data, 'out', 'parquet')
    X, y = select_features(data)
    ros = RandomOverSampler(sampling_strategy=0.7)
    X_ros, y_ros = ros.fit_resample(X, y)
    return train_test_split(X_ros, y_ros, train_size=train_size, stratify=y_ros)

if __name__ == '__main__':
    params = get_features_params()
    print(params)