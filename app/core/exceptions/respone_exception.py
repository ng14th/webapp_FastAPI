# -*- coding: utf-8 -*-
from typing import Any, List


class ErrorResponseException(Exception):
    def __init__(
        self,
        error: str,
        success: bool = False,
        data: List[Any] = [],
        status_code: int = 200,
        error_code: int = 0
    ):
        self.error = error
        self.success = success
        self.data = data
        self.length = len(data) if data else 0
        self.status_code = status_code
        self.error_code = error_code


class ErrorHtmlResponseException(Exception):
    def __init__(
        self,
        error: str
    ):
        self.error = error
