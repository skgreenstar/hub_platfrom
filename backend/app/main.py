# backend/app/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import auth, files, search, users

app = FastAPI(
    title="Hub Platform API",
    description="AI 기반 문서 검색 및 관리 플랫폼",
    version="1.0.0",
    contact={
        "name": "Hub Platform Support",
        "email": "support@hubplatform.com",
    },
    docs_url="/docs",  # Swagger UI 경로
    redoc_url="/redoc",  # ReDoc UI 경로
    openapi_url="/openapi.json"  # OpenAPI 문서 URL
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/auth", tags=["Authentication"])
app.include_router(files.router, prefix="/files", tags=["File Management"])
app.include_router(search.router, prefix="/search", tags=["AI Search"])
app.include_router(users.router, prefix="/users", tags=["User Management"])