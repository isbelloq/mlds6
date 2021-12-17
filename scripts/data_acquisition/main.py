
from mlds6.database.collect import saveSecopJSON, obtener_convocados
from mlds6.environment.base import get_data_paths
from mlds6.database.io import export_table
from argparse import ArgumentParser

def main():
    parser = ArgumentParser()
    parser.add_argument('--convocados', '-c',
                        dest='convocados',
                        action='store_true',
                        help="load convocados data")
    args = parser.parse_args()
    data_paths = get_data_paths()

    for year in range(2016, 2021):
        if args.convocados:
            filename = f'convocados_{year}'
            df = obtener_convocados(year)
            export_table(data_paths.raw_data,
                         filename,
                         'parquet',
                         df)
            print(f'filename {filename} saved')
        else:
            saveSecopJSON(year, dest=data_paths.raw_data)


if __name__ == "__main__":
    main()