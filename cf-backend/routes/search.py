from flask import Flask, request, jsonify, Blueprint
import pymysql

from config.config import DB_CONFIG

# 创建一个蓝图
search_bp = Blueprint("search", __name__)

# 连接数据库
connection = pymysql.connect(**DB_CONFIG)

@search_bp.route("/search", methods=["GET"])
def search():
    query = request.args.get("query", "")
    if not query:
        return jsonify([])
    try:
        with connection.cursor() as cursor:
            sql = "SELECT id, title FROM project WHERE title LIKE %s"
            cursor.execute(sql, ("%" + query + "%",))
            result = cursor.fetchall()
            return jsonify(result)
    finally:
        # connection.close()
        pass
