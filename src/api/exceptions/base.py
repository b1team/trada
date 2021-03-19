from fastapi import HTTPException, status
from typing import Any, Optional, Dict


class BaseError(HTTPException):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    detail = "Internal Error"
    headers = {}

    def __init__(
        self,
        status_code: Optional[int] = None,
        detail: Optional[Any] = None,
        headers: Optional[Dict[str, Any]] = None,
    ) -> None:
        if not status_code:
            status_code = self.status_code
        if not detail:
            detail = self.detail
        self.detail = detail
        if not headers:
            headers = self.headers
        super().__init__(status_code, detail=detail, headers=headers)

    def __str__(self) -> str:
        return self.detail