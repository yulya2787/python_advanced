import time

def decorator(num_of_repeats=1):
    def time_to_do_function(function):
        def wrapped(*args, **kwargs):
            dic_result = {}
            for i in range(num_of_repeats):
                dic_result[f"result for iteration {i}"] = {}
                start_time = time.time()
                end_time = time.time() - start_time
                func_results = function()
                dic_result[f"result for iteration {i}"]["function name"] = function.__name__
                dic_result[f"result for iteration {i}"]["time of function extcution: "] = end_time
                dic_result[f"result for iteration {i}"]["result of function extcution: "] = func_results
            return dic_result
        return wrapped
    return time_to_do_function

@decorator(5)
def func():
    return 100000+300000

print(func())
