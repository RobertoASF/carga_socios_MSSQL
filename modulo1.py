import os, sys
from variables import *
from conn_sql import busca_rut

clean_csv = 'clean_' + archivo
headers = "nombre,rut,mail,celular,fecha_nacimiento,obra,fechadonacion,comuna,captador,monto,moneda,mediopago"

if len(sys.argv) >= 2:
    fecha = sys.argv[1]
    archivo = f'socios_nuevos_{fecha}.csv'

def separa_rut(linea: str) -> str:
    new_linea = linea.split(",")
    rut = format_rut(new_linea[1])
    return rut


def limpia_csv():
    with open(archivo, 'r', encoding='utf-8') as archivo_csv:
        leido = archivo_csv.readlines()
        clear = []
        [clear.append(_.replace('"', '')) for _ in leido]
        clear = set(clear)

    with open(clean_csv, 'w', encoding='utf-8') as archivo_csv:
        archivo_csv.write(headers + "\n")

    with open(clean_csv, 'a', encoding='utf-8') as archivo_csv:
        for linea in clear:
            if linea.startswith('nombre'):
                pass
            else:
                rut = separa_rut(linea)
                if not busca_rut(rut):
                    archivo_csv.write(linea)
                else:
                    print(f'RUT: {rut} ya existe en base de datos')

    if os.path.exists(clean_csv):
        os.remove(archivo)
        os.renames(clean_csv, archivo)

