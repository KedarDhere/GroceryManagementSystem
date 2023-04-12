from flask import Flask, request, jsonify
import product_dao
import sql_connection

connection = sql_connection.setup_sql_connection()

app = Flask(__name__)

@app.route('/getProducts', methods=['GET'])
def get_products():
    products = product_dao.get_all_products(connection)
    response = jsonify(products)
    response.headers.add('Access-Control-Allow-Orign', '*')
    return response

if __name__ == '__main__':
    app.run(port=5000)