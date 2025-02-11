import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

export default defineConfig({
  plugins: [react()],
  server: {
    port: 3000,
    open: false,
    strictPort: true,
    watch: {
      usePolling: true,  // ✅ 파일 감지 방식 변경
    },
    proxy: {
      "/api": "http://localhost:8000", // 백엔드 프록시 설정
    },
    fs: {
      strict: false, // 파일 시스템 액세스 제한 해제
    },
  },
  build: {
    outDir: "dist",
  },
});
