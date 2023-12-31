from datetime import datetime
import uuid


dir_descarga = '/home/roberto/Documentos/workspaces/Jesuitas'
ftp_hostname = '34.71.23.201'
ftp_username = 'fundacion_etas_2023'
ftp_password = 'N@oKn^WCpUwHP9&3'
dir_entrada = 'upload/Reporte Socios/'
fecha = datetime.now().strftime("%Y%m%d")
archivo = f'socios_nuevos_{fecha}.csv'
sql_server = '127.0.0.1'
database = 'master'
sql_username = 'sa'
sql_password = 'Valorant.0811'
table_name = 'usuarios'
driver = 'ODBC Driver 17 for SQL Server'

campos = ['Id', 'new_canal', 'new_suscriptorrmactiva', 'new_region', 'new_ciudad', 'modifiedby', 'new_pais',
              'new_comuna', 'new_nombrerepresentantelegal', 'mobilephone', 'accountidyominame', 'address1_line1',
              'modifiedonbehalfbyname', 'new_girodelaempresa', 'birthdate', 'createdon', 'emailaddress1', 'firstname',
              'modifiedon', 'versionnumber', 'new_rutdelrepresentantelegal', 'modifiedonbehalfbyyominame', 'fullname',
              'lastname', 'new_rut']

old_insert = """INSERT INTO [dbo].[contact] 
            ([Id]
           ,[new_canal]
           ,[new_suscriptorrmactiva]
           ,[new_region]
           ,[new_ciudad]
           ,[modifiedby]
           ,[new_pais]
           ,[new_comuna]
           ,[new_nombrerepresentantelegal]
           ,[mobilephone]
           ,[accountidyominame]
           ,[address1_line1]
           ,[modifiedonbehalfbyname]
           ,[new_girodelaempresa]
           ,[birthdate]
           ,[createdon]
           ,[emailaddress1]
           ,[firstname]
           ,[modifiedon]
           ,[versionnumber]
           ,[new_rutdelrepresentantelegal]
           ,[modifiedonbehalfbyyominame]
           ,[fullname]
           ,[lastname]
           ,[new_rut]) VALUES
           """

insert = """
INSERT INTO [dbo].[contact] (
    [Id], [new_canal], [new_suscriptorrmactiva], [new_region], [new_ciudad], 
    [modifiedby], [new_pais], [new_comuna], [new_nombrerepresentantelegal], 
    [mobilephone], [accountidyominame], [address1_line1], [modifiedonbehalfbyname], 
    [new_girodelaempresa], [birthdate], [createdon], [emailaddress1], [firstname], 
    [modifiedon], [versionnumber], [new_rutdelrepresentantelegal], 
    [modifiedonbehalfbyyominame], [fullname], [lastname], [new_rut]
) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
"""
def new_id() -> str:
    unique_id = str(uuid.uuid4())
    return unique_id


def getdate():
    return str(datetime.now())


def format_rut(rut) -> str:
    dv = rut[-1]
    if len(rut) == 9:
        num_rut = rut[0:2] + "." + rut[2:5] + "." + rut[5:8]
    else:
        num_rut = rut[0] + "." + rut[1:4] + "." + rut[4:7]
    newrut = num_rut + '-' + dv
    return newrut



