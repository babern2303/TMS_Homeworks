import tasks

import pytest

from exceptions import TaskException
from tests.data import TestData


@pytest.mark.parametrize("x, y, res", TestData.task1)
def test_task1(x, y, res):
    assert tasks.task1(x, y) == res


@pytest.mark.parametrize("a, res", TestData.task2)
def test_task2(a, res):
    assert tasks.task2(a) == res


def test_task2_errors():
    with pytest.raises(TaskException):
        tasks.task2(-5)


@pytest.mark.parametrize("a, b, res", TestData.task3)
def test_task3(a, b, res):
    assert tasks.task3(a, b) == res


def test_task3_errors():
    with pytest.raises(TaskException):
        tasks.task3(-5, 0)


@pytest.mark.parametrize("task_name, string, res", TestData.task4_11)
def test_task4_11(task_name, string, res):
    assert getattr(tasks, task_name)(string=string) == res


@pytest.mark.parametrize("string, symbol, res", TestData.task12)
def test_task12(string, symbol, res):
    assert tasks.task12(string=string, symbol=symbol) == res


@pytest.mark.parametrize("number, res", TestData.task13)
def test_task13(number, res):
    assert tasks.task13(number=number) == res


@pytest.mark.parametrize("a, res", TestData.task14)
def test_task14(a, res):
    assert tasks.task14(a) == res


def test_task14_errors():
    with pytest.raises(TaskException):
        tasks.task14(-5)


@pytest.mark.parametrize("a, b, sign, res", TestData.micro_calc)
def test_micro_calc(a, b, sign, res):
    assert tasks.micro_calc(a, b, sign) == res


@pytest.mark.parametrize("a, b, sign", TestData.micro_calc_errors)
def test_micro_calc_errors(a, b, sign):
    with pytest.raises(TaskException):
        tasks.micro_calc(a, b, sign)


@pytest.mark.parametrize("string, res", TestData.perfect_square)
def test_perfect_square(string, res):
    assert tasks.perfect_square(string) is res


@pytest.mark.parametrize("string, res", TestData.big_letters)
def test_big_letters(string, res):
    assert tasks.big_letters(string) == res
