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

* Se emplea un modelo de regresión logística, con los siguientes criterios:
  * C: 15
  * max_iter: 1000




## Results (Model Performance)
El desempeño de los modelos se midió basado en cuatro métricas y el mejor resultado se encuentra a continuación

| label    | Precision | recall | f1-score |
|----------|-----------|--------|----------|
| 0        | 0.68      | 0.76   | 0.72     |
| 1        | 0.59      | 0.48   | 0.53     |

Accuracy 0.65



## Model Understanding

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

## Conclusion and Discussions for Next Steps

* El fenómeno de estudio tiene una baja incidencia sin embargo las cuantías involucradas son altas. 
  
* No logramos incluir la variable cuantía del contrato debido a la varianza de la misma ya que a pesar de realizarle distintas transformaciones mantenía su dispersion. Por lo anterior proponemos para una próxima iteracion categorizar la variable cuantía del contrato por rango.
  
* Presentamos problemas de convergencia lo cual obligo a aumentar el número máximo de iteraciones así como probar otros modelos. Al revisar las variables más relevantes no encontramos una relación directa entre ellas y los sobrecostos de los proyectos.