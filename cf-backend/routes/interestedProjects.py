from flask import Blueprint, jsonify, request
import pymysql

from config.config import DB_CONFIG


getInterestedProjects_bp = Blueprint('getInterestedProjects_bp', __name__)
connection = pymysql.connect(**DB_CONFIG)

@getInterestedProjects_bp.route('/<int:user_id>/interested_projects', methods=['GET'])
def get_interested_projects(user_id):
    try:
        connection.ping(True)
        with connection.cursor() as cursor:
            sql = "SELECT interested_projects FROM user WHERE id = %s"
            cursor.execute(sql, (user_id,))
            result = cursor.fetchone()
            interested_projects = result['interested_projects'] if result else ''
            # Assuming interested_projects is stored as a comma-separated string of project IDs
            project_ids = [int(x) for x in interested_projects.split(',') if x.isdigit()]
            return jsonify(project_ids)
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        connection.close()

