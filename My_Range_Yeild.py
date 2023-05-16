# is not fast
def my_range(start, end, step=1):
    list = []
    while start < end:
        list.append(start)
        start += step
    return list

# is very fast
def my_range_generator(start, end, step=1):
    while start < end:
        yield start
        start += step



for i in my_range(1, 12, 3):
    print(i)


for i in my_range_generator(1, 12, 3):
    print(i)