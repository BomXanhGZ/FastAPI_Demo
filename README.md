# FastAPI Authentication Demo

A modern, high-performance API boilerplate built with **FastAPI**, **SQLAlchemy**, and **PostgreSQL**. This project demonstrates a complete authentication flow including JWT-based security, unit testing, and deployment configurations.

## 🚀 Features

- **FastAPI**: Modern, fast (high-performance), web framework for building APIs.
- **PostgreSQL**: Robust relational database management.
- **SQLAlchemy (ORM)**: Industry-standard Object Relational Mapper.
- **JWT Authentication**: Secure user login and authorization logic.
- **Code Coverage**: Integrated unit tests with coverage reporting.
- **Environment Management**: Separation of configuration and secrets.
- **Cloud Ready**: Configured for deployment on **Render**.

## 📁 Project Structure

```text
├── app/
│   ├── controllers/      # Route handlers (Auth, etc.)
│   ├── core/             # Middlewares & core logic
│   ├── database.py       # DB engine & SessionLocal
│   ├── main.py           # Application entry point
│   ├── models/           # SQLAlchemy database models
│   ├── schemas/          # Pydantic data validation models
│   ├── services/         # Business logic layer
│   └── settings.py       # Configuration & Env management
├── Test/                 # Unit & Integration tests
├── .env                  # Environment secrets (DO NOT COMMIT)
├── Dockerfile            # Container definition
├── render.yaml           # Deployment config for Render
└── requirements.txt      # Python dependencies
```

## 🛠️ Getting Started

### 1. Prerequisites
- Python 3.9+
- PostgreSQL (Local or Docker)

### 2. Installation
Clone the repository and install dependencies:
```bash
# Create virtual environment
python -m venv venv
source venv/Scripts/activate  # On Windows: venv\Scripts\activate

# Install requirements
pip install -r requirements.txt
```

### 3. Configuration
Create a `.env` file from the example (already exists in your repo) and fill in your details:
```ini
DB_SERVER=dpg-xxxx.render.com        # Postgres Host
DB_PORT=5432
DB_NAME=test_db
DB_USER=testuser
DB_PASSWORD=your_password
SECRET_KEY=generate-a-long-random-key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

### 4. Running the Application
```bash
uvicorn app.main:app --reload
```
The API will be available at [http://127.0.0.1:8000](http://127.0.0.1:8000)

## 📖 API Documentation

FastAPI provides interactive documentation out of the box:
- **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **Redoc**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## 🧪 Testing

Run tests using `pytest` to ensure everything works as expected:

- **Run all unit tests**:
  ```bash
  python -m pytest Test/unit-test/
  ```

- **Check coverage**:
  ```bash
  python -m pytest --cov=app/services Test/unit-test/
  ```

## 🚢 Deployment

This project includes a `render.yaml` for one-click deployment to **Render**.
1. Connect your GitHub repository to Render.
2. Render will automatically detect the configuration and deploy your service.
3. Ensure you set the `DATABASE_URL` or individual DB environment variables in the Render Dashboard.

---
Built with ❤️ by [BomXanhG-Z]
