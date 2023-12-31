import os
archivo = 'socios_nuevos_20231230.csv'
clean_csv = 'clean_socios_nuevos_20231230.csv'
headers = "nombre,rut,mail,celular,fecha_nacimiento,obra,fechadonacion,comuna,captador,monto,moneda,mediopago"


def limpia_csv():
    with open(archivo, 'r', encoding='utf-8') as archivo_csv:
        leido = archivo_csv.readlines()
        clear = []
        [clear.append(_.replace('"','')) for _ in leido]
        clear = set(clear)

    with open(clean_csv, 'w', encoding='utf-8') as archivo_csv:
        archivo_csv.write(headers + "\n")

    with open(clean_csv, 'a', encoding='utf-8') as archivo_csv:
        for linea in clear:
            if linea.startswith('nombre'):
                pass
            else:
                archivo_csv.write(linea)

    if os.path.exists(clean_csv):
        os.remove(archivo)
        os.renames(clean_csv, archivo)
