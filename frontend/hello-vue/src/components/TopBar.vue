<template>
  <header class="topbar">
    <!-- 브랜드 / 홈 -->
    <RouterLink class="brand" to="/dashboard" title="홈(대시보드)">
      <div class="logo">H•TI</div>
      <div class="sysname">HanaTI APT Training</div>
    </RouterLink>

    <!-- 좌측 정렬 네비게이션 -->
    <nav class="nav" aria-label="주요 메뉴">
      <RouterLink class="navbtn" to="/users">사용자관리</RouterLink>
      <RouterLink class="navbtn" to="/senders">메일 발송 주소</RouterLink>
      <RouterLink class="navbtn" to="/groups">훈련대상</RouterLink>
      <RouterLink class="navbtn" to="/mail-templates">피싱메일</RouterLink>
      <RouterLink class="navbtn" to="/page-templates">피싱페이지</RouterLink>
      <RouterLink class="navbtn" to="/campaigns">모의훈련</RouterLink>
    </nav>

    <!-- 우측 계정 / 로그인 -->
    <div class="account">
      <template v-if="isAuthed">
        <span class="who">
          <span class="dot"></span>{{ displayName }}
        </span>
        <button class="btn ghost" @click="logout">로그아웃</button>
      </template>
      <template v-else>
        <RouterLink class="btn primary" to="/login">로그인</RouterLink>
      </template>
    </div>
  </header>
</template>

<script>
export default {
  name: 'TopBar',
  data() {
    return {
      user: null
    };
  },
  computed: {
    isAuthed() {
      return !!this.user;
    },
    displayName() {
      return this.user?.name || this.user?.id || 'Unknown';
    }
  },
  created() {
    // 매우 단순한 목업 인증정보: localStorage 사용
    const raw = localStorage.getItem('hanati_user');
    if (raw) {
      try { this.user = JSON.parse(raw); } catch {}
    }
  },
  methods: {
    logout() {
      localStorage.removeItem('hanati_user');
      this.user = null;
      this.$router.push('/login');
    }
  }
};
</script>

<style scoped>
:root{
  --brand:#00a39a;
  --brand-dark:#008c83;
  --line:#e6ebf2;
  --text:#0d1b2a;
  --muted:#5b6779;
  --card:#fff;
}
.topbar{
  position: sticky; top:0; z-index: 9;
  display:flex; align-items:center; gap:16px;
  padding:12px 16px; background:var(--card); border-bottom:1px solid var(--line);
}
.brand{display:flex;align-items:center;gap:10px;color:var(--text);font-weight:700}
.logo{width:30px;height:30px;border-radius:8px;background:linear-gradient(135deg,var(--brand),var(--brand-dark));
  display:grid;place-items:center;color:#fff;font-size:12px;font-weight:800;letter-spacing:.5px}
.sysname{font-size:16px}
.nav{display:flex;gap:8px;margin-left:18px;flex-wrap:wrap}
.navbtn{
  border:1px solid var(--line); background:#fff; color:#22303c;
  padding:8px 12px; border-radius:8px;
}
.navbtn.router-link-active{background:var(--brand); color:#fff; border-color:var(--brand-dark)}
.account{margin-left:auto; display:flex; align-items:center; gap:10px}
.who{color:var(--muted); display:flex; align-items:center; gap:6px}
.dot{width:8px;height:8px;border-radius:50%;background:#16a34a;display:inline-block}
.btn{border:1px solid var(--line);padding:8px 12px;border-radius:8px;background:#fff;color:#22303c}
.btn.primary{background:var(--brand);border-color:var(--brand-dark);color:#fff}
.btn.ghost{background:#fff}
</style>
