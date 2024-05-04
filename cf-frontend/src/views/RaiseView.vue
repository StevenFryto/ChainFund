<template>
    <div class="raise">
        <main class="container">
            <!-- Step 1: Guarantor Information -->
            <section v-if="step === 1" class="user-profile">
                <h1 class="username-title">👨‍👦 保证人基本信息</h1>
                <div class="profile-header">
                    <input type="file" id="photo" @change="previewPhoto" accept="image/*" class="photo-upload">
                    <label for="photo" class="photo-upload-label">
                        <img v-if="suretyPhotoPreview" :src="suretyPhotoPreview" alt="保证人照片预览" class="photo-preview" />
                        <span v-else class="photo-placeholder">点击此处上传保证人持身份证照片</span>
                    </label>
                </div>
            </section>
            <form v-if="step === 1" @submit.prevent="nextStep">
                <!-- Guarantor's form fields -->
                <div class="form-field">
                    <label for="name">保证人姓名</label>
                    <input type="text" id="name" placeholder="请填写保证人姓名" v-model="suretyInfo.name" >
                </div>
                <div class="form-field">
                    <label for="id">保证人身份证号</label>
                    <input type="text" id="id" placeholder="请填写保证人身份证号" v-model="suretyInfo.idCard" >
                </div>
                <div class="form-field">
                    <label for="phone">保证人手机号码</label>
                    <input type="tel" id="phone" placeholder="请填写手机号码" v-model="suretyInfo.phone" >
                </div>

                <button type="submit" class="submit-button">下一步</button>
            </form>

            <!-- Step 2: Project Information -->
            <section v-if="step === 2" class="project-info">
                <h1 class="username-title">📇 众筹基本信息</h1>
                <div class="form-field">
                    <label for="title">众筹标题</label>
                    <textarea id="title" rows="4" placeholder="请输入众筹请求标题" v-model="projectInfo.title" ></textarea>
                </div>
                <div class="form-field">
                    <label for="description">病情描述</label>
                    <textarea id="description" rows="4" placeholder="请输入病情描述" v-model="projectInfo.description" ></textarea>
                </div>
                <div class="form-field">
                    <label for="cost-estimate">治疗费用预估（人民币）</label>
                    <input type="number" id="cost-estimate" placeholder="请填写预估治疗费用" v-model="projectInfo.targetAmount" >
                </div>
                <div class="form-field">
                    <label for="deadline">众筹截至日期</label>
                    <input type="date" id="deadline" v-model="projectInfo.deadline" >
                </div>
                <div class="form-field">
                    <label for="patient-photos">患者目前状况照片（最多可上传9张）</label>
                    <input type="file" id="patient-photos" @change="previewProjectPhotos" accept="image/*" multiple>
                    <div class="photo-grid">
                        <div class="photo-preview" v-for="(photo, index) in projetcPhotosPreview" :key="index">
                            <img :src="photo" alt="患者照片预览">
                        </div>
                    </div>
                </div>
                <div class="buttons">
                    <button type="submit" @click="lastStep" class="submit-button">上一步</button>
                    <button type="submit" @click="nextStep" class="submit-button">下一步</button>
                </div>
            </section>

            <!-- Step 3: Patient Information -->
            <section v-if="step === 3" class="patient-info">
                <h1 class="username-title">🤕 患者基本信息</h1>
                <!-- Patient's form fields -->
                <div class="form-field">
                    <label for="patient-name">患者姓名</label>
                    <input type="text" id="patient-name" placeholder="请填写患者姓名" v-model="projectInfo.patientName" >
                </div>
                <div class="form-field">
                    <label for="patient-id">患者身份证号</label>
                    <input type="text" id="patient-id" placeholder="请填写患者身份证号" v-model="projectInfo.patientIdCard" >
                </div>
                <div class="form-field">
                    <label for="patient-gender">患者性别</label>
                    <select id="patient-gender" class="form-input" v-model="projectInfo.patientGender" >
                        <option value="">请选择性别</option>
                        <option value="male">男</option>
                        <option value="female">女</option>
                    </select>
                </div>
                <div class="form-field">
                    <label for="patient-birthdate">患者出生日期</label>
                    <input type="date" id="patient-birthdate" v-model="projectInfo.patientBirth" >
                </div>
                <div class="form-field">
                    <label for="patient-job">患者职业</label>
                    <input type="text" id="patient-job" placeholder="请填写患者职业" v-model="projectInfo.patientOccupation" >
                </div>
                <div class="buttons">
                    <button type="submit" @click="lastStep" class="submit-button">上一步</button>
                    <button type="submit" @click="nextStep" class="submit-button">下一步</button>
                </div>
            </section>

            <!-- Step 4: Submit Request -->
            <section v-if="step === 4" class="bubbles-container">
                <h2>🏷️ 选择关键词标签</h2>
                <div class="bubbles">
                    <div class="bubble-title">🧑‍🦽 患者类型</div>
                        <div class="bubble-container">
                            <div class="bubble" v-for="(symptom, index) in patientSymptoms" :key="index"
                                @click="toggleSelection(symptom)" :class="{ selected: projectInfo.labels.includes(symptom) }">
                                {{ symptom }}
                        </div>
                    </div>
                </div>
                <div class="bubbles">
                    <div class="bubble-title">🫀 疾病部位</div>
                        <div class="bubble-container">
                            <div class="bubble" v-for="(symptom, index) in bodySymptoms" :key="index"
                                @click="toggleSelection(symptom)" :class="{ selected: projectInfo.labels.includes(symptom) }">
                                {{ symptom }}
                        </div>
                    </div>
                </div>
                <div class="bubbles">
                    <div class="bubble-title">🦠 疾病类型</div>
                        <div class="bubble-container">
                            <div class="bubble" v-for="(symptom, index) in diseaseSymptoms" :key="index"
                                @click="toggleSelection(symptom)" :class="{ selected: projectInfo.labels.includes(symptom) }">
                                {{ symptom }}
                        </div>
                    </div>
                </div>
                <div class="bubbles">
                    <div class="bubble-title">💰 主要花销</div>
                    <div class="bubble-container">
                        <div class="bubble" v-for="(symptom, index) in expenseSymptoms" :key="index"
                            @click="toggleSelection(symptom)" :class="{ selected: projectInfo.labels.includes(symptom) }">
                            {{ symptom }}
                        </div>
                    </div>
                </div>
                <div class="form-field">
                    <input type="text" v-model="customSymptom" placeholder="不足以表达您的情况？请在此输入" />
                </div>
                <div class="buttons">
                    <button type="submit" @click="lastStep" class="submit-button">上一步</button>
                    <button type="submit" @click="submitRequest" class="submit-button">发布众筹</button>
                </div>
            </section>
        </main>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    name: 'RaiseView',
    data() {
        return {
            step: 1, // 控制步骤的数据属性
            suretyPhotoPreview: null,
            projetcPhotosPreview: [],
            patientSymptoms: [
                '儿童', '孕妇', '老年人', '家庭支柱'
            ],
            bodySymptoms: [
                '脑', '心脏', '肝脏', '肾脏', '脾脏', '胰脏', '肺部', '皮肤组织', '骨髓', '内分泌系统', '血管系统', '免疫系统', '神经系统'
            ],
            diseaseSymptoms: [
                '心脏病', '癌症', '肿瘤', '瘫痪', '糖尿病', '风湿病', '癫痫', '失明', '失聪', '结核类', '骨折', '脑中风', '艾滋病', '心肌梗塞'
            ],
            expenseSymptoms: [
                '手术', '化疗', '慢性病管理', '重症监护', '康复治疗', '药物', '检查', '康复设备'
            ],
            customSymptom: '',
            
            formData: new FormData(),
            suretyInfo: {
                name: '',
                idCard: '',
                phone: '',
            },
            suretyPhoto: null,
            projectInfo: {
                userId: parseInt(this.$route.params.userId),
                title: '',
                description: '',
                patientName: '',
                patientIdCard: '',
                patientGender: '',
                patientBirth: '',
                patientOccupation: '',
                labels: [],
                deadline: '',
                targetAmount: ''
            },
            projectPhotos: [],
        };
    },
    methods: {
        nextStep() { this.step++; },
        lastStep() { this.step--; },
        previewPhoto(event) {
            // 处理保证人照片预览逻辑
            const file = event.target.files[0];
            if (file && file.type.startsWith('image/')) {
                this.suretyPhoto = file; // 将图片数据赋值给 formData
                // 创建前端预览
                const reader = new FileReader();
                reader.onload = e => {
                    this.suretyPhotoPreview = e.target.result;
                };
                reader.readAsDataURL(file);
            }
        },
        previewProjectPhotos(event) {
            const files = event.target.files;
            if (files.length + this.projectPhotos.length <= 9) {
                Array.from(files).forEach(file => {
                    if (file.type.startsWith('image/')) {
                        this.projectPhotos.push(file); // 将图片数据赋值给 formData
                        // 创建前端预览
                        const reader = new FileReader();
                        reader.onload = e => {
                            this.projetcPhotosPreview.push(e.target.result);
                        };
                        reader.readAsDataURL(file);
                    }
                });
            } else {
                alert('您最多只能上传9张照片。');
            }
        },
        toggleSelection(symptom) {
            const index = this.projectInfo.labels.indexOf(symptom);
            if (index === -1) {
                this.projectInfo.labels.push(symptom);
            } else {
                this.projectInfo.labels.splice(index, 1);
            }
        },
        async submitRequest() {
            // 将数据添加到 FormData 对象中
            this.formData.append('suretyInfo', JSON.stringify(this.suretyInfo));
            this.formData.append('suretyPhoto', this.suretyPhoto)
            this.formData.append('projectInfo', JSON.stringify(this.projectInfo));
            // 处理 project.photos[] 中的文件数组
            this.projectPhotos.forEach((photo, index) => {
                this.formData.append(`projectPhoto_${index}`, photo); // 使用唯一的键，如 photo_0, photo_1, ...
            });
            
            try {
                const response = await axios.post('http://localhost:5000/publishProject', this.formData);
                if (response.data.status === true) {
                    alert('众筹项目发布成功！');
                    this.$router.push(`/${this.$route.params.userId}/mine`);
                    // this.$router.push('/mine'); 
                }
            } catch (error) {
                    console.error('Error submitting request:', error);
                    alert('众筹项目发布失败，请稍后重试！');
            }
        },
    }
}
</script>

