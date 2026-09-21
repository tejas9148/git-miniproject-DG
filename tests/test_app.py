from app import greet, add, validate_email


def test_greet():
    assert greet("tejas") == "Hello, Tejas!"


def test_add():
    assert add(2, 3) == 5


def test_valid_email():
    assert validate_email("test@example.com") is True


def test_invalid_email():
    assert validate_email("invalid-email") is False