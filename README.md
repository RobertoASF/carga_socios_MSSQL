## Script de carga de csv a MS SQL



### Dependencias
* Python 3.11 o superior
* ODBC Driver 17 for SQL Server

### Librerías de Python utilizadas:
* pandas
* paramiko
* pysftp
* pyodbc
* python-dotenv

### Instalación de dependencias
* Instalación de Python -> [link de descarga](https://www.python.org/downloads/)

  Para Verificar que se encuentre correctamente instalado ejecutar el siguiente comando en una terminal
  ```
  python --version
  ```
  Esto devería devolver la versión de Python que está instalda


* Instalación de librerías de Python:

  1. abrir una terminal en el directorio del proeycto
  2. ejecutar el siguiente comando 


  ```
  pip install -r requirements.txt
  ```

### Configuración del entorno

Para el correcto funcionamiento del programa se deben configurar los siguientes parámetros:

1. crear archivo .env con los siguientes datos:
    * FTP_IP
    * FTP_USER
    * FTP_PASS
    * SQL_IP
    * SQL_DATABASE
    * SQL_PASS
2. en **variables.py** modificar variable _dir_descarga_ por el directorio donde se descargará el archivo .csv

3. en **variables-py modificar variable _archivo_,  por lo siguiente:
```python
archivo = f'socios_nuevos_{fecha}.csv'
```
4. en el archivo **main.py** modificar la línea:
```python
clear_csv = pd.read_csv('socios_nuevos_20231228.csv')
```

por 

```python
clear_csv = pd.read_csv(archivo)
```