import sys
import pandas as pd
from conn_sql import make_insert
from descarga_csv import descarga_archivo_csv
from modulo1 import limpia_csv
from variables import archivo

if __name__ == '__main__':
    if len(sys.argv) >= 2:
        fecha = sys.argv[1]
        archivo = f'socios_nuevos_{fecha}.csv'

    if descarga_archivo_csv():
        limpia_csv()
        clear_csv = pd.read_csv(archivo)
        try:
            for each in clear_csv.itertuples():
                try:
                    make_insert(each)
                except Exception as e:
                    print(f'Error: {e}')
        except Exception as e:
            print(f'Error al realizar insert: {e}')
