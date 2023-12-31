import pandas as pd
from conn_sql import crea_insert
from modulo1 import limpia_csv
from variables import *

archivo = pd.read_csv('socios_nuevos_20231230.csv')


new_canal = 20
new_suscriptorrmactiva = 0
new_region = '8EDED6DA-7FE8-E811-A971-000D3AC1BB19'
new_ciudad = 'BF7FDD22-60CC-EA11-A812-000D3AC0A0B3'
modifiedby = 'null'
new_pais = 'C1876847-CBE5-E811-A979-000D3AC02DD5'
accountidyominame = 'null'
modifiedonbehalfbyname = 'null'
new_girodelaempresa = 'null'
createdon = getdate()
versionnumber = 'null'
modifiedon = getdate()
new_nombrerepresentantelegal = 'null'
new_rutdelrepresentantelegal = 'null'
modifiedonbehalfbyyominame = getdate()


if __name__=='__main__':

    for i in archivo.itertuples():
       crea_insert(i)

    #print(archivo.get('celular'))
    """
    if descarga_archivo_csv():
        limpia_csv()
        print(archivo)
    """