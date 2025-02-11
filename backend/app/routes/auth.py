from fastapi import APIRouter, HTTPException, Depends
from app.schemas.auth import LoginRequest, TokenResponse, RegisterRequest, UserResponse
from app.services.auth_service import authenticate_user, hash_password, verify_password, create_access_token
from sqlalchemy.orm import Session
from app.database import SessionLocal, engine
from app.models.user import User
from app.database import get_db

router = APIRouter()

@router.post("/login", response_model=TokenResponse, summary="사용자 로그인", description="사용자의 자격 증명을 확인하고 액세스 토큰을 반환합니다.")
def login(request: LoginRequest, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == request.username).first()
    """
    ### 사용자 로그인 API
    - **username**: 사용자 ID
    - **password**: 비밀번호
    - **반환값**: 액세스 토큰
    """
    if not user:
        raise HTTPException(status_code=401, detail="User not found")

    if not verify_password(request.password, user.hashed_password):
        print(f"🚀 비밀번호 검증 실패: {request.password} vs {user.hashed_password}")  # ✅ 디버깅 추가
        raise HTTPException(status_code=401, detail="Invalid credentials")

    access_token = create_access_token({"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}

@router.post("/register", response_model=UserResponse, summary="회원 가입", description="새 사용자를 등록합니다.")
def register_user(user_data: RegisterRequest, db: Session = Depends(get_db)):
    """
    ### 회원 가입 API
    - **username**: 사용자 아이디
    - **email**: 이메일
    - **password**: 비밀번호 (해싱 처리됨)
    - **반환값**: 생성된 사용자 정보
    """
    existing_user = db.query(User).filter(User.username == user_data.username).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="이미 존재하는 아이디입니다.")

    existing_email = db.query(User).filter(User.email == user_data.email).first()
    if existing_email:
        raise HTTPException(status_code=400, detail="이미 존재하는 이메일입니다.")

    hashed_password = hash_password(user_data.password)
    print(f"🚀 비밀번호 해싱됨: {hashed_password}")  # ✅ 해싱된 비밀번호 출력 (디버깅)

    new_user = User(username=user_data.username, email=user_data.email, hashed_password=hashed_password)

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

