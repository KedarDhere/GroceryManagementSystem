from mysql.connector import (connection)
__cnx = None

def setup_sql_connection():
    global __cnx 

    if __cnx == None:
        __cnx = connection.MySQLConnection(user='root', password='root1234',
                                    host='127.0.0.1',
                                    database='groceryStore')
    
    return __cnx

