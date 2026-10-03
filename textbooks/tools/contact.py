#!/usr/bin/env python3
"""Render a range of PDF pages as a contact sheet PNG: contact.py file.pdf first last out.png [cols] [zoom]"""
import sys, pymupdf
from PIL import Image
pdf, a, b, out = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]
cols = int(sys.argv[5]) if len(sys.argv) > 5 else 4
zoom = float(sys.argv[6]) if len(sys.argv) > 6 else 0.45
doc = pymupdf.open(pdf)
ims = []
for p in range(a-1, min(b, len(doc))):
    pix = doc[p].get_pixmap(matrix=pymupdf.Matrix(zoom, zoom))
    ims.append(Image.frombytes("RGB", [pix.width, pix.height], pix.samples))
w, h = ims[0].size
rows = (len(ims)+cols-1)//cols
sheet = Image.new("RGB", (cols*w + (cols-1)*6, rows*h + (rows-1)*6), "white")
for i, im in enumerate(ims):
    sheet.paste(im, ((i % cols)*(w+6), (i//cols)*(h+6)))
sheet.save(out)
print(out, sheet.size)
