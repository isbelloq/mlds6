
from collect import saveSecopJSON
import os
from mlds6.environment.base import get_data_paths
if __name__=="__main__":
    data_path = get_data_paths()
    BASE_DIRECTORY = os.environ['DATA_PATH']

    saveSecopJSON(2018, dest=data_path.raw_data)
    saveSecopJSON(2017, dest=data_path.raw_data)
    saveSecopJSON(2016, dest=data_path.raw_data)
    saveSecopJSON(2019, dest=data_path.raw_data)
