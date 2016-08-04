import time, sys, os
from errors import unigram_one, unigram_two

sys.path.insert(0, os.path.abspath('.'))

from lib.checker import Checker

checker = Checker()


def evaluator(tests, bias=None):
  n, bad, unknown, start = 0, 0, 0, time.clock()
  if bias:
    for target in tests: checker.word_count[target] += bias
  for target, wrongs in tests.items():
    for wrong in wrongs.split():
      n+= 1
      trys = get_ans(wrong)
      if target not in trys:
        bad += 1
        unknown += (target not in checker.word_count)
  return dict(bad=bad, n=n, bias=bias, pct=int(100. -100.*bad/n), unknown=unknown, secs=int(time.clock() - start))

what = []
def get_ans(word):
  result = checker.check_sentence(word)
  try:
    words = [w[0] for w in result[0]]
    return words
  except IndexError:
    what.append(word)
    return []


print(evaluator(unigram_one))
print(what)
#print(evaluator(unigram_two))
