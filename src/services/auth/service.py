import hashlib
from datetime import datetime, timedelta
from typing import Any, Dict

import jwt
from src.api.exceptions.auth import UnauthenticatedError
from src.libs.models.users import User


class AuthService:

    def __init__(self, secret_key: str) -> None:
        self._secret_key = secret_key

    def create_access_token(self,
                            data: dict,
                            algorithm: str = "HS256",
                            token_duration: float = 3600):
        to_encode = data.copy()
        expires_delta = timedelta(seconds=token_duration)
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(hours=1)
        to_encode.update({"exp": expire})
        access_token = jwt.encode(
            to_encode, self._secret_key, algorithm=algorithm)
        return access_token

    def hash_password(self, password: str):
        return hashlib.sha256(password.encode("utf-8")).hexdigest()

    def verify_password(self, plain_password: str, hashed_password: str):
        return self.hash_password(plain_password) == hashed_password

    def authenticate_user(self, username: str, password: str):
        user = User.objects(username=username).first()
        if not user:
            return None
        if not self.verify_password(password, user.password):
            return None
        return user
