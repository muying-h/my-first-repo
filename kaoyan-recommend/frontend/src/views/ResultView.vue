<template>
  <div style="max-width:700px;margin:40px auto;">
    <h2>推荐结果（候选清单 · 共 {{ candidates.length }} 条）</h2>
    <div v-if="loading">加载中...</div>
    <div v-else-if="error" style="color:red">{{ error }}</div>
    <div v-else-if="candidates.length===0">未命中，请放宽条件</div>
    <div v-else>
      <div v-if="degraded" style="color:orange;margin-bottom:10px;">{{ notice }}</div>
      <div v-for="(c, i) in candidates" :key="i" style="border:1px solid #ccc;padding:10px;margin:10px 0;">
        <h3>{{ c.university }} · {{ c.major }}</h3>
        <p>复试线：{{ c.score_line }} | 报录比：{{ c.ratio }}</p>
        <p>理由：{{ c.reason }}</p>
        <p v-if="c.risk">风险：{{ c.risk }}</p>
        <p v-if="c.pending" style="color:#b8860b;">△ 待核实：数据缺失，请以官网为准</p>
      </div>
    </div>
    <button @click="$router.push('/')">返回首页</button>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import axios from 'axios'

const route = useRoute()
const loading = ref(true)
const error = ref('')
const degraded = ref(false)
const notice = ref('')
const candidates = ref([])

onMounted(async () => {
  try {
    const profileId = route.params.profileId
    const res = await axios.post('http://127.0.0.1:8000/api/recommend', { profile_id: profileId })
    degraded.value = res.data.degraded
    notice.value = res.data.notice
    candidates.value = res.data.candidates
  } catch (e) {
    error.value = '获取推荐失败，请稍后重试'
  } finally {
    loading.value = false
  }
})
</script>