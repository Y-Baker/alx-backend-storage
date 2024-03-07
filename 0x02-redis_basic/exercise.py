#!/usr/bin/env python3
"""Module Exercise"""
import redis
import uuid
from functools import wraps
from typing import Union, Callable, Optional, Any


def count_calls(method: Callable) -> Callable:
    """Decorator that takes a single method and returns a new method"""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Wrapper function"""
        self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """Decorator that takes a single method and returns a new method"""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Wrapper function"""
        self._redis.rpush(f"{method.__qualname__}:inputs", str(args))
        v = method(self, *args, **kwargs)
        self._redis.rpush(f"{method.__qualname__}:outputs", str(v))
        return v
    return wrapper


class Cache:
    def __init__(self) -> None:
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        rand = str(uuid.uuid4())
        self._redis.set(rand, data)
        return rand

    def get(self, key: str, fn: Optional[Callable] = None) -> Any:
        data = self._redis.get(key)
        if fn:
            return fn(data)
        return data

    def get_str(self, key: str) -> str:
        return self.get(key, lambda data: data.decode('utf-8'))

    def get_int(self, key: str) -> int:
        try:
            value = self.get(key, lambda data: int(data.decode('utf-8')))
        except Exception:
            value = 0
        return value
