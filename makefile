

leerDatos:
	source mlds6.env && python scripts/data_acquisition/main.py 

eda:
	source mlds6.env && \
	python scripts/eda/main.py 

runJupyter:
	source mlds6.env && jupyter notebook