from flask import Flask, jsonify, Blueprint, request
import pymysql

from config.config import DB_CONFIG


# Blueprint配置
personalView_bp = Blueprint("personalView", __name__)

def create_connection():
    """创建新的数据库连接"""
    return pymysql.connect(**DB_CONFIG)

@personalView_bp.route("/getPersonalInfo")
def getPersonalInfo():
    user_id = int(request.args.get('id'))
    connection = create_connection()  # 每个请求创建新的连接
    try:
        with connection.cursor() as cursor:
            # 执行SQL查询获取用户信息
            user_sql = "SELECT * FROM user WHERE id = %s"
            cursor.execute(user_sql, (user_id,))
            result = cursor.fetchone()

            if result:
                # 提取所需字段
                return jsonify({
                    "avatar": result.get("avatar"),
                    "name": result.get("username"),
                    "email": result.get("email"),
                })
            else:
                return jsonify({"message": "用户未找到"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        connection.close()  # 确保连接被关闭

@personalView_bp.route("/getHistory")
def getHistory():
    user_id = int(request.args.get('id'))
    connection = create_connection()  # 每个请求创建新的连接
    try:
        with connection.cursor() as cursor:
            # SQL查询获取浏览记录
            history_sql = """
                SELECT 
                    r.user_id,
                    r.project_id,
                    r.duration,
                    p.title
                FROM 
                    record r
                JOIN 
                    project p
                ON 
                    r.project_id = p.id
                WHERE 
                    r.user_id = %s
                ORDER BY 
                    r.duration DESC
            """
            cursor.execute(history_sql, (user_id,))
            result = cursor.fetchall()

            if result:
                for row in result:
                    row["id"] = row["project_id"]
                    row["watchedAt"] = row["duration"].strftime("%Y-%m-%d %H:%M:%S")
                return jsonify({"history": result})  # 返回历史记录
            else:
                return jsonify({"message": "没有找到浏览记录"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        connection.close()  # 确保连接被关闭


@personalView_bp.route("/deleteHistory", methods=["DELETE"])
def deleteHistory():
    record_id = request.args.get('id')  # 确保从请求中获取 ID

    if not record_id:
        return jsonify({"error": "缺少记录 ID"}), 400  # 参数无效

    connection = create_connection()  # 每个请求创建新的连接
    try:
        with connection.cursor() as cursor:
            delete_sql = "DELETE FROM record WHERE project_id = %s"
            cursor.execute(delete_sql, (record_id,))
            connection.commit()  # 提交事务

            if cursor.rowcount == 0:
                return jsonify({"error": "记录未找到"}), 404  # 如果没有删除任何记录

            return jsonify({"message": "记录已删除"}), 200
    except pymysql.MySQLError as e:
        # 捕获数据库错误，并提供更多信息
        return jsonify({"error": str(e)}), 500
    except Exception as e:
        # 捕获一般异常
        return jsonify({"error": str(e)}), 500
    finally:
        connection.close()  # 确保连接被关闭
