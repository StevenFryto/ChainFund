from flask import Blueprint, request, jsonify
import pymysql
import hashlib
import os

from config.config import DB_CONFIG

login_bp = Blueprint('login_and_register', __name__)


# 数据库连接参数
connection = pymysql.connect(**DB_CONFIG)

# 登陆路由
@login_bp.route('/user-login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    # password_hash = hashlib.sha256(password.encode('utf-8')).hexdigest()
        
    # 查询数据库中是否存在匹配的用户记录
    with connection.cursor() as cursor:
        # 使用参数化查询以防止 SQL 注入攻击
        sql = "SELECT id FROM user WHERE username = %s AND password = %s"
        cursor.execute(sql, (username, password))
        userId = cursor.fetchone()

    if userId:
        return jsonify( {'status': True, 'id': userId['id']} )
    else:
        return jsonify( {'status': False} )


# 注册路由
@login_bp.route('/user-register', methods=['POST'])
def register():
    # 保存上传的文件到指定目录
    try:
        avatar = request.files['avatar']
        avatar_filename = avatar.filename
        avatar_path = os.path.join(".\\cf-frontend\\src\\assets\\avatars", avatar_filename)
        avatar.save(avatar_path)
    except Exception:
        avatar_filename = "default-avatar.jpg"
    
    username = request.form.get('username')
    password = request.form.get('password')
    email = request.form.get('email')

    # password_hash = hashlib.sha256(password.encode('utf-8')).hexdigest()
        
    # 查询数据库中是否存在匹配的用户记录
    with connection.cursor() as cursor:
        sql = "INSERT INTO user (avatar, username, password, email) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (avatar_filename, username, password, email))
        # 提交事务
        connection.commit()
        sql = "SELECT id FROM user WHERE username = %s AND password = %s"
        cursor.execute(sql, (username, password))
        userId = cursor.fetchone()


    # 返回注册成功的 JSON 响应
    return jsonify({'status': True, 'id': userId['id']})
