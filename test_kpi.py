from kpi import (
    calculate_average_waiting_time,
    calculate_operator_load,
    calculate_fcr,
    calculate_csat
)


def test_calculate_average_waiting_time():
    result = calculate_average_waiting_time([2, 4, 6, 8])
    assert result == 5


def test_calculate_average_waiting_time_empty_list():
    result = calculate_average_waiting_time([])
    assert result == 0


def test_calculate_operator_load():
    result = calculate_operator_load(360, 480)
    assert result == 75


def test_calculate_operator_load_zero_time():
    result = calculate_operator_load(100, 0)
    assert result == 0


def test_calculate_fcr():
    result = calculate_fcr(80, 100)
    assert result == 80


def test_calculate_csat():
    result = calculate_csat(90, 100)
    assert result == 90
