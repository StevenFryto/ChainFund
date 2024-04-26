use chainfund;
INSERT INTO user (avatar, username, password, email, raised_amount, interest_matrix) VALUES
('avatar_1.webp', '李伟', 'hashedpassword001', 'liwei@example.com', 300000.00, '["医疗", "教育"]'),
('avatar_2.webp', '王婷婷', 'hashedpassword002', 'wangtingting@example.com', 450000.00, '["艺术", "科技"]'),
('avatar_3.webp', '张明', 'hashedpassword003', 'zhangming@example.com', 200000.00, '["科学", "音乐"]'),
('avatar_4.webp', '刘洋', 'hashedpassword004', 'liuyang@example.com', 500000.00, '["体育", "财经"]'),
('avatar_5.webp', '陈悦', 'hashedpassword005', 'chenyue@example.com', 750000.00, '["旅游", "文学"]'),
('avatar_6.webp', '赵刚', 'hashedpassword006', 'zhaogang@example.com', 600000.00, '["游戏", "教育"]'),
('avatar_7.webp', '黄蓉', 'hashedpassword007', 'huangrong@example.com', 350000.00, '["健康", "环保"]'),
('avatar_8.webp', '周杰', 'hashedpassword008', 'zhoujie@example.com', 420000.00, '["科技", "政治"]'),
('avatar_9.webp', '吴林', 'hashedpassword009', 'wulin@example.com', 650000.00, '["艺术", "科学"]'),
('avatar_10.webp', '孙艺宁', 'hashedpassword010', 'sunyining@example.com', 800000.00, '["旅游", "体育"]');
INSERT INTO project (user_id, surety_id, title, description, patient_name, patient_id_card, patient_gender, patient_birth, patient_occupation, photos, label, create_time, deadline, target_amount, current_amount) VALUES
(1, 1, '李伟的心脏手术', '李伟急需心脏手术', '李伟', 'ID100000001', 'male', '1975-08-30', '会计', '["sample_1.webp","sample_3.webp"]', '医疗,紧急,手术,心脏病,治疗', NOW(), '2024-05-20', 2000000.00, 200000.00),
(2, 2, '王婷婷的大学教育基金', '支持王婷婷的大学教育', '王婷婷', 'ID100000002', 'female', '2003-09-15', '学生', '["sample_1.webp","sample_3.webp"]', '教育,学生资助,大学,学习支持,学费', NOW(), '2024-11-30', 100000.00, 150000.00),
(3, 3, '张明的抗癌治疗', '帮助张明对抗胃癌', '张明', 'ID100000003', 'male', '1980-01-22', '自由职业者', '["sample_1.webp","sample_3.webp"]', '医疗,癌症治疗,健康,抗癌,支持', NOW(), '2024-06-15', 3000000.00, 500000.00),
(4, 4, '刘洋的事故恢复支持', '协助刘洋从车祸中恢复', '刘洋', 'ID100000004', 'male', '1970-04-17', '机械师', '["sample_1.webp","sample_3.webp"]', '恢复,事故,康复,支持,医疗费', NOW(), '2024-09-25', 1500000.00, 120000.00),
(5, 5, '陈悦的脊柱手术资金', '为陈悦的脊柱手术筹集资金', '陈悦', 'ID100000005', 'female', '1992-12-08', '设计师', '["sample_1.webp","sample_3.webp"]', '医疗,手术,脊柱,康复,健康', NOW(), '2024-08-30', 2500000.00, 350000.00),
(6, 6, '赵刚的火灾重建支持', '支持赵刚在毁灭性家庭火灾后的重建', '赵刚', 'ID100000006', 'male', '1985-06-19', '厨师', '["sample_1.webp","sample_3.webp"]', '灾难救援,重建,支持,家庭,捐助', NOW(), '2024-07-20', 1200000.00, 300000.00),
(7, 7, '黄蓉的肝脏移植', '黄蓉急需进行肝脏移植', '黄蓉', 'ID100000007', 'female', '1994-02-14', '教师', '["sample_1.webp","sample_3.webp"]', '医疗,移植,肝脏病,健康,手术', NOW(), '2024-12-31', 4500000.00, 800000.00),
(8, 1, '周杰的轮椅适配车辆', '筹款为周杰购买适配轮椅的车辆', '周杰', 'ID100000008', 'male', '1980-11-25', '作家', '["sample_1.webp","sample_3.webp"]', '无障碍设施,轮椅,适配,交通,支持', NOW(), '2024-10-05', 500000.00, 650000.00),
(9, 9, '吴林的心理健康治疗', '支持吴林进行心理健康治疗', '吴林', 'ID100000009', 'female', '1973-03-30', '艺术家', '["sample_1.webp","sample_3.webp"]', '健康,心理治疗,支持,情绪,恢复', NOW(), '2024-04-22', 800000.00, 90000.00),
(10, 1, '孙艺宁的创业基金', '孙艺宁筹集资金开设自己的咖啡馆', '孙艺宁', 'ID100000010', 'male', '1990-08-16', '创业者', '["sample_1.webp","sample_3.webp"]', '创业,商业,资金,咖啡馆,支持', NOW(), '2024-10-18', 3000000.00, 200000.00);
INSERT INTO surety (name, id_card, phone, photo) VALUES
('李四', 'SURETY200001', '12345678901', 'dingzhen.png'),
('王五', 'SURETY200002', '12345678902', 'dingzhen.png'),
('赵六', 'SURETY200003', '12345678903', 'dingzhen.png'),
('钱七', 'SURETY200004', '12345678904', 'dingzhen.png'),
('孙八', 'SURETY200005', '12345678905', 'dingzhen.png'),
('周九', 'SURETY200006', '12345678906', 'dingzhen.png'),
('吴十', 'SURETY200007', '12345678907', 'dingzhen.png'),
('郑十一', 'SURETY200008', '12345678908', 'dingzhen.png'),
('王十二', 'SURETY200009', '12345678909', 'dingzhen.png'),
('冯十三', 'SURETY200010', '12345678910', 'dingzhen.png');
INSERT INTO record (user_id, project_id, duration, raised_amount) VALUES
(1, 1, '2023-04-21 00:10:00', 50000.00),
(1, 2, '2023-04-21 00:20:00', 75000.00),
(1, 3, '2023-04-21 00:15:00', 100000.00),
(1, 4, '2023-04-21 00:05:00', 25000.00),
(1, 5, '2023-04-21 00:30:00', 150000.00),
(2, 6, '2023-04-21 00:45:00', 200000.00),
(2, 7, '2023-04-21 00:25:00', 125000.00),
(2, 8, '2023-04-21 00:55:00', 180000.00),
(3, 9, '2023-04-21 00:35:00', 160000.00),
(3, 10, '2023-04-21 00:40:00', 190000.00);

