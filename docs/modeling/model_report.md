# Baseline Model Report

A continuación haremos una descripción de la fase de modelamiento de los datos.

## Analytic Approach
* Nuestra variable objetivo es el sobrecosto, la cual identifica con 1 los registros en donde el valor total de las adiciones sea superior al 20% de la cuantía del contrato o 0 en otro caso
* Nuestras variables predictoras son las siguientes:
	* Objeto a contratar: actividad economica del objetivo del contrato.
	* Departamento entidad: Departamento de la ejecución del contrato.
	* Tipo persona: Esta variable identifica si el contratista es una persona natural o jurídica.
	* Origen de los recursos: Identificador de la forma en que se consiguen los recursos con los que se va a pagar el contrato.
* Como los proyectos con sobrecosto eran menos del 10% del total de la base, decidimos hacer oversampling sobre la categoría con sobrecosto.
* Se construyeron modelos de regresión logística, árboles de decision, bosques aleatorios y una red neuronal multicapa. Elgiendo el modelo con mejor desempeño en este caso fue un árbol de decisión.

## Solution Description
* Simple solution architecture (Data sources, solution components, data flow)
  
* La variable de salida es si el contrato presentaría sobrecosto o no.
  
## Data
* Source
* Data Schema
* Sampling
* Selection (dates, segments)
* Stats (counts)

## Algorithm
* Description or images of data flow graph
  * if AzureML, link to:
    * Training experiment
    * Scoring workflow
* What learner(s) were used?
* Learner hyper-parameters
-------
Para la eleccion del modelo se realiza una busqueda de hiperparámetros con las siguientes combinaciones.
  * max_depth : [5,10,15,20,25],
  * criterion : ['gini', 'entropy']
  * numero de pliegues: 5
  * scoring : F1
  
Empleando estos parámteros se consiguió el siguiente modelo.
  
  * criterio: 'gini'
  * max_depth: 25
  
## Features
* List of raw and derived features 
* Importance ranking.



