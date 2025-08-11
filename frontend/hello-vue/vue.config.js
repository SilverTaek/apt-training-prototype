const { defineConfig } = require('@vue/cli-service')
module.exports = {
  devServer: {
    proxy: {
      "/mail": { target: "http://127.0.0.1:8000", changeOrigin: true },
    },
  },
};
