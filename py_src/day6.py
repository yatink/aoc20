import re

test_input = """abc

a
b
c

ab
ac

a
a
a
a

b"""

real_input = """<paste problem input here"""

answers = set()
count = 0
first = True

for entry in real_input.split("\n"):
    if entry == '':
        count += len(answers)
        answers = set()
        first = True
    elif first:
        answers = set(entry)
        first = False
    else:
        answers &= set(entry)
import pdb; pdb.set_trace()
count += len(answers)

print count
