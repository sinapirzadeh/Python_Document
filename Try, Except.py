try:
    x = int(input(" Enter Your Code : "))
    x *= 12
except Exception as ex:
    print(ex.__class__.__name__)
finally:
    print('is don.')