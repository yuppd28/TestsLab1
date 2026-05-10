import random


class Operator:
    def __init__(self, name):
        self.name = name
        self.processed_calls = 0
        self.busy_time = 0

    def process(self, service_time):
        self.processed_calls += 1
        self.busy_time += service_time
        return service_time


def generate_call_time(call_rate):
    return random.expovariate(call_rate)


def generate_service_time(min_time=3, max_time=10):
    return random.randint(min_time, max_time)


def process_call(operator):
    service_time = generate_service_time()
    return operator.process(service_time)


def run_simulation(operators_count, calls_count):
    operators = [Operator(f"Operator {i + 1}") for i in range(operators_count)]

    processed_calls = 0
    waiting_times = []

    for i in range(calls_count):
        operator = operators[i % operators_count]
        waiting_time = generate_call_time(0.5)
        waiting_times.append(waiting_time)

        process_call(operator)
        processed_calls += 1

    return {
        "processed_calls": processed_calls,
        "waiting_times": waiting_times,
        "operators": operators
    }
