#Libreria de conexion de base de datos en Python 

#Importacion de la librerias
import mysql.connector 

#Definicion de valores de conexion
dbUser = "User"
dbPass = "Password"
dbHost = "127.0.0.1"
dbPort = "3306"
dbBase = "DataBase"
dbTabl = "Table"

#Testeo de conexion
def TestConexion ():
    try:
        cnx = mysql.connector.connect(user='User', 
                    password='Password', 
                    host='127.0.0.1', 
                    port=3306, 
                    database='DataBase')
        query = str.format("SELECT * FROM Table LIMIT 1;")
        crs = cnx.cursor()
        cnx.commit()
        cnx.close()
        return True
    except mysql.connector.Error as err:
        print(err)
        return False

#Subir data a la base de datos
def LoadData(table, data):
    try:
        cnx = mysql.connector.connect(user=dbUser,  password=dbPass, host=dbHost, port=dbPort, database=dbBase)
        query = str.format("INSERT INTO {0} VALUES ({1});", table, data)
        crs = cnx.cursor()
        cnx.commit()
        cnx.close()
        return True
    except mysql.connector.Error as err:
        print(err)
        return False

#Leer data de la base de datos
def GetData(table):
    result = []
    try:
        cnx = mysql.connector.connect(user='User', 
                    password='Password', 
                    host='127.0.0.1', 
                    port=3306, 
                    database='DataBase')
        query = str.format ("SELECT * FROM {0};", table)
        crs = cnx.cursor(buffered = True)
        crs.execute(query)
        cnx.commit()
        dat = crs.fetchall()
        for data in dat:
            result.append(data)
        cnx.close()
        return result
    except mysql.connector.Error as err:
        print(err)
        return

#Prueba para curso de git y github

#Licencia GPL   v2



#Libreria de ejemplo para conexiones a base de datos mysql 
# desde python 
