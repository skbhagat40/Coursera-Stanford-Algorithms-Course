# using named tupels
from collections import namedtuple
Results = namedtuple('Results', ['passed', 'failed'])
r = Results(0,4)
print(r.passed)
print(r.failed)
print(r[0])
print(r[1])
