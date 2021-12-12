"""
get_data
        module for extract and save data from Secop API
"""
import requests
import json
from os import path, getcwd
import pandas as pd
import io 

__URL="https://www.datos.gov.co/resource/xvdy-vvsk.json"
__headers = {
        'Accept':'application/json'
        }
__params = {
        "$select": ",".join([
                "uid",
                "tipo_identifi_del_contratista",
                "objeto_a_contratar",
                "nit_de_la_entidad",
                "nombre_de_la_entidad",
                "c_digo_de_la_entidad",
                "nombre_grupo",
                "tipo_de_contrato",
                "departamento_entidad",
                "tiempo_adiciones_en_dias",
                "cuantia_contrato",
                "valor_total_de_adiciones",
                "valor_contrato_con_adiciones",
                "origen_de_los_recursos",
                "moneda"]),
        "estado_del_proceso":"Liquidado"
        }

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
        params = dict(__params)
        params['anno_firma_del_contrato'] = year
        params['$limit'] = str(total_data)
        
        if len(extra_columns):
                params['$select'] = params['$select']+","+",".join(extra_columns)

        secopData = requests.get(__URL,
                headers=__headers, 
                params=params)
        try:
                secopData.raise_for_status()
                
        except requests.exceptions.HTTPError:
                print("Error en la peticion revise las columnas adicionales")
                return None
        else: 
                return secopData
    



