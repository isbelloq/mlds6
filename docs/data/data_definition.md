# Definición de datos y características

Los datos están disponibles como formato json en la plataforma de datos abiertos, que se obtienen a traves de la [api](https://www.datos.gov.co/resource/xvdy-vvsk.json)
 
Con el proyecto de Datos Abiertos, el Gobierno Colombiano promueve la transparencia, el acceso a la información pública, la competitividad, el desarrollo económico, y la generación de impacto social a través de la apertura, la reutilización de los datos públicos, y el uso y apropiación de las TIC.

La iniciativa de Datos Abiertos busca que todas las entidades del sector público publiquen la información pertinente y de calidad en formatos estructurados a disposición de los usuarios para que ellos y las entidades la utilicen de diferentes maneras, según su interés: generar informes, reportes, estadísticas, investigaciones, control social, oportunidades de negocio (ej. aplicaciones), entre otros temas.

Dicha información es compartida públicamente en datos.gov.co, en formatos digitales estandarizados con una estructura de fácil comprensión para que la misma pueda ser utilizada por los ciudadanos. Dado que son financiados y recopilados con dinero público, la información contenida en estos datos es pública y debe estar a disposición de cualquier ciudadano y para cualquier fin.



## Fuentes de datos brutos

| Dataset Name | Original Location   | Destination Location  | Data Movement Tools / Scripts | Link to Report |
| ---:| ---: | ---: | ---: | -----: |
| SECOP I | https://www.datos.gov.co/resource/xvdy-vvsk.json | `/home/mlds6_sbkfcp/data/raw/` | [uso de `make leerDatos`](https://raw.githubusercontent.com/isbelloq/mlds6/main/makefile) | [Reporte al demo de secop](https://github.com/isbelloq/mlds6/raw/main/docs/data/secop_summary.html)|


* **Resumen de SECOP I**: El resumen de los datos se encuentra en el [siguiente enlace](https://github.com/isbelloq/mlds6/raw/main/docs/data/secop_summary.html)


## Datos procesados
| Processed Dataset Name | Input Dataset(s)   | Data Processing Tools/Scripts | Link to Report |
| ---:| ---: | ---: | ---: | 
| Processed Dataset 1 | [Dataset1](link/to/dataset1/report), [Dataset2](link/to/dataset2/report) | [Python_Script1.py](link/to/python/script/file/in/Code) | [Processed Dataset 1 Report](link/to/report1)|
| Processed Dataset 2 | [Dataset2](link/to/dataset2/report) |[script2.R](link/to/R/script/file/in/Code) | [Processed Dataset 2 Report](link/to/report2)|
* Processed Data1 summary. <Provide brief summary of the processed data, such as why you want to process data in this way. More detailed information about the processed data should be in the Processed Data1 Report.>
* Processed Data2 summary. <Provide brief summary of the processed data, such as why you want to process data in this way. More detailed information about the processed data should be in the Processed Data2 Report.> 

## Feature Sets

| Feature Set Name | Input Dataset(s)   | Feature Engineering Tools/Scripts | Link to Report |
| ---:| ---: | ---: | ---: | 
| Feature Set 1 | [Dataset1](link/to/dataset1/report), [Processed Dataset2](link/to/dataset2/report) | [R_Script2.R](link/to/R/script/file/in/Code) | [Feature Set1 Report](link/to/report1)|
| Feature Set 2 | [Processed Dataset2](link/to/dataset2/report) |[SQL_Script2.sql](link/to/sql/script/file/in/Code) | [Feature Set2 Report](link/to/report2)|

* Feature Set1 summary. <Provide detailed description of the feature set, such as the meaning of each feature. More detailed information about the feature set should be in the Feature Set1 Report.>
* Feature Set2 summary. <Provide detailed description of the feature set, such as the meaning of each feature. More detailed information about the feature set should be in the Feature Set2 Report.> 
