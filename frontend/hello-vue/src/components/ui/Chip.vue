<template>
  <span class="chip" :class="kind"><slot /></span>
</template>

<script>
export default {
  name: 'UiChip',
  props: {
    kind: { type: String, default: '' } // ok|warn|bad|info
  }
};
</script>

<style scoped>
.chip{display:inline-block;padding:.2rem .55rem;border-radius:999px;font-size:12px;border:1px solid transparent}
.ok{background:#ecfdf5;color:#065f46;border-color:#bbf7d0}
.warn{background:#fffbeb;color:#92400e;border-color:#fde68a}
.bad{background:#fef2f2;color:#991b1b;border-color:#fecaca}
.info{background:#eff6ff;color:#1e40af;border-color:#bfdbfe}
</style>
