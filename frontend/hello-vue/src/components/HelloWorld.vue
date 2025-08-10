<template>
    <div class="hello">
    <h1>Vue ↔ FastAPI 테스트</h1>
    <button @click="callApi">백엔드 호출</button>
    <p v-if="loading">로딩 중…</p>
    <pre v-if="error" style="color:red">{{ error }}</pre>
    <pre v-if="data">{{ data }}</pre>
  </div>
</template>

<script>
export default {
  name: "HelloWorld",
  data() {
    return {
      loading: false,
      data: null,
      error: null,
    };
  },
  methods: {
    async callApi() {
      this.loading = true;
      this.data = null;
      this.error = null;
      try {
        const res = await fetch("http://127.0.0.1:8000/hello");
        if (!res.ok) throw new Error(`HTTP ${res.status}`);
        const json = await res.json();
        this.data = JSON.stringify(json, null, 2);
      } catch (e) {
        this.error = String(e);
      } finally {
        this.loading = false;
      }
    },
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
