#!/usr/bin/env python3
"""redis module"""

import redis
import requests
from functools import wraps
from typing import Union, Callable, Optional

_redis = redis.Redis()


def count_url(method: Callable) -> Callable:
    """Decorator count the url in last 10 min"""

    @wraps(method)
    def wrapper(url):
        """Wrapper for Decorator"""
        name = f"count:{url}"
        _redis.incr(name)
        cached_html = _redis.get(f"cached:{url}")
        if cached_html:
            return cached_html.decode('utf-8')
        html = method(url)
        _redis.setex(f"cached:{url}", 10, html)
        return html

    return wrapper

@count_url
def get_page(url: str) -> str:
    """obtain the HTML content of a particular URL and returns it"""

    res = requests.get(url)
    return res.text
