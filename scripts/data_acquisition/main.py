
from mlds6.database.collect import saveSecopJSON
from mlds6.environment.base import get_data_paths

def main():
    data_path = get_data_paths()
    for year in range(2016,2020):
        saveSecopJSON(year, dest=data_path.raw_data)

if __name__=="__main__":
  main()

