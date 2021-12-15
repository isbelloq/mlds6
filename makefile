SHELL := /usr/bin/bash

leerDatos:
	source mlds6.env && python scripts/data_acquisition/main.py 

eda:
	source mlds6.env && \
	python scripts/eda/main.py 

runPreprocessing:
	source mlds6.env && \
	python scripts/preprocessing/main.py

runJupyter:
	source mlds6.env && jupyter notebook

runEvaluation:
	source mlds6.env && python scripts/evaluation/main.py --model LogisticRegression
	
runIpython:
	source mlds6.env && ipython