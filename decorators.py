from typing import Any, Callable
from functools import wraps
import time


def audit_log(func: Callable[..., Any]) -> Callable[..., Any]:
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        # pre log
        print(
            f"[audit_log]function invoked: {func.__name__} with args: {args} kwargs: {kwargs}"
        )
        # execute the function
        start: float = time.perf_counter()

        try:
            result: Any = func(*args, **kwargs)
            end: float = time.perf_counter()
            # post log
            print(f"[audit_log]function completed: {func.__name__} returning: {result}")
            duration: float = end - start
            print(
                f"[audit_log]function '{func.__name__}' executed in {duration:.4f} seconds"
            )
            return result
        except Exception as e:
            end: float = time.perf_counter()
            duration: float = end - start
            print(
                f"[audit_log]function '{func.__name__}' failed after {duration:.4f} seconds with error: {e}"
            )
            raise e

    return wrapper
