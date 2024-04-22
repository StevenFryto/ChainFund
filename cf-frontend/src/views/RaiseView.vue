<template>
  <div class="raise">
    <main class="container">
      <!-- Step 1: Guarantor Information -->
      <section v-if="step === 1" class="user-profile">
        <h1 class="username-title">保证人基本信息</h1>
        <div class="profile-header">
          <input type="file" id="photo" @change="previewPhoto" accept="image/*" class="photo-upload">
          <label for="photo" class="photo-upload-label">
            <img v-if="photoPreview" :src="photoPreview" alt="保证人照片预览" class="photo-preview"/>
            <span v-else class="photo-placeholder">点击此处上传保证人照片</span>
          </label>
        </div>
      </section>
      <form v-if="step === 1" @submit.prevent="nextStep">
        <!-- Guarantor's form fields -->
        <div class="form-field">
          <label for="name">保证人姓名</label>
          <input type="text" id="name" placeholder="请填写保证人姓名" required>
        </div>
        <div class="form-field">
          <label for="id">保证人身份证号</label>
          <input type="text" id="id" placeholder="请填写保证人身份证号" required>
        </div>
        <div class="form-field">
          <label for="phone">保证人手机号码</label>
          <input type="tel" id="phone" placeholder="请填写手机号码" required>
        </div>
        <div class="form-field">
          <label for="title">众筹标题</label>
          <textarea id="title" rows="4" placeholder="请输入众筹请求标题" required></textarea>
        </div>
        <button type="submit" class="submit-button">下一步</button>
      </form>

      <!-- Step 2: Patient Information -->
      <section v-if="step === 2" class="patient-info">
        <h1 class="username-title">患者基本信息</h1>
        <!-- Patient's form fields -->
        <div class="form-field">
          <label for="patient-name">患者姓名</label>
          <input type="text" id="patient-name" placeholder="请填写患者姓名" required>
        </div>
        <div class="form-field">
          <label for="patient-id">患者身份证号</label>
          <input type="text" id="patient-id" placeholder="请填写患者身份证号" required>
        </div>
        <div class="form-field">
          <label for="patient-gender">患者性别</label>
          <select id="patient-gender" class="form-input" required>
            <option value="">请选择性别</option>
            <option value="male">男</option>
            <option value="female">女</option>
          </select>
        </div>
        <div class="form-field">
          <label for="patient-birthdate">患者出生日期</label>
          <input type="date" id="patient-birthdate" required>
        </div>
        <div class="form-field">
          <label for="patient-job">患者职业</label>
          <input type="text" id="patient-job" placeholder="请填写患者职业" required>
        </div>
        <div class="form-field">
          <label for="cost-estimate">治疗费用预估（人民币）</label>
          <input type="number" id="cost-estimate" placeholder="请填写预估治疗费用" required>
        </div>
        <div class="form-field">
          <label for="patient-description">病情描述</label>
          <textarea id="patient-description" rows="4" placeholder="请输入病情描述" required></textarea>
        </div>
        <div class="form-field">
          <label for="patient-photos">患者目前状况照片（最多可上传9张）</label>
          <input type="file" id="patient-photos" @change="previewPatientPhotos" accept="image/*" multiple>
          <div class="photo-grid">
            <div class="photo-preview" v-for="(photo, index) in patientPhotoPreviews" :key="index">
              <img :src="photo" alt="患者照片预览">
            </div>
          </div>
        </div>
        <button type="submit" @click="nextStep" class="submit-button">下一步</button>
      </section>

      <!-- Step 3: Submit Request -->
      <section v-if="step === 3" class="bubbles-container">
        <h2>选择关键词标签</h2>
        <div class="bubbles">
          <div
            class="bubble"
            v-for="(symptom, index) in symptoms"
            :key="index"
            @click="toggleSelection(symptom)"
            :class="{ selected: selectedSymptoms.includes(symptom) }"
          >
            {{ symptom }}
          </div>
        </div>
        <div class="form-field">
          <input
          type="text"
          v-model="customSymptom"
          placeholder="如果列表中没有，请在此输入"
        />
        </div>
        <button type="submit" @click="submitRequest" class="submit-button">提交</button>
      </section>
    </main>
  </div>
