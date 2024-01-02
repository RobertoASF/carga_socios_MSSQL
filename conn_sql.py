import pyodbc
from variables import *

connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={sql_server};DATABASE={database};UID={sql_username};PWD={sql_password}'
engine = pyodbc.connect(connection_string)
engine.setdecoding(pyodbc.SQL_CHAR, encoding='utf-8')
cursor = engine.cursor()


def get_table_fields(tabla: str) -> list:
    fields = cursor.execute(f"""
    SELECT
    COLUMN_NAME
    FROM
    INFORMATION_SCHEMA.COLUMNS
    WHERE
    TABLE_NAME = '{tabla}';
    """).fetchall()
    fields = [str(_[0]) for _ in fields]
    return fields


def get_comuna(comuna: str) -> str:
    comuna = comuna.upper()
    try:
        comunaid = cursor.execute(
            f"SELECT DISTINCT NEW_COMUNAID FROM DBO.NEW_COMUNA WHERE UPPER(NEW_NAME) = '{comuna}' ").fetchone()
        return "'" + comunaid[0] + "'"
    except:
        comunaid = 'NULL'
        return comunaid


campos = get_table_fields(f'{table_name}')


def make_insert(line):
    valores = {
        'Id': new_id().upper(),
        'new_canal': '20',
        'new_suscriptorrmactiva': '0',
        'new_region': "'8EDED6DA-7FE8-E811-A971-000D3AC1BB19'",
        'new_ciudad': "'BF7FDD22-60CC-EA11-A812-000D3AC0A0B3'",
        'modifiedby': 'NULL',
        'new_pais': "'C1876847-CBE5-E811-A979-000D3AC02DD5'",
        'new_comuna': get_comuna(line.comuna),
        'new_nombrerepresentantelegal': 'NULL',
        'mobilephone': f"'{line.celular}'",
        'accountidyominame': 'NULL',
        'address1_line1': f"'{line.comuna}'",
        'modifiedonbehalfbyname': 'NULL',
        'new_girodelaempresa': 'NULL',
        'birthdate': "'" + f'{line.fecha_nacimiento}' + "T00:00:00'",
        'createdon': getdate(),
        'emailaddress1': f"'{line.mail}'".lower(),
        'firstname': f"'{line.nombre}'",
        'modifiedon': getdate(),
        'versionnumber': 'NULL',
        'new_rutdelrepresentantelegal': 'NULL',
        'modifiedonbehalfbyyominame': getdate(),
        'fullname': f"'{line.nombre}'",
        'lastname': f"'{line.nombre}'",
        'new_rut': format_rut(f'{line.rut}')}

    campos_str = ", ".join(campos)
    valores_str = ", ".join([valores[campo] for campo in campos if campo in valores])
    new_insert = f"INSERT INTO {table_name} ({campos_str}) VALUES\n ({valores_str});"
    print(f'ejecutando insert del rut {valores.get("new_rut")} ')
    cursor.execute(new_insert)
    cursor.commit()
