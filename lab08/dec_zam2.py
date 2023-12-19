import functools

def limit_calls(max_calls, func=None):
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
def unique_values_closure():
    unique_values = set()
    def inner(*args):
        nonlocal unique_values
        unique_values.update(args)
        return list(unique_values)
    return limit_calls(2, inner)
# пример использования
unique_values = unique_values_closure()
print(unique_values(1, 2, 3, 2, 4, 5, 3, 6))
print(unique_values(5, 6, 7, 8, 1, 2, 3, 4))
print(unique_values(9, 1, 2, 3, 4, 5, 6))
