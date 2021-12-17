from mlds6.preprocessing.cleaning import preprocess_pipe
from mlds6.database.io import load_table, export_table
from mlds6.environment.base import get_data_paths
from argparse import ArgumentParser

def main():
    parser = ArgumentParser()
    parser.add_argument('--convocados', '-c',
                        dest='convocados',
                        action='store_true',
                        help="load convocados data")
    args = parser.parse_args()
    data_paths = get_data_paths()
    
    if args.convocados:
        for year in range(2016,2021):   
            filename = f'convocados_{year}'
            extension = 'parquet'
            df = load_table(data_paths.raw_data, 
                            filename, 
                            extension)
            df = preprocess_pipe(df)
            export_table(data_paths.preprocessed_data,
                         filename,
                         extension,
                         df)
    else:
        df = load_table(data_paths.raw_data, 
                        'datos_secop_2016', 
                        'json')
        for year in range(2017, 2020):
            df = df.append(load_table(data_paths.raw_data, 
                                      f'datos_secop_{year}', 
                                      'json'))        
        df = df.reset_index()
        df = preprocess_pipe(df)
        
        export_table(data_paths.preprocessed_data, 'out', 'parquet', df)

if __name__ == "__main__":
    main()
