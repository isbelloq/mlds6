from mlds6.preprocessing.cleaning import preprocess_pipe
from mlds6.database.io import load_table, export_table
from mlds6.environment.base import get_data_paths

def main():
    paths = get_data_paths()
    df = load_table(paths.raw_data, 'datos_secop_2016', 'json')
    
    for year in range(2017, 2020):
        df = df.append(load_table(paths.raw_data, f'datos_secop_{year}', 'json'))
        
    df = df.reset_index()
    df = preprocess_pipe(df)
    export_table(paths.preprocessed_data, 'out', 'parquet', df)

if __name__ == "__main__":
    main()
