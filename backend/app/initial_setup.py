import os
import time
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.database import Base, engine, SessionLocal
from app.models.user import User  # 예제 모델
from app.config import DATABASE_URL

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:password@postgres/dbname")

def wait_for_db():
    """PostgreSQL이 실행될 때까지 대기"""
    retries = 5
    while retries > 0:
        try:
            engine.connect()
            print("✅ Database is ready!")
            return
        except Exception as e:
            print(f"⏳ Waiting for database... {retries} retries left.")
            time.sleep(5)
            retries -= 1
    raise Exception("🚨 Database connection failed!")

def create_tables():
    """테이블이 없으면 생성"""
    Base.metadata.create_all(bind=engine)
    print("✅ Tables created!")

def seed_data():
    """초기 데이터 삽입"""
    db = SessionLocal()
    if not db.query(User).first():  # 유저 테이블에 데이터가 없으면 기본 데이터 추가
        admin = User(username="admin", email="admin@test.com", hashed_password="hashed_admin_pw")
        db.add(admin)
        db.commit()
        print("✅ Initial admin user created!")
    db.close()

if __name__ == "__main__":
    wait_for_db()
    create_tables()
    seed_data()