</template>

<script>
export default {
  name: 'RaiseView',
  data() {
    return {
      step: 1, // 控制步骤的数据属性
      photoPreview: null, // 用于存储保证人照片预览的链接
      patientPhotoPreviews: [], // 用于存储患者照片预览的链接数组
      // 患者信息表单数据，实际应用中你可能需要更复杂的数据结构
      patientInfo: {
        name: '',
        id: '',
        gender: '',
        birthdate: '',
        job: '',
        description: '',
        photos: []
      },
      symptoms: [
        '儿童', '孕妇', '植物人', '脑血管', '心脏', '肝脏', '肾脏', '脾脏', '胰脏', '肺部', '消化系统', '免疫系统', '神经系统', '心脏病', '癌症', '肿瘤', '瘫痪', '糖尿病', '风湿病', '癫痫', '失明', '失聪', '骨折', '脑中风', '心肌梗塞', '手术', '化疗', '慢性病管理', '重症监护', '康复治疗', '药物', '检查', '康复设备'
      ],
      selectedSymptoms: [],
      customSymptom: '',
    };
  },
  methods: {
    nextStep() {
      // 验证当前步骤表单数据的逻辑可以在这里实现
      this.step++;
    },
    previewPhoto(event) {
      // 处理保证人照片预览逻辑
      const file = event.target.files[0];
      if (file && file.type.startsWith('image/')) {
        this.photoPreview = URL.createObjectURL(file);
      }
    },
    previewPatientPhotos(event) {
      const files = event.target.files;
      if (files.length + this.patientPhotoPreviews.length <= 9) {
        Array.from(files).forEach(file => {
          if (file.type.startsWith('image/')) {
            const reader = new FileReader();
            reader.onload = e => {
              this.patientPhotoPreviews.push(e.target.result);
            };
            reader.readAsDataURL(file);
          }
        });
      } else {
        alert('您最多只能上传9张照片。');
      }
    },
    toggleSelection(symptom) {
      const index = this.selectedSymptoms.indexOf(symptom);
      if (index === -1) {
        this.selectedSymptoms.push(symptom);
      } else {
        this.selectedSymptoms.splice(index, 1);
      }
    },
    submitRequest() {
      // 这里处理表单提交逻辑，例如向服务器发送数据
      alert('众筹信息已提交！');
      // 实际应用中，您会在这里发送一个请求到服务器
      // 然后清空表单，或者跳转到其他页面
    }
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
  margin: 0 auto;
  padding: 2rem;
  background-color: #fff;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

.profile-header {
  text-align: center;
  margin-bottom: 2rem;
}

.photo-upload {
  display: none; /* 隐藏默认的文件输入 */
}

.photo-upload-label {
  display: inline-block;
  cursor: pointer;
  border-radius: 50%;
  background-color: #ddd;
  width: 120px;
  height: 120px;
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
  width: 120px; /* 相同的宽度和高度将保证是圆形 */
  height: 120px; /* 保持与.photo-upload-label一致 */
  object-fit: cover;
  border-radius: 50%;
}

.username-title {
  text-align: center;
}

.form-field {
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

.submit-button {
  width: 100%;
  padding: .75rem;
  border: none;
  border-radius: .25rem;
  background-color: #007bff;
  color: white;
  cursor: pointer;
}

.submit-button:hover {
  background-color: #0056b3;
}

h2 {
  color: #333;
}

.bubbles {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 10px;
  margin-bottom: 20px;
}

.bubble {
  padding: 10px 20px;
  background-color: #e2e2e2;
  border-radius: 20px;
  cursor: pointer;
  transition: background-color 0.3s ease;
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
