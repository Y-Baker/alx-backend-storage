#!/usr/bin/env python3
"""Module Exercise"""
import redis
import uuid
from typing import Union


class Cache:
    def __init__(self) -> None:
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[int, str, float, bytes]) -> str:
        rand = str(uuid.uuid4())
        self._redis.set(rand, data)
        return rand
