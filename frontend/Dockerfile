FROM node:18

WORKDIR /app

COPY package.json package-lock.json ./
RUN npm install --legacy-peer-deps

COPY . .

RUN npm install -D vite  # Vite 강제 설치
RUN npm install -D @vitejs/plugin-react  # ✅ Vite React 플러그인 강제 설치
RUN npm run build

CMD ["npm", "run", "dev"]

EXPOSE 3000
