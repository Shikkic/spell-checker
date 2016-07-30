import re, collections, os

class Checker:

  def __init__(self):    
    self.word_count = self.train(self.words(open(os.path.join('data', 'corpus.txt')).read()))
    self.alphabet = 'abcdefghijklmnopqrstuvwxyz'

  def bigrams(self, text):
    l = []
    for i in range(len(text) - 1):
      l.append((text[i], text[i+1]))
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
