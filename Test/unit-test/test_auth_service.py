import pytest
from unittest.mock import MagicMock, patch
from fastapi import HTTPException, status
from app.services.auth import AuthService
# Giả định class User có sẵn từ app.models.user như trong code service
from app.models.user import User


class TestAuthService:

    @pytest.fixture
    def mock_db(self):
        """Fixture để tạo mock session database"""
        return MagicMock()

    @patch("app.services.auth.get_password_hash")
    def test_register_user_success(self, mock_hash, mock_db):
        """Test đăng ký user thành công"""
        # Arrange
        username = "newuser"
        password = "secretpassword"
        hashed = "hashed_secret"

        # Mock không tìm thấy user cũ
        mock_db.query.return_value.filter.return_value.first.return_value = None
        mock_hash.return_value = hashed

        # Act
        new_user = AuthService.register_user(mock_db, username, password)

        # Assert
        assert new_user.username == username
        assert new_user.hashed_password == hashed
        mock_db.add.assert_called_once()
        mock_db.commit.assert_called_once()
        mock_db.refresh.assert_called_once()

    def test_register_user_already_exists(self, mock_db):
        """Test đăng ký user đã tồn tại -> Lỗi 400"""
        # Arrange
        username = "existing"
        existing_user = User(username=username, hashed_password="old_hash")

        # Mock tìm thấy user
        mock_db.query.return_value.filter.return_value.first.return_value = existing_user

        # Act & Assert
        with pytest.raises(HTTPException) as excinfo:
            AuthService.register_user(mock_db, username, "password")

        assert excinfo.value.status_code == status.HTTP_400_BAD_REQUEST
        assert excinfo.value.detail == "Username already registered"
        mock_db.add.assert_not_called()

    @patch("app.services.auth.settings")
    @patch("app.services.auth.create_access_token")
    @patch("app.services.auth.verify_password")
    def test_login_user_success(self, mock_verify, mock_create_token, mock_settings, mock_db):
        """Test login thành công"""
        # Arrange
        username = "user"
        password = "password"
        user = User(username=username, hashed_password="hashed_pw")

        mock_db.query.return_value.filter.return_value.first.return_value = user
        mock_verify.return_value = True
        mock_create_token.return_value = "access_token_abc"
        mock_settings.ACCESS_TOKEN_EXPIRE_MINUTES = 30

        # Act
        result = AuthService.login_user(mock_db, username, password)

        # Assert
        assert result["access_token"] == "access_token_abc"
        assert result["token_type"] == "bearer"

    @patch("app.services.auth.verify_password")
    def test_login_user_wrong_password(self, mock_verify, mock_db):
        """Test login sai pass -> Lỗi 401"""
        # Arrange
        user = User(username="user", hashed_password="hashed_pw")
        mock_db.query.return_value.filter.return_value.first.return_value = user
        mock_verify.return_value = False

        # Act & Assert
        with pytest.raises(HTTPException) as excinfo:
            AuthService.login_user(mock_db, "user", "wrong_pass")

        assert excinfo.value.status_code == status.HTTP_401_UNAUTHORIZED

    @patch("app.services.auth.decode_access_token")
    def test_get_current_user_success(self, mock_decode, mock_db):
        """Test lấy current user từ token thành công"""
        # Arrange
        token = "valid_token"
        username = "user1"
        mock_decode.return_value = {"sub": username}

        user = User(username=username, hashed_password="pw")
        mock_db.query.return_value.filter.return_value.first.return_value = user

        # Act
        result = AuthService.get_current_user(token, mock_db)

        # Assert
        assert result == user

    @patch("app.services.auth.decode_access_token")
    def test_get_current_user_invalid_token(self, mock_decode, mock_db):
        """Test token không hợp lệ -> Lỗi 401"""
        mock_decode.return_value = None

        with pytest.raises(HTTPException) as excinfo:
            AuthService.get_current_user("invalid", mock_db)

        assert excinfo.value.status_code == status.HTTP_401_UNAUTHORIZED
