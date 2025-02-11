FROM node:21 AS build

WORKDIR /app
COPY . /app

RUN npm install
# ✅ package.json만 먼저 복사 (캐시 최적화)
COPY package.json package-lock.json /app/  

# Install dependencies and build React app
RUN npm run build

# Nginx 설정
FROM nginx:latest
COPY --from=build /app/dist /usr/share/nginx/html
COPY ./nginx.conf /etc/nginx/nginx.conf  
# ✅ Nginx 설정 파일 복사

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]

# COPY package.json package-lock.json ./
# RUN npm install --legacy-peer-deps

# COPY . .

# RUN npm install vite --save-dev  # Vite 강제 설치
# RUN npm install -D @vitejs/plugin-react  # ✅ Vite React 플러그인 강제 설치
# RUN npm update vite
# # RUN npm run build

# CMD ["npm", "run", "dev"]

# EXPOSE 3000
