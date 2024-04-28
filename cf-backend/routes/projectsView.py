from flask import Flask, jsonify, Blueprint, request
import pymysql
import json

from config.config import DB_CONFIG


# Blueprint配置
getProjects_bp = Blueprint("getProjects", __name__)

# 连接数据库
connection = pymysql.connect(**DB_CONFIG)

@getProjects_bp.route("/getProjects", methods=["GET"])
def get_projects():
    projects = []
    try:
        with connection.cursor() as cursor:
            # 执行SQL查询
            sql = "SELECT * FROM project"
            cursor.execute(sql)
            result = cursor.fetchall()
            # print(result)
            
            for row in result:
                row["target_amount"] = float(row["target_amount"])
                row["current_amount"] = float(row["current_amount"])
                row["image"] = json.loads(row["photos"])[0]
                row["label"] = row["label"].split(",")[:2]
                projects.append(row)
    finally:
        pass
    # print(projects)
    return jsonify(projects)


@getProjects_bp.route("/record", methods=["POST"])
def record():
    data = request.get_json()
    user_id = data.get('userId')
    project_id = data.get('projectId')
    try:
        with connection.cursor() as cursor:
            # 执行SQL查询
            sql = "INSERT INTO record(user_id, project_id, raised_amount) VALUES (%s, %s, %s)"
            cursor.execute(sql, (user_id, project_id, 0))
        connection.commit()
    except Exception as e:
        print('Error inserting record', e)
        connection.rollback()
        return jsonify({'status': 'error'})

    return jsonify({'status': 'success'})