import time
from test_errors import unigram_one, unigram_two
from checker import Checker

checker = Checker()


def evaluator(tests, bias=None):
  n, bad, unknown, start = 0, 0, 0, time.clock()
  if bias:
    for target in tests: checker.NWORDS[target] += bias
  for target, wrongs in tests.items():
    for wrong in wrongs.split():
      n+= 1
      w = checker.correct(wrong)
      if w != target:
        bad += 1
        unknown += (target not in checker.NWORDS)
  return dict(bad=bad, n=n, bias=bias, pct=int(100. -100.*bad/n), unknown=unknown, secs=int(time.clock() - start))

print(evaluator(unigram_one))
print(evaluator(unigram_two))
