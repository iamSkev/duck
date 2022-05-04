from __future__ import annotations

import io
from dataclasses import dataclass

__all__ = (
    "_DataDict",
    "CustomException",
    "FileNotUploaded",
    "CouldNotConnect",
    "NotFound",
)


@dataclass
class _DataDict:
    gif_count: int
    gifs: list[str]
    http: list[str]
    image_count: int
    images: list[str]


async def _open_image(data: bytes) -> io.BytesIO:
    """_summary_

    Parameters
    ----------
    data : bytes
        _description_

    Returns
    -------
    io.BytesIO
        _description_
    """
    img = io.BytesIO(data)
    return img


class CustomException(Exception):
    """
    The base exception class for all of the other exceptions.
    """

    def __init__(self, message: str) -> None:
        super().__init__(message)


class FileNotUploaded(CustomException):
    def __init__(self, message: str) -> None:
        super().__init__(message)


class CouldNotConnect(CustomException):
    def __init__(self, status: int) -> None:
        message = f"Could Not Connect to the API. Response status: {status}"
        super().__init__(message)


class NotFound(CustomException):
    def __init__(self) -> None:
        message = "404 not found"
        super().__init__(message)
