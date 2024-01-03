import pysftp,sys
from variables import *


cnopts = pysftp.CnOpts()
cnopts.hostkeys = None

if len(sys.argv) >= 2:
    fecha = sys.argv[1]
    archivo = f'socios_nuevos_{fecha}.csv'

def valida_archivo() -> bool:
    with pysftp.Connection(ftp_hostname, username=ftp_username, password=ftp_password, cnopts=cnopts) as sftp:
        sftp.chdir(dir_entrada)
        in_ftp = sftp.listdir()
        if archivo in in_ftp:
            return True
        else:
            return False


def descarga_archivo():
    with pysftp.Connection(ftp_hostname, username=ftp_username, password=ftp_password, cnopts=cnopts) as sftp:
        sftp.chdir(dir_entrada)
        in_ftp = sftp.listdir()
        local_path = os.path.join(dir_descarga, archivo)
        if archivo in in_ftp:
            try:
                sftp.get(archivo,local_path)
            except Exception as e:
                print(f'Error: {e}')


def descarga_archivo_csv():
    if valida_archivo():
        print(f'Descargando {archivo}')
        descarga_archivo()
        return True
    else:
        print('El archivo no existe')
        return False
