import traceback
from fastapi import Request, status
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware
from fastapi.exceptions import HTTPException, RequestValidationError


class ExceptionMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        try:
            return await call_next(request)
        except HTTPException as exc:
            return JSONResponse(
                status_code=exc.status_code,
                content={
                    "success": False,
                    "error": {
                        "code": exc.status_code,
                        "message": exc.detail
                    }
                },
                headers=exc.headers
            )
        except RequestValidationError as exc:
            return JSONResponse(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                content={
                    "success": False,
                    "error": {
                        "code": status.HTTP_422_UNPROCESSABLE_ENTITY,
                        "message": "Validation Error",
                        "details": exc.errors()
                    }
                }
            )
        except Exception as exc:
            # Log the error here if needed
            print(f"Unhandled Error: {str(exc)}")
            traceback.print_exc()
            return JSONResponse(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                content={
                    "success": False,
                    "error": {
                        "code": status.HTTP_500_INTERNAL_SERVER_ERROR,
                        "message": "Internal Server Error"
                    }
                }
            )
