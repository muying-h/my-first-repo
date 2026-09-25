<template>
  <div style="max-width:700px;margin:40px auto;">
    <h2>院校库</h2>
    <div v-if="list.length===0">暂无院校数据，请先导入样例数据</div>
    <div v-for="u in list" :key="u.university_id" style="border:1px solid #ccc;padding:10px;margin:10px 0;">
      <h3>{{ u.name }}（{{ u.level }}，{{ u.region }}）</h3>
      <p v-for="m in u.majors" :key="m.major_id">{{ m.name }}（{{ m.degree_type }}）</p>
    </div>
    <button @click="$router.push('/')">返回首页</button>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'

const list = ref([])

onMounted(async () => {
  try {
    const res = await axios.get('http://127.0.0.1:8000/api/universities/')
    list.value = res.data
  } catch (e) {
    console.error('加载院校数据失败', e)
  }
})
</script>