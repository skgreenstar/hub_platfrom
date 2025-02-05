from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.user_schema import UserCreate, UserResponse
from app.services.user_service import create_user, get_user
from app.database import get_db

router = APIRouter()

@router.post("/", response_model=UserResponse, summary="새로운 사용자 생성", description="새로운 사용자를 생성하고 데이터베이스에 저장합니다.")
def create_user_endpoint(user: UserCreate, db: Session = Depends(get_db)):
    """
    ### 사용자 생성 API
    - **user**: 사용자 정보 (이름, 이메일, 비밀번호 등)
    - **반환값**: 생성된 사용자 정보
    """
    return create_user(db, user)

@router.get("/{user_id}", response_model=UserResponse, summary="사용자 정보 조회", description="사용자의 ID를 기반으로 정보를 조회합니다.")
def get_user_endpoint(user_id: int, db: Session = Depends(get_db)):
    """
    ### 사용자 정보 조회 API
    - **user_id**: 조회할 사용자의 ID
    - **반환값**: 사용자 정보
    """
    user = get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
