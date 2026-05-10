from unittest.mock import patch

from chatbot import process_with_chatbot


def test_chatbot_resolves_call():
    with patch("chatbot.random.random", return_value=0.3):
        result = process_with_chatbot(success_probability=0.6)

    assert result == "resolved"


def test_chatbot_transfers_call_to_operator():
    with patch("chatbot.random.random", return_value=0.9):
        result = process_with_chatbot(success_probability=0.6)

    assert result == "transfer_to_operator"
