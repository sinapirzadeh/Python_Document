import functools

def decorator(func):
    @functools.wraps(func)
    def wapper_decorator(*args, **kwargs):
        # Do sumetiong before
        value = func(*args, **kwargs)
        # Do Sumetiong after
        return value
    return wapper_decorator

# Example for Decorator --------

# def decrator123(devaid):
#     def a(x, y):
#         if y == 0:
#             return 'warning!!!'
#         else:
#             return devaid
#     return devaid

# @decrator123
# def devaid(x, y):
#     return x / y

# print(devaid(10,5))
