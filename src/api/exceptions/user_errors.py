from typing import Any, Optional, Dict
from .base import BaseError
from fastapi import status


class UserError(BaseError):
    status_code = status.HTTP_400_BAD_REQUEST
    detail = "User Error"


class NotFoundError(UserError):
    status_code = status.HTTP_404_NOT_FOUND

    def __init__(
        self,
        obj: Any,
        headers: Optional[Dict[str, Any]] = None,
    ) -> None:
        self.detail = f"{obj} is not found"
        super().__init__(
            status_code=self.status_code, detail=self.detail, headers=headers
        )


class ExistingError(UserError):
    status_code = status.HTTP_400_BAD_REQUEST

    def __init__(
        self,
        obj: Any,
        headers: Optional[Dict[str, Any]] = None,
    ) -> None:
        self.detail = f"{obj} is already existing"
        super().__init__(
            status_code=self.status_code, detail=self.detail, headers=headers
        )


class UnAuthorizedError(UserError):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Unauthorized"


class MissingPermissionError(UserError):
    status_code = status.HTTP_403_FORBIDDEN
    detail = "Permission Denied"