from flask import Flask, request, jsonify, Blueprint
import pymysql

# 创建 Flask 应用
app = Flask(__name__)

# 创建一个蓝图
search_bp = Blueprint("search", __name__)


@search_bp.route("/search", methods=["GET"])
def search():
    query = request.args.get("query", "")
    if not query:
        return jsonify([])

    connection = pymysql.connect(
        host="localhost",
        user="root",
        port=3306,
        password="Doncic77++",
        db="chainfund",
        charset="utf8mb4",
        cursorclass=pymysql.cursors.DictCursor,
    )
    try:
        with connection.cursor() as cursor:
            sql = "SELECT id, title FROM project WHERE title LIKE %s"
            cursor.execute(sql, ("%" + query + "%",))
            result = cursor.fetchall()
            return jsonify(result)
    finally:
        connection.close()
