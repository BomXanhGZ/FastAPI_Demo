# FastAPI + MySQL Demo (Docker DB + Local API)

Chạy MySQL bằng Docker và chạy FastAPI local để dev/debug nhanh.

## Yêu cầu

- Python 3.9+
- Docker + Docker Compose

## Chạy nhanh

1) Chạy MySQL:

```bash
docker compose up -d
# hoặc: docker-compose up -d
```

2) Cài backend:

```bash
python -m venv venv
pip install -r requirements.txt
```

3) Cấu hình `.env` (đã có sẵn trong repo) và chạy API:

```bash
uvicorn app.main:app --reload
```

## URL

- Swagger UI: http://127.0.0.1:8000/docs
- Redoc: http://127.0.0.1:8000/redoc

## Chạy Test

Sử dụng `pytest` để chạy các unit test. Để đảm bảo Python tìm thấy module `app`, hãy chạy bằng lệnh `python -m pytest`:

- Chạy toàn bộ unit test:
  ```bash
  python -m pytest Test/unit-test/
  ```

- Chạy và kiểm tra độ bao phủ của Service:
  ```bash
  python -m pytest --cov=app/services Test/unit-test/
  ```

## Ghi chú

- App tự tạo bảng khi khởi động (xem `app/main.py`).
- Nếu chạy FastAPI trong Docker cùng compose network: đặt `DB_SERVER=db` (tên service trong `docker-compose.yml`).
