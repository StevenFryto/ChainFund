from flask import Flask, jsonify, Blueprint, request
from datetime import datetime
import pymysql

import sys
sys.path.append("d:\\CyberSecurity\\me\\JiShe\\4.0\\ChainFund")
from blockchain import chainfund

from config.config import DB_CONFIG

# Blueprint配置
donate_bp = Blueprint("donate", __name__)

# 后端数据库
connection = pymysql.connect(**DB_CONFIG)

@donate_bp.route("/donate", methods=["POST"])
def donate():
    data = request.get_json()
    from_user = data.get("user_id")
    project_id = data.get("project_id")
    raised_amount = data.get("raised_amount")
    message = data.get("message")
    print(data)

    try:
        with connection.cursor() as cursor:
            # 获取项目保证人的id
            select_sql = """
                SELECT user_id FROM project WHERE id = %s
            """
            cursor.execute(select_sql, (project_id))
            to_user = cursor.fetchone()['user_id']

            # 更新项目当前筹款金额
            update_sql = """
                UPDATE project
                SET current_amount = current_amount + %s
                WHERE id = %s
            """
            cursor.execute(update_sql, (raised_amount, project_id))
            connection.commit()
    except Exception as e:
        return jsonify({"error": str(e)}), 500

    block_hash = chainfund.insertRecord(args=[from_user, to_user, project_id, raised_amount, message])

    return jsonify({"status": True, "blockHash": block_hash})

