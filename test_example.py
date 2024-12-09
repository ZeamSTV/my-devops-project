from example import hello
from example2 import helloTeacher
from example3 import helloABC
def test_hello():
    assert hello() == 'Hello, My Team!'
def helloTeacher():
    assert helloTeacher == 'Hello, Teacher'
def helloABC():
    assert helloABC == 'Hello, Teacher'
