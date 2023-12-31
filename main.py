import pandas as pd
from conn_sql import crea_insert
from descarga_csv import descarga_archivo_csv, valida_archivo, descarga_archivo
from modulo1 import limpia_csv
from variables import *

archivo = pd.read_csv('socios_nuevos_20231230.csv')


if descarga_archivo_csv():
    limpia_csv()
    try:
        [crea_insert(i) for i in archivo.itertuples()]
    except Exception as e:
        print(f'Error al realizar insert: {e}')
