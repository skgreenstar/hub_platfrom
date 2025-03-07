import os
import shutil
from fastapi import APIRouter, HTTPException, UploadFile, Query
from fastapi.responses import FileResponse
from app.services.google_drive import search_file, download_file

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)  # 업로드 디렉토리 자동 생성

router = APIRouter()

# 📂 업로드된 파일 목록 API
@router.get("/files/list", summary="파일 목록 가져오기")
async def list_files():
    try:
        files = os.listdir(UPLOAD_DIR)
        return files
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.post("/files/upload", summary="파일 업로드", description="로컬 서버에 파일을 업로드합니다.")
async def save_file(file: UploadFile):
    """
    ## 🔹 파일 업로드 API
    - **파일을 업로드하여 서버의 `uploads/` 디렉토리에 저장합니다.**
    - **요청 본문:** `multipart/form-data`
    
    **📌 응답 예시**
    ```json
    {
        "filename": "example.pdf",
        "status": "uploaded",
        "path": "uploads/example.pdf"
    }
    ```
    """
    file_location = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {"filename": file.filename, "status": "uploaded", "path": file_location}


@router.get("/files/download", summary="로컬 파일 다운로드", description="서버에서 특정 파일을 다운로드합니다.")
async def get_file(filename: str):
    """
    ## 🔹 로컬 파일 다운로드 API
    - **업로드된 파일을 다운로드합니다.**
    - **쿼리 파라미터:** `filename`
    
    **📌 응답 예시**
    ```json
    {
        "message": "File downloaded",
        "filename": "example.pdf"
    }
    ```
    """
    file_path = os.path.join(UPLOAD_DIR, filename)
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="File not found")
    return FileResponse(file_path, filename=filename)


@router.get("/files/search", summary="Google Drive 파일 검색", description="Google Drive에서 특정 파일을 검색합니다.")
async def search_files(filename: str = Query(..., description="검색할 파일 이름")):
    """
    ## 🔹 Google Drive 파일 검색 API
    - **Google Drive에서 특정 파일을 검색합니다.**
    - **쿼리 파라미터:** `filename`
    
    **📌 응답 예시**
    ```json
    {
        "files": [
            {"id": "1A2B3C4D", "name": "example.pdf"}
        ]
    }
    ```
    """
    files = search_file(filename)
    if not files:
        raise HTTPException(status_code=404, detail="File not found in Google Drive")
    return {"files": files}


@router.get("/files/download/google", summary="Google Drive 파일 다운로드", description="Google Drive에서 특정 파일을 다운로드합니다.")
async def download_google_drive_file(filename: str = Query(..., description="다운로드할 파일 이름")):
    """
    ## 🔹 Google Drive 파일 다운로드 API
    - **Google Drive에서 특정 파일을 다운로드합니다.**
    - **쿼리 파라미터:** `filename`
    
    **📌 응답 예시**
    ```json
    {
        "message": "File downloaded",
        "path": "downloads/example.pdf"
    }
    ```
    """
    files = search_file(filename)
    if not files:
        raise HTTPException(status_code=404, detail="File not found in Google Drive")

    file_id = files[0]["id"]  # 첫 번째 검색 결과 다운로드
    save_path = f"downloads/{filename}"
    os.makedirs("downloads", exist_ok=True)
    
    download_file(file_id, save_path)
    return {"message": "File downloaded", "path": save_path}

# from app.services.google_drive import search_file
# from fastapi import APIRouter, UploadFile, File, HTTPException
# import shutil, os
# from fastapi.responses import FileResponse
# from app.services.file_service import save_file


# router = APIRouter()
# UPLOAD_DIR = "uploads"
# os.makedirs(UPLOAD_DIR, exist_ok=True)

# @router.post("/upload", summary="파일 업로드", description="파일을 업로드하고 저장합니다.")
# async def upload_file(file: UploadFile = File(...)):
#     """
#     ### 파일 업로드 API
#     - **file**: 업로드할 파일
#     - **반환값**: 업로드 성공 여부 메시지
#     """
# async def upload_file(file: UploadFile = File(...)):
#     return await save_file(file)

# @router.get("/download/{filename}", summary="파일 다운로드", description="업로드된 파일을 다운로드합니다.")
# async def download_file(filename: str):
#     """
#     ### 파일 다운로드 API
#     - **filename**: 다운로드할 파일 이름
#     - **반환값**: 파일 응답 (파일이 존재하지 않으면 404 에러 발생)
#     """
#     return await get_file(filename)



# @router.get("/files/search")
# def search_files(filename: str):
#     """Google Drive에서 파일 검색 API"""
#     files = search_file(filename)
#     if not files:
#         raise HTTPException(status_code=404, detail="File not found in Google Drive")
#     return {"files": files}
