from fastapi import APIRouter, Query
from app.ai.search_engine import search_documents

router = APIRouter()

@router.get("/", summary="AI 기반 문서 검색", description="Qdrant를 활용한 AI 기반 문서 검색을 수행합니다.")
async def search_api(query: str = Query(..., description="검색할 문장 입력")):
    """
    ### AI 기반 문서 검색 API
    - **query**: 검색할 키워드
    - **반환값**: 검색된 문서 목록
    """
    return search_documents(query)