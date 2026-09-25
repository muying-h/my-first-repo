<template>
  <div style="max-width:500px;margin:40px auto;">
    <h2>录入个人背景</h2>
    <div v-if="error" style="color:red">{{ error }}</div>
    <div><input v-model="form.undergraduate_school" placeholder="本科院校 *" /></div>
    <div><input v-model="form.undergraduate_major" placeholder="本科专业 *" /></div>
    <div><input v-model="form.rank_percent" placeholder="成绩排名（如前20%）*" /></div>
    <div><input v-model="form.target_major" placeholder="目标专业" /></div>
    <div><input v-model="form.preferred_region" placeholder="意向地域" /></div>
    <div>
      <select v-model="form.risk_preference">
        <option value="">风险偏好</option>
        <option value="冲">冲</option>
        <option value="稳">稳</option>
        <option value="保">保</option>
      </select>
    </div>
    <button @click="submit">生成推荐</button>
  </div>
</template>

<script setup>
import { reactive, ref } from 'vue'
import { useRouter } from 'vue-router'
import axios from 'axios'

const router = useRouter()
const form = reactive({
  undergraduate_school: '',
  undergraduate_major: '',
  rank_percent: '',
  target_major: '',
  preferred_region: '',
  risk_preference: '',
})
const error = ref('')

const submit = async () => {
  if (!form.undergraduate_school) { error.value = '本科院校为必填项'; return }
  if (!form.undergraduate_major) { error.value = '本科专业为必填项'; return }
  if (!form.rank_percent) { error.value = '成绩排名为必填项'; return }
  if (!/^(前\d+%|\d+\/\d+)$/.test(form.rank_percent)) {
    error.value = "成绩排名格式应为'前X%'或'X/Y'"
    return
  }
  error.value = ''
  try {
    const res = await axios.post('http://127.0.0.1:8000/api/profile', form)
    router.push('/result/' + res.data.profile_id)
  } catch (e) {
    error.value = '提交失败，请检查后端服务是否启动'
  }
}
</script>