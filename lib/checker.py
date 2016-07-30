import re, collections, os

class Checker:

  def __init__(self):
    corpus = open(os.path.join('data', 'corpus.txt')).read()
    word_list = self.words(corpus)
    bigram_list = self.bigrams(corpus)
    self.word_count = self.train(word_list)
    self.bigram_count = self.train(bigram_list)
    self.alphabet = 'abcdefghijklmnopqrstuvwxyz'

  def bigrams(self, text):
    l = []
    lines = filter(None, re.split('[.?1\n]+', text))
    for line in lines:
      mod_line = ["^"] + self.words(line) + ["$"]
      for i in range(len(mod_line) - 1):
        l.append((mod_line[i], mod_line[i+1]))
    return l

  def trigrams(self, text):
    l = []
    for i in range(len(text) - 2):
      l.append((text[i], text[i+1], text[i+2]))
    return l
      
  def words(self, text):
    return re.findall('[a-z\']+', text.lower())

  def train(self, features):
    model = collections.defaultdict(lambda:1)
    for f in features:
      model[f]+= 1
    return model

  def edit_distance_one(self, word):
    splits = [(word[:i], word[i:]) for i in range(len(word) + 1)]
    deletes = [a + b[1:] for a, b in splits if b]
    transposes = [a + b[1] + b[0] + b[2:] for a, b in splits if len(b)>1]
    replace = [a + c + b[1:] for a, b in splits for c in self.alphabet if b]
    inserts = [a + b + b for a, b in splits for c in self.alphabet]
    return set(deletes + transposes + replace + inserts)

  def known_edit_distance_one(self, word):
    return (self.known(self.edit_distance_one(word)))

  def known_edit_distance_two(self, word):
    return set(e2 for e1 in self.edit_distance_one(word) for e2 in self.edit_distance_one(e1) if e2 in self.word_count)

  def known(self, words):
    return set(w for w in words if w in self.word_count)

  def correct(self, word):
    candidates = self.known([word]) or self.known_edit_distance_one(word) or self.known_edit_distance_two(word) or [word]
    return max(candidates, key=self.word_count.get)
