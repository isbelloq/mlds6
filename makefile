SHELL := /usr/bin/bash

leerDatos:
	source mlds6.env && python scripts/data_acquisition/main.py -c

eda:
	source mlds6.env && \
	python scripts/eda/main.py 

runPreprocessing:
	source mlds6.env && \
	python scripts/preprocessing/main.py -c

runJupyter:
	source mlds6.env && jupyter notebook

runEvaluation:
	source mlds6.env && python scripts/evaluation/main.py --model LogisticRegression
	
runIpython:
	source mlds6.env && ipython

runDashboard:
	source mlds6.env && python mlds6/visualization/main.py