from typing import Any, Optional, Dict
from .base import BaseError
from fastapi import status


class RoomError(BaseError):
    status_code = status.HTTP_400_BAD_REQUEST
    detail = "Room Error"


class NotFoundError(RoomError):
    status_code = status.HTTP_404_NOT_FOUND

    def __init__(
        self,
        obj: Any,
        headers: Optional[Dict[str, Any]] = None,
    ) -> None:
        self.detail = f"{obj} is not found"
        super().__init__(status_code=self.status_code,
                         detail=self.detail,
                         headers=headers)


class ExistingError(RoomError):
    status_code = status.HTTP_400_BAD_REQUEST

    def __init__(
        self,
        obj: Any,
        headers: Optional[Dict[str, Any]] = None,
    ) -> None:
        self.detail = f"{obj} is already existing"
        super().__init__(status_code=self.status_code,
                         detail=self.detail,
                         headers=headers)


class UnAuthorizedError(RoomError):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Unauthorized"


class MissingPermissionError(RoomError):
    status_code = status.HTTP_403_FORBIDDEN
    detail = "Permission Denied"


class IdFormatError(RoomError):
    status_code = status.HTTP_406_NOT_ACCEPTABLE
    detail = "Format id not acceptable"