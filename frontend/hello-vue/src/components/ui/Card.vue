<template>
  <div class="card">
    <div class="hd" v-if="title || $slots.actions">
      <div class="title">{{ title }}</div>
      <div class="actions"><slot name="actions"></slot></div>
    </div>
    <div class="bd"><slot /></div>
  </div>
</template>

<script>
export default {
  name: 'UiCard',
  props: {
    title: { type: String, required: false }
  }
};
</script>

<style scoped>
.card{background:#fff;border:1px solid var(--line);border-radius:12px;overflow:hidden}
.hd{display:flex;align-items:center;justify-content:space-between;padding:14px 16px;border-bottom:1px solid var(--line);font-weight:600}
.bd{padding:14px 16px}
.title{font-weight:600}
.actions :deep(.btn){margin-left:8px}
</style>
