import pytest
from ..lib.checker import Checker
from ..lib.trainer import Trainer

#trainer = Trainer(corpus='corpus_test.txt')
checker = Checker()

def test_knowns():
  assert checker.knowns(['dog','fox','wereafasfasdf']) == {'dog','fox'}

def test_is_known():
  assert checker.is_known('dog') == True

def test_error_prob():
  assert checker.error_prob('chair', 'chaire') == (1/2)
  assert checker.error_prob('chair', 'caire') == (1/4)
  
def test_check_sentence():
  results = checker.check_sentence('thh')
  words = [w[0] for w in results[0]]
  assert 'the' in words
