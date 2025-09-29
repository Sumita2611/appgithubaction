# import add,sub
from src.math_operations import add,sub

def test_add():
  assert add(2,3)==5
  assert add(4,2)==6

def test_sub():
  assert sub(5,3)==2
  assert sub(7,2)==5
  assert sub(1,2)==-1