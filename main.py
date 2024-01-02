import pandas as pd
from conn_sql import make_insert
from descarga_csv import descarga_archivo_csv
from modulo1 import limpia_csv
from variables import archivo


if descarga_archivo_csv():
    limpia_csv()
    clear_csv = pd.read_csv('socios_nuevos_20231228.csv')
    try:
        for each in clear_csv.itertuples():
            try:
                make_insert(each)
            except Exception as e:
                print(f'Error: {e}')
    except Exception as e:
        print(f'Error al realizar insert: {e}')
