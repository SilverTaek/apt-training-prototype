<template>
  <div class="app-container">
    <TopBar />
    <main class="main-content">
      <router-view />
    </main>
  </div>
</template>

<script>
import TopBar from './components/TopBar.vue';
export default {
  name: 'App',
  components: { TopBar }
};
</script>

<style>
.app-container {
  display: flex;
  flex-direction: column;
  height: 100vh;
}
.main-content {
  flex: 1;
  padding: 20px;
  background: #f5f7fa;
}
</style>
