from datetime import datetime, timedelta
from typing import Optional
from jose import JWTError, jwt
from passlib.context import CryptContext
import logging

logging.basicConfig(level=logging.DEBUG)

# JWT 설정
SECRET_KEY = "your-secret-key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# 비밀번호 암호화 설정
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# 비밀번호 해싱
def hash_password(password: str) -> str:
    return pwd_context.hash(password)

# 비밀번호 검증
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

# JWT 액세스 토큰 생성
def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta if expires_delta else timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

# 사용자 인증 (더미 데이터 사용)
fake_users_db = {
    "user@example.com": {
        "email": "user@example.com",
        "hashed_password": hash_password("password123"),
    }
}

def authenticate_user(email: str, password: str) -> Optional[str]:
    logging.debug(f"Authenticating user: {email}")
    user = fake_users_db.get(email)

    if not user:
        logging.debug("User not found")
    return None

    if not verify_password(password, user["hashed_password"]):
        logging.debug("Password verification failed")
    return None
    
    # if not user or not verify_password(password, user["hashed_password"]):
        # return None

    token = create_access_token({"sub": email})
    logging.debug(f"Token generated: {token}")
    return token
    # return create_access_token({"sub": email})