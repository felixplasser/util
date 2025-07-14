#!/usr/bin/env python3
"""
Remove a tag from a latex file.
"""

print("""
rm_tex-tag.py <file> <tag>
""")

import sys

fname = sys.argv[1]
tag   = sys.argv[2]

ttag = '\\%s'%tag
print("Removing %s from file %s ...\n"%(ttag, fname))

outf = open('%s_%s'%(tag, fname), 'w')

f = open(fname, 'r')

while True:
    try:
        line = next(f)
    except StopIteration:
        break
    if ttag in line and not 'newcommand' in line:
        indt = line.index(ttag)
        outf.write(line[:indt])
        line = line[indt + len(ttag) + 1:]

        nopen  = 1 # Number of open curly brackets
        tofind = True # Becomes False if we found the closing }
        while nopen > 0: # Loop until all curly brackets are closed
            outline = ''
            for lett in line:
                if lett == '{' and tofind:
                    nopen += 1
                    outline += lett
                elif lett == '}' and tofind:
                    nopen -= 1
                    if nopen > 0:
                        outline += lett
                    else:
                        tofind = False
                else:
                    outline += lett
            outf.write(outline)
            if nopen > 0 and tofind:
                line = next(f)

    else:
        outf.write(line)
outf.close()
