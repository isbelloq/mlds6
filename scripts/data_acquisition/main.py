
from collect import saveSecopJSON
import os

if __name__=="__main__":
    BASE_DIRECTORY = os.environ['DATA_PATH']

    saveSecopJSON(2018, dest=os.path.join(BASE_DIRECTORY,'raw'))
    saveSecopJSON(2017, dest=os.path.join(BASE_DIRECTORY,'raw'))
    saveSecopJSON(2016, dest=os.path.join(BASE_DIRECTORY,'raw'))
    saveSecopJSON(2019, dest=os.path.join(BASE_DIRECTORY,'raw'))

    

