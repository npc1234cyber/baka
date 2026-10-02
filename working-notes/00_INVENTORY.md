# SOURCE INVENTORY (user: 4 modules; 8 PDFs total, 5 received so far; user wants: read all 5, WAIT for next 3, then one book per module)
Source files copied to scratchpad/src/partN.pdf; text split into section files (tr -s squeezed, pdftotext -layout):
- part1 p1-36   -> mth_sg_w8_12.txt  : MTH4500/4600 Applied Prob & Stats Weeks 8-12 exam-focused study guide (AI-made revision aid; built from lecture notes Ch5,6,8,9,10,11 + user's revision sheet; lists 6 errors in revision sheet)
- part1 p37-75  -> ecn113_rg.txt     : ECN113 Principles of Economics revision guide weeks 1-12 (QMUL SEF) incl. past-paper map, textbook ref index
- part1 p76-100 + part2 p1-4 -> ecn115_sg_a/b.txt : ECN115 Mathematical Methods Topic 1 Lecture 1 study guide
- part2 p5-100 + part3 p1-59 -> ecn115_slides_a/b.txt : ECN115 lecture slides (module info, Topic 1 L1: logic, sets, numbers, inequalities, summation, induction; L2: induction, abs value, triangle ineq, binomial formula, functions, polynomials, quantifiers, sequences, limits)
- part3 p60-100, part4 p1-100, part5 p1-72 -> mth_notes_a/b/c.txt : MTH4500/4600 full lecture notes 2023/24 (Del Baño Rollin, Blitvić, Moriarty, Shaheen) Ch0-20 + Errata (Appendix A)
- part5 p73-100 -> mth_examsg_a.txt : MTH4500/4600 "Exam-focused study guide" (pages 1-26 of it, continues into part6?)
Notes on each module in notes/MTH.md, notes/ECN113.md, notes/ECN115.md

## STATUS after reading the first 5 PDFs (all read fully; notes in notes/*.md)
- 4 modules per user: MTH4500/4600 Applied Prob & Stats; ECN113 Principles of Economics; ECN115 Mathematical Methods; + 4th module (unknown, presumably in parts 6–8).
- Hyperlink scan (pymupdf): part2 has Russell's paradox wiki link (ECN115 slides); part4 has wiki/website links in MTH notes Ch11–13 (German tank, Simpson, YouGov, etc.). NO economics textbook hyperlinks in parts 1–5 → the ECN113 lecture notes with textbook hyperlinks must be in parts 6–8.
- Part 5 ends mid-way through MTH "Exam-focused study guide (Semesters A & B)" (its pp.1–26 of ~40) → continues in part 6.
- Tools: pdftotext, python3 + pymupdf, pypdf, matplotlib installed via pip. No LaTeX/pandoc found (pdflatex missing). Chromium available at /opt/pw-browsers (Playwright) → option: HTML+KaTeX → print to PDF. Or try installing TeX later.
- NEXT: wait for user's remaining 3 PDFs (user explicitly said: read all, then let them send next 3 before carrying on). Then build one textbook per module.