<style scoped>
.raise {
    font-family: 'Arial', sans-serif;
    /* background-color: #f0f0f0; */
    /* background-color: #f7f2ef; */
    height: 100vh;
    /* color: #6a5d5d; */
}

.container {
    max-width: 500px;
    margin: 20px auto;
    padding: 2rem;
    background-color: #fff;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.profile-header {
    text-align: center;
    margin-bottom: 2rem;
}

.photo-upload {
    display: none;
    /* 隐藏默认的文件输入 */
}

.photo-upload-label {
    display: inline-block;
    cursor: pointer;
    /* border-radius: 50%; */
    background-color: #ddd;
    width: 300px;
    height: 200px;
    margin: 0 auto;
    overflow: hidden;
    position: relative;
}

.photo-placeholder {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100%;
    color: #fff;
    font-size: 14px;
}

.photo-preview {
    width: 200px;
    height: 200px;
    /* 保持与.photo-upload-label一致 */
    object-fit: cover;
    border-radius: 50%;
}

.username-title {
    text-align: center;
}

.form-field {
    margin-top: 2rem;
    margin-bottom: 1rem;
}

.form-field label {
    display: block;
    margin-bottom: .5rem;
}

.form-field input,
.form-field textarea,
.form-field select {
    width: 100%;
    padding: .5rem;
    border: 1px solid #ddd;
    border-radius: .25rem;
    font-family: inherit;
    background-color: #fff;
}

