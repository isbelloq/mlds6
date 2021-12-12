
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

## Model Description

* Empleando un metodo de busqueda óptima de hiperparametros, se determinó los parámetros con mejores resultados en las metricas los siguientes:
  * criterio: 'gini'
  * max_depth: 25

## Results (Model Performance)
El desempeño de los modelos se midió basado en cuatro métricas y el mejor resultado se encuentra a continuación
| label | Precision | recall | recall |
|-------|-----------|--------|--------|
| 0     | 0.69      | 0.84   | 0.76   |
| 1     | 0.67      | 0.46   | 0.54   |
Accuracy 0.68


## Model Understanding

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

## Conclusion and Discussions for Next Steps

* El fenómeno de estudio tiene una baja incidencia sin embargo las cuantías involucradas son altas. Despues de varios intentos encontramos un modelo que discrimina bien en la clase con sobrecosto y sin ellos.
  
* Es de resaltar que el modelo con mejor desempeño nos permite no solo predecir si un contrato va a tener sobrecostos o no, si no que además nos brinda cuales son las principales variables que describen ese comportamiento.

* No logramos incluir la variable cuantía del contrato debido a la varianza de la misma ya que a pesar de realizarle distintas transformaciones mantenía su dispersion. Por lo anterior proponemos para una próxima iteracion categorizar la variable cuantía del contrato por rango.
  
* Consideramos overfitting cuando el mejor parámetro para max_depth fue 25, sin embargo al revisar las métricas tanto en train como en test no encontramos grandes diferencias entre ellas y por lo tanto asumimos que no se presentó overfitting.

* Se podría revisar nuevamente el conjunto de variables completo sin embargo para este estudio lo revisamos y nos quedamos con las variables que nos podían dar mas información, no correlacionadas entre si y sin un alta cardinalidad.
