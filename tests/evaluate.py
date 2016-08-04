import time, sys, os
from errors import unigram_one, unigram_two

sys.path.insert(0, os.path.abspath('.'))

from lib.checker import Checker

checker = Checker()


def evaluator(tests):
  n, bad, unknown, start, false_neg = 0, 0, 0, time.clock(), 0
  for target, wrongs in tests.items():
    for wrong in wrongs.split():
      n+= 1
      trys = get_ans(wrong)
      if trys == []:
        false_neg += 1
      if target not in trys:
        bad += 1
        unknown += (target not in checker.word_count)
  return dict(bad=bad, n=n, false_neg=false_neg,pct=int(100. -100.*bad/n), unknown=unknown, secs=int(time.clock() - start))

what = []
def get_ans(word):
  result = checker.check_sentence(word)
  try:
    words = [w[0] for w in result[0]]
    return words
  except IndexError:
    return []


print(evaluator(unigram_one))
#print(evaluator(unigram_two))
