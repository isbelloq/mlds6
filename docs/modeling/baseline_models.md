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
* Se construyeron modelos de regresión logística, árboles de decision, bosques aleatorios y una red neuronal multicapa.En este caso se documenta el primer modelo que se empleó (Regresión logística).

## Model Description

#### Regresión logística
* Se emplea un modelo de regresión logística, con los siguientes criterios:
  * Penalty: ["l1", "l2"]
  * C: [5, 10, 15, 20]
  * solver: ["liblinear", "saga"]
#### Árboles de decisión
* Se emplea un modelo de arboles de decisión, con los siguientes criterios:
    * criterion: ["gini", "entropy"],
    * max_depth: [5, 10, 15, 20, 25]
#### Bosque aleatorios
* Se emplea un modelo de arboles de decisión, con los siguientes criterios:
  
    * n_estimators: [25, 50, 100]
    * criterion: ["gini", "entropy"]
    * max_depth: [5, 10, 15]
#### Red neuronal multicapa
Se emplea el siguiente diseño de red neuronal multicapa, con los siguientes hiperparámetros

| Nombre capa    | Total de neuronas | Función de activación | relación dropout |
|----------------|-------------------|-----------------------|------------------|
| input          | 102               |                       |                  |
| den1           | 125               | tanh                  |                  |
| den2           | 1025              | softmax               |                  |
| den3           | 250               | softmax               |                  |
| den4           | 50                | softmax               |                  |
| den5           | 30                | tanh                  |                  |
| den6           | 10                | softmax               |                  |
| act            |                   | softmax               |                  |
| drop1(dropout) |                   |                       | 0.2              |
| den5           | 5                 | softmax               |                  |
| sobrecosto     | 1                 | tanh                  |                  |

optimizador: Adam Learning Rate 1e-3
Loss: Binary CrossEntropy



## Results (Model Performance)

### Regresión Logística

El desempeño de los modelos se midió basado en cuatro métricas y el mejor resultado se encuentra a continuación

| label    | Precision | recall | f1-score |
|----------|-----------|--------|----------|
| 0        | 0.68      | 0.76   | 0.72     |
| 1        | 0.59      | 0.48   | 0.53     |

Accuracy = 0.65
Estos resultados se obtuvieron usando los siguientes hiperparámetros
 * c=10
 * penalty= 'l1'
 * solver = 'liblinear'

### Árboles de decision

| Label 	| Precision 	| recall 	| f1- score 	|
|-------	|-----------	|--------	|-----------	|
| 0     	| 0.69      	| 0.84   	| 0.76      	|
| 1     	| 0.67      	| 0.46   	| 0.54      	|
 
Accuracy = 0.68
Estos resultados se obtuvieron usando los siguientes hiperparámetros
* criterion = gini
* max_depth = 25

### Bosques aleatorios
| Label 	| Precision 	| recall 	| f1- score 	|
|-------	|-----------	|--------	|-----------	|
| 0     	| 0.66      	| 0.90   	| 0.76      	|
| 1     	| 0.70      	| 0.34   	| 0.46      	|
Accuracy = 0.67
Estos resultados se obtuvieron usando los siguientes hiperparámetros

 * criterion = gini
 * max_depth = 15
 * n_estimators = 50
#### Red neuronal multicapa


| Label 	| Precision 	| recall 	| f1- score 	|
|-------	|-----------	|--------	|-----------	|
| 0     	| 0.50      	| 1.00   	| 0.67      	|
| 1     	| 0.00      	| 0.00   	| 0.00      	|

Accuracy = 0.5
## Model Understanding
### Regresión logística
Las variables mas importantes en este modelo se presentan en la siguiente tabla.
| Variable transformada                                                    | Importancia |
|--------------------------------------------------------------------------|-------------|
| objeto a contratar: Productos para Relojería, Joyería y Piedras Preciosas | 3.70492147  |
| origen de los recursos: Recursos privados/cooperación                     | 2.87804381  |
| departamento entidad: MAGDALENA                                           | 2.64476511  |
| departamento entidad: AMAZONAS                                            | 2.5637476   |
| departamento entidad: LA GUAJIRA                                          | 1.99229361  |


* Objeto a contratar, departamento de la entidad  y origen de los recursos, son las que mejor nos ayudan a discriminar entre las dos clases en estudio.

* Los departamentos de Magdalena, Amazonas y La Guajira. discriman bien si se pueden presentar sobrecostos en los proyectos o no.
  
* Los objetos a contratar productos para relojería, Joyería y piedras precioas es el que mejor discrimina este fenómeno.

###	Árbol de decisión
Las variables mas importantes en este modelo se presentan en la siguiente tabla.


| Variable transformada                                            | Importancia |
|------------------------------------------------------------------|-------------|
| Departamento entidad: BOGOTÁ D.C.                                | 0.08385778  |
| Origen de los recursos: Sistema General de Participaciones - SGP | 0.0744165   |
| Objeto a contratar:Servicios de Salud                            | 0.06012829  |
| Objeto a contratar: Servicios Profesionales y Administrativos    | 0.05729308  |
| Departamento entidad: NARIÑO                                     | 0.04963427  |


* Objeto a contratar, departamento de la entidad, origen de los recursos y tipo de persona, son las que mejor nos ayudan a discriminar entre las dos clases en estudio.

* Los departamentos de Nariño y Bogotá D.C. discriman bien si se pueden presentar sobrecostos en los proyectos o no.
  
* Los objetos a contratar servicios de salud, y servicios profesionales y administrativos son las categorías que mejor discriminan este fenómeno.

### Bosques aleatorios

Las variables mas importantes en este modelo se presentan en la siguiente tabla.

| Variable transformada                                            | Importancia |
|------------------------------------------------------------------|-------------|
| Origen de los recursos: Sistema general de Participaciones - SGP | 0.08951     |
| Departamento entidad: Nariño                                     | 0.06999     |
| Departamento entidad: Bogotá D.C                                 | 0.05644     |
| Departamento entidad: Santander                                  | 0.05313     |
| Departamento entidad: Casanare                                   | 0.05164     |

* Con este modelo identificamos dos variables que permite determinar si un proyecto va a presentar sobrecostos o no. Estas variables son: Departamento de la entidad y origen de los recursos.Los departamentos que mejor discriminan son Nariño, Santander , Casanare y Bogotá D.C para este modelo, así como el origen de los recursos del sistema general de de participaciones.
## Conclusion and Discussions for Next Steps

* El fenómeno de estudio tiene una baja incidencia sin embargo las cuantías involucradas son altas. 
  
* No logramos incluir la variable cuantía del contrato debido a la varianza de la misma ya que a pesar de realizarle distintas transformaciones mantenía su dispersion. Por lo anterior proponemos para una próxima iteracion categorizar la variable cuantía del contrato por rango.
  
* Presentamos problemas de convergencia en el modelo de regresión logśitica lo cual obligó a aumentar el número máximo de iteraciones así como probar otros modelos. Al revisar las variables más relevantes no encontramos una relación directa entre ellas y los sobrecostos de los proyectos.
  
* Se evidencia que la variable departamento es común en todos los modelos. Sin embargo cada modelo identifica como relevantes categorías diferentes de esta variable. Así como el origen de recursos.
