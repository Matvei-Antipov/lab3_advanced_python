from typing import Callable, Any

def cache(func: Callable[..., Any]) -> Callable[..., Any]:

    cache = {}

    def wrapper(*args: Any, **kwargs: Any) -> Any:

        cache_key = (args, tuple(sorted(kwargs.items())))

        if cache_key in cache:
            return cache[cache_key]

        result = func(*args, **kwargs)
        cache[cache_key] = result
        
        return result
      
    return wrapper