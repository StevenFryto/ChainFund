from flask import Flask, jsonify, Blueprint, request
from datetime import datetime
import pymysql

from config.config import DB_CONFIG

# Blueprint配置
record_bp = Blueprint("record", __name__)

# 后端数据库
connection = pymysql.connect(**DB_CONFIG)

@record_bp.route("/record", methods=["POST"])
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