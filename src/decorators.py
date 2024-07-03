from functools import wraps
from time import time


def log_out(log_str: str, f_name: str = "", sep: str = " ") -> None:

    if f_name != "":
        with open(f_name, "a") as file:
            file.write(log_str + sep)
    else:
        print(log_str, end=sep)


def timer_log(f_name: str = ""):
    def wrapper1(func):
        @wraps(func)
        def wrapper2(*args, **kwargs):

            start = time()
            result = func(*args, **kwargs)
            run_time = time() - start
            log_str = f"{run_time} sec."
            log_out(log_str, f_name)
            return result

        return wrapper2

    return wrapper1


def name_func_log(f_name=""):
    def wrapper1(func):
        @wraps(func)
        def wrapper2(*args, **kwargs):

            result = func(*args, **kwargs)
            log_str = f"{func.__name__}"
            log_out(log_str, f_name)
            return result

        return wrapper2

    return wrapper1


def arguments_func_log(f_name=""):
    def wrapper1(func):
        @wraps(func)
        def wrapper2(*args, **kwargs):

            result = func(*args, **kwargs)
            log_str = f"Inputs: {*args, *kwargs}"

            log_out(log_str, f_name)
            return result

        return wrapper2

    return wrapper1


def error_func_log(f_name=""):
    def wrapper1(func):
        @wraps(func)
        def wrapper2(*args, **kwargs):

            result = None
            try:
                result = func(*args, **kwargs)
            except Exception as e:
                log_str = f"{func.__name__} error:  {e}. Inputs: {*args, *kwargs}"
            else:
                log_str = f"{func.__name__} ok"

            log_out(log_str, f_name, ", ")
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
            d2 = error_func_log(f_name)
            result = d1(d2(func))(*args, **kwargs)
            log_out("", f_name, "\n")

            return result

        return wrapper

    return wrapper1


#
# if __name__ == '__main__':
#     # проверочки:
#     @log('log.txt')
#     def div (a,b):
#         '''dididididi'''
#         return a/b
#     # g0 = print
#     # g1 = sleep
#     # g2 = timer_log(g0)
#     # g3 = arguments_func_log(g0)
#     # g4 = error_func_log(g0)
#     #
#     # g2(2)
#     hhh = {'k':9,7:0}
#     lst=[9,8,9]
#     # g3(f"{hhh}боьлдо{lst}")
#     div(3,1)
#     # print(f'{div(3,5)}')
#     # print(help(log))
#
#
#
# if __name__ == '__main__':
#     import pytest
#     def test_log_out(capsys):
#
#         result = log_out('123')
#         out, err = capsys.readouterr()
#         sys.stdout.write(out)
#         sys.stderr.write(err)
#
#         assert out.startswith('123 ')
#         assert result == None
#
#     def test_log(capsys):
#
#         @log()
#         def add_numbers(a,b):
#             return a + b
#         result = add_numbers(2,7)
#         out, err = capsys.readouterr()
#         sys.stdout.write(out)
#         sys.stderr.write(err)
#
#         assert out.startswith('add_numbers ok, 0.0 sec. \n')
#         assert result == 9
#
#
#
#
#
#
#
