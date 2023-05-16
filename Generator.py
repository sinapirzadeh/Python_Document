def generator():
    for i in range(10):
        yield i**2


x = generator()
while True:
    print(next(x))