import re


def greet(name):

    return f"Hello, {name}!"


def add(a, b):
    return a + b

def validate_email(email):
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(pattern, email) is not None


def get_user_input():
    name = input("Enter your name: ").strip()
    return name


if __name__ == "__main__":
    print(greet("World"))