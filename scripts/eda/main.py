# -*- coding: utf-8 -*-
#Carga de librerias
import os
import pandas as pd
from pandas_profiling import ProfileReport

#Extracción de variables de entorno
BASE_DIRECTORY = os.environ['PROJECT_DIRECTORY']
SUMMARY_DIRECTORY = os.environ['SUMMARY_DIRECTORY']

#Listado archivos en BASE_DIRECTORY
raw_files = sorted(os.listdir(f"{BASE_DIRECTORY}data/raw/"), reverse=True)
raw_files

#Lectura del primer conjunto de datos
secop = pd.read_json(f"{BASE_DIRECTORY}data/raw/{raw_files[0]}")

#Iteración para lectura y consolidación de dataframes
for f in raw_files[1:]:
    temp_df = pd.read_json(f"{BASE_DIRECTORY}data/raw/{f}")
    secop = pd.concat([secop, temp_df])

#Creación del reporte
profile = ProfileReport(secop, title="Reporte de datos para SECOP-I")

#Almacenamieto del reporte
profile.to_file(f"{SUMMARY_DIRECTORY}secop_summary.html")
