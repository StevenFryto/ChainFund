from flask import Flask, jsonify, Blueprint, request
from datetime import datetime
import pymysql

from config.config import DB_CONFIG

# Blueprint配置
donate_bp = Blueprint("donate", __name__)

def create_connection():
    """创建新的数据库连接"""
    return pymysql.connect(**DB_CONFIG)

@donate_bp.route("/donate", methods=["POST"])
def donate():
    data = request.get_json()
    user_id = data.get("user_id")
    project_id = data.get("project_id")
    duration = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    raised_amount = data.get("raised_amount")
    message = data.get("message")

    print(data)

    connection = create_connection()
    try:
        with connection.cursor() as cursor:
            # 插入捐赠记录
            donate_sql = """
                INSERT INTO record (user_id, project_id, duration, raised_amount, message)
                VALUES (%s, %s, %s, %s, %s)
            """
            cursor.execute(donate_sql, (user_id, project_id, duration, raised_amount, message))
            connection.commit()

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
    finally:
        connection.close()

    return jsonify({"status": True})

