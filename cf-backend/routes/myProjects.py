from flask import Blueprint, request, jsonify
from datetime import datetime
import pymysql
import threading

from config.config import DB_CONFIG

mine_bp = Blueprint('my_projects', __name__)


# 数据库连接参数
connection = pymysql.connect(**DB_CONFIG)
lock = threading.Lock()

# 查询浏览记录和项目信息的SQL语句
RECORD_SQL = """
SELECT project_id 
FROM record 
WHERE user_id = %(user_id)s AND raised_amount > 0
"""

RAISED_SQL = """
SELECT id, title, description, photos, label, target_amount, current_amount 
FROM project 
WHERE id IN (%s)
"""

PUBLISHED_SQL = """
SELECT id, title, description, photos, label, target_amount, current_amount 
FROM project 
WHERE user_id = %(user_id)s
"""

# 连接数据库并执行SQL语句
def execute_sql(sql, params=None):
    lock.acquire()
    connection.ping(True)
    try:
        with connection.cursor() as cursor:
            cursor.execute(sql, params)
            result = cursor.fetchall()
    finally:
        lock.release()
        connection.close()
    return result


# 获取发布项目信息
@mine_bp.route('/my_published_projects')
def get_published_projects():
    user_id = int(request.args.get('id'))
    try:
        project_result = execute_sql(PUBLISHED_SQL, {'user_id': user_id})
        projects = project_result if project_result else []

        print(projects)
        return jsonify({'projects': projects})
    
    except Exception as e:
        print('Error fetching projects:', e)
        return jsonify({'error': str(e)}), 500


# 获取参与项目信息
@mine_bp.route('/my_raised_projects')
def get_raised_projects():
    user_id = int(request.args.get('id'))
    try:
        # 查询浏览记录
        record_result = execute_sql(RECORD_SQL, {'user_id': user_id})
        project_ids = [record['project_id'] for record in record_result]

        # 查询项目信息
        if project_ids:
            project_ids_str = ','.join(str(project_id) for project_id in project_ids)
            project_result = execute_sql(RAISED_SQL % project_ids_str)
            projects = project_result if project_result else []
        else:
            projects = []

        print(projects)
        return jsonify({'projects': projects})
    
    except Exception as e:
        print('Error fetching projects:', e)
        return jsonify({'error': str(e)}), 500
