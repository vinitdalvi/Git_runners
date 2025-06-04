#!/bin/bash
# app.py
# This is a test commit
def add(a, b, c):
    return a + b + c

def test_add():
    assert add(1, 2, 3) == 6
    assert add(1, -1, 2) == 2
    print("all tests passed!")
test_add() #call the test function
