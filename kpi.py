def calculate_average_waiting_time(waiting_times):
    if not waiting_times:
        return 0
    return sum(waiting_times) / len(waiting_times)


def calculate_operator_load(busy_time, total_time):
    if total_time == 0:
        return 0
    return round((busy_time / total_time) * 100, 2)


def calculate_fcr(resolved_calls, total_calls):
    if total_calls == 0:
        return 0
    return round((resolved_calls / total_calls) * 100, 2)


def calculate_csat(successful_calls, total_calls):
    if total_calls == 0:
        return 0
    return round((successful_calls / total_calls) * 100, 2)