.photo-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 0.5rem;
    margin-top: 1rem;
}

.photo-preview {
    width: 100%;
    border-radius: 5px;
    background-color: #eee;
    overflow: hidden;
}

.photo-preview img {
    width: 100%;
    height: auto;
    object-fit: cover;
    border-radius: 5px;
}

.buttons {
    display: flex;
}

.submit-button {
    width: 100%;
    padding: .75rem;
    border: none;
    border-radius: .25rem;
    background-color: #007bff;
    color: white;
    cursor: pointer;

    margin: 10px;
}

.submit-button:hover {
    background-color: #0056b3;
}

h2 {
    color: #333;
}

.bubbles {
    display: flex;
    flex-direction: column;
    flex-wrap: wrap;
    justify-content: center;
    gap: 10px;
    margin-top: 30px;
    margin-bottom: 20px;
}

.bubble-title {
    margin-left: 10px;
    text-align: left;
}

.bubble-container {
    display: flex;
    flex-wrap: wrap;
}

.bubble {
    padding: 10px 20px;
    background-color: #e2e2e2;
    border-radius: 20px;
    cursor: pointer;
    transition: background-color 0.3s ease;
    margin: 5px;
}

.bubble.selected {
    background-color: #4CAF50;
    color: white;
}

/* input[type="text"] {
  width: 100%;
  padding: 10px;
  border-radius: 5px;
  border: 1px solid #ddd;
  margin-top: 10px;
} */

button {
    padding: 10px 20px;
    background-color: #5cb85c;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    margin-top: 10px;
}

button:hover {
    background-color: #4cae4c;
}
</style>
