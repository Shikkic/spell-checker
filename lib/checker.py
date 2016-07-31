import re
from .trainer import Trainer
from pyxdameraulevenshtein import damerau_levenshtein_distance

class Checker:
  def __init__(self, trainer=Trainer):
    trainer = Trainer()
    data = trainer.data
    self.word_count = data['word_count']
    self.unigram_probs = data['unigram_probs']
    self.bigram_probs = data['bigram_probs']
    self.trigram_probs = data['trigram_probs']

  def knowns(self, words):
    return set(w for w in words if w in self.word_count)

  def is_known(self, word):
    return word in self.word_count

  def words(self, text):
    return re.findall('[a-z\']+', text.lower())

  def check_sentence(self, sentence):
    sentence_list = ["^"] + self.words(sentence) + ["$"]
    corrections_list = []
    for i, word in enumerate(sentence_list):
      if self.is_known(word) or word in ["^", "$"]:
        continue
      else:
        before = sentence_list[i-1]
        after = sentence_list[i+1]
        corrections_list.append(self.calculate(word, before, after))
    return corrections_list

  def calculate(self, word, before, after):
    rl = []
    for poss in self.word_count:
      prob = self.prob(word, poss, before, after)
      rl.append((poss, prob))
    rl.sort(key=lambda tup: tup[1])
    rl.reverse()
    return rl[:5]

  def prob(self, word, poss, before, after):
    r = (
      self.unigram_prob(poss) +
      self.bigram_prob((poss, after)) +
      self.bigram_prob((before, poss)) +
      self.trigram_prob((before, poss, after)) +
      self.error_prob(word, poss))
    return r
          
  def unigram_prob(self, word):
    prob = self.unigram_probs[word]
    return prob

  def bigram_prob(self, bigram):
    prob = self.bigram_probs[bigram]
    return prob

  def trigram_prob(self, trigram):
    prob = self.trigram_probs[trigram]
    return prob

  def error_prob(self, error, poss):
    dist = damerau_levenshtein_distance(error, poss)
    prob = (1/(2**dist))
    return prob
  
