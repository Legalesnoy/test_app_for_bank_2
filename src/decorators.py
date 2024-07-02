from functools import wraps
from time import time


def log_out(log_str: str, f_name:str="") -> None:
    if f_name != "":
        with open(f_name, "a") as file:
            file.write(log_str + "\n")
    else:
        print(log_str)


def timer_log(f_name: str=""):
    def wrapper1(func):
        @wraps(func)
        def wrapper2(*args, **kwargs):
            start = time()
            result = func(*args, **kwargs)
            run_time = time() - start
            log_str = f"Время затраченное на выполнение функции {func.__name__}: {run_time} секунд"
            log_out(log_str, f_name)
            return result

        return wrapper2

    return wrapper1


def name_func_log(f_name=""):
    def wrapper1(func):
        @wraps(func)
        def wrapper2(*args, **kwargs):
            result = func(*args, **kwargs)
            log_str = f"Имя фунции: {func.__name__}"
            log_out(log_str, f_name)
            return result

        return wrapper2

    return wrapper1


def arguments_func_log(f_name=""):
    def wrapper1(func):
        @wraps(func)
        def wrapper2(*args, **kwargs):
            result = func(*args, **kwargs)
            log_str = f"Аргументы фунции: {*args, *kwargs}"
            log_out(log_str, f_name)
            return result

        return wrapper2

    return wrapper1


def error_func_log(f_name=""):
    def wrapper1(func):
        @wraps(func)
        def wrapper2(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
            except Exception as e:
                log_str = f"Ошибка в функции {func.__name__}, {e} "
            else:
                log_str = f"Функция {func.__name__} выполнена без ошибок"

            log_out(log_str, f_name)
            return result

        return wrapper2

    return wrapper1


def log(f_name=""):
    """
    Декоратор записывает
    время вызова, имя функции, передаваемые аргументы
    результат выполнения и информацию об ошибках функции и ее
    в файл или в консоль (по умолчанию)
    """

    def wrapper1(func):

        @wraps(func)
        def wrapper(*args, **kwargs):
            d1 = timer_log(f_name)
            d2 = arguments_func_log(f_name)
            d3 = error_func_log(f_name)
            d4 = name_func_log(f_name)
            result = d1(d2(d3(d4(func))))(*args, **kwargs)

            return result

        return wrapper

    return wrapper1


## проверочки:
# @log('1.txt')
# def div (a,b):
#     '''dididididi'''
#     return a/b
# # g0 = print
# # g1 = sleep
# # g2 = timer_log(g0)
# # g3 = arguments_func_log(g0)
# # g4 = error_func_log(g0)
# #
# # g2(2)
# hhh = {'k':9,7:0}
# lst=[9,8,9]
# # g3(f"{hhh}боьлдо{lst}")
# div(3,hhh[7])
# # print(f'{div(3,5)}')
# # print(help(log))
