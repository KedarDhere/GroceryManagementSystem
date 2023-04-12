from sql_connection import setup_sql_connection

def get_all_products(connection):
    cursor = connection.cursor()

    query = "SELECT p.productId, p.name, p.price, u.name  FROM groceryStore.productDetails AS p inner join groceryStore.unitOfMeasurement As u on p.uomId = u.uomId"

    cursor.execute(query)

    response = []

    for (productId, name, price, unitOfMeasurement) in cursor:
        response.append(
            {
                'productId': productId,
                'product_name': name,
                'price_per_unit': price,
                'unitOfMeasurement': unitOfMeasurement
            }
        )
    
    return response

def insert_product(connection, product):
    cursor = connection.cursor()

    query = ("INSERT INTO groceryStore.productDetails (name, uomId, price) values (%s, %s, %s)")

    data = (product['product_name'], product['unitOfMeasurementId'], product['price_per_unit'])

    cursor.execute(query, data)
    connection.commit()

    return cursor.lastrowid

def delete_product(connection, productId):
    cursor = connection.cursor()

    query = ("DELETE from groceryStore.productDetails where productId=" + str(productId))

    cursor.execute(query)
    connection.commit()

if __name__ == '__main__':
    connection = setup_sql_connection()
    delete_product(connection, 7)
