from flask import Flask, request, jsonify
from pymongo import MongoClient
from flask_mysqldb import MySQL
from bson import ObjectId
app = Flask(__name__)

app.config["MYSQL_DB"] = "btvdxsdfjoxbawrflmiu"
app.config["MYSQL_USER"] = "uezcn2sfks2ur8h7"
app.config["MYSQL_HOST"] = "btvdxsdfjoxbawrflmiu-mysql.services.clever-cloud.com"
app.config["MYSQL_PASSWORD"] ="vzL2npw7IBb9n8TA25t3" 
app.config["MYSQL_PORT"] = 3306
mysql = MySQL(app)


# client = MongoClient("mongodb+srv://admin:admin@micluster.gg9in.mongodb.net/")
# db = client["apirestmongo"]
# productos = db["productos"]


# @app.route("/")
# def home():
#     query = list(productos.find())
#     print(query)
#     return jsonify({"productos": str(query)})


# @app.route("/add", methods=["POST"])
# def add():
#     data = request.json
#     nombre = data["nombre"]
#     categoria = data["categoria"]
#     precio = data["precio"]
#     color = data["color"]
#     query = productos.insert_one({"nombre":nombre, "categoria":categoria, "precio":precio, "color":color})
#     return jsonify({"message": str(query)})


# @app.route("/edit/<string:id>", methods=["PUT"])
# def edit(id):
#     data = request.json
#     nombre = data["nombre"]
#     categoria = data["categoria"]
#     precio = data["precio"]
#     color = data["color"]
#     query = productos.update_one({"_id": ObjectId(id)},{"$set" : {"nombre":nombre, "categoria":categoria, "precio":precio, "color":color}})
#     return jsonify({"message": str(query)})
    
    
    
# @app.route("/delete/<string:id>", methods=["DELETE"])
# def delete(id):
#     query = productos.delete_one({"_id":ObjectId(id)})
#     if query:
#         return jsonify({"producto eliminado": str(query)})



@app.route("/")
def home():
    cursor = mysql.connection.cursor()
    query = cursor.execute("SELECT * FROM productos")
    productos = cursor.fetchall()
    if query:
        return jsonify({"productos": productos})
    else:
        return "no hay productos"


@app.route("/add", methods=["POST"])
def add():
    data = request.json
    nombre = data["nombre"]
    categoria = data["categoria"]
    precio = data["precio"]
    color = data["color"]
    cursor = mysql.connection.cursor()
    query = cursor.execute("INSERT INTO productos values (null, %s, %s, %s, %s)",(nombre, categoria, precio, color))
    mysql.connection.commit()
    if query:
        return jsonify({"message":"Producto agregado"})


@app.route("/edit/<string:id>", methods=["PUT"])
def edit(id):
    data = request.json
    nombre = data["nombre"]
    categoria = data["categoria"]
    precio = data["precio"]
    color = data["color"]
    cursor = mysql.connection.cursor()
    query = cursor.execute("UPDATE productos SET nombre=%s, categoria=%s, precio=%s, color=%s WHERE id=%s",(nombre, categoria, precio, color, id))
    mysql.connection.commit()
    return jsonify({"message": "producto modificado"})
    
    
    
@app.route("/delete/<string:id>", methods=["DELETE"])
def delete(id):
    cursor = mysql.connection.cursor()
    query = cursor.execute("DELETE from productos WHERE id=%s",(id))
    mysql.connection.commit()
    if query:
        return jsonify({"message": "producto eliminado"})
    else:
        return jsonify({"message": "producto incorrecto"})     

if __name__ == "__main__":
    app.run(debug=True, port=3030, host="0.0.0.0")
    







