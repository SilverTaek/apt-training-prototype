<template>
  <div class="kpi">
    <h3>{{ title }}</h3>
    <p>{{ value }}</p>
    <div v-if="note" class="note">{{ note }}</div>
  </div>
</template>

<script>
export default {
  name: 'KpiStat',
  props: {
    title: { type: String, required: true },
    value: { type: String, required: true },
    note: { type: String, default: '' }
  }
};
</script>

<style scoped>
.kpi{flex:1 1 220px;background:#fff;border:1px solid var(--line);border-radius:12px;padding:14px 16px}
.kpi h3{margin:0 0 6px 0;font-size:12px;color:var(--muted);font-weight:600}
.kpi p{margin:0;font-size:22px;font-weight:700}
.note{font-size:12px;color:var(--muted)}
</style>
