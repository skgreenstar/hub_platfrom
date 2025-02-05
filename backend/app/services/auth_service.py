from datetime import datetime, timedelta
from typing import Optional
from jose import JWTError, jwt
from passlib.context import CryptContext
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

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

# 사용자 인증 (더미 데이터)
fake_users_db = {
    "testuser": {  # ✅ 아이디(username) 기반으로 변경
        "username": "testuser",
        "hashed_password": hash_password("password123"),
    }
}


def authenticate_user(username: str, password: str):
    logging.debug(f"Authenticating user: {username}")
    user = fake_users_db.get(username)

    if not user:
        logger.warning(f"User not found: {username}")
    return None

    if not verify_password(password, user["hashed_password"]):
        logger.warning(f"Password verification failed for user: {username}")
    return None
    
    # if not user or not verify_password(password, user["hashed_password"]):
        # return None

    token = create_access_token({"sub": username})
    logging.debug(f"Token generated: {token}")
    return token
    # return create_access_token({"sub": username})