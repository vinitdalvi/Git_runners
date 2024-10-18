# app.py
# This is a test commit to test github actions
def add(a, b):
    return a + b

def test_add():
    assert add(1, 4) == 5
    assert add(1, -1) == 0
