from __future__ import annotations

import io

__all__ = ("_Cache",)


class _Cache:
    def __init__(self) -> None:
        self._cache: dict[str, list[str | io.BytesIO | bytes]] = {}

    @property
    async def gif_cache(self) -> list[str | io.BytesIO | bytes] | None:
        return self._cache.get("gifs")

    @property
    async def http_cache(self) -> list[str | io.BytesIO | bytes] | None:
        return self._cache.get("https")

    @property
    async def jpg_cache(self) -> list[str | io.BytesIO | bytes] | None:
        return self._cache.get("jpgs")

    @property
    async def get_cache(self) -> dict[str, list[str | io.BytesIO | bytes]]:
        return self._cache
