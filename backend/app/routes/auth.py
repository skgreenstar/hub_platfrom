from fastapi import APIRouter, HTTPException
from app.schemas.auth import LoginRequest, TokenResponse
from app.services.auth_service import authenticate_user

router = APIRouter()

@router.post("/login", response_model=TokenResponse, summary="사용자 로그인", description="사용자의 자격 증명을 확인하고 액세스 토큰을 반환합니다.")
async def login(request: LoginRequest):
    """
    ### 사용자 로그인 API
    - **email**: 사용자 이메일
    - **password**: 비밀번호
    - **반환값**: 액세스 토큰
    """
    token = await authenticate_user(request.email, request.password)
    if not token:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return {"access_token": token, "token_type": "bearer"}
