# Project Charter

## Business background

* Who is the client, what business domain the client is in.

La Agencia Nacional de Contratación Pública - Colombia Compra Eficiente (ANCPCCE) es la entidad del gobierno de Colombia *encargada de desarrollar e impulsar políticas públicas y herramientas, orientadas a la organización y articulación, de los partícipes en los procesos de compras y contratación pública* (Tomado de [Colombia Compra Eficiente/Nuestra misión](https://colombiacompra.gov.co/colombia-compra/colombia-compra-eficiente/nuestra-mision)). Una de las herramientas que dispone para cumplir su mision es la platafomra SECOP I en donde *las Entidades Estatales deben publicar los Documentos del Proceso, desde la planeación del contrato hasta su liquidación* (Tomado de [Colombia Compra Eficiente/SECOP I](https://colombiacompra.gov.co/secop/secop-i)).


   
* What business problems are we trying to address?
  Caracterizar los contratos liquidados en el 2018 para determinar variables relevantes en la identificación de sobrecostos

## Scope
* What data science solutions are we trying to build?
  
  Determinar un modelo de datos que ayude a identificar anticipadamente los contratos propensos a tener sobrecosto.
* What will we do?
  1. Análisis exploratorio de datos para identificar las variables relevantes en la identificación de sobrecostos
  2. Ingeniería de características que sirvan para alimentar el entrenamiento y la validación del modelo.
  3. Generación del un modelo que identifique los contratos propensos a tener sobrecostos.
  
* How is it going to be consumed by the customer?
  
  La entidad tendrá acceso a un API que apoye en la identificación temprana de contratos con sobrecostos. Este API le permitirá a ANCPCCE tomar acciones  orientadas a la disminución de contratos con estas características.

## Personnel
* Who are on this project:
	* MLDS6_SBKFCP:
		* Project lead:
    		* Juan Lara
		* PM:
    		* Santiago Bello
		* Data scientist(s):
    		* Santiago Bello
    		* Kendy Luz Fuentes
    		* Carlos Pinto
		* Account manager:
    		* Kendy Luz Fuentes
	* Client:
		* Data administrator:
    		* Melissa de la Pava
		* Business contact:
    		* Melissa de la Pava
	
## Metrics
* What are the qualitative objectives? (e.g. reduce user churn) *Generar un modelo predictivo que permita detectar las licitaciones propensas a tener sobrecostos en la contratación pública*
* What is a quantifiable metric  (e.g. reduce the fraction of users with 4-week inactivity) *Reducir el porcentaje de sobrecostos con respecto al total de proyectos en proceso de licitación.*
* Quantify what improvement in the values of the metrics are useful for the customer scenario (e.g. reduce the  fraction of users with 4-week inactivity by 20%) *Reducir el porcentaje de sobrecostos con respecto al total de proyectos en proceso de licitación a un solo dígito.*
* What is the baseline (current) value of the metric? (e.g. current fraction of users with 4-week inactivity = 60%) *El porcentaje actual de sobrecostos es el 11.7%*
* How will we measure the metric? (e.g. A/B test on a specified subset for a specified period; or comparison of performance after implementation to baseline)

## Plan
* Phases (milestones), timeline, short description of what we'll do in each phase.
1. Entendimiento del negocio.
2. Diseño de arquitectura.
3. Exploración de datos de SECOP-I para el año 2018.
4. Preparación de datos
   1. Limpieza
   2. Transformación
   3. Ingeniería de características
5. Implementación del modelo
6. Evaluación del modelo
7. Despliegue del modelo

## Architecture
* Data
  * What data do we expect? Raw data in the customer data sources (e.g. on-prem files, SQL, on-prem Hadoop etc.) *Conjunto de datos abiertos https://www.datos.gov.co/Gastos-Gubernamentales/SECOP-I/xvdy-vvsk consumibles por peticiones API que generan archivos .json*
* Data movement from on-prem to Azure using ADF or other data movement tools (Azcopy, EventHub etc.) to move either
*Consumo del API en Python para almacenamiento de datos en Google Drive para uso posterior en Google Colab*  
  * all the data, 
  * after some pre-aggregation on-prem,
  * Sampled data enough for modeling 

* What tools and data storage/analytics resources will be used in the solution e.g.,
  
  *Almacenamiento: Google Drive*

  *Procesamiento: Google Colab (lenguaje de programación Python)*

  *Despliegue: Docker u otro*
  * ASA for stream aggregation
  * HDI/Hive/R/Python for feature construction, aggregation and sampling
  * AzureML for modeling and web service operationalization
* How will the score or operationalized web service(s) (RRS and/or BES) be consumed in the business workflow of the customer? If applicable, write down pseudo code for the APIs of the web service calls.
  * How will the customer use the model results to make decisions
  * Data movement pipeline in production
  * Make a 1 slide diagram showing the end to end data flow and decision architecture
    * If there is a substantial change in the customer's business workflow, make a before/after diagram showing the data flow.

## Communication
* Se usará el grupo de whatsapp https://chat.whatsapp.com/GCrUf5AMswb52VpkOSurWG para centralizar las comunicaciones internas del grupo de trabajo.
* Se usará la plataforma de campuswire para la comunicación con los product owner https://campuswire.com/c/G97B62515/rooms/C98D336EC
