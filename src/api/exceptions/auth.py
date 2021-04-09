from typing import Any, Dict, Optional
from .base import BaseError
from fastapi import status


class UnauthenticatedError(BaseError):
    def __init__(self, detail: Optional[Any] = None, headers: Optional[Dict[str, Any]] = None) -> None:
        super().__init__(status_code=status.HTTP_401_UNAUTHORIZED, detail=detail, headers=headers)

class UnauthorizedError(BaseError):
    def __init__(self, detail: Optional[Any] = None, headers: Optional[Dict[str, Any]] = None) -> None:
        super().__init__(status_code=status.HTTP_403_FORBIDDEN, detail=detail, headers=headers)