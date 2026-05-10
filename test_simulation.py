from unittest.mock import Mock, patch

from simulation import (
    Operator,
    generate_call_time,
    generate_service_time,
    process_call,
    run_simulation
)


def test_generate_call_time_with_mock():
    with patch("simulation.random.expovariate", return_value=2.5):
        result = generate_call_time(0.5)

    assert result == 2.5


def test_generate_service_time_with_mock():
    with patch("simulation.random.randint", return_value=5):
        result = generate_service_time()

    assert result == 5


def test_process_call_with_mock_operator():
    operator = Mock()
    operator.process.return_value = 7

    result = process_call(operator)

    operator.process.assert_called_once()
    assert result == 7


def test_operator_process_call():
    operator = Operator("Operator 1")

    result = operator.process(6)

    assert result == 6
    assert operator.processed_calls == 1
    assert operator.busy_time == 6


def test_run_simulation_with_mocked_random_values():
    with patch("simulation.generate_call_time", return_value=1), \
         patch("simulation.generate_service_time", return_value=4):

        result = run_simulation(operators_count=2, calls_count=5)

    assert result["processed_calls"] == 5
    assert len(result["waiting_times"]) == 5
    assert len(result["operators"]) == 2
