import os
from mlds6.datamodels.environment import DataLakePaths

def get_data_paths() -> DataLakePaths:
    """Collect path environmet varaibles.

    Returns
    -------
    paths: DataLakePaths
        Object with the required data paths.
    """
    paths = DataLakePaths(
        raw_data = os.environ["RAW_DATA_PATH"],
        preprocessed_data = os.environ["PREPROCESSED_DATA_PATH"],
        models = os.environ["MODELS_PATH"],
        features = os.environ["FEATURES_PATH"]
    )
    return paths
    
    