# BUILD PLAN AND PROGRESS (read this first after any context reset)

## Deliverable
One complete textbook PDF per module (4 books), full spec from user's first message (teach not summarise; 10-point
formula treatment; chapter prerequisites + end-of-chapter review (summary, key definitions, key equations,
connections, common mistakes, exam checklist) + practice questions (basic, conceptual, mathematical, application,
multi-step, exam-style) with full solutions; CORE CONCEPT labels; flag source errors in `sourcenote` boxes;
`external` boxes for knowledge beyond the materials; British English; no lecture-speak; no emoji; prose-first;
front matter: title page, ToC, How to use, Module overview; back matter: FINAL MASTER REVIEW = module summary,
connections, concept map, master formula sheet, glossary (term/definition/plain terms), "What do I actually need
to know?" checklist by chapter (□ Define X ...), final practice + solutions).

## Toolchain (WORKING)
- TeX Live installed via apt (pdflatex). Shared style: /home/user/baka/textbooks/common/textbook.sty
- Each book: /home/user/baka/textbooks/<BookDir>/main.tex + chNN-*.tex ; build with
  `cd <BookDir> && pdflatex -interaction=nonstopmode main.tex` x3 (or latexmk -pdf).
- Final PDFs copied to /home/user/baka/textbooks/pdf/<Name>.pdf ; .gitignore build junk.
- Visual check: pdftoppm -r 70 -f N -l N -png main.pdf /scratch/pg ; then Read the png.
- ALWAYS use absolute paths; `cd` changes the primary working dir notice.

## Style environments (textbook.sty)
definition[Name][label]; theorem/proposition/lemma/corollary/rulebox/principle [Name][label];
example[Title][label] with \solution and \answer{...}; note[Title]; intuition[Title]; warning[Title] (default
"Common mistake"); examtip[Title]; sourcenote[Title] (flags source errors); external[Title]; why[Title];
core[Title] (CORE CONCEPT); prerequisites; keyformula[Name][label]{display} with \fsymbols \fmeaning \forigin
\fuse \fexample \fmistakes \frearrange \fchanges \fexam \fconditions \funits; \src{Notes Def 4.18} tag;
checklist (□ items); \pq[type] questions (numbered Question c.n); \pqsol{c.n}; \glossentry{term}{def}{plain};
\term{...}; chapterintro env; macros \R \N \Z \Q \C \E \Var \Cov \dd \abs \PP.
Colours: accent (redefine per book via \definecolor{accent}{HTML}{..} and accentlight).
Book accents: MTH 1F4E79 (blue), ECN113 0B6E4F (green), ECN115 5B2C83 (purple), NSF 8B1E3F (crimson).

## Order of work and status
1. ECN115 (smallest; validates pipeline)  -- status: DONE (122pp, textbooks/pdf)
2. NSF (MTH4113/4213)                      -- status: pending
3. MTH4500/4600 Prob & Stats              -- status: pending
4. ECN113 Principles of Economics          -- status: pending (core-econ.org still 403-blocked as of 2026-10-02 23:50; retry)
5. QA + commit/push (branch claude/funny-keller-7rpffj) + SendUserFile PDFs

## ECN115 plan (Topic 1 + L2 material; only Lectures 1–2 provided)
Ch1 Language of mathematics (propositions, proofs, axioms, theorems, ⇒, ⇔, negation, quantifiers ∃ ∀, De Morgan)
Ch2 Sets (elements, equality, ∅, Russell remark, ⊆, ∩, ∪, \, set-builder, fruit example, past-paper set Qs)
Ch3 Number systems and real-number axioms (N Z Q R, why R, O1–O2, A1–A5, M1–M6, derived facts, LUB non-exam, intervals)
Ch4 Inequalities (linear via axioms, products sign cases, quadratics via roots/discriminant, D=0/D<0, rational, parameters)
Ch5 Absolute value and triangle inequality
Ch6 Summation notation
Ch7 Mathematical induction
Ch8 Binomial formula
Ch9 Functions and polynomials (factor theorem L2.1)
Ch10 Sequences and limits (ε–N)
Final master review.
Chapter files: ch01-logic.tex ... ch10-limits.tex, review.tex, front.tex
ECN115 progress: (update as chapters complete)
