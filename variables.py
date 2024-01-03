from datetime import datetime
import uuid
from dotenv import load_dotenv
import os

load_dotenv()

dir_descarga = os.getenv('DIR_DESCARGA')
ftp_hostname = os.getenv('FTP_IP')
ftp_username = os.getenv('FTP_USER')
ftp_password = os.getenv('FTP_PASS')
dir_entrada = 'upload/Reporte Socios/'
fecha = datetime.now().strftime("%Y%m%d")
#archivo = 'socios_nuevos_20231228.csv'
archivo = f'socios_nuevos_{fecha}.csv'
sql_server = os.getenv('SQL_IP')
database = os.getenv('SQL_DATABASE')
sql_username = 'sa'
sql_password = os.getenv('SQL_PASS')
table_name = 'contact'
driver = 'ODBC Driver 17 for SQL Server'



def new_id() -> str:
    unique_id = str(uuid.uuid4())
    return "'" + unique_id + "'"


def getdate():
    current_time = datetime.now()
    formatted_time = current_time.strftime('%Y-%m-%dT00:00:00')
    return "'" + str(formatted_time) + "'"


def format_rut(rut: str) -> str:
    dv = rut[-1]
    if len(rut) == 9:
        num_rut = rut[0:2] + "." + rut[2:5] + "." + rut[5:8]
    else:
        num_rut = rut[0] + "." + rut[1:4] + "." + rut[4:7]
    newrut = "'" + num_rut + '-' + dv + "'"
    return newrut

