import mysql.connector

cnx = mysql.connector.connect(host='localhost', user='root',password='12345678',database='cadastro')

cnx.close()
