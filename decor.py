

#decorators

    
# def my_decorator(func):
#     def wrap_func(x,y):
#         print("*******")
#         func(x,y)
#         print('******')
#     return wrap_func

# @my_decorator
# def walk(slowly,emoji):
#     print(slowly,emoji)
# walk('slowly','🤣' )


# def my_decorator(func):
#     def wrap_func(*args, **kwargs):
#         #print("*******")
#         func(*args, **kwargs)
#         #print('******')
#     return wrap_func

# @my_decorator
# def walk(slowly,emoji):
#     print(slowly,emoji)
# walk('slowly','🤣' )
from time import time
def performance(fn):
    def wrapper(*args,**kawrgs):
        t1 = time()
        result = fn(*args,**kawrgs)
        t2 = time()
        print(f'took{t2-t1} ms')
        return result
    return wrapper
    

@performance 
def long_time():
    for i in range(10000000):
        i * 5
long_time( )



# @my_decorator
# def hello():
#     print('helllooo')
# @my_decorator
# def bye():
#     print('see ya later')
# hello()
# bye()


