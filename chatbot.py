import random


def process_with_chatbot(success_probability=0.6):
    value = random.random()

    if value <= success_probability:
        return "resolved"

    return "transfer_to_operator"
