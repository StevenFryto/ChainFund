from flask import Flask, request, jsonify, Blueprint
from werkzeug.utils import secure_filename
import os
import pymysql
import json

from config.config import DB_CONFIG

from bert.inference import inference_user_ids


# Blueprint配置
publishProject_bp = Blueprint("publishProject", __name__)

avatar_photo_folder = ".\\cf-frontend\\src\\assets\\avatars"  # 指定图片上传路径
project_photo_folder = ".\\cf-frontend\\src\\assets\\projects"  # 指定图片上传路径

# 数据库连接参数
connection = pymysql.connect(**DB_CONFIG)


@publishProject_bp.route('/publishProject', methods=['POST'])
def publish_project():
    surety_info = json.loads(request.form.get('suretyInfo'))
    project_info = json.loads(request.form.get('projectInfo'))

    # print(surety_info, '\n', project_info)

    # 存储保证人头像
    surety_photo = request.files['suretyPhoto']
    if surety_photo:
        file_path = os.path.join(avatar_photo_folder, surety_photo.filename)
        surety_photo.save(file_path)
    
    # 存储病人照片列表
    project_photos = []
    for key in request.files:
        if key.startswith('projectPhoto_'):
            project_photo = request.files[key]
            project_photo.save(os.path.join(project_photo_folder, project_photo.filename))
            project_photos.append(project_photo.filename)  # 选择保存文件名
        else:
            continue

    # 插入 surety 表
    surety_id = insert_surety(surety_info['name'], surety_info['idCard'], surety_info['phone'], surety_photo.filename)

    # 插入 project 表
    photos_str = '["' + '","'.join([photo for photo in project_photos]) + '"]'
    labels_str = ','.join([label for label in project_info['labels']])
    project_id = insert_project(project_info['userId'], surety_id, project_info['title'], project_info['description'], project_info['patientName'], project_info['patientIdCard'], project_info['patientGender'], project_info['patientBirth'], project_info['patientOccupation'], photos_str, labels_str, project_info['deadline'], project_info['targetAmount'])

    # try:
    print(project_info['description'], project_info['userId'])
    top_user_ids = inference_user_ids(project_info['description'], project_info['userId'], 10)
    top_user_ids = [int(item) for item in top_user_ids[0]]
    # print(",".join(top_user_ids))
    # except:
    #     print("Fail in predict top users!")
    #     pass

    if surety_id != -1 and project_id != -1:
        return jsonify({'status': True, 'id': project_id})
    else:
        return jsonify({'status': False})


def insert_project(user_id, surety_id, title, description, patient_name, patient_id_card, patient_gender, patient_birth, patient_occupation, photos, label, deadline, target_amount):
    try:
        with connection.cursor() as cursor:
            sql = "INSERT INTO project (user_id, surety_id, title, description, patient_name, patient_id_card, patient_gender, patient_birth, patient_occupation, photos, label, deadline, target_amount, current_amount) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(sql, (user_id, surety_id, title, description, patient_name, patient_id_card, patient_gender, patient_birth, patient_occupation, photos, label, deadline, target_amount, 0))
        connection.commit()
        return cursor.lastrowid
    except Exception as e:
        print("Error inserting project:", e)
        connection.rollback()
        return -1


def insert_surety(name, id_card, phone, photo):
    try:
        with connection.cursor() as cursor:
            sql = "INSERT INTO surety (name, id_card, phone, photo) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, (name, id_card, phone, photo))
        connection.commit()
        return cursor.lastrowid
    except Exception as e:
        print("Error inserting surety:", e)
        connection.rollback()
        return -1