import pyodbc
from pandas import read_csv
from variables import *
import pandas


connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={sql_server};DATABASE={database};UID={sql_username};PWD={sql_password}'
engine = pyodbc.connect(connection_string)
engine.setdecoding(pyodbc.SQL_CHAR, encoding='utf-8')
cursor = engine.cursor()
select = f'SELECT * FROM {table_name}'
archivo = read_csv('socios_nuevos_20231230.csv')


def get_comuna(comuna: str) -> str:
    comuna = comuna.upper()
    comunaid = cursor.execute(f"SELECT NEW_COMUNAID FROM DBO.NEW_COMUNA WHERE UPPER(NEW_NAME) = '{comuna}'").fetchall()
    return "'" + comunaid[0][0] + "'"


def crea_insert(line):
    id_sql = "'8EDED6DA-7FE8-E811-A971-000D3AC1BB19'"
    new_canal = '20'
    new_suscriptorrmactiva = '0'
    new_region = "'8EDED6DA-7FE8-E811-A971-000D3AC1BB19'"
    new_ciudad = "'BF7FDD22-60CC-EA11-A812-000D3AC0A0B3'"
    modifiedby = 'NULL'
    new_pais = "'C1876847-CBE5-E811-A979-000D3AC02DD5'"
    new_comuna = get_comuna(f'{line.comuna}')  # TODO buscar coomuna en base de datos
    new_nombrerepresentantelegal = 'NULL'
    mobilphone = f"'{line.celular}'"  # TODO rescatar del csv
    accountidyominame = 'NULL'
    address1_line1 = f"'{line.comuna}'"  # TODO rescatar del csv
    modifiedonbehalfbyname = 'NULL'
    new_girodelaempresa = 'NULL'
    birthdate = f'{line.fecha_nacimiento}'  # TODO rescatar del csv
    createdon = getdate()
    emailaddress1 = f"'{line.mail}'"  # TODO rescatar del csv
    firstname = f"'{line.nombre}'"  # TODO rescatar del csv
    modifiedon = getdate()
    versionnumber = 'NULL'
    new_rutdelrepresentantelegal = 'NULL'
    modifiedonbehalfbyyominame = getdate()
    fullname = f"'{line.nombre}'"  # TODO rescatar del csv MISMO DEL NOMBRE
    lastname = f"'{line.nombre}'"  # TODO rescatar del csv
    new_rut = format_rut(f'{line.rut}')  # TODO rescatar del csv

    new_insert = old_insert + id_sql + "," + new_canal + "," + new_suscriptorrmactiva + "," + new_region + "," + new_ciudad + "," + modifiedby + "," +new_pais + "," +new_comuna + "," + new_nombrerepresentantelegal + "," + mobilphone + "," + accountidyominame + "," + address1_line1
    new_insert = new_insert + "," + modifiedonbehalfbyname + "," + new_girodelaempresa + "," + birthdate + "," + createdon + "," + emailaddress1 + "," + firstname + "," + modifiedon + "," + versionnumber + "," + new_rutdelrepresentantelegal + "," + modifiedonbehalfbyyominame
    new_insert = new_insert + "," + fullname + "," + lastname + "," + new_rut + ");"
    print(f'ejecutando insert del rut {new_rut} ')
    cursor.execute(new_insert)
    cursor.commit()
    cursor.close()
