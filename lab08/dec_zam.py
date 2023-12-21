import functools

def limit_calls(max_calls):
    def decorator(func):
        calls = 0
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal calls
            if calls < max_calls:
                calls += 1
                return func(*args, **kwargs)
            else:
                return "Максимальное количество вызовов превышено!"
        return wrapper
    return decorator
    
@limit_calls(4)
def unique_values_closure(*args):
    unique_values = set()
    unique_values.update(args)
    return list(unique_values)
    
print(unique_values_closure(1, 2, 3, 2, 4, 5, 3, 6))
print(unique_values_closure(5, 6, 7, 8, 1, 2, 3, 4))
print(unique_values_closure(9, 1, 2, 3, 4, 5, 6, 3))
print(unique_values_closure(2, 0, 3, 0, 2, 4, 8, 5))
