# Project Charter

## Antecedentes

La Agencia Nacional de Contratación Pública - Colombia Compra Eficiente (ANCPCCE) es la entidad del gobierno de Colombia *encargada de desarrollar e impulsar políticas públicas y herramientas, orientadas a la organización y articulación, de los partícipes en los procesos de compras y contratación pública* (Tomado de [Colombia Compra Eficiente/Nuestra misión](https://colombiacompra.gov.co/colombia-compra/colombia-compra-eficiente/nuestra-mision)). Una de las herramientas que dispone para cumplir su mision es la platafomra SECOP I en donde *las Entidades Estatales deben publicar los Documentos del Proceso, desde la planeación del contrato hasta su liquidación* (Tomado de [Colombia Compra Eficiente/SECOP I](https://colombiacompra.gov.co/secop/secop-i)).

La entidad desea clasificar los contratos más susceptibles a tener sobrecostos en su ejecución.

## Alcance

El proyecto tiene como objetivo desarrollar un algoritmo de clasificación que ayude a identificar anticipadamente los contratos propensos a tener sobrecostos

Para la implementación del modelo se realizarán los siguiente pasos:
1. Extracción de los registros de SECOP I de la plataforma de [datos abiertos](https://www.datos.gov.co/Gastos-Gubernamentales/SECOP-I/xvdy-vvsk) cuyos contratos fueron firmados en el 2018 y su proceso se encuentre liquidado
2. Realizar un análisis exploratorio sobre el conjunto de datos para identificar las variables relevantes en la identificación de sobrecostos.
3. Entrenar y evaluar un modelo de clasificación usando técnicas de machine learning para detectar los contratos con sobrecostos.
4. Desplegar el modelo de clasificación para consumo de la entidad que le permita ingresar nuevos registros y detectar si tiene o no riesgos de sobrecostos.

La entidad tendrá acceso a un API donde se ingresarán los detalles del contrato (columnas del conjunto de datos del SECOP I) y se retornará si este registro tiene o no riesgo de sobrecosto.


## Personal

El equipo de trabajo de MLDS6_SBKFCP es:

|**Nombre**|**Rol**|**Email**|
|---|---|---|
|Juan Lara|Project lead/Solutions architect|julara@unal.edu.co|
|Santiago Bello|Data engineer/Data scientist|isbelloq@unal.edu.co|
|Kendy Luz Fuentes|Data scientist|kendyluz@gmail.com|
|Carlos Francisco Pinto Guerrero|Data scientist/Application developer|cfpintog@gmail.com|
|Fabian David Andres Moreno|Data engineer/Application developer|fabiandandres@gmail.com|

El equipo de trabajo de Agencia Nacional de Contratación Pública - Colombia Compra Eficiente (ANCPCCE) es:

|**Nombre**|**Rol**|**Email**|
|---|---|---|
|Juan Lara|Stakeholder|julara@unal.edu.co|
|Melissa de la Pava|Stakeholder|medel@unal.edu.co|

	
## Métricas


### Objetivos cualitativos
* Detectar los procesos propensos a tener sobrecostos en SECOP I

### Métricas de desempeño

Para evaluar el modelo de clasificación se usarán las métricas:
* Exactitud: fracción de datos predichos correctamente por el modelo
* Precisión: fracción de datos predichos de sobrecostos  clasificados correctamente
* Sensibilidad: fracción de datos con sobrecostos identificados correctamente
* Especificidad: fracción de datos sin sobrecostos identificados correctamente
* f1-score: combinación entre **precisión** y **sensibilidad**

Se le dará especial énfasis a la métrica de *f1-score* ya el el conjunto de datos es desbalanceado

Para obtener las métricas de desempeño del modelo se usará el método de validación cruzada con los datos extraídos de datos abiertos.

## Plan



||**Semana 1 -  22 Nov**|**Semana 2 -  29 Nov**|**Semana 3 -  5 Dic**|**Semana 4 -  12 Dic**|
|---|---|---|---|---|
|Entendimiento del negocio|[X]||||
|Extracción de datos||[X]|||
|Análisis exploratorio||[X]|||
|Entrenamiento del modelo|||[X]||
|Evaluación del modelo del modelo|||[X]||
|Despliegue del modelo||||[X]|



## Arquitectura

Todo el proceso de los datos estará soportado por la máquina virtual con ruta de acceso `mlds6_sbkfcp@35.209.123.29` con las siguientes especificaciones

```
OS: Ubuntu 20.04.3 LTS x86_64
Kernel: 5.11.0-1022-gcp
Shell: bash 5.0.17 
CPU: Intel Xeon (2) @ 2.199GHz 
Memory: 3928MiB 
```

A contuniación se detallan los diferentes componentes de la arquitectura.

### Datos
Los datos de SECOP-I se extraerán en formato `.json` del API https://www.datos.gov.co/resource/xvdy-vvsk.json 

### Movimiento de datos
Mediante un código en Python3 y con ayuda de la librería `request` se extraerán los datos de SECOP-I aplicando los filtros de año de firma del contrato 2018 y estado del proceso liquidado. El código en python almacenará la información en la ruta `/home/mlds6_sbkfcp/data/raw` de la máquina virtual disponible para el proyecto.

### Analítica de datos
Se toman los datos de `/home/mlds6_sbkfcp/data/raw` y se realizará el proceso de exploración de datos usando librerías típicas de ciencia de datos como lo son `numpy`, `pandas`, `scikit-learn`, `matplotlib` y`seaborn`.

### Despliegue
*Tentativo despliegue: Docker u otro. Posteriormente se especificará el diseño de API de consumo*


## Communication
* Se usará el grupo de whatsapp https://chat.whatsapp.com/GCrUf5AMswb52VpkOSurWG para centralizar las comunicaciones internas del grupo de trabajo.
* Se usará la plataforma de campuswire para la comunicación con los stakeholder https://campuswire.com/c/G97B62515/rooms/C98D336EC
