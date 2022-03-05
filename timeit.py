import time


def calculate_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        output = func(*args, **kwargs)
        end_time = time.time()
        print(f"Total time {end_time - start_time}")
        return output

    return wrapper


@calculate_time
def test():
    time.sleep(5)


test()