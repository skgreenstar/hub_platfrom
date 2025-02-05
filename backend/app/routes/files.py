from fastapi import APIRouter, UploadFile, File, HTTPException
import shutil, os
from fastapi.responses import FileResponse
from app.services.file_service import save_file


router = APIRouter()
UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post("/upload", summary="파일 업로드", description="파일을 업로드하고 저장합니다.")
async def upload_file(file: UploadFile = File(...)):
    """
    ### 파일 업로드 API
    - **file**: 업로드할 파일
    - **반환값**: 업로드 성공 여부 메시지
    """
async def upload_file(file: UploadFile = File(...)):
    return await save_file(file)

@router.get("/download/{filename}", summary="파일 다운로드", description="업로드된 파일을 다운로드합니다.")
async def download_file(filename: str):
    """
    ### 파일 다운로드 API
    - **filename**: 다운로드할 파일 이름
    - **반환값**: 파일 응답 (파일이 존재하지 않으면 404 에러 발생)
    """
    return await get_file(filename)