import { defineStore } from 'pinia'

export const useAuthStore = defineStore('auth', {
  state: () => ({
    user: { name: '홍길동', role: '관리자' }, // null 이면 로그아웃
  }),
  actions: {
    login(name = '홍길동', role = '관리자') { this.user = { name, role } },
    logout() { this.user = null },
  },
})
