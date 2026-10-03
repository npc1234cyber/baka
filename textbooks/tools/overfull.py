#!/usr/bin/env python3
"""Map Overfull/Underfull box warnings in a LaTeX log to the source file being read."""
import re, sys
log = open(sys.argv[1], encoding='latin-1').read()
stack = []
out = []
i = 0
tok = re.compile(r'\((\./[^\s()]+\.tex)|\)|(Overfull \\hbox \(([\d.]+)pt too wide\)[^\n]*lines? (\d+)(?:--(\d+))?)|(Overfull \\hbox \(([\d.]+)pt too wide\) detected at line (\d+))')
for m in tok.finditer(log):
    if m.group(1):
        stack.append(m.group(1))
    elif m.group(0) == ')':
        if stack: stack.pop()
    elif m.group(2):
        f = stack[-1] if stack else '?'
        out.append((f, float(m.group(3)), m.group(4)))
    elif m.group(6):
        f = stack[-1] if stack else '?'
        out.append((f, float(m.group(7)), m.group(8)))
thr = float(sys.argv[2]) if len(sys.argv) > 2 else 1.0
for f, w, l in out:
    if w >= thr:
        print(f"{f}:{l}  {w:.1f}pt")
