from example import hello
from example2 import helloTeacher
def test_hello():
    assert hello() == 'Hello, My Team!'
def helloTeacher():
    assert helloTeacher == 'Hello, Teacher'