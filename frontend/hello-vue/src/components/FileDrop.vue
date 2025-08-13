<template>
  <div
    class="drop"
    :class="{ dragover: dragging }"
    @dragover.prevent="dragging=true"
    @dragleave.prevent="dragging=false"
    @drop.prevent="onDrop"
  >
    <p class="hint">
      📎 파일을 드래그앤드롭 하거나 <label class="link">여기</label>를 클릭해 업로드
    </p>
    <input ref="picker" type="file" :multiple="multiple" :accept="accept" hidden @change="onPick"/>
    <button class="btn" @click="$refs.picker.click()">파일 선택</button>

    <ul v-if="files.length" class="list">
      <li v-for="(f,i) in files" :key="i">
        {{ f.name }} <span class="muted">({{ pretty(f.size) }})</span>
        <button class="btn ghost small" @click="remove(i)">삭제</button>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: 'FileDrop',
  props: {
    multiple: { type: Boolean, default: true },
    accept: { type: String, default: '' },
    modelValue: { type: Array, default: () => [] }
  },
  emits: ['update:modelValue', 'change'],
  data(){ return { dragging:false, files: this.modelValue.slice() }; },
  watch:{
    files: {
      deep:true,
      handler(v){ this.$emit('update:modelValue', v); this.$emit('change', v); }
    }
  },
  methods:{
    onDrop(e){
      this.dragging=false;
      const dropped = Array.from(e.dataTransfer.files || []);
      this.files = this.multiple ? [...this.files, ...dropped] : (dropped[0] ? [dropped[0]] : []);
    },
    onPick(e){
      const picked = Array.from(e.target.files || []);
      this.files = this.multiple ? [...this.files, ...picked] : (picked[0] ? [picked[0]] : []);
      e.target.value = '';
    },
    remove(i){ this.files.splice(i,1); },
    pretty(bytes){
      if(bytes < 1024) return bytes+' B';
      if(bytes < 1024*1024) return (bytes/1024).toFixed(1)+' KB';
      return (bytes/1024/1024).toFixed(1)+' MB';
    }
  }
};
</script>

<style scoped>
.drop{
  border:1px dashed var(--line); border-radius:10px; padding:16px; background:#fafcff;
}
.dragover{ background:#f0fbf9; border-color:#9de4df }
.hint{margin:0 0 10px 0; color:var(--muted)}
.link{color:var(--brand); cursor:pointer}
.list{margin:12px 0 0 0; padding:0 0 0 16px}
.muted{color:var(--muted); margin-left:6px}
.btn{border:1px solid var(--line);padding:6px 10px;border-radius:8px;background:#fff;color:#22303c}
.btn.small{padding:4px 8px; font-size:12px; margin-left:8px}
.btn.ghost{background:#fff}
</style>
