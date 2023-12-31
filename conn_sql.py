import pyodbc
from pandas import read_csv
from variables import *
import pandas


connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={sql_server};DATABASE={database};UID={sql_username};PWD={sql_password}'


engine = pyodbc.connect(connection_string)
cursor = engine.cursor()
select = f'select * from {table_name}'
archivo = read_csv('socios_nuevos_20231230.csv')


def crea_insert(line: pandas.DataFrame) -> str:
    id = new_id()
    new_canal = '20'
    new_suscriptorrmactiva = '0'
    new_region = '8EDED6DA-7FE8-E811-A971-000D3AC1BB19'
    new_ciudad = 'BF7FDD22-60CC-EA11-A812-000D3AC0A0B3'
    modifiedby = 'null'
    new_pais = 'C1876847-CBE5-E811-A979-000D3AC02DD5'
    new_comuna = 'None'  # TODO buscar coomuna en base de datos
    new_nombrerepresentantelegal = 'null'
    mobilphone = f'{line.celular}' # TODO rescatar del csv
    accountidyominame = 'null'
    address1_line1 = f'{line.comuna}'  # TODO rescatar del csv
    modifiedonbehalfbyname = 'null'
    new_girodelaempresa = 'null'
    birthdate = f'{line.fecha_nacimiento}' + 'T00:00:00'  # TODO rescatar del csv
    createdon = getdate()
    emailaddress1 = f'{line.mail}'  # TODO rescatar del csv
    firstname = f'{line.nombre}'  # TODO rescatar del csv
    modifiedon = getdate()
    versionnumber = 'null'
    new_rutdelrepresentantelegal = 'null'
    modifiedonbehalfbyyominame = getdate()
    fullname = f'{line.nombre}'  # TODO rescatar del csv MISMO DEL NOMBRE
    lastname = f'{line.nombre}'  # TODO rescatar del csv
    new_rut = format_rut(f'{line.rut}')  # TODO rescatar del csv
    # TODO ordenar el insert con todos los campos
    # TODO formatear con comas y con comillas simples para los campos varchar

    # new_insert = insert + id + "," + new_canal + "," + new_suscriptorrmactiva + "," + new_region + "," + new_ciudad + "," + modifiedby + "," +new_pais + "," +new_comuna + "," + new_nombrerepresentantelegal + "," + mobilphone + "," + accountidyominame + "," + address1_line1
    # new_insert = new_insert + "," + modifiedonbehalfbyname + "," + new_girodelaempresa + "," + birthdate + "," + createdon + "," + emailaddress1 + "," + firstname + "," + modifiedon + "," + versionnumber + "," + new_rutdelrepresentantelegal + modifiedonbehalfbyyominame
    # new_insert = new_insert + "," + fullname + "," + lastname + "," + new_rut
    # print(new_insert)

    cursor.execute(insert, id, new_canal, new_suscriptorrmactiva, new_region, new_ciudad,
                   modifiedby, new_pais, new_comuna, new_nombrerepresentantelegal,
                   mobilphone, accountidyominame, address1_line1, modifiedonbehalfbyname,
                   new_girodelaempresa, birthdate, createdon, emailaddress1, firstname,
                   modifiedon, versionnumber, new_rutdelrepresentantelegal,
                   modifiedonbehalfbyyominame, fullname, lastname, new_rut)