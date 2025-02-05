FROM python:3.9
WORKDIR /app
COPY . /app

# ✅ alembic.ini를 /app 루트에 복사 (Alembic 실행 시 필요)
COPY alembic.ini /app/alembic.ini
COPY alembic /app/alembic



RUN pip install --no-cache-dir -r requirements.txt

# Alembic 실행을 위해 PATH 설정
ENV PATH="/app/.local/bin:$PATH"

CMD ["sh", "-c", "alembic upgrade head && uvicorn app.main:app --host 0.0.0.0 --port 8000"]