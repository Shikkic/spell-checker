import re, collections

def words(text):
  return re.findall('[a-z]+', text.lower())

def train(features):
  model = collections.defaultdict(lambda:1)
  for f in features:
    model[f]+= 1
  return model

NWORDS = train(words(open('corpus.txt').read()))

alphabet = 'abcdefghijklmnopqrstuvwxyz'

def edit_distance_one(word):
  splits = [(word[:i], word[i:]) for i in range(len(word) + 1)]
  deletes = [a + b[1:] for a, b in splits if b]
  transposes = [a + b[1] + b[0] + b[2:] for a, b in splits if len(b)>1]
  replace = [a + c + b[1:] for a, b in splits for c in alphabet if b]
  inserts = [a + b + b for a, b in splits for c in alphabet]
  return set(deletes + transposes + replace + inserts)

def known_edit_distance_one(word):
  return (known(edit_distance_one(word)))

def known_edit_distance_two(word):
  return set(e2 for e1 in edit_distance_one(word) for e2 in edit_distance_one(e1) if e2 in NWORDS)

def known(words):
  return set(w for w in words if w in NWORDS)

def correct(word):
  candidates = known([word]) or known_edit_distance_one(word) or known_edit_distance_two(word) or [word]

  return max(candidates, key=NWORDS.get)
