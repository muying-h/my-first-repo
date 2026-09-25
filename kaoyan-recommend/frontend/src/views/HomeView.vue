<template>
  <div style="text-align:center;padding:60px;">
    <h1>考研院校推荐系统</h1>
    <p>输入你的背景，几分钟得到带理由的院校清单</p>
    <button @click="$router.push('/profile')">开始评估</button>
    <button @click="$router.push('/universities')">浏览院校库</button>
  </div>
</template>