import pytest
from ..lib.checker import Checker

checker = Checker()

def test_knowns():
  assert checker.knowns(['dog','cat','wereafasfasdf']) == {'dog','cat'}

def test_is_known():
  assert checker.is_known('dog') == True

def test_error_prob():
  assert checker.error_prob('chair', 'chaire') == (1/2)
  assert checker.error_prob('chair', 'caire') == (1/4)
  
