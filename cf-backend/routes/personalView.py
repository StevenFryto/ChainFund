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
                    r.user_id = %s AND r.raised_amount = 0
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
    user_id = request.args.get("userId")  # 从请求参数中获取 userId
    project_id = request.args.get("projectId")  # 从请求参数中获取 projectId

    # 确保所有必需的参数都被提供
    if not user_id or not project_id:
        return jsonify({"error": "缺少 userId 或 projectId"}), 400

    connection = create_connection()  # 为每个请求创建新的数据库连接
    try:
        with connection.cursor() as cursor:
            # 根据 userId 和 projectId 删除记录
            delete_sql = "DELETE FROM record WHERE user_id = %s AND project_id = %s AND raised_amount = 0"
            cursor.execute(delete_sql, (user_id, project_id))
            connection.commit()  # 提交事务

            # 检查删除操作的结果
            if cursor.rowcount == 0:
                return jsonify({"error": "记录未找到"}), 404  # 如果没有记录被删除

            return jsonify({"message": "记录已删除"}), 200
    except pymysql.MySQLError as e:
        # 捕获数据库相关错误
        return jsonify({"error": f"数据库错误: {e}"}), 500
    except Exception as e:
        # 捕获其他异常
        return jsonify({"error": f"服务器错误: {e}"}), 500
    finally:
        connection.close()  # 确保在离开前关闭数据库连接