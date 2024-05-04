# 数据库说明

## MySQL

### 用户user

| 字段              | 类型           | 描述         |
| ----------------- | -------------- | ------------ |
| Id                | INT            | 主键         |
| avatar            | VARCHAR(255)   | 头像         |
| username          | VARCHAR(255)   | 用户名       |
| password          | VARCHAR(255)   | 密码         |
| email             | VARCHAR(255)   | 邮箱         |
| create_time       | DATETIME       | 创建时间     |
| raised_amount     | DECIMAL(10, 2) | 已捐出的金额 |
| interest_projects | TEXT           | 兴趣矩阵     |

### 众筹项目project

| 字段            | 类型       | 描述             |
| --------------- | ---------------- | --------------- |
| id              | INT           | 主键             |
| user_id | INT | 发布用户id |
| surety_id      | INT   | 保证人id           |
| title           | VARCHAR(255) | 标题             |
| description     | VARCHAR(255) | 描述             |
| patient_name       | VARCHAR(100) | 患者姓名       |
| patient_id_card   | VARCHAR(20) | 患者身份证号 |
| patient_gender     | ENUM('male', 'female', 'other') | 患者性别       |
| patient_birth        | DATE | 患者出生日期       |
| patient_occupation | VARCHAR(255) | 患者职业       |
| photos         | TEXT     | 患者目前状况照片 |
| label           | VARCHAR(255) | 小标签           |
| create_time     | DATETIME | 创建时间         |
| deadline        | DATETIME | 截止日期         |
| target_amount   | DECIMAL(10, 2) | 目标金额         |
| current_amount  | DECIMAL(10, 2) | 已经筹到的金额   |

说明

* label：小标签是用户随便选或者随便填的，比如：
    * 患者：儿童、孕妇、植物人
    * 部位：脑血管、心脏、肝脏、肾脏、脾脏、胰脏、肺部、消化系统、免疫系统、神经系统
    * 疾病：心脏病、癌症、肿瘤、瘫痪、糖尿病、风湿病、癫痫、失明、失聪、骨折、脑中风、心肌梗塞
    * 类型：手术、化疗、慢性病管理、重症监护、康复治疗、药物、检查、康复设备
    * 用户自己填写：
* label 标签存储时用`,`隔开，比如`标签1,标签2,...`
* photos 存储格式为`["图片文件名1","图片文件名2","图片文件名3",...]`
* 图片只存储文件名，不存储路径


### 保证人信息surety

| 字段       | 类型     | 描述       |
| ---------- | ---------- | ---------- |
| id         | INT      | 主键       |
| name     | VARCHAR(255) | 保证人姓名       |
| id_card  | VARCHAR(20) | 保证人身份证号码 |
| phone    | VARCHAR(20) | 保证人联系方式   |
| photo | VARCHAR(255) | 保证人照片 |


### 浏览记录表record

| 字段          | 类型           | 描述           |
| ------------- | -------------- | -------------- |
| user_id       | INT            | 用户id         |
| project_id    | INT            | 项目id         |
| duration      | DATETIME       | 浏览时间       |
| raised_amount | DECIMAL(10, 2) | 本次捐赠的金额 |
| message       | TEXT           | 捐款时留言     |

### 建库脚本

```sql
-- 创建用户表
CREATE TABLE user (
    id INT AUTO_INCREMENT PRIMARY KEY,
    avatar VARCHAR(255),
    username VARCHAR(100) NOT NULL,
    password VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    create_time DATETIME DEFAULT CURRENT_TIMESTAMP,
    raised_amount DECIMAL(10, 2),
    interest_matrix TEXT
);

-- 创建众筹项目表
CREATE TABLE project (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id, INT NOT NULL,
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
    photo VARCHAR(255)
);

-- 创建浏览记录表
CREATE TABLE record (
    user_id INT,
    project_id INT,
    duration DATETIME,
    raised_amount DECIMAL(10, 2)
);
```

## 链

### 捐款记录

```solidity
    struct Transfer {
        uint256 id; 	// 编号
        address from; 	// 捐款人
        address to;		// 收款人
        uint256 amount;	// 金额
        string message; // 留言
        uint256 time;	// 时间戳
    }
```

## 更改记录

**user表**

* 修改密码哈希为明文存储

**surety表**

* 增加头像字段photo

**project表**

* 增加用户id（不然只通过surety来让项目和用户连接起来是有问题的）
