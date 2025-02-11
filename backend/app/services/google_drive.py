import os
import json
from googleapiclient.discovery import build
from google.oauth2 import service_account

# Google Drive API 설정
SCOPES = ["https://www.googleapis.com/auth/drive"]
SERVICE_ACCOUNT_FILE = "credentials.json"  # Google Cloud에서 받은 JSON 파일

def authenticate_drive():
    """Google Drive API 인증"""
    creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES
    )
    return build("drive", "v3", credentials=creds)

drive_service = authenticate_drive()

def search_file(filename: str):
    """Google Drive에서 특정 파일 검색"""
    query = f"name contains '{filename}' and trashed = false"
    results = drive_service.files().list(q=query, fields="files(id, name)").execute()
    files = results.get("files", [])
    
    return files if files else None

def download_file(file_id: str, save_path: str):
    """Google Drive에서 특정 파일 다운로드"""
    request = drive_service.files().get_media(fileId=file_id)
    with open(save_path, "wb") as file:
        file.write(request.execute())
    return save_path
