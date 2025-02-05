from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.config import DATABASE_URL

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Alembic 마이그레이션 실행 전에 테이블이 없으면 기본 생성 (초기 실행용)
def init_db():
    from app.models.user import User  # ✅ 필요한 모델 임포트
    Base.metadata.create_all(bind=engine)  # ✅ 테이블 생성