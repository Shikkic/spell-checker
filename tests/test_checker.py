import pytest
from ..lib.checker import Checker

checker = Checker()
checker.train()

def test_words():
  s = 'Hello World!'
  words = checker.words(s)
  assert words == ["hello", "world"]

def test_bigram():
  s = "Hello World!, What's up?"
  bigrams = checker.bigrams(s)
  assert bigrams == [("^", "hello"),("hello", "world"), ("world", "what's"), ("what's", "up"), ("up", "$")]

def test_trigrams():
  s = "The quick brown fox"
  trigrams = checker.trigrams(s)
  assert trigrams == [("^", "the", "quick"), ("the","quick","brown"), ("quick","brown","fox"), ("brown", "fox", "$")]

def test_train_model():
  l = ['hello', 'world']
  model = checker.train_model(l)
  assert model['hello'] == 2
  assert model['world'] == 2
  assert model['moon'] == 1
  assert model['hey'] == 1

def test_train_bigrams():
  s = "Hello World!, What's up?"
  l = checker.bigrams(s)
  model = checker.train_model(l)
  assert model[("^", "hello")] == 2
  assert model[("april", "moon")] == 1

def test_train_trigrams():
  s = "The quick brown fox"
  l = checker.trigrams(s)
  model = checker.train_model(l)
  assert model[("^", "the", "quick")] == 2
  assert model[("a", "b", "c")] == 1

def test_edit_one():
  edits = {'aat', 'act', 'at', 'bat', 'ca', 'caa', 'cab', 'cac', 'cad', 'cae', 'caf', 'cag', 'cah', 'cai', 'caj', 'cak', 'cal', 'cam', 'can', 'cao', 'cap', 'caq', 'car', 'cas', 'cat', 'catat', 'catcat', 'catt', 'cau', 'cav', 'caw', 'cax', 'cay', 'caz', 'cbt', 'cct', 'cdt', 'cet', 'cft', 'cgt', 'cht', 'cit', 'cjt', 'ckt', 'clt', 'cmt', 'cnt', 'cot', 'cpt', 'cqt', 'crt', 'cst', 'ct', 'cta', 'ctt', 'cut', 'cvt', 'cwt', 'cxt', 'cyt', 'czt', 'dat', 'eat', 'fat', 'gat', 'hat', 'iat', 'jat', 'kat', 'lat', 'mat', 'nat', 'oat', 'pat', 'qat', 'rat', 'sat', 'tat', 'uat', 'vat', 'wat', 'xat', 'yat', 'zat'}
  assert checker.edit_distance_one('cat') == edits

def test_known_edit_one():
  assert len(checker.known_edit_distance_one('cat')) == 25
  
def test_known_edit_two():
  assert len(checker.known_edit_distance_two('cat')) == 236

def test_knowns():
  assert checker.knowns(['dog','cat','wereafasfasdf']) == {'dog','cat'}

def test_is_known():
  assert checker.is_known('dog') == True

def test_correct_knowns():
  assert checker.correct('chair') == 'chair'

def test_correct_dist_one():
  assert checker.correct('chiar') == 'chair'

def test_correct_dist_two():
  assert checker.correct('chaire') == 'chair'

def test_correct_unknown():
  assert checker.correct('asdfasghaguhapefhsahuapsas') == 'asdfasghaguhapefhsahuapsas'

def test_unigram_prob():
  wds = checker.words("echo bravo fox echo golf")
  checker.word_count = checker.train_model(wds)
  assert checker.unigram_prob('echo') == (3/9)
  
