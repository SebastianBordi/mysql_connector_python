#Libreria de conexion de base de datos en Python 

#importacion de la libreria 
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
        cnx = mysql.connector.connect(user='User',  password='Password', host='127.0.0.1', port=3306, database='DataBase')
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