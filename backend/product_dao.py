from mysql.connector import (connection)

cnx = connection.MySQLConnection(user='root', password='root1234',
                                 host='127.0.0.1',
                                 database='groceryStore')

cursor = cnx.cursor()

query = "SELECT * FROM groceryStore.productDetails"

cursor.execute(query)

for (productId, name, unitOfMeasurement, price) in cursor:
    print(productId, name, unitOfMeasurement, price)
    
cnx.close()