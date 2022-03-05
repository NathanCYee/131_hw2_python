def doubler(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)

    return wrapper


@doubler
def say_hi():
    print("Hello World!")


say_hi()
