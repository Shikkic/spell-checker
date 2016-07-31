import re, collections, os

class Trainer:
  def __init__(self, corpus='corpus.txt'):
    self.corpus = open(os.path.join('data', corpus)).read()
    self.data = {}
    word_list = self.words(self.corpus)
    bigram_list = self.bigrams(self.corpus)
    trigram_list = self.trigrams(self.corpus)
    word_count = self.train_model(word_list)
    bigram_count = self.train_model(bigram_list)
    trigram_count = self.train_model(trigram_list)
    self.data['word_count'] = word_count
    self.data['bigram_count'] = bigram_count
    self.data['trigram_count'] = trigram_count
    self.data['unigram_probs'] = self.get_probs(word_count)
    self.data['bigram_probs'] = self.get_probs(bigram_count)
    self.data['trigram_probs'] = self.get_probs(trigram_count)

  def get_probs(self, count):
    prob_dict = collections.defaultdict(lambda:1)
    denom = sum(count.values())
    for gram in count:
      prob_dict[gram] = (count[gram]/denom)
    return prob_dict

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
    lines = filter(None, re.split('[.?1\n]+', text))
    for line in lines:
      mod_line = ["^"] + self.words(line) + ["$"]
      for i in range(len(mod_line) - 2):
        l.append((mod_line[i], mod_line[i+1], mod_line[i+2]))
    return l
      
  def words(self, text):
    return re.findall('[a-z\']+', text.lower())

  def train_model(self, features):
    model = collections.defaultdict(lambda:1)
    for f in features:
      model[f]+= 1
    return model

