import time

def time_to_do_function(function):
    def wrapped(*args):
        start_time = time.process_time()
        resalt = function(*args)
        print(time.process_time() - start_time)
        return resalt
    return wrapped


n = input("введите число повторений выполнения функции - ")
for i in n:
    @time_to_do_function
    def func(first, second):
        return bin(int(first, 2) + int(second, 2))

    print(func("1", "0"))