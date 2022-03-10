def func_counter(func):
    def wrapper(*args, **kwargs):
        wrapper.counter += 1
        return func(*args, **kwargs)

    wrapper.counter: int = 0  # declare variable to persist globally but to be in scope of wrapper namespace
    return wrapper
