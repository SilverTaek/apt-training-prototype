<template>
  <div class="searchbar">
    <div class="row">
      <input
        v-model="local.q"
        type="text"
        class="input"
        :placeholder="placeholder"
        @keyup.enter="emitSearch"
      />
      <select v-if="showRole" v-model="local.role" class="select">
        <option value="">역할(전체)</option>
        <option value="admin">관리자</option>
        <option value="operator">운영자</option>
        <option value="viewer">사용자</option>
      </select>
      <select v-if="showStatus" v-model="local.status" class="select">
        <option value="">상태(전체)</option>
        <option value="active">활성</option>
        <option value="locked">잠금</option>
        <option value="inactive">비활성</option>
      </select>
      <button class="btn" @click="emitSearch">
        🔍 검색
      </button>
      <button v-if="showReset" class="btn ghost" @click="reset">초기화</button>
      <slot name="extra"></slot>
    </div>
  </div>
</template>

<script>
export default {
  name: 'SearchBar',
  props: {
    placeholder: { type: String, default: '이름/아이디 등 검색' },
    showRole: { type: Boolean, default: false },
    showStatus: { type: Boolean, default: false },
    showReset: { type: Boolean, default: true },
    value: { type: Object, default: () => ({}) } // v-model용(옵션)
  },
  emits: ['search', 'update:value'],
  data() {
    return {
      local: {
        q: this.value.q || '',
        role: this.value.role || '',
        status: this.value.status || ''
      }
    };
  },
  watch: {
    local: {
      deep: true,
      handler(v){ this.$emit('update:value', v); }
    }
  },
  methods: {
    emitSearch() { this.$emit('search', { ...this.local }); },
    reset() {
      this.local = { q:'', role:'', status:'' };
      this.emitSearch();
    }
  }
};
</script>

<style scoped>
.searchbar{padding:10px 0}
.row{display:flex;flex-wrap:wrap;gap:8px;align-items:center}
.input,.select{
  border:1px solid var(--line); padding:8px 10px; border-radius:8px; min-width:200px; background:#fff
}
.btn{border:1px solid var(--line);padding:8px 12px;border-radius:8px;background:#fff;color:#22303c}
.btn.ghost{background:#fff}
</style>
