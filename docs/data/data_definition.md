# Definición de datos y características

Los datos están disponibles como formato json en la plataforma de datos abiertos, que se obtienen a traves de la [api](https://www.datos.gov.co/resource/xvdy-vvsk.json)
 
Con el proyecto de Datos Abiertos, el Gobierno Colombiano promueve la transparencia, el acceso a la información pública, la competitividad, el desarrollo económico, y la generación de impacto social a través de la apertura, la reutilización de los datos públicos, y el uso y apropiación de las TIC.

La iniciativa de Datos Abiertos busca que todas las entidades del sector público publiquen la información pertinente y de calidad en formatos estructurados a disposición de los usuarios para que ellos y las entidades la utilicen de diferentes maneras, según su interés: generar informes, reportes, estadísticas, investigaciones, control social, oportunidades de negocio (ej. aplicaciones), entre otros temas.

Dicha información es compartida públicamente en datos.gov.co, en formatos digitales estandarizados con una estructura de fácil comprensión para que la misma pueda ser utilizada por los ciudadanos. Dado que son financiados y recopilados con dinero público, la información contenida en estos datos es pública y debe estar a disposición de cualquier ciudadano y para cualquier fin.



## Fuentes de datos brutos

| Dataset Name | Original Location   | Destination Location  | Data Movement Tools / Scripts | Link to Report |
| ---:| ---: | ---: | ---: | -----: |
| SECOP I | https://www.datos.gov.co/resource/xvdy-vvsk.json | `/home/mlds6_sbkfcp/data/raw/` | [uso de `make leerDatos`](https://raw.githubusercontent.com/isbelloq/mlds6/main/makefile) | [Reporte al demo de secop](https://github.com/isbelloq/mlds6/raw/main/docs/data/secop_summary.html)|


* **Resumen de SECOP I**: El resumen de los datos se encuentra en el [siguiente enlace](https://nash3025.github.io/)


## Datos procesados
| Processed Dataset Name | Input Dataset(s)   | Data Processing Tools/Scripts | Link to Report |
| ---:| ---: | ---: | ---: | 
| Processed Dataset 1 | [Dataset1](link/to/dataset1/report), [Dataset2](link/to/dataset2/report) | [Python_Script1.py](link/to/python/script/file/in/Code) | [Processed Dataset 1 Report](link/to/report1)|
| Processed Dataset 2 | [Dataset2](link/to/dataset2/report) |[script2.R](link/to/R/script/file/in/Code) | [Processed Dataset 2 Report](link/to/report2)|
* Processed Data1 summary. <Provide Para el  procesamiento de datos se tuvieron en cuenta las siguientes operaciones:
1. Filtros: Se filtraron los registron que tuvieran la cuantía de contrato y el valor del contrato con adiciones mayores a cero. Así como también los valores con NIT válido y que la moneda en la que se encontraba la cuantía del contrato sea peso colombiano.
2. Limpieza de nulos y duplicados: Elimina los registros sin datos y los registros duplicados en todos los valores de sus variables.
3. Creación de columnas: Se crearon las columnas Departamento de ejecución del contrato y tipo de persona para identificar si es persona jurídica o natural a partir del tipo de identificación del contratista. Finalmente se construyó la variable sobrecosto, la cual identifica con 1 los registros en donde el valor total de las adiciones sea superior al 20% de la cuantía del contrato o 0 en otro caso>


## Feature Sets

| Feature Set Name | Input Dataset(s)   | Feature Engineering Tools/Scripts | Link to Report |
| ---:| ---: | ---: | ---: | 
| Feature Set 1 | [Dataset1](link/to/dataset1/report), [Processed Dataset2](link/to/dataset2/report) | [R_Script2.R](link/to/R/script/file/in/Code) | [Feature Set1 Report](link/to/report1)|
| Feature Set 2 | [Processed Dataset2](link/to/dataset2/report) |[SQL_Script2.sql](link/to/sql/script/file/in/Code) | [Feature Set2 Report](link/to/report2)|

* Feature Set1 summary. <Provide Se realizaron 2 tipos de transformación en este dataset, por un lado se realizó OneHotEncoder en donde se crea una variable para cada categoría de las variables categóricas a las variables departaaamento de ejecución, objeto a contratar, tipo de persona y origen de los recursos. Por otro lado se hizo una transformación logarítmica a la variable cuantía del contrato.>
