def exceptionhandler(exc: Exception, raise_exc: Exception = RuntimeError):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except exc:
                raise raise_exc
        return wrapper
    return decorator


@exceptionhandler(ValueError, RuntimeError)
def main(val: bool):
    if val: raise ValueError
    print("Got here")


if __name__ == "__main__":
    main(True)
