def func (*args, **kwargs):
    sum = 0
    for i in args:
        sum += i


    for key, value in kwargs.items():
        print(f"{key}: {value}")
    return sum, kwargs

print(func(1,2,3,4,5, a=1, b=2, c=3, d=4, e=5))