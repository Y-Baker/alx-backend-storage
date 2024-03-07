#!/usr/bin/env python3
"""Module Exercise"""
import redis
import uuid
from functools import wraps
from typing import Union

def count_calls(method: callable) -> callable:
    """Decorator that takes a single method and returns a new method"""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Wrapper function"""
        self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)
    return wrapper


class Cache:
    def __init__(self) -> None:
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        rand = str(uuid.uuid4())
        self._redis.set(rand, data)
        return rand

    def get(self, key: str, fn: callable = None) -> Union[str, bytes, int, float]:
        data = self._redis.get(key)
        if fn:
            return fn(data)
        return data

    def get_str(self, key: str) -> str:
        return self.get(key, lambda data: data.decode('utf-8'))

    def get_int(self, key: str) -> int:
        return int(key)

    def incr(self, key: str) -> int:
        return self._redis.incry(key)