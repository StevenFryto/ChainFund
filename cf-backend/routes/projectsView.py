from flask import Flask, jsonify, Blueprint
from flask_cors import CORS
import pymysql
import json

app = Flask(__name__)
CORS(app)

# Blueprint配置
getProjects_bp = Blueprint("getProjects", __name__)


@getProjects_bp.route("/getProjects", methods=["GET"])
def get_projects():
    # 连接数据库
    connection = pymysql.connect(
        host="localhost",
        user="root",
        port=3306,
        password="Doncic77++",
        db="chainfund",
        charset="utf8mb4",
        cursorclass=pymysql.cursors.DictCursor,
    )

    projects = []
    try:
        with connection.cursor() as cursor:
            # 执行SQL查询
            sql = "SELECT * FROM project"
            cursor.execute(sql)
            result = cursor.fetchall()
            for row in result:
                row["target_amount"] = float(row["target_amount"])
                row["current_amount"] = float(row["current_amount"])
                row["image"] = json.loads(row["photos"])[0]
                row["label"] = row["label"].split(",")[:2]
                projects.append(row)
    finally:
        connection.close()
    print(projects)
    return jsonify(projects)


# 注册Blueprint
app.register_blueprint(getProjects_bp)

# if __name__ == "__main__":
#     app.run(debug=True, port=5050)
