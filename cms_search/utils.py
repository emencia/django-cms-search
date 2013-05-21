import functools


def memoize(hasher=lambda *args, **kwargs: 0):
    def decorator_fn(old_fn):
        cache = {}

        @functools.wraps(old_fn)
        def new_fn(*args, **kwargs):
            key = hasher(*args, **kwargs)

            if key not in cache:
                cache[key] = old_fn(*args, **kwargs)

            return cache[key]

        return new_fn

    return decorator_fn
