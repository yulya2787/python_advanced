from threading import Thread
import time


def decorator(num_of_repeats):

    def my_decorator(custom_func):
        def wrapper(*args):
            threads = []
            for i in range(1, num_of_repeats + 1):
                thread = Thread(target=custom_func, args=args, name=f'{args[0]}_{i}')
                if False in args:
                    thread.start()
                    print(f'\nthread {thread.name} started')
                else:
                    thread.daemon
                    print(f'thread {thread.name} started as daemon')
                while thread.is_alive():
                    print(f'thread {thread.name} is still running')
                    time.sleep(1)
                else:
                    print(f'thread {thread.name} has been finished')
                    threads.append(thread)
            return threads
        return wrapper
    return my_decorator


@decorator(4)
def func(name, is_daemon: bool=False):
    print(f'name = {name} would run as {"daemon" if is_daemon is True else "thread"}')


print(func('new_one', False))