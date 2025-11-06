#!/usr/bin/env python3

import sys

nmark=0
iqu=0
solution=False

for line in open(sys.argv[1], 'r'):
    if '\\question' in line:
        if iqu >= 1:
            print(f'Question {iqu}: {nmark} marks')
        nmark = 0
        iqu += 1
    elif '\\begin{solution}' in line:
        solution=True
    elif '\\end{solution}' in line:
        solution=False
    elif '\\tmarks' in line and not solution:
        lrep  = line.replace('{', ' ').replace('}', ' ')
        words = lrep.split()
        nmark += int(words[-1])

print(f'Question {iqu}: {nmark} marks')
