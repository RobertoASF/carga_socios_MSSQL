from datetime import datetime
from variables import insert, campos, new_id, getdate

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


def crea_insert():
    id = new_id
    new_canal = 20
    new_suscriptorrmactiva = 0
    new_region = '8EDED6DA-7FE8-E811-A971-000D3AC1BB19'
    new_ciudad = 'BF7FDD22-60CC-EA11-A812-000D3AC0A0B3'
    modifiedby = 'null'
    new_pais = 'C1876847-CBE5-E811-A979-000D3AC02DD5'
    new_comuna = None  # TODO buscar coomuna en base de datos
    new_nombrerepresentantelegal = 'null'
    mobilphone = None  # TODO rescatar del csv
    accountidyominame = 'null'
    address1_line1 = None  # TODO rescatar del csv
    modifiedonbehalfbyname = 'null'
    new_girodelaempresa = 'null'
    birthdate = None  # TODO rescatar del csv
    createdon = getdate()
    emailaddress1 = None  # TODO rescatar del csv
    firstname = None  # TODO rescatar del csv
    modifiedon = getdate()
    versionnumber = 'null'
    new_rutdelrepresentantelegal = 'null'
    modifiedonbehalfbyyominame = getdate()
    fullname = None # TODO rescatar del csv MISMO DEL NOMBRE
    lastname = None  # TODO rescatar del csv
    new_rut = None   # TODO rescatar del csv
    pass


if __name__=="__main__":
    print(campos)