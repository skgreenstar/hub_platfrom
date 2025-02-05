import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

export default defineConfig({
  plugins: [react()],
  root: ".",  // 프로젝트 루트가 index.html을 찾도록 설정
  publicDir: "public",  // ✅ public 폴더 명시
  build: {
    outDir: "dist",
    emptyOutDir: true,
    rollupOptions: {
      input: "public/index.html", // ✅ index.html을 명확히 지정
    },
  },
  server: {
    port: 3000,
  },
});
