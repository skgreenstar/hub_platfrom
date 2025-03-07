# 1단계: Node 환경에서 빌드
FROM node:21 AS build

WORKDIR /app

# (1) package.json, pnpm-lock.yaml만 먼저 복사 => 의존성 설치용 (캐시 최적화)
COPY package.json pnpm-lock.yaml ./

# (2) pnpm이 기본 설치되어 있지 않다면, npm으로 전역 설치
RUN npm install -g pnpm

# (3) 의존성 설치
RUN pnpm install

# (4) 나머지 소스 전체 복사
COPY . .

# (5) 빌드 (React라면 "pnpm run build" 같은 스크립트)
RUN pnpm run build

# 2단계: Nginx에 정적 파일 배포
FROM nginx:latest

# (6) 빌드된 결과물(dist 폴더 등)만 복사
COPY --from=build /app/dist /usr/share/nginx/html

# (7) Nginx 설정 파일 복사 (커스텀 설정 필요 시)
COPY ./nginx.conf /etc/nginx/nginx.conf

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
