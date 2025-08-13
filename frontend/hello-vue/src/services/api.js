import axios from 'axios'

export const api = axios.create({
  baseURL: import.meta.env.VITE_API_BASE_URL,
  withCredentials: false,
})

api.interceptors.response.use(r => r, (err) => {
  console.error('[API ERROR]', err?.response?.status, err?.message)
  return Promise.reject(err)
})
