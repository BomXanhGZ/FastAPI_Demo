# FastAPI Auth Demo

Project nay gom 2 phan rieng:

```text
backend/   FastAPI API
frontend/  React + Vite UI de test API
```

## 1. Yeu Cau

Can co san:

- Python va virtualenv `venv/` o root project
- Node.js va npm
- Bash hoac PowerShell

Neu chua cai package frontend thi chay `npm install` trong folder `frontend/`.

## 2. Chay Backend

Mo terminal thu nhat tai root project:

```bash
cd backend
```

Dung SQLite in-memory de test nhanh, khong can Postgres:

```bash
export DATABASE_URL="sqlite://"
```

Start FastAPI:

```bash
../venv/Scripts/python.exe -m uvicorn app.main:app --reload
```

Neu chay thanh cong, backend se o:

```text
http://127.0.0.1:8000
```

Swagger UI:

```text
http://127.0.0.1:8000/docs
```

## 3. Chay Frontend

Mo terminal thu hai tai root project:

```bash
cd frontend
```

Cai dependencies neu chua cai:

```bash
npm install
```

Start React dev server:

```bash
npm run dev
```

Frontend se o:

```text
http://127.0.0.1:5173
```

Mo link tren browser de test dang ky, dang nhap va goi `/me`.

## 4. Thu Tu Chay De Test

1. Chay backend truoc o terminal 1.
2. Chay frontend o terminal 2.
3. Mo `http://127.0.0.1:5173`.
4. Nhap username/password.
5. Bam `Dang ky`.
6. Bam `Dang nhap`.
7. Bam `Goi /me` de kiem tra token.

Frontend da cau hinh proxy cac API nay sang backend:

- `POST /register`
- `POST /login`
- `GET /me`
- `/docs`

## 5. Dung Postgres Thay SQLite

Neu muon dung Postgres, set `DATABASE_URL` truoc khi chay backend:

```bash
export DATABASE_URL="postgresql://user:password@host:5432/dbname?sslmode=require"
../venv/Scripts/python.exe -m uvicorn app.main:app --reload
```

Hoac set cac bien rieng:

```bash
export DB_SERVER="your-host"
export DB_PORT="5432"
export DB_NAME="your-db"
export DB_USER="your-user"
export DB_PASSWORD="your-password"
```

## 6. Chay Test Backend

Tai folder `backend/`:

```bash
export DATABASE_URL="sqlite://"
../venv/Scripts/python.exe -m pytest Test/unit-test/
```

## 7. Build

Build backend Docker:

```bash
cd backend
docker build -t fastapi-auth-demo .
```

Build frontend:

```bash
cd frontend
npm run build
```

## 8. Loi Thuong Gap

Neu frontend bao loi khi dang ky/dang nhap:

- Kiem tra backend co dang chay o `http://127.0.0.1:8000` khong.
- Kiem tra terminal backend co loi database khong.
- Neu chi can test nhanh, dung `export DATABASE_URL="sqlite://"` truoc khi start backend.

Neu Bash bao khong tim thay `../venv/Scripts/python.exe`:

- Hay dam bao ban dang o folder `backend/`.
- Kiem tra folder `venv/` co nam o root project khong.

Neu shell cua ban la Git Bash tren Windows, duong dan Python co the dung:

```bash
../venv/Scripts/python.exe -m uvicorn app.main:app --reload
```

Neu shell cua ban la WSL/Linux, thuong se la:

```bash
../venv/bin/python -m uvicorn app.main:app --reload
```
