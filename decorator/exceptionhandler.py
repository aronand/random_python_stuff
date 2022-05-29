def exceptionhandler(exc: Exception, raise_exc: Exception = RuntimeError):
    """
    Wraps a try...except block within a decorator. 
    
    By default raises RuntimeError if exception caught.
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except exc:
                raise raise_exc
        return wrapper
    return decorator


@exceptionhandler(ValueError)
def main(val: bool):
    if val: raise ValueError
    print("Got here")


if __name__ == "__main__":
    main(True)
