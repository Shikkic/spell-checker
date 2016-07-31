import pytest
from ..lib.trainer import Trainer

trainer = Trainer(corpus='corpus_test.txt')

def test_words():
  s = 'Hello World!'
  words = trainer.words(s)
  assert words == ["hello", "world"]

def test_bigram():
  s = "Hello World!, What's up?"
  bigrams = trainer.bigrams(s)
  assert bigrams == [("^", "hello"),("hello", "world"), ("world", "what's"), ("what's", "up"), ("up", "$")]

def test_trigrams():
  s = "The quick brown fox"
  trigrams = trainer.trigrams(s)
  assert trigrams == [("^", "the", "quick"), ("the","quick","brown"), ("quick","brown","fox"), ("brown", "fox", "$")]

def test_train_unigrams():
  l = ['hello', 'world']
  model = trainer.train_model(l)
  assert model['hello'] == 2
  assert model['world'] == 2
  assert model['moon'] == 1
  assert model['hey'] == 1

def test_train_bigrams():
  s = "Hello World!, What's up?"
  l = trainer.bigrams(s)
  model = trainer.train_model(l)
  assert model[("^", "hello")] == 2
  assert model[("april", "moon")] == 1

def test_train_trigrams():
  s = "The quick brown fox"
  l = trainer.trigrams(s)
  model = trainer.train_model(l)
  assert model[("^", "the", "quick")] == 2
  assert model[("a", "b", "c")] == 1

def test_get_prob():
  s = "echo tango golf echo tango"
  l = trainer.bigrams(s)
  model = trainer.train_model(l)
  probs = trainer.get_probs(model)
  assert probs[("echo", "tango")] == (3/11)
