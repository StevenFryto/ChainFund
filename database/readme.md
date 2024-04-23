# 数据库说明

## MySQL

### 用户user

| 字段            | 描述         |
| --------------- | ------------ |
| id              | 主键         |
| avatar          | 头像         |
| username        | 用户名       |
| password_hash   | 密码哈希     |
| email           | 邮箱         |
| create_time     | 创建时间     |
| raised_amount   | 已捐出的金额 |
| interest_matrix | 兴趣矩阵     |

### 众筹项目project

| 字段            | 描述             |
| --------------- | ---------------- |
| id              | 主键             |
| title           | 标题             |
| description     | 描述             |
| surety_name     | 保证人姓名       |
| surety_phone    | 保证人联系方式   |
| surety_id_card  | 保证人身份证号码 |
| surety_id_photo | 保证人身份证照片 |
| patient_id      | 患者id           |
| photo           | 患者目前状况照片 |
| label           | 小标签           |
| create_time     | 创建时间         |
| deadline        | 截止日期         |
| target_amount   | 目标金额         |
| current_amount  | 已经筹到的金额   |

说明

* label：小标签是用户随便选或者随便填的，比如：
    * 患者：儿童、孕妇、植物人
    * 部位：脑血管、心脏、肝脏、肾脏、脾脏、胰脏、肺部、消化系统、免疫系统、神经系统
    * 疾病：心脏病、癌症、肿瘤、瘫痪、糖尿病、风湿病、癫痫、失明、失聪、骨折、脑中风、心肌梗塞
    * 类型：手术、化疗、慢性病管理、重症监护、康复治疗、药物、检查、康复设备
    * 用户自己填写：


### 病人信息patient

| 字段       | 描述       |
| ---------- | ---------- |
| id         | 主键       |
| name       | 姓名       |
| gender     | 性别       |
| age        | 年龄       |
| occupation | 职业       |

### 浏览记录表record

| 字段          | 描述           |
| ------------- | -------------- |
| user_id       | 用户id         |
| project_id    | 项目id         |
| duration      | 浏览时间       |
| raised_amount | 本次捐赠的金额 |

### 建库脚本

```sql
-- 创建用户表
CREATE TABLE user (
    id INT AUTO_INCREMENT PRIMARY KEY,
    avatar VARCHAR(255),
    username VARCHAR(255) NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    email VARCHAR(255),
    create_time DATETIME DEFAULT CURRENT_TIMESTAMP,
    raised_amount DECIMAL(10, 2) DEFAULT 0,
    interest_matrix TEXT
);

-- 创建众筹项目表
CREATE TABLE project (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    surety_name VARCHAR(255) NOT NULL,
    surety_phone VARCHAR(20) NOT NULL,
    surety_id_card VARCHAR(18) NOT NULL,
    surety_id_photo VARCHAR(255),
    patient_id INT NOT NULL,
    photo VARCHAR(255),
    label VARCHAR(255),
    create_time DATETIME DEFAULT CURRENT_TIMESTAMP,
    deadline DATETIME,
    target_amount DECIMAL(10, 2),
    current_amount DECIMAL(10, 2) DEFAULT 0
);

-- 创建病人信息表
CREATE TABLE patient (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    gender VARCHAR(10),
    age INT,
    occupation VARCHAR(255)
);

-- 创建浏览记录表
CREATE TABLE record (
    user_id INT,
    project_id INT,
    duration DATETIME DEFAULT CURRENT_TIMESTAMP,
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

