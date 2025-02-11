from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db

router = APIRouter()

@router.get(
    "/documents/search",
    summary="문서 검색 API",
    description="검색어(`q`)를 받아 문서를 검색하는 API입니다.",
    response_description="검색된 문서 목록을 반환합니다."
)
def search_documents(q: str, db: Session = Depends(get_db)):
    """
    ### 🔍 문서 검색 API
    - `q`: 검색할 키워드
    - `db`: 데이터베이스 세션 (자동 주입)
    
    **📌 응답 예시**
    ```json
    {
        "query": "test",
        "results": [
            {"id": 1, "title": "Test Document", "content": "This is a test document"}
        ]
    }
    ```
    """
    return {"query": q, "results": []}  # 실제 검색 로직 필요
