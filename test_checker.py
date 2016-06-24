import pytest
from checker import Checker

checker = Checker()

def test_words():
  s = 'Hello World!'
  words = checker.words(s)
  assert words == ["hello", "world"]

def test_train():
  l = ['hello', 'world']
  model = checker.train(l)
  assert model['hello'] == 2
  assert model['world'] == 2
  assert model['moon'] == 1
  assert model['hey'] == 1

def test_edit_one():
  edits = {'aat', 'act', 'at', 'bat', 'ca', 'caa', 'cab', 'cac', 'cad', 'cae', 'caf', 'cag', 'cah', 'cai', 'caj', 'cak', 'cal', 'cam', 'can', 'cao', 'cap', 'caq', 'car', 'cas', 'cat', 'catat', 'catcat', 'catt', 'cau', 'cav', 'caw', 'cax', 'cay', 'caz', 'cbt', 'cct', 'cdt', 'cet', 'cft', 'cgt', 'cht', 'cit', 'cjt', 'ckt', 'clt', 'cmt', 'cnt', 'cot', 'cpt', 'cqt', 'crt', 'cst', 'ct', 'cta', 'ctt', 'cut', 'cvt', 'cwt', 'cxt', 'cyt', 'czt', 'dat', 'eat', 'fat', 'gat', 'hat', 'iat', 'jat', 'kat', 'lat', 'mat', 'nat', 'oat', 'pat', 'qat', 'rat', 'sat', 'tat', 'uat', 'vat', 'wat', 'xat', 'yat', 'zat'}
  assert checker.edit_distance_one('cat') == edits

def test_known_edit_one():
  assert len(checker.known_edit_distance_one('cat')) == 15
  
def test_known_edit_two():
  assert len(checker.known_edit_distance_two('cat')) == 149

def test_known():
  assert checker.known(['dog','cat','wereafasfasdf']) == {'dog','cat'}

def test_correct_knowns():
  assert checker.correct('chair') == 'chair'

def test_correct_dist_one():
  assert checker.correct('chiar') == 'chair'

def test_correct_dist_two():
  assert checker.correct('chaire') == 'chair'

def test_correct_unknown():
  assert checker.correct('asdfasghaguhapefhsahuapsas') == 'asdfasghaguhapefhsahuapsas'
