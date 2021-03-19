from .base import BaseError
from fastapi import status


class InternalError(BaseError):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR