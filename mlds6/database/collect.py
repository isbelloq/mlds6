"""
collect
        module for extract and save data from Secop API
"""
import requests
import json
from mlds6.datamodels.api import ApiParams
from mlds6.environment.base import get_data_paths
from os import path, getcwd
import pandas as pd
import io 
import os


def getLocalDataFrame(src: str)->pd.DataFrame:
    """
    Get a pandas dataframe from JSON file
    =====================================
    Params
        src: str
            Source path file
    Returns
        out: Pandas.DataFrame
            DataFrame from JSON file
    """
    file = path.join(getcwd, src)
    return pd.read_json(file)

def getDataFrameDataByYear( year:int, *extra_columns:str, total_data= 200_000)->pd.DataFrame:
    """
    Get a pandas dataframe from Secop API
    =====================================
    Params
        year: Int
                year that will get registers
        *extra_columns: str 
                extra columns to extract data
        total_data: Int, optional
                max number of items that will collect from api
    returns
        secopDataFrame: Pandas.DataFrame
                dataframe that contains the data of the specified year
    """
    secopData = __requestDataByYear( year, total_data, *extra_columns)
    secopData = secopData.content
    secopDataFrame = pd.read_json(io.StringIO(secopData.decode('utf-8')))
    return secopDataFrame


def saveSecopJSON(year:int , *extra_columns:str, total_data=200_000, dest='./raw', filename="datos_secop_")->None:
        """ 
        save a JSON file that contains secop data
        =========================================
        Params
        year: Int
                year that will get registers
        *extra_columns: str 
                extra columns to extract data
        total_data: Int, optional
                max number of items that will collect from api
        dest: str, optional
                file destination path
        filename: str, optional
                output filename
        """        
        file = f'{filename}{year}.json'
        file_path = path.join(getcwd(), dest, file)
        secopData = __requestDataByYear(year, total_data, *extra_columns).json()

        with open( file_path ,'w') as f:
                json.dump(secopData, f)

        print(f"Total data writed in {file} {len(secopData)}")


def __requestDataByYear( year:int, total_data:int, *extra_columns:str)->requests.Response:
        """
        generate a request to Secop API
        =============================
        Params
        year: Int
                year of the data
        total_data: Int
                max number of items that will get from the api
        *extra_columns: str 
                extra columns to extract data
        """
        api_params = get_api_params()
        params = api_params.params
        params['$select'] = ",".join(params['$select'])
        params['anno_firma_del_contrato'] = year
        params['$limit'] = str(total_data)
        
        if len(extra_columns):
                params['$select'] = params['$select']+","+",".join(extra_columns)

        secopData = requests.get(api_params.URL,
                headers=api_params.headers, 
                params=params)
        
        secopData.raise_for_status()
                
        return secopData
    



def obtener_convocados( year:int, total_data= 200_000)->pd.DataFrame:
        api_params = get_api_params()
        params = get_api_params().params
        
        params['$select'] = ",".join(params['$select'])
        params["$where"] = 'estado_del_proceso = "Convocado"'
        
        del params['estado_del_proceso']
        
        params['anno_firma_del_contrato'] = year
        params['$limit'] = str(total_data)

        request = requests.get(api_params.URL,
                headers=api_params.headers, 
                params=params)
        
        request.raise_for_status()
        
        secopData = request.content
        return pd.read_json(io.StringIO(secopData.decode('utf-8')))     
                
    
def get_api_params()->ApiParams:
        """Load api params from file

        Returns
        -------
        ApiParams
            [description]
        """
        paths = get_data_paths()
        file = os.path.join(paths.api_params, 'params.json')
        with open(file) as f:
               api_params = json.load(f)
        
        return ApiParams(**api_params) 
