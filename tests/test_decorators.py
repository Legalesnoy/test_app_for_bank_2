import sys
from time import time

from src.decorators import arguments_func_log, error_func_log, log, log_out, name_func_log, timer_log


def test_log_out(capsys):
    result = log_out("123")
    out, err = capsys.readouterr()
    sys.stdout.write(out)
    sys.stderr.write(err)

    assert out.startswith("123 ")
    assert result is None


def test_timer_log(capsys):
    @timer_log()
    def add_numbers(a, b):
        return a + b

    start = time()
    result = add_numbers(2, 7)
    run_time = time() - start
    expected_result = f"{run_time} sec. "
    out, err = capsys.readouterr()
    sys.stdout.write(out)
    sys.stderr.write(err)

    assert out.startswith(expected_result)
    assert result == 9


def test_name_func_log(capsys):
    @name_func_log()
    def add_numbers(a, b):
        return a + b

    result = add_numbers(2, 7)

    out, err = capsys.readouterr()
    sys.stdout.write(out)
    sys.stderr.write(err)

    assert out.startswith("add_numbers ")
    assert result == 9


def test_arguments_func_log(capsys):
    @arguments_func_log()
    def add_numbers(a, b):
        return a + b

    result = add_numbers(2, 7)
    out, err = capsys.readouterr()
    sys.stdout.write(out)
    sys.stderr.write(err)

    assert out.startswith("Inputs: (2, 7) ")
    assert result == 9


def test_error_func_log(capsys):
    @error_func_log()
    def add_numbers(a, b):
        return a + b

    result = add_numbers(2, 7)
    out, err = capsys.readouterr()
    sys.stdout.write(out)
    sys.stderr.write(err)

    assert out.startswith("add_numbers ok, ")
    assert result == 9


def test_error_f_log(capsys):
    @error_func_log()
    def div_numbers(a, b):
        return a / b

    result = div_numbers(2, 0)
    out, err = capsys.readouterr()
    sys.stdout.write(out)
    sys.stderr.write(err)

    assert out.startswith("div_numbers error:  division by zero. Inputs: (2, 0), ")
    assert result is None


def test_log(capsys):
    @log()
    def add_numbers(a, b):
        return a + b

    start = time()
    result = add_numbers(2, 7)
    run_time = time() - start
    expected_result = f"add_numbers ok, {run_time} sec. \n"

    out, err = capsys.readouterr()
    sys.stdout.write(out)
    sys.stderr.write(err)

    assert out.startswith(expected_result)
    assert result == 9
