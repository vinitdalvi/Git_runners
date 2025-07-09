# app.py
# This is a test commit
# This is a second commit to have substraction code
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def test_add():
    assert add(1, 2) == 3
    assert add(1, -1) == 0

def test_sub():
    assert sub(5, 2) == 3
    assert sub(3, 1) == 2
