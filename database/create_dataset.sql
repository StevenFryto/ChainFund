-- 创建用户表
CREATE TABLE user (
    id INT AUTO_INCREMENT PRIMARY KEY,
    avatar VARCHAR(255),
    username VARCHAR(100) NOT NULL,
    password VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    create_time DATETIME DEFAULT CURRENT_TIMESTAMP,
    raised_amount DECIMAL(10, 2),
    interested_projects TEXT
);

-- 创建众筹项目表
CREATE TABLE project (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    surety_id INT NOT NULL,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    patient_name VARCHAR(100) NOT NULL,
    patient_id_card VARCHAR(20) NOT NULL,
    patient_gender ENUM('male', 'female', 'other') NOT NULL,
    patient_birth DATE NOT NULL,
    patient_occupation VARCHAR(255),
    photos TEXT,
    label VARCHAR(255),
    create_time DATETIME DEFAULT CURRENT_TIMESTAMP,
    deadline DATE,
    target_amount DECIMAL(10, 2),
    current_amount DECIMAL(10, 2)
);

-- 创建保证人信息表
CREATE TABLE surety (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    id_card VARCHAR(20) NOT NULL,
    phone VARCHAR(20) NOT NULL,
    photo VARCHAR(255) NOT NULL
);

-- 创建浏览记录表
CREATE TABLE record (
    user_id INT,
    project_id INT,
    duration DATETIME,
    raised_amount DECIMAL(10, 2),
    message varchar(255)
);
