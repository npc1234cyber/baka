# MTH4500/MTH4600 (Applied) Probability and Statistics — NOTES
Primary source: lecture notes 2023/24, S. Del Baño Rollin, N. Blitvić, J. Moriarty, L. Shaheen (QMUL School of Mathematical Sciences).
"These notes define the examinable content — everything here examinable unless explicitly stated otherwise." Each chapter = one week.
Starred exercises (*) for high grade; ** beyond syllabus. Books: Ross "A First Course in Probability" [Ros20] (closest), Anderson-Seppäläinen-Valkó [ASV18], Tijms [Tij12] (Ch 7-9).
Part I Semester A: Ch0-12 ; Part II Semester B: Ch13-20 (13 Intro Stats & R, 14 EDA, 15 Sampling distributions, 16 CIs, 17 Hypothesis tests, 18 Conditional prob, 19 Total prob & Bayes, 20 Conditional expectation). Appendix A Errata.
NOTE: lecture-note numbering: Ch4 uses conditional prob Def 4.1 early; refs "Definition 18.1", "Theorem 18.2" (mult rule), "Example 18.4" (die info) => Ch18 originally earlier (notes were reordered). Textbook should teach conditional probability BEFORE independence (pedagogical reorder).
Text source lines: mth_notes_a.txt (Ch0-4 start), mth_notes_b.txt (Ch4.1-13.5), mth_notes_c.txt (Ch14-20, errata)

## Ch0 Prologue
- Ex0.1 birthday matching; frequency interpretation: repeat N times, event occurs m times, m/N -> P(A) as N large. Axiomatic approach Ch2.
- Ex0.2 "smarter than a pigeon" (Monty-Hall style 3 cards; switch?) -> danger of assuming equally likely.
- Ex0.3 prosecutor's fallacy: fingerprint match chance 1 in 50,000; needs cond prob/Bayes.
- Ex0.4 Choices (£5 vs toss for £10; £5000 vs £10000; £1 vs 10 heads for £1000) -> expectation & variation; utility beyond scope.
## Ch1 Sample spaces & events
- Outcomes precisely specified, mutually exclusive, cover all possibilities. Def1.1 sample space S (or Ω). Def1.2 event = subset of S; occurs if outcome ∈ subset. Def1.3 simple/elementary event = single element.
- Ex1.1 die S={1..6}, A even={2,4,6}. Ex1.2 toss thrice: S={hhh,...,ttt}; alt notation S~ = sets of toss indices that are heads {{1,2,3},...,{}}; B exactly one head={htt,tht,tth}; C second toss head={hhh,hht,thh,tht}; B~={{1},{2},{3}}, C~={{2},{1,2},{2,3},{1,2,3}}. Number of elements invariant under notation change (check). Prime ≠ complement (use c superscript).
- Ex1.3 two die rolls; Ex1.4 exam until pass: S1={P,FP,FFP,...}, S2={1,2,3..}, S3={0,1,2...} (number of fails), S4 finite — which can be sample space (S1,S2,S3 yes; S4 no).
- Mainly finite/countably infinite sample spaces.
- 1.2 Set theory: set = unordered collection of well-defined distinct objects ({2,3,3} not a set in this course). Specify by listing, pattern (countable), rule {x: ...}. x∈A, ∉. |A| cardinality (≠ absolute value). A∪B (1.1), A∩B (1.2) (books write AB), A\B (1.3), A△B=(A\B)∪(B\A) (1.4), A⊆B, A^c = S\A (1.5), disjoint/mutually exclusive A∩B=∅. De Morgan (1.6) (A∪B)^c=A^c∩B^c; (1.7) (A∩B)^c=A^c∪B^c. Ex1.7 A△B=(A∩B^c)∪(A^c∩B). Ex1.8 disjoint decomposition A=(A∩B)∪(A∩B^c); A∪B = (A\B)∪(A∩B)∪(B\A). Ex1.9 A={2..8},B={1,3,5,7},C={2,4,5,8}: D={2,4,8}? E={4,5}? Ex1.10* derive 1.7 from 1.6.
- 1.3 events: A^c "A does not occur"; A∩B both; A∪B at least one; A\B A but not B; A△B exactly one. Ex1.11 die: A even {2,4,6}, B prime {2,3,5}; F1=A∪B={2,3,4,5,6}; F2=A△B={3,4,5,6}. Ex1.12 lecture attendance (Alisha,Bilal,Chloe,Daniel). Ex1.13 rugby squad C captain,F forward,I injured: (i) F∩I (ii) F\C or F∩C^c (iii) F∩I=∅; (b)(i) F^c∪I^c "not an injured forward" (ii) |I^c|<15 fewer than 15 uninjured. Ex1.15 horse racing (Adobe, Brandy, Chopin). Ex1.16 stopping rules (two heads or three tails).
## Ch2 Properties of probabilities
- Def2.1 Kolmogorov axioms: P assigns real P(A) to each event: (a) P(A)≥0 (b) P(S)=1 (c) pairwise disjoint A1..An => P(∪)=ΣP(Ak). (finite version; countable version used implicitly in Ch5). P = probability measure. Pairwise disjoint = mutually exclusive.
- Ex2.2 biased coin P({h})=1/3, P({t})=2/3: verify axioms (check all disjoint unions). Notation P({h}) preferred over P(h).
- Ex2.3 S={1..8}, P(A)=(|A∩{1,2,3,4}|+2|A∩{5,6,7,8}|)/12.
- Prop2.2 P(A^c)=1−P(A) (proof: A1=A, A2=A^c disjoint, union S). Cor2.3 P(∅)=0. Cor2.4 P(A)≤1. Prop2.5 A⊆B => P(A)≤P(B) (B = A ∪ (B\A)). Prop2.6 finite event = sum of simple event probabilities. Remark: strategy = write events as disjoint unions.
- Ex2.4 rugby: 50% forwards, 25% injured, 10% injured forwards: P(forward not injured)=0.5−0.1=0.4. Ex2.5 P(A)=1/2,P(B)=1/4,P(A∩B)=1/10: friend says P(A∪B)=3/4 wrong; correct 1/2+1/4−1/10=13/20.
- Prop2.7 inclusion-exclusion two events P(A∪B)=P(A)+P(B)−P(A∩B) (proof E1=A\B,E2=A∩B,E3=B\A). Rota quote.
- Ex2.6 (2018 exam) bus lines Xinji–Yiwu: line1 buses A (Xinji–Ulanqab) & B (Ulanqab–Yiwu), line2 C,D via Weihui; P(A)=.9,P(B)=.8,P(C)=.7,P(D)=.8; at least 3 of 4 running => P(A∪B)=1 => P(A∩B)=0.9+0.8−1=0.7.
- Prop2.8 incl-excl three events (proof apply 2.7 three times with D=A∪B; C∩(A∪B)=(C∩A)∪(C∩B)).
- Ex2.7 P(A)=P(B)=P(C)=1/3, pairwise intersections 1/10: P(none)=1−P(A∪B∪C)=1−(1−3/10+P(A∩B∩C)) = 3/10 − P(A∩B∩C); with 0≤P(A∩B∩C)≤1/10 → P(none) ∈ [1/5, 3/10]. Ex2.8** 4 events/general.
- 2.4 Equally likely: P(A)=|A|/|S| (2.5); not for biased; impossible for infinite S=N uniformly. Ex2.9 check axioms. Gives |A∪B|=|A|+|B|−|A∩B|. Probability becomes counting.
- Ex2.10 doubles with two dice = 6/36=1/6. Ex2.11 five fair tosses at least two heads = 1−(1+5)/32=26/32=13/16.
- Ex2.12 P(A)=1/2,P(B)=1/4,P(A∩B)=1/10: P(B^c)=3/4, P(A∪B)=13/20, P(A∩B^c)=2/5. Ex2.13 P(A∪B)=0 ⇒ P(A)=P(B)=0. Ex2.14 Bonferroni P(A∩B)≥P(A)+P(B)−1; P(A△B)=P(A)+P(B)−2P(A∩B).
## Ch3 Sampling (equally likely)
- Basic principle of counting m×n. n-tuple ordered (b1..bn) not necessarily distinct vs set unordered distinct.
- 3.2 Ordered with replacement: S={(s1..sr): si∈U}, |S|=n^r (3.1). Ex3.1 words from A–E length 3: 125. Ex3.2 E1 no vowels 27/125; E2 begin & end same letter 25/125=1/5. Ex3.3 Bank PIN 4-digit (10^4): all even 5^4/10^4=1/16; palindrome 100/10^4=1/100; no digit exceeds 7: 8^4/10^4=0.4096; largest exactly 7: (8^4−7^4)/10^4=(4096−2401)/10000=0.1695.
- 3.3 Ordered without replacement: n!/(n−r)! (3.2); k!, 0!=1. Ex3.4 60 words. Ex3.5 permutations 5!=120. Ex3.6 P(no repeated letters with replacement)=60/125=12/25. Ex3.7* PIN at least one repeat 1−10·9·8·7/10^4=1−0.504=0.496; strictly increasing C(10,4)/10^4=210/10000=0.021.
- 3.4 Unordered without replacement: subsets size r, |S|=n!/((n−r)!r!) = C(n,r) (3.3) (overcount by r!). Ex3.8: 60/6=10. C(n,r)=0 when r>n. Binomial theorem (a+b)^n=Σ C(n,k) a^k b^{n−k}. Ex3.9** prove by induction. Ex3.10 course reps 2 of 246 MTH4107 & 2 of 256 MTH4207: C(246,2)C(256,2)=983,606,400. Ex3.11 Lotto 1/C(49,6)=1/13,983,816; 1/C(59,6)=1/45,057,474; *match 5: C(6,5)C(53,1)/C(59,6).
- Thm3.1 (a) n^r (b) n!/(n−r)! (c) C(n,r). Remarks: decide #selected, from what set, order?, repetition? Can use ordered sample space for unordered event — be consistent. Unordered with replacement not covered.
- Ex3.12 coins: 7 gold 3 copper, pick 4: P(all gold) ordered 7·6·5·4/(10·9·8·7)=1/6; unordered C(7,4)/C(10,4)=35/210=1/6. Coins distinct objects. (source typo "|F2|/|S|" should be |F1|).
- Ex3.13 F2 two gold then two copper (ordered only): 7·6·3·2/(10·9·8·7)=252/5040=1/20; F3 two gold two copper any order C(7,2)C(3,2)/C(10,4)=63/210=3/10.
- Ex3.14 poker dice pair: |S|=6^5, |G|=C(5,2)·6·5·4·3=10·360=3600, P=3600/7776=25/54.
- Ex3.16 4 reps of 502 random: C(246,2)C(256,2)/C(502,4). Ex3.17 cricket 10 batsmen 8 bowlers choose 11: P(6 bat,5 bowl)=C(10,6)C(8,5)/C(18,11); fewer than 3 bowlers: need ≥9 batsmen: C(10,9)C(8,2)+C(10,10)C(8,1) over C(18,11). Ex3.18* Pascal C(n,r)=C(n−1,r)+C(n−1,r−1) via P(1 in subset)=r/n.
## Ch4 Independence
- Def4.1 conditional probability P(E2|E1)=P(E1∩E2)/P(E1), P(E1)≠0 (taught fully in Ch18).
- Ex4.2 two die rolls: A first even, B second >4: P(A)=1/2,P(B)=1/3,P(A∩B)=6/36=1/6 = product; P(A|B)=1/2,P(B|A)=1/3.
- Def4.2 independent: P(E1∩E2)=P(E1)P(E2); else dependent. May assume independence if (i) physically unrelated (ii) checked by calculation (iii) told so. Independence ≠ physically unrelated (unrelated ⇒ independent; related may or may not be).
- Ex4.3 Alphabus P(A)=9/10, Betabus P(B)=4/5 independent: P(A∪B)=0.9+0.8−0.72=0.98.
- Thm4.3 (P(E1),P(E2)>0) equivalent: (a) independent (b) P(E1|E2)=P(E1) (c) P(E2|E1)=P(E2). Proof cycle a⇒b⇒c⇒a.
- Ex4.4 P(E1∪E2)=P(E1)P(E2^c)+P(E2) ⇒ independent.
- Ex4.5 refers to Example 18.4 (die info A,B,C).
- Ex4.6 two dice D first odd, E second odd, F sum odd: pairwise independent (each 1/4) but P(D∩E∩F)=0≠1/8 ⇒ not mutually independent.
- Def4.4 three events pairwise independent (3 eqns) ; mutually independent if also triple product. Def4.5 n events mutually independent: every sub-collection of size t (2≤t≤n) factorises. Unqualified "independent" for ≥3 usually means mutually.
- Ex4.7 toss thrice: A first=second, B first≠last, C first tail. (Answer: P(A)=P(B)=P(C)=1/2; A∩B={first=second≠third}: hht,tth: 2/8=1/4 ✓; A∩C: tt?: 2/8 ✓; B∩C: t?h: 2/8 ✓; A∩B∩C: tth 1/8 ✓ ⇒ mutually independent.)
- Def4.6 conditional independence given E3: P(E1∩E2|E3)=P(E1|E3)P(E2|E3).
- Ex4.8 magic coins: fair & P(H)=3/4 coin chosen at random, tossed twice. H1,H2 cond. indep given F (1/4) and given F^c (9/16); P(H1)=P(H2)=5/8; P(H1∩H2)=1/8+9/32=13/32=26/64 ≠ 25/64 ⇒ not independent (first head suggests biased coin).
- Ex4.9 two dice A first odd, B at least one six, C sum seven. (A: 18/36; B: 11/36; A∩B: first odd & at least one six = first odd and second six = 3/36; P(A)P(B)=1/2·11/36=11/72 ≠ 6/72 ⇒ not independent).
- Ex4.10* examples. Ex4.11 integers 1..36: E,O (not indep: P(E∩O)=0); E & Q squares (1,4,9,16,25,36: 6; even squares 4,16,36: 3/36=1/12 = (1/2)(1/6) ⇒ independent); O,Q: odd squares 1,9,25: 3/36 = 1/12 ⇒ independent; D3,D4: D12 multiples of 12: 3/36=1/12 = (12/36)(9/36)=1/3·1/4 ⇒ independent; D4,D6: lcm 12: 3/36 = 1/12 vs (9/36)(6/36)=1/24 ⇒ not.
- Ex4.12 top card A ace, R red, M major suit (♡,♠): mutually independent. Ex4.13* A,B,C mutually indep ⇒ A and B∪C independent.
## Ch5 Random variables
- Def5.1 random variable = function S→R (subtlety for uncountable S beyond scope). Capital letters, late alphabet; events early alphabet. P(X) meaningless; "X=x" shorthand {ω∈S: X(ω)=x}; "X≤x"; "Y>2Z" = {ω: Y(ω)>2Z(ω)}.
- Ex5.2 sum of two dice: X:(j,k)↦j+k, domain S (36 pairs), range {2..12}; X((5,2))=7, X((6,4))=X((4,6))=10 (not injective), X((2,2))=4; X(5,6) and X(∅) make no sense. P(X=5)=4/36=1/9, P(X=3)=1/18, P(X=1)=0, P(X≤2)=1/36, P(X≤12)=1.
- Ex5.3 head count X, tails Y, Z=max{X,Y}: ranges {0,1,2,3}, Z∈{2,3}; X(hht)=2,Y(hht)=1,Z(hht)=2; P(more tails than heads)=1/2.
- Def5.2 discrete: set of values finite or countably infinite. Footnote: for continuous X, P(X=x)=0.
- Def5.3 p.m.f. x↦P(X=x); notation p(x), pX(x); p(X=x) and P(x) are wrong notation; must have p(xk)>0 for possible values.
- Ex5.5 pmf two dice table: 1/36,1/18,1/12,1/9,5/36,1/6,5/36,1/9,1/12,1/18,1/36 (x=2..12). Ex5.6* formula P(X=x)=(6−|x−7|)/36.
- Ex5.7 waiting for Tail: T values N, P(T=n)=1/2^n (geometric).
- Ex5.8 4 balls from 10 without replacement X largest: values 4..10; P(X=5)=C(4,3)/C(10,4)=4/210=2/105; pmf P(X=k)=C(k−1,3)/C(10,4); P(X>5)=1−P(X≤5)=1−C(5,4)/210=1−5/210=41/42.
- Prop5.4 Σ P(X=xk)=1 (proof: events X=xk partition S; countable additivity). Check plausibility. Ex5.9 checks (geometric series).
- Ex5.10 X pmf: −2:1/10, −1:2/5, 0:1/4, 1:1/5, 2:1/20; Y=X²+4: values 4,5,8: P(Y=4)=1/4, P(Y=5)=2/5+1/5=3/5, P(Y=8)=1/10+1/20=3/20.
- c.d.f. F: x↦P(X≤x) (for continuous: pdf). Ex5.11 P(X=2)=1/20, P(X=3)=0, P(X≤1)=19/20, P(X²<2)=17/20. Ex5.12 marbles 6 red 2 blue choose 5: B∈{0,1,2}: P(B=0)=C(6,5)/C(8,5)=6/56, P(B=1)=C(2,1)C(6,4)/56=30/56, P(B=2)=C(6,3)/56=20/56; R=5−B. Ex5.13 coin p tossed 3: Bin(3,p). Ex5.14* geometric series (1−z^n)/(1−z); 1/(1−z) for |z|<1; (c) toss until head or n tails. Ex5.15** Σ C(n,k)=2^n; best n for exactly two tails: n=3 or 4 (P=3/8).
## Ch6 Expectation & variance
- Def6.1 E(X)=Σ xk P(X=xk) (mean, µ); need not be a possible value. Ex6.1 die E(W)=7/2. Ex6.2 two dice E(X)=7.
- Prop6.2 m≤X≤M ⇒ m≤E(X)≤M (sanity check). Ex6.3* E(T)=2 for geometric(1/2). Infinite case may be infinite/undefined.
- Ex6.4 E(Y)=E(X²+4)=26/5 via pmf of Y or via f(x). Prop6.3 LOTUS E(f(X))=Σ f(xk)P(X=xk) (proof omitted).
- Ex6.5 E(X+c)=E(X)+c, E(cX)=cE(X).
- Ex6.6 Great Expectations restaurant: 4 meals cost £4 each, sell £9, P(X=0)=1/12,P(X=3)=1/6,P(X=4)=1/8,E(X)=2 ⇒ find P(X=1),P(X=2): a+b=1−1/12−1/6−1/8=15/24=5/8; a+2b+3/6+4/8 = 2 → a+2b=1 → b=3/8, a=1/4. Y=9X−16, E(Y)=18−16=£2.
- Def6.4 nth moment E(X^n). Def6.5 Var(X)=Σ[xk−E(X)]²P(X=xk)=E([X−E(X)]²) ≥0; sd = sqrt Var.
- Ex6.7 investments X 99/101 (Var 1), Y 90/110 (Var 100), same mean 100: Y riskier.
- Prop6.6 Var(X)=E(X²)−[E(X)]² (proof expand). "mean of the square minus square of the mean"; E(X²)≥[E(X)]².
- Ex6.8 die Var=91/6−49/4=35/12. Ex6.9 two dice Var=35/6. Ex6.10 E(Y)=2,Var=6 ⇒ E(2Y²)=2(6+4)=20.
- Prop6.7 E(aX+b)=aE(X)+b; E(b)=b degenerate; E(3X²−4X+5)=3E(X²)−4E(X)+5. Prop6.8 Var(aX+b)=a²Var(X) (proof); Var(b)=0; shift doesn't change spread.
- Ex6.11 Y=X/2 (empirical mean of two dice): E=7/2, Var=35/24 (< 35/12 single die).
- Ex6.12* E(3X+7)=10, Var(3X+7)=36 ⇒ E(X)=1, Var(X)=4 ⇒ e.g. X=−1 or 3 each w.p. 1/2.
- Ex6.13 E=5, Var=2/3: E(3X)=15, Var(3X)=6, E(4−3X)=−11, Var(4−3X)=6, E(4−3X²)=4−3(2/3+25)=−73.
- Ex6.14 Bin(3,p): E=3p, Var=3p(1−p). Ex6.15** Σk z^{k−1}=1/(1−z)², Σk² z^{k−1}=2/(1−z)³−1/(1−z)² (not required to prove). Ex6.16* E(Z)=Σ_{i=1}^n P(Z≥i); Markov P(Z≥t)≤E(Z)/t. Ex6.17** St Petersburg (E infinite), Angela–Boris E(Y) doesn't exist.
## Ch7 Interlude — tips (read actively, do examples, show working, check answers). Notes define examinable content; "open-book exam" mentioned in 7.2!
## Ch8 Common discrete RVs
- Ex8.1 two fair tosses X heads: pmf 1/4,1/2,1/4; E=1, Var=1/2, σ=1/√2; Y=X²−1 pmf −1:1/4, 0:1/2, 3:1/4. pmf contains all probabilistic info; different scenarios same pmf ⇒ named distributions.
- Bernoulli(p): P(0)=1−p,P(1)=p; E=p, Var=p(1−p). Ex8.2 one toss. (Fig 8.1 bar plots p=.2,.5,.8)
- Binomial Bin(n,p): C(n,k)p^k(1−p)^{n−k}, k=0..n; E=np, Var=np(1−p) (8.1). n independent stages, success p; C(n,k) counts orderings. Sum of n indep Bernoulli (Ch10). Bernoulli trials. (Fig 8.2 n=15)
- Geometric Geom(p): (1−p)^{k−1}p, k=1,2,...; E=1/p, Var=(1−p)/p²; number of trials up to & incl first success. Alt def counts failures Y=X−1, (1−p)^k p, k=0,1,...
- Hypergeometric Hg(n,m,ℓ): bag n balls, m white, pick ℓ without replacement, X white: C(m,k)C(n−m,ℓ−k)/C(n,ℓ); E=ℓm/n, Var=ℓ(m/n)((n−m)/n)((n−ℓ)/(n−1)) (finite population correction). ≈ Bin(ℓ, m/n) for n,m large [notes typo "Bin(m/n, ℓ)"]. pmf zero if k>m. R: dhyper(k,m,n−m,l).
- Negative binomial NB(r,p): X = number of failures before r-th success: C(k+r−1, r−1) p^r (1−p)^k, k=0,1,...; E=(1−p)r/p, Var=(1−p)r/p²; matches R. Ex8.5 die until three 6s; P(10 rolls)=P(X=7)=C(9,2)(1/6)^3(5/6)^7.
- Discrete Uniform U(m,m+n): 1/(n+1) for k=m..m+n; E=m+n/2, Var=n(n+2)/12. Fig 8.6 m=−2,n=5. Derive!
- Poisson(λ): λ^k e^{−λ}/k!, k=0,1,..; E=Var=λ. Ex8.6 von Bortkiewicz 1898 Prussian cavalry horse kicks: deaths/yr 0..4 freq 109,65,22,3,1 (rel .545,.325,.110,.015,.005), mean 0.61, fits Poisson(0.61). Large population, small prob ("law of small numbers").
- Summary table with R commands: dbinom(k,n,p), dgeom(k,p) [note R's geom counts failures!], dhyper(k,m,n-m,l), dnbinom(k,r,p), dunif, dpois(k,lambda). Bell shape for many independent incidents (→CLT).
- 8.2 c.d.f. Def: t↦P(X≤t), defined for all real t, piecewise constant step function. Ex8.7 five dice max X: P(X=4)=(4/6)^5−(3/6)^5. P(X≤t)=Σ_{k≤⌊t⌋}; P(X=k)=F(k)−F(k−1); P(k≤X≤ℓ)=F(ℓ)−F(k−1) [notes have typo "P(X≤k)−P(X≤ℓ−1)"]. Ex8.8 20 red 30 blue pick 15 X blue ~Hg(50,30,15): P(5≤X≤10)=F(10)−F(4). Figs 8.8 (die pmf & cdf), 8.9 (Hg m=16,n=80,ℓ=15).
- mgf Def: M_X(t)=E(e^{tX}); M(0)=1; M'(0)=E(X); M^{(n)}(0)=E(X^n). Ex8.9 Bin: M(t)=(1−p+pe^t)^n, M'(t)=np(1−p+pe^t)^{n−1}e^t, M''... E(X²)=n(n−1)p²+np ⇒ Var=np−np².
- Ex8.10 red balls N total M red pick n: with replacement Bin(n,M/N); without: hypergeometric (8.2), support max(0,n−(N−M))≤k≤min(n,M).
- Ex8.11 (2016 exam) typo every 1000 chars, 600-char page, fewer than 2 errors: Poisson(0.6): e^{−0.6}(1+0.6)=1.6e^{−0.6}≈0.878 (or Bin(600,1/1000)).
- Ex8.12 A~Poisson(3), B~Geom(1/3), C~Bin(4,1/6): P(A=2)=9e^{-3}/2; P(A>2)=1−17e^{-3}/2; P(B=3)=4/27; P(B≤3)=19/27; P(C=2)=25/216.
- Ex8.13 Geometric memoryless P(G>k+ℓ|G>k)=P(G>ℓ) (P(G>k)=(1−p)^k). Ex8.14* Poisson thinning: Y~Poisson(λp). Ex8.15 HH count in 4 tosses — not binomial (overlapping, dependent): N values 0..3; count sequences: N=3: hhhh (1); N=2: hhht, thhh (2); N=1: hhth, hhtt, thht, tthh, hthh (5)... careful; N=0: 8? total 16. Let me verify later.
- Ex8.16** Hg mean/var derivation.
## Ch9 Continuous RVs (lines mth_notes_b ~2390-3410)
- 9.1 P(X=2)=0 for continuous; only intervals informative. Def3: X continuous if ∃ continuous f_X: R→[0,∞) with ∫_a^b f_X = P(a≤X≤b). Area under graph. P(a≤X≤b)=P(a<X≤b)=P(a≤X<b)=P(a<X<b). Additivity over disjoint intervals. f≥0; normalisation ∫f=1.
- Ex9.1 bus wait uniform 3–5 min: c=1/2; P(4<X<4.5)=1/4. Fig 9.1 shaded.
- Def4 E(X)=∫ t f(t) dt; Var=∫(t−E X)² f = E((X−EX)²); Var=E(X²)−(EX)². µ_X, σ_X², σ_X sd. Ex9.2 µ=4, σ²=1/3 (sub s=t−4: ∫_{-1}^{1} s²/2 ds=1/3).
- cdf F_X(x)=∫_{−∞}^x f; dF/dx=f (FTC); F non-decreasing; P(a≤X≤b)=F(b)−F(a). Ex9.3 F=(x−3)/2 on [3,5], 0 below, 1 above. Fig 9.2.
- 9.2 Uniform U(a,b): f=1/(b−a) on [a,b]; µ=(a+b)/2; σ²=(b²+ab+a²)/3 − (a+b)²/4 = (b−a)²/12; F=(x−a)/(b−a). R: dunif(x,min=a,max=b), punif.
- Exponential Exp(λ): f=λe^{−λx}, x≥0 (0 for x<0), "decay rate λ". Ex9.4 times between radioactive decays. µ=1/λ, σ²=2/λ²−1/λ²=1/λ². F=1−e^{−λx} (x≥0). Figs 9.3/9.4 λ=0.7,2,4. Ex9.5 bus Exp(0.4): E=2.5 min; P(X>5)=1−F(5)=e^{−2}≈0.1353. Fig 9.5. mgf M(t)=λ/(λ−t), t<λ; M'(0)=1/λ.
- 9.3 Normal: f=(1/(σ√(2π))) e^{−(x−µ)²/(2σ²)}; bell, max at µ, inflection points at µ±σ. Fig 9.6 (µ=.5,σ=1.5), 9.7 (µ=1,σ=.5; µ=−.5,σ=.5; µ=−.5,σ=1.5). Normalisation via z=(x−µ)/σ, ∫e^{−z²/2}=√(2π) (not elementary). E=µ (odd integrand), Var=σ² (integration by parts). Notation X~N(µ,σ²) [VARIANCE in 2nd slot]. Determined by mean & variance.
- Standardisation Z=(X−µ)/σ: E(Z)=0, Var(Z)=1 [notes typo "Z~N(1,0)" twice — should be N(0,1)]. P(a<X≤b)=P((a−µ)/σ<Z≤(b−µ)/σ).
- Φ(z)=P(Z≤z)=∫_{−∞}^z (1/√(2π))e^{−t²/2}dt ("probability integral"), S-shape, Φ(−∞)=0, Φ(∞)=1, Φ(−z)=1−Φ(z). R pnorm(x).
- Ex9.6 P(|X−µ|>σ)=P(|Z|>1)=1−Φ(1)+Φ(−1)=0.3173 (31.7%); P(|X−µ|>2σ)≈0.0455 ⇒ within 2σ w.p. 95.4%. Figs 9.9/9.10.
- z-scores: z_α with P(Z>z_α)=α ⇒ Φ(z_α)=1−α ⇒ z_α=Φ^{−1}(1−α). Def5 quartiles/median: x_α with P(X≤x_α)=1−α: α=1/2 median; α=1/4 upper quartile (P≤ =3/4); α=3/4 lower quartile. Ex9.7 P(X−µ>C)=0.01 ⇒ C=σ z_{0.01}, z_{0.01}=Φ^{−1}(0.99) (≈2.326). Lemma1: P(Z>z_α)=P(Z<−z_α)=α; P(|Z|>z_α)=2α. Ex9.8 P(|X−µ|>b)=0.05 ⇒ b=σ z_{0.025}, z_{0.025}=Φ^{−1}(0.975)=1.959964 ≈1.96. Fig 9.11.
- Lemma2 normal mgf M(t)=e^{tµ+t²σ²/2} (proof complete square). M''(0)=σ²+µ².
- 9.3.1 Table (Fig 9.12): text says "row 0.4, column 2 is 0.1628 ⇒ Φ(0.42)=0.6628" — i.e. that table gives area between 0 and z (Φ(z)−0.5)! Ex9.9: Φ(1.72)=0.9573 (table .4573), Φ(0.46)=0.6772, Φ(2.3)=0.9893, Φ(4.3)=1 (z≥3.9 → 1). P(Z≤−z)=P(Z≥z)=1−Φ(z). P(z1<Z≤z2)=Φ(z2)−Φ(z1). [CHECK Fig 9.12 image; Ex9.10 solution reads full-cdf values 0.9452 for 1.60, 0.1539 for −1.02 — inconsistent table conventions within notes.]
- Ex9.10 P(Z>1.60)=0.0548; P(Z>−1.02)=0.8461; P(0.5<Z<1.57)=0.9418−0.6915=0.2503; P(−2.55<Z<0.09)=0.5359−0.0054=0.5305.
- Ex9.11 component Exp(1/120) days: P(X<60)=1−e^{−0.5}=0.393; (b) more than 240: notes compute P(X<240)=0.865 by mistake — correct P(X>240)=e^{−2}=0.135. Ex9.12 memoryless P(X>340|X>100)=P(X>240)=0.135 (used component as good as new). Ex9.13 phone call Exp(1/12): µ=σ=12, P(X>5)=e^{−5/12}=0.6592. Ex9.14 30 customers/hr: mean 2 min between, 3 customers 6 min avg, λ=0.5/min: P(<1 min)=1−e^{−0.5}=0.3935; P(>5)=e^{−2.5}≈0.0821; reasonableness (groups, varying rate). Figs 9.13–9.15.
## Ch10 Several RVs
- Def10.1 joint pmf (xk,yℓ)↦P((X=xk)∩(Y=yℓ)) written P(X=xk,Y=yℓ); nonneg, sums to 1; table.
- Ex10.1 bag 3 red 2 yellow 2 green, pick 3: |S|=C(7,3)=35; P(R=1,Y=1)=3·2·2/35=12/35; P(R=3,Y=1)=0.
- Ex10.2 full table: P(R=r,Y=y)=C(3,r)C(2,y)C(2,3−r−y)/35. Compute: (r,y): (0,1):C(2,1)C(2,2)=2 →2/35; (0,2):C(2,2)C(2,1)=2→2/35; (1,0):3·C(2,2)=3→3/35; (1,1):12/35; (1,2):3·1·1=3→3/35; (2,0):C(3,2)·C(2,1)=6→6/35; (2,1):3·2=6→6/35; (3,0):1→1/35; (0,0):0 (need 3 green, only 2); (2,2),(3,1),(3,2),(1,... etc 0. Sum: 2+2+3+12+3+6+6+1=35 ✓.
- Prop10.2 marginals = row/column sums. Ex10.4 marginals: R: 0:4/35,1:18/35,2:12/35,3:1/35 ⇒ E(R)=(18+24+3)/35=45/35=9/7; Y: 0:10/35,1:20/35,2:5/35 ⇒ E(Y)=(20+10)/35=30/35=6/7.
- Prop10.3 E(g(X,Y))=ΣΣ g(xk,yℓ)P(X=xk,Y=yℓ). Ex10.5 U∈{1,2},V∈{1,3}: P(1,1)=1/2,P(2,1)=1/6,P(1,3)=1/3,P(2,3)=0: E(UV+U)=2·½+4·⅙+4·⅓+8·0=1+2/3+4/3=3.
- Thm10.4 E(X+Y)=E(X)+E(Y). Cor10.5 linearity E(Σ c_i X_i)=Σ c_i E(X_i) — NO assumptions (even X2=(X1+3)²).
- Ex10.6 E(R+Y)=15/7, E(RY)=6/7 [from Ex10.15: E(RY)=6/7]; E(R)E(Y)=54/49 ≠ 6/7=42/49.
- Def10.6 independent RVs: P(X=xk,Y=yℓ)=P(X=xk)P(Y=yℓ) for ALL xk,yℓ; n RVs: joint factorises. Ex10.7* three RVs factorising ⇒ pairs factorise (simpler than events).
- Ex10.8 U,V not independent: P(U=2,V=3)=0 ≠ (1/6)(1/3).
- Thm10.7 X,Y independent ⇒ (a) E(XY)=E(X)E(Y) (b) Var(X+Y)=Var(X)+Var(Y) (proof via E(XY)). Extends to 3+.
- Cor10.8 independent: Var(Σc_iX_i)=Σc_i²Var(X_i). Converse of E(XY)=EXEY false. Ex10.9* counterexample. Ex10.10 R,Y not independent (P(R=0,Y=0)=0≠(4/35)(10/35)). Ex10.11 five dice sum: E=35/2, Var=5·35/12=175/12.
- 10.4 Binomial revisited: indicators X_k ~Bernoulli(p); E(X)=np (no independence needed); Var=np(1−p) needs independence.
- Ex10.12 X~Bin(7,1/6) (E 7/6, Var 35/36), Y~Geom(1/2) (E 2, Var 2), Z~Poisson(6) (E=Var=6); X⊥Y, X not⊥Z: (a) E(X+Y)=19/6 (b) E(X+Z)=43/6 (c) E(X+2Y+3Z)=7/6+4+18=139/6 (d) E(X²+Y²+Z²)=(35/36+49/36)+(2+4)+(6+36)=84/36+6+42=7/3+48=151/3 (e) Var(X+Y)=35/36+2=107/36 (f) Var(X+Z) cannot (g) cannot.
- Ex10.13 ones and twos (two dice). Ex10.14* joint from marginals with zeros: X∈{0,1} each 1/2; Y∈{0,1,2} each 1/3; P(0,0)=P(1,2)=0 ⇒ P(1,0)=1/3, P(0,2)=1/3, P(0,1)=1/2−1/3=1/6, P(1,1)=1/6.
- 10.6 Def10.9 Cov(X,Y)=E([X−EX][Y−EY]); Corr=Cov/√(VarX VarY) (Var>0). Cov(X,X)=Var(X). Prop10.10 Cov=E(XY)−E(X)E(Y). Uncorrelated if Cov=0; independent ⇒ Cov=0, converse false. Cov>0 deviate together (revision hours & exam score); Cov<0 opposite (temperature & hot chocolate sales). Correlation ≠ causation (storks & babies in Germany [Sie88]; Spurious Correlations [Vig15]).
- Ex10.15 Cov(R,Y)=6/7−(9/7)(6/7)=42/49−54/49=−12/49: negative (more red ⇒ fewer yellow).
- Prop10.11 (a) Corr(aX+b,cY+d)=Corr(X,Y) for a,c>0 (b) −1≤Corr≤1. Ex10.16 Cov(aX+b,cY+d)=acCov(X,Y); Y=aX+b, a>0 ⇒ Corr=1; a<0 ⇒ −1.
## Ch11 CLT (George Box quote "all models are wrong but some are useful")
- Ex11.1 coin p=0.3, n=50: X~Bin(50,0.3), µ=15, σ²=10.5; "if np(1−p) larger than 10" normal approx good; P(X=k)≈P(k−½≤Y≤k+½); k=16: exact dbinom=0.1147002; approx Φ((16.5−15)/√10.5)−Φ((15.5−15)/√10.5)=0.1169709 (two digits). Fig 11.1.
- Prop11.1 CLT: X1..Xn i.i.d. mean µ, var σ²; X=ΣXk; Y~N(nµ,nσ²): P(a≤X≤b)≈P(a−½≤Y≤b+½) for large n [informal; continuity correction is for integer-valued X]. Rigorous statement/proof beyond first year.
- Ex11.2 fair die 120 rolls sum: µ=7/2, σ²=35/12, Y~N(420,350): P(410≤X≤430)≈Φ(10.5/√350)−Φ(−10.5/√350)=0.4253719 (42.5%). 95.4% interval [420−2√350, 420+2√350]≈[382.6,457.4] → notes say [382,458].
- Prop11.2 sum of n independent N(µ,σ²) is exactly N(nµ,nσ²) (proof via mgf product, uses independence).
- Progress check: lay CLT; binomial approx conditions; Z1+Z2 pdf (if independent N(0,2)); die 3000 rolls sum>15000 (µ=10500, σ²=3000·35/12=8750); 3 rolls can't (n small); 700 picks w/o replacement from 500 gold 500 copper — not independent ⇒ can't use CLT (hypergeometric).
## Ch12 Epilogue: exam tips (read question, show working, use time, check). Ex12.1 Santa: Rudolph + 8 reindeer each cold w.p. 1/4: (i) P(red nose)=1/9·1+8/9·1/4=1/9+2/9=1/3 (ii) P(Rudolph|red)=(1/9)/(1/3)=1/3 (iii) Y~Bin(8,1/4), E(X)=1+2=3. (b) Var(U−V)=VarU+VarV−2Cov(U,V).
## Ch13 Intro to statistics (Semester B)
- Statistics = analysis of data using probability tools. Ex13.1 German tank problem (serial numbers 124,3,65,122,48; estimate N). Ex13.2 Simpson's paradox: drug A 160 (100 men 20 recover; 60 women 40 recover), drug B 230 (210 men 50 recover; 20 women 15 recover): men A 20% vs B 23.8%; women A 66.7% vs B 75%; overall A 60/160=37.5% vs B 65/230=28.3% — B better in each group, A better overall (unfortunate design). Ex13.3 Polling 27 June 2019 ukpollingreport (YouGov CON 22 LAB 20 LDEM 19 BREX 22 GRN 10; Ipsos MORI CON 26 LAB 24 LDEM 22 BREX 12 GRN 8).
- 13.2 population (finite/infinite, real/hypothetical); sample = subset studied. Survey (sample) vs census (whole population); observational study; designed experiment. Ex13.4 Coke/Pepsi 400 survey; UK BioBank 500,000 observational; 60 carpal tunnel patients acupuncture+exercise vs exercise designed experiment.
- Data types: quantitative continuous (blood pressure), quantitative discrete (attendance), qualitative categorical/factors (eye colour, no order), qualitative ordinal (Definitely agree...). Remarks: bus delay seconds discrete vs arbitrary precision continuous; car colours could be ordered by spectrum; phone numbers/IDs qualitative. Ex13.5 MTH4107 evaluation "My mathematical background..." 12,37,23,6,1 → ordinal (type determined by answers not frequencies).
- 13.3 R: binomial dbinom/pbinom; Ex13.6 P(BUY)=0.05, 100 customers, P(X>5)=1−pbinom(5,100,0.05)=0.3840009. Plot code k=0:10, pmf=dbinom(k,n,p), plot(k,pmf), barplot(pmf~k) (n=10, p=0.2; X=2 most likely ≈30%; exact 0.302). Poisson: counts per unit time; Ex13.7 red lights λ=13.6, P(X<11)=ppois(10,13.6)=0.2037285; barplot k=0:35. Geometric: R uses failures: P(X=k)=dgeom(k−1,p), P(X≤k)=pgeom(k−1,p); Ex13.8 projector fails p=0.05/day; P(no fail in 5 days)=P(X>5)=1−pgeom(4,0.05)=0.7737809 (=0.95^5). Hypergeometric dhyper(k,m,n−m,l), phyper; Ex13.9 30 judges 5 minority, panel 7: most likely X=1 (>40%); P(X=0)≈20% (C(25,7)/C(30,7)=480700/2035800=0.2361) ⇒ not evidence of unfairness. Normal: dnorm(x,mu,sigma), pnorm(x,mu,sigma) [R uses SD!]; z-score; Ex13.10 EU male height N(178,7²): P(X>200)=1−pnorm(200,178,7)=0.0008365374; z=3.142857. plot(x,pdf,type="l",yaxs="i"); seq(140,210,0.1). Estimate P(<170cm) from cdf chart (≈0.127).
- 13.4 Excel: BINOM.DIST(number,trials,probability,cumulative), POISSON.DIST(x,mean,cumulative), HYPGEOM.DIST(sample_s, number_sample, population_s, number_pop, cumulative), NORM.DIST(x,mean,standard_dev,cumulative), NORM.S.DIST(z,cumulative).
- 13.5 career/R resources (non-technical). Progress check: data collection methods; qual vs quant; examples; R lists; plot ln(x); datasets.
## Ch14 EDA (mth_notes_c lines 1-560)
- Qualitative: Ex14.1 MTH4107 2018 grades (207 students): A124 B37 C23 D8 E4 F11 (ordinal). Frequency distribution; relative frequency = freq/total; relative frequency distribution (Ex14.2 /207). Bar chart: barplot(x,names.arg=grade); x/sum(x). Fig14.1.
- Quantitative discrete: Ex14.3 failing marks 26,35,23,32,35,33,39,32,25,38,34 (n=11); hist(x,breaks=seq(22.5,39.5,1)). Shapes: symmetric, unimodal, multimodal, skewed right, skewed left (Fig 14.3).
- 14.2 sample mean x̄=(1/n)Σxk. Order statistic; median Q2 = x_{(n+1)/2} (n odd) or average of x_{n/2},x_{n/2+1} (even). Ex14.4 sorted 23,25,26,32,32,33,34,35,35,38,39: median 33, mean 32. Symmetric x̄=Q2; skewed left x̄<Q2; skewed right x̄>Q2.
- Population variance σ_x²=(1/n)Σ(xk−x̄)²; sample variance s²=(1/(n−1))Σ(xk−x̄)² (unbiased); var(x), sd(x). Quartiles: Q1 median of lower half, Q3 of upper half (exclude median if n odd). Ex14.5 Q1=26, Q3=35; quantile(x,probs=0.25,type=2) (nine definitions!). Fig14.4. IQR=Q3−Q1; IQR(x,type=2). Ex14.6 var=27.4, sd=5.234501, IQR=9 (≈ twice sd).
- Five-number summary (min,Q1,Q2,Q3,max); summary(x,quantile.type=2): 23 26 33 32(mean) 35 39. Boxplot: box over [Q1,Q3], line at median, whiskers to min/max; R boxplot uses different quartile def (Tukey hinges: 29 and 35 for this data) — Fig 14.5 caption says "Q3 = 33... Q1 = 29" [typo: Q3=35]. Outliers shown.
- 14.3 univariate vs multivariate/bivariate. Ex14.8 Calc I vs Int Prob marks 29 students (x: 62,84,18,64,88,69,66,69,73,84,95,82,68,91,65,100,83,95,91,82,44,83,45,82,93,74,73,91,14; y: 84,73,47,74,64,86,88,76,76,79,98,85,72,81,93,91,90,89,95,77,91,75,62,90,61,77,69,65,49). Scatter plot plot(x,y,xlab,ylab) Fig14.6 minor positive correlation.
- Sample covariance s_xy=(1/(n−1))Σ(xk−x̄)(yk−ȳ); sample correlation r=s_xy/(s_x s_y); −1≤r≤1; r=1 if y=ax+b a>0; −1 if a<0 [notes says "positive slope a<0" typo]. Cauchy–Schwarz. Ex14.10 cor(x,y)=0.5281328. Correlation ≠ causation; significance later.
- Progress check: Likert data — which summaries make sense (median, IQR yes; mean/sd questionable).
## Ch15 Sampling distributions
- Ex15.1 average height British: census vs survey n=10,000; data as realisation of i.i.d. X1..Xn; X̄ random variable. Independence: sampling with replacement or infinite population; w/o replacement need N≫n (hypergeometric vs binomial).
- Sample mean X̄ = estimator for µ; x̄ = point estimate. Def6 statistic = real function g(X1..Xn).
- Prop15.1 E(X̄)=µ, Var(X̄)=σ²/n (linearity; independence). Sampling distribution = distribution of X̄. CLT ⇒ X̄≈N(µ,σ²/n) for large n regardless of population shape.
- Ex15.2 Int Prob 2019: µ=70.21, σ²=380.27, n=10: P(X̄≤65.21)=Φ(−5/√38.027)=0.2087 (one in five). Ex15.3 need n>(−Φ^{−1}(0.05))²σ²/5² = 41.15 ⇒ n≥42 (qnorm(0.05)≈−1.645); critical note about independence/population size.
- Ex15.4 proportion of home owners: Bernoulli indicators; sample proportion X̄; E=p, Var=p(1−p)/n; unbiased.
- Ex15.5 Calc I 2019 41.4% A grades, n=15: P(X̄>0.5)=1−Φ((0.5−0.414)/√(0.414·0.586/15))=0.249447.
- Conditions: Independence: n ≤ 0.05N (5% rule) when sampling w/o replacement. Normality: normal population ⇒ any n (Prop11.2); Bernoulli: np(1−p)>10; general: n>20 often OK.
- 15.2 Def7 unbiased: E(g(X1..Xn))=θ. X̄ unbiased for µ; sample proportion unbiased for p. Naive Σ²=(1/n)Σ(Xk−X̄)² = (1/n)ΣXk²−X̄² biased: Lemma3 E(Σ²)=((n−1)/n)σ² [notes write σ for variance: typo]. Proof: E(Xk²)=σ²+µ², E(X̄²)=σ²/n+µ². Unbiased S²=(1/(n−1))Σ(Xk−X̄)² [notes miss square].
- 15.3 MSE: Def8 MSE_g=E((g−θ)²); unbiased ⇒ MSE=Var(g). X1 alone is unbiased but Var σ² vs σ²/n ⇒ X̄ better.
- 15.4 Simulation: pseudorandom numbers. Ex15.6 rhyper(200,30,20,15) (bag 50: 20 red 30 blue pick 15): mean 9.085, var 2.701 vs E=9, Var=18/7≈2.571; hist(x,freq=FALSE,breaks=seq(-0.5,15.5,1)); lines(0:15,dhyper(0:15,30,20,15),type="p"); Fig15.1 (200 vs 5000). Ex15.7 rexp(500,0.4): mean 2.354746, var 6.160399 vs 2.5, 6.25; Fig15.2. Ex15.8 Poisson λ=4, n=50: mean(rpois(50,lambda=4)); replicate(1000,mean(rpois(n=50,lambda=4))); X̄≈N(4, λ/n=4/50=2/25); Fig15.3.
- Progress check Q7: three heads, X tails: rnbinom(20,3,0.5).
## Ch16 Confidence intervals
- Ex16.1 MTH4107 2018 sample marks 63,43,41,59,49,54,74,17,67,92: x̄=55.9; population variance 248.58.
- 16.1 known σ: P(|X̄−µ|<δ)=1−α ⇒ δ=σ_X̄ z_{α/2}, z_{α/2}=Φ^{−1}(1−α/2). CI [x̄ − (σ/√n) z_{α/2}, x̄ + (σ/√n) z_{α/2}]; confidence level 1−α = fraction of all possible samples whose intervals contain µ. NOT "µ in interval with probability 1−α" — statement about the procedure/sample statistic. Check independence & normality.
- Ex16.2 σ_X̄²=24.858; z=1.959964; CI [46.12805, 65.67195] ≈[46,66].
- Unknown σ: use s² if n large (more sophisticated theory — t — beyond first year). Ex16.3 var(x)=418.5444 ⇒ CI [43.22001, 68.57999] (differs; n too small).
- 16.2 proportion CI: [x̄ ± z_{α/2} √(x̄(1−x̄)/n)] (replace p by x̄).
- Ex16.4 2017 Int Prob 15 marks 79,75,70,26,88,32,83,69,46,50,69,37,72,76,49 → A grades (≥70) 1,1,1,0,1,0,1,0,0,0,0,0,1,1,0: x̄=0.4666667 (7/15); σ²≈x̄(1−x̄)=0.2488889 (var(x)=0.2666667); σ_X̄²=0.01659259; 95% CI [0.2141993, 0.719134]; 99% z=2.575829 → [0.1348683, 0.798465] wider. Higher confidence ⇒ wider interval.
- Sample size for half-width δ: δ=z_{α/2}√(p(1−p)/n) ⇒ n=p(1−p)z²/δ²; p(1−p)≤1/4 ⇒ n ≥ z²/(4δ²). **SOURCE ERROR**: notes write n ≤ (1/4)Φ^{−1}(1−α/2)/δ² and compute 1/4*qnorm(0.975)/0.1^2 = 48.9991 ⇒ "49 students": the z should be SQUARED and inequality is n ≥: correct n ≥ 1.96²/(4·0.01) = 96.04 ⇒ 97. (With p̂=7/15: 0.2489·3.8415/0.01 = 95.6 ⇒ 96.) Flag in textbook.
- Progress check: point vs interval estimate; what's needed for 95% CI; meaning; 99% CI; dependence on n (width ∝ 1/√n); 95% vs 99% (95% narrower); conditions.
## Ch17 Hypothesis testing
- Ex17.1 fair coin 10000 tosses. Def9 hypothesis = statement about parameter θ of pmf/pdf. Ex17.2 cannot confirm (tiny bias p=0.50000000001); find evidence AGAINST; reject ("nullify") or not reject (not "accept").
- Def10 null hypothesis H0: θ=θ0. Ex17.3 do not reject if X∈[4900,5100]: P(reject|H0)=1−pbinom(5100,10000,.5)+pbinom(4899,10000,.5)=0.0444258 → type-I error, significance level.
- Def11 type-I error: reject valid H0; its probability = significance level α. Def12 alternative H1. Two-sided test (p≠1/2). Ex17.4 H1: p<1/2, reject if X<4900: α=pbinom(4899,...)=0.0222129 (left-tailed) [notes typo "If X≥4800" → 4900].
- Remark: H1 θ≠θ0 two-sided; θ>θ0 right-tailed; θ<θ0 left-tailed. Fig17.1 rejection regions shaded area α.
- Type-II error: fail to reject false H0. Ex17.5 p=0.48: β=P(4900≤X≤5100)=0.02322684. Def13 β, power 1−β (w.r.t. alternative θ1). Table17.1 (do not reject & H0 valid: correct; not reject & H0 invalid: type II; reject & H0 valid: type I; reject & invalid: correct).
- Ex17.6 do not reject if X∈[4950,5050]: α=0.3124952 [notes typo P(X≤5051)]; β(p=0.48)=0.001387635; power 0.9986 vs 0.9767. Trade-off: increasing α decreases β and vice versa.
- 17.2 proportion test: Ex17.7 QMUL ≥35% A grades; sample 15 with 3 A (20%). Statistic Z=(X̄−p0)/√(p0(1−p0)/n) ~N(0,1) under H0 (uses p0 in SE!). Two-sided: reject if |z|>z_{α/2}. Ex17.8 1994 52% parents; 256/800=0.32: z=−11.32277 vs 1.959964 ⇒ reject (perception changed). Conditions: n small vs population, np0(1−p0)>10.
- Left-tailed: reject if z<−z_α, z_α=Φ^{−1}(1−α). Ex17.9 p0=0.35, x̄=0.2, n=15, α=0.1: z=−1.217997 vs −1.281552 ⇒ do not reject; but np0(1−p0)=3.4<10 — normal approx doubtful.
- Right-tailed: reject if z>z_α. Ex17.10 Gallup April 2009 352/676 adults not enough money in retirement; H0 p=0.5, H1 p>0.5: z=1.076923 vs 1.644854 ⇒ do not reject (x̄=0.520...).
- 17.3 mean test (σ known): Z=(X̄−µ0)/(σ/√n). Ex17.11 target mean 60, x̄=61.4 (2017 data). Two-sided Ex17.12 death row 2002 mean 40.7 sd 9.6; n=32, x̄=38.9: z=−1.06066 vs 1.96 ⇒ do not reject. Left-tailed Ex17.13 hippocampal volume (Am J Psychiatry May 2000) 12 adolescents, µ0=9.02 cm³, σ=0.7, x̄=8.10, α=0.01: z=−4.552819 < −2.326348 ⇒ reject (n small caveat). Right-tailed Ex17.14 σ=19.7, n=15, x̄=61.4: z=0.2752374 < 1.644854 ⇒ do not reject; sample ≈7% of ~200 population.
- 17.4 P-values: Def14 probability (under H0) of sample statistic as or more extreme than observed; reject at level α if P<α. Guide: P>0.1 no evidence; 0.05–0.1 weak; 0.01–0.05 moderate; 0.001–0.01 strong [notes typo "0.001<P<0.1"]; <0.001 overwhelming.
- Proportion P-values: two-sided 2(1−Φ(|x̄−p0|/√(p0(1−p0)/n))); right 1−Φ(z); left Φ(z). Ex17.15 2.1% worked at home 2009; 6/150=0.04: P=0.0523028 ⇒ not reject at 5%, reject at 10% (weak evidence).
- Mean P-values analogous with σ/√n. Ex17.16 P=0.3915669 (no evidence).
- Progress check: teen mothers 10.5% 2007 — H0 p=0.105, H1 p>0.105; type I/II meaning; P=0.15 ⇒ no evidence, do not reject.
## Ch18 Conditional probability
- Ex18.2 die: A odd {1,3,5}, B<4 {1,2,3}: P(B|A)=2/3 = P(A∩B)/P(A). Def18.1 P(E2|E1)=P(E1∩E2)/P(E1), P(E1)≠0. Remarks: E2|E1 not an event; ≠ P(E2\E1); no time order required (secret experiment, E1 revealed); don't assume equally likely.
- Ex18.3 pens blue/red/green, two w/o replacement: P(2nd blue|1st red)=1/2; P(1st red|2nd blue)=1/2.
- 18.2 P(E2|E1)<P(E2) less probable; > more; = independent.
- Ex18.4 two dice: A six first (1/6), B double (1/6), C at least one odd (27/36=3/4): P(B|A)=1/6, P(A|B)=1/6, P(C|B)=1/2, P(B|C)=(3/36)/(3/4)=1/9. P(E1|E2)≠P(E2|E1) in general.
- Ex18.5 (a) P(E1|E2)>P(E1) ⇒ P(E2|E1)>P(E2) (b) P(E1^c|E2)=1−P(E1|E2) (c) nothing in general about P(E1|E2^c).
- 18.3 multiplication rule (18.1) P(E1∩E2)=P(E1)P(E2|E1); Thm18.2 chain rule for n events (proof by induction).
- Ex18.6 coins all gold: 7/10·6/9·5/8·4/7=1/6.
- 18.4 ordered sampling revisited: Ex18.7 w/o replacement P(A)=1/n·1/(n−1)···=(n−r)!/n!; Ex18.8 with replacement 1/n^r.
- Ex18.9 two dice: (a) P(sum≥9)=10/36=5/18 (b) P(first 4|sum≥9)=2/10=1/5 [(4,5),(4,6)] (c) 4/5 (d) P(first 4|sum<9)=4/26=2/13 (e) P(sum≥9|first 4)=2/6=1/3.
- Ex18.10 train A not late 1/2, B late ≤15 1/4, C seat 1/3, P(A∩C)=1/4: (a) P(late>15|late)=(1/4)/(1/2)=1/2 (b) P(C|late)=P(C∩A^c)/P(A^c)=(1/3−1/4)/(1/2)=1/6.
- Ex18.11 Simpson's paradox medical testing as conditional probabilities: P(R|A)=60/160 > P(R|B)=65/230; men P(R|A∩M)=0.2 < P(R|B∩M)=0.238; women 0.667<0.75.
## Ch19 Total probability & Bayes
- Ex19.1 toss thrice partition E1 first head {hhh,hht,hth,htt} [notes typo lists htt twice], E2 {thh,tht}, E3 {tth,ttt}. Def19.1 partition: pairwise disjoint, union S (non-empty not insisted).
- Thm19.2 LTP: P(A)=Σ P(A|Ek)P(Ek) (P(Ek)>0); proof Ak=A∩Ek. "conditioning"; marginal probabilities P(Ek).
- Ex19.2 YouGov 11–16 June 2020, 1088 adults Watford in London: ages 18-24:124 (31%), 25-49:544 (34%), 50-64:247 (15%), 65+:173 (19%): P = (124·.31+544·.34+247·.15+173·.19)/1088 = (38.44+184.96+37.05+32.87)/1088=293.32/1088≈0.2696.
- Thm19.3 conditional LTP: P(A|B)=Σ P(A|B∩Ek)P(Ek|B).
- Ex19.3 magic coins: P(F|H1)=(1/2·1/2)/(5/8)=2/5; P(H2|H1)=1/2·2/5+3/4·3/5=13/20 (uses conditional independence: P(H2|H1∩F)=P(H2|F)). Ex19.4 consistent: (13/32)/(5/8)=13/20 ✓.
- Thm19.4 Bayes P(B|A)=P(A|B)P(B)/P(A) (Thomas Bayes 1702–1761, [Bay63] 1763). Denominator via LTP.
- Ex19.5 disease 0.1%, P(pos|D)=0.99, false positive 0.5%: P(D|P)=990/5985=22/133≈0.1654 (~83% of positives false). Ex19.6* two independent positive tests (cond. indep given D and D^c): P = .99²·.001/(.99²·.001+.005²·.999)=0.00098010/(0.00098010+0.000024975)=0.9752.
- 19.4 axioms → applications. Ex19.7 prosecutor's fallacy: (a) confuses P(F|I) with P(I|F) (b) London 10 million, P(F|I^c)=1: P(I|F)=9999999/(9999999+50000)=0.9950 (c) 100 people access: P(I|F)=99/(99+50000)=0.0020 [note: notes' displayed denominator writes 1/100000000 typo for 1/10000000; final value correct].
- Ex19.9 football two injured recover p each, independent: win prob 2/3 both, 5/12 one, 1/6 neither: P(win)=(2/3)p²+(5/12)·2p(1−p)+(1/6)(1−p)² = ... show p>2/3 ⇒ >1/2. Compute: = (2/3)p² + (5/6)(p−p²) + (1/6)(1−2p+p²) = p²(2/3−5/6+1/6) + p(5/6−1/3) + 1/6 = 0·p² + p/2 + 1/6 → P(win)=p/2+1/6 >1/2 iff p>2/3. 
- Ex19.10 partitions: (a) no (A and B overlap; A,A^c... not disjoint) (b) no unless A∪B=S (c) yes (d) yes (e) no in general (A∩B≠∅).
- Ex19.11 lost key Mimi/Rodolfo: (a) 1/3·3/5+1/3·1/5=4/15 (b) (1/15)/(4/15)=1/4 (c) P(corridor|not found)=(1/3)/(11/15)=5/11.
- Ex19.12* Monty Hall variant with p.
## Ch20 Conditional expectation
- Ex20.1 P(R=r|Y=1): 1/10,3/5,3/10,0 (P(Y=1)=20/35=4/7). Def20.1 conditional pmf P(X=xk|A)=P((X=xk)∩A)/P(A); E(X|A)=Σ xk P(X=xk|A). X|A as RV. Independence ⇒ E(X|Y=y)=E(X).
- Ex20.2 E(R|Y=1)=6/5 < E(R)=9/7.
- Ex20.3 X~Geom(1/3) (E=3); Y|X=n ~Bin(n,1/4): E(Y|X=n)=n/4. Ex20.5* E(Y)=Σ(n/4)P(X=n)=E(X)/4=3/4; E(XY)=Σ n·(n/4)P(X=n)=E(X²)/4; E(X²)=Var+E²=(1−p)/p²+1/p²=(2/3)/(1/9)+9=6+9=15 ⇒ E(XY)=15/4; Cov=15/4−3·3/4=6/4=3/2.
- Thm20.2 law of total expectation E(X)=Σ E(X|Ei)P(Ei) (proof via LTP & swap sums).
- Ex20.4 coin then six-sided (H) or four-sided (T) die: E=7/2·1/2+5/2·1/2=3.
- Ex20.6 Var(X+Y)=VarX+VarY+2Cov. Ex20.7* E(X|A)=10/3 (A at least one odd). Ex20.8* die N then N coin tosses: E(X)=E(N)/2=7/4. Ex20.9* two dice, fair coin or always-tails coin picked at random: P(heads)=1/4: E=1/4·E(product)+3/4·E(sum)=1/4·49/4+3/4·7=49/16+84/16=133/16. Ex20.10** random walk E(Xt)=0, Var(Xt)=t.
- Bibliography: ASV18, Bay63, Ros20, Rot64, Sie88, Tij12, Vig15.
## Normal table (Fig 9.12, part4 p61 image checked): it is a FULL cdf table Φ(z) for z=0.00..3.49 (rows .0 to 3.4, cols .00–.09), e.g. row .4 col .02 = .6628, row 1.7 col .02 = .9573, row 2.3 col .00=.9893, row 1.6 col .00=.9452, row 3.4 col .09=.9998. The notes' TEXT describes a 0-to-z table ("entry 0.1628 → Φ(0.42)=0.6628", "0.4573", "0.4893") — INCONSISTENT with the table actually printed; and "Φ(z)=1 for z≥3.9" refers to a longer table. Flag; teach full-cdf reading + mention the 0-to-z variant.
## Appendix A Errata (lecture notes): [Page 55] H corrected to read H1 below (6.5); [Page 55] P corrected to read P in first line of argument for P(H2|H1∩F). (These refer to an earlier ordering where conditional chapter was p55; trivial.)
## Exam info gleaned: Ch7.2 "For an open-book exam, memorising the notes word-by-word is especially pointless" (exam format unclear — check study guides). Past exam questions cited: 2018 (Ex2.6 buses; Ex20.3/20.5 geometric-binomial), 2016 (Ex8.11 typos).

# STUDY GUIDE 1: "Weeks 8–12 Exam-Focused Study Guide" (part1 p1-36; mth_sg_w8_12.txt) — secondary, AI-built aid
- Built from lecture notes Ch5,6,8,9,10,11 + user's "revision sheet: Applied Probability and Statistics Weeks 8–12" (that sheet itself NOT in the 5 PDFs — maybe in parts 6–8). So "Weeks 8–12" = Ch5,6,8,9,10,11 (Semester A second half). Priority labels CORE/IMPORTANT/SUPPORTING/EXAMPLE/NOT ON SHEET.
- Revision sheet errors found (E1–E10): E1 Exp mean/var given as λ, λ² (correct 1/λ, 1/λ²); E2 normal pdf denominator √(2πσ) (correct σ√(2π)); E3 sheet uses N(µ,σ) (sd) vs notes N(µ,σ²) (variance) — use notes convention; CLT sheet N(nµ,σ√n); E4 CLT continuity correction missing on sheet; E5 "Φ(b)=Φ(a)" should be minus; E6 "PDF is derivative of the PDF" → of the CDF; E7 "variance of a constant is a constant" → zero; E8 joint table rows x1,x1,x3 typo; E9 Var(aX+b) labelled Prop 6.7 (is 6.8); E10 uniform cdf only middle piece given.
- Notes' own slips: N1 Z~N(1,0) typo; N2 errata p.209.
- GUIDE CLAIM (WRONG per my check of the image): "the table in your notes is an area-from-0-to-z table, Φ(z)=0.5+entry". Actual Fig 9.12 table has .5000 at z=0 → full Φ table. Inconsistency is between notes' text and printed table. In textbook: teach "check z=0 entry: 0.5000 → Φ table; 0.0000 → 0-to-z table, add 0.5".
- Useful exam-check habits: units/dimensions; push parameter to extremes; probability in [0,1]; mean within range (Prop 6.2); variance ≥0.
- Cheat sheet tables (distributions, algebra with independence column). Decision tree for choosing discrete distribution: one trial → Bernoulli; fixed n with replacement → Bin; without replacement → Hg; until first success → Geom; until r-th success → NB; events in continuous interval → Poisson; waiting time between → Exp; sum of many iid → Normal.
- Concept cards C1–C12 (RV, pmf, expectation (balance-point analogy), variance, linear transformations, named discrete, relations between distributions (Bin(1,p)=Ber; sum of Bernoullis; Hg≈Bin; NB(1,p)=Geom shifted down), continuous & pdf (density can exceed 1: Exp(4) f(0)=4), normal & standardisation, joint/marginals/independence, E adds always/Var only under independence, CLT).
- Compare tables: Bin vs Hg (5 cards from 52 aces → Hg(52,4,5)); Bin vs Geom vs Poisson; discrete vs continuous; pmf vs cdf; independent vs uncorrelated vs disjoint (disjoint events with positive prob are dependent); variance vs sd (σ_{X+Y}=√(σX²+σY²)); Geom vs NB.
- Processes P1 build pmf; P2 E & Var from pmf; P3 joint table (check sum, marginals, independence via zero cell, E(g)); P4 normal probability end to end; P5 CLT end to end; continuity correction table: P(a≤X≤b)→P(a−½≤Y≤b+½); P(X=k)→[k−½,k+½]; P(X≤b)→Y≤b+½; P(X<b)→Y≤b−½; P(X≥a)→Y≥a−½. (Also P(X>a)→Y≥a+½.)
- "If X changes": p→1/2 maximises binomial variance; Exp λ↑ ⇒ mean & var ↓; sum of n: mean ∝ n, sd ∝ √n; average: var σ²/n; ℓ→n in Hg ⇒ Var→0; σ↑ flattens normal.
- Memory hooks: "mean of the square minus the square of the mean"; "shift doesn't spread"; "rate and wait are reciprocals"; "Poisson one parameter one number"; "1/p tries"; "picks times proportion"; "half a step out both ways"; "n for mean, √n for spread".
- Numbers: die 7/2, 35/12; two dice 7, 35/6; P(|X−µ|>σ)=.317; >2σ .0455; 95.4%; z.025=1.96; np(1−p)>10.
- Traps M1–M15 (binomial w/o replacement; overlapping trials Ex8.15; adding variances w/o independence; E(XY)=EXEY ⇏ independent; E f(X) ≠ f(EX); pdf as probability; < vs ≤; table misreading; dividing by variance; continuity correction; CLT w/o replacement; µ of sum vs term; sd add; few cells independence; NB counts failures).
- Active recall R1–R19, U1–U15, A1–A10 (A1 Bin(12,.3): 3.6, 2.52; A2 Hg(20,8,5) mean 2; A3 Poisson(3), e^{−3}=.0498; A4 −11, 6, −73; A5 Exp(.25): 4, e^{−1.5}=.2231; A6 N(70,25): 1−Φ(2)=.0228; A7 200 dice: µ=700, σ²=1750/3≈583.3, P(≥720)≈1−Φ((719.5−700)/24.15)=1−Φ(0.807); A8 var decreases from .25n to .09n; A9 Geom(.02): mean 50, median 35 (k≥ln.5/ln.98=34.3); A10 E(2Y²)=30), C1–C9, I1–I8 with answers.
- Exam-style Q1–Q12 with model answers: Q1 pmf c=3/8, P(X≥1)=1/2, P(X²≤1)=3/4; Q2 E(2X−5)=3, Var=12, E(X²)=19, E(3X²−2X+1)=50; Q3 Bin(30,1/6) E5; Geom(0.05) E20; Hg(25,6,8) E1.92; Q4 explain; Q5 f=kx on[0,4]: k=1/8; P(1≤X≤3)=1/2; F=x²/16; E=8/3; E(X²)=8; Var=8/9; Q6 30 counters 12 red pick 5: Bin(5,.4) mean2 var1.2; Hg(30,12,5) mean 2 var 1.2·25/29≈1.034; Q7 joint U∈{1,2},V∈{0,1,2} rows .10,.20,.10/.15,.30,.15: independent, E(U)=1.6,E(V)=1,E(UV)=1.6,Cov 0; Q8 Poisson(3): P(N=2)=4.5e^{−3}≈.224; P(N≥2)=1−4e^{−3}≈.801; T~Exp(3): E=1/3 min, P(T>1)=e^{−3}=.0498 (=P(N=0)); Q9 N(250,64): σ=8; P(X<260)=Φ(1.25)=.8944; P(242≤X≤260)=.8944−.1587=.7357; reject 4.55%; Q10 150 dice: N(525,437.5), σ≈20.92; P(500≤X≤560)≈Φ(1.70)−Φ(−1.22)=.9554−.1112=.844; Q11 Bernoulli sum derivation; Q12 ones & twos: joint table (16,8,1/8,2,0/1,0,0)/36; V~Bin(2,1/6); dependent (P(2,2)=0); V+W~Bin(2,1/3) var 4/9 vs 5/9; Cov=−1/18.

# STUDY GUIDE 2: "EXAM-FOCUSED STUDY GUIDE (Applied) Probability and Statistics MTH4500/MTH4600 Semesters A & B" (part5 p74-100 = its pp.1–26; CONTINUES in part6: §8 active recall, §9 exam questions, §10 traps, §11 rapid review, §12 "Points where notes need care" (p35), §13–14 answers). Derivative of notes (214 pp, Ch0–20). Labels CORE/IMPORTANT/SUPPORTING/EXAMPLE/EXTRA/ADDITIONAL CONTEXT/FLAG.
- Big picture: Sem A probability (known mechanism → what to expect); Sem B statistics (data → unknown mechanism); hinge = CLT. 8 takeaways. Chapter dependency diagram (Ch18–20 late in notes but early in logic; notes forward-reference conditional probability from Ch4).
- Terminology table (what it is NOT): significance level ≠ P(H0 true); P-value ≠ P(H0|data); unbiased ≠ accurate.
- Cheat sheet sections 2.1–2.13, incl. z-values: z0.05=1.6449, z0.025=1.9600, z0.01=2.3263, z0.005=2.5758; P(|X−µ|<σ)≈68.3%; Φ(z)=1 to 4 dp for z≥3.9.
- FLAG: two different normal tables in 9.3.1 (0-to-z for Φ(0.42); full cdf with negative rows for Ex9.10 Φ(−1.02)=0.1539). FLAG: P-value band typo. 
- R commands table (d/p/q/r; mean, median, var, sd (n−1), quantile type=2, IQR, summary, barplot, hist, plot, boxplot, cor, replicate). R traps: dgeom counts failures; dhyper(k,m,n−m,l); nine quartile definitions.
- Concept cards 1–24 (sample space … EDA). Notable: Monty Hall = trap for equally likely; analogy conditioning = zooming photograph (additional context); CI–test duality (two-sided test rejects θ0 iff outside (1−α) CI) [additional/derived]; "mode is most likely, not expectation"; ordinal data: median & IQR defensible, mean/sd not.
- Compare: independent vs mutually exclusive (P(A∪B)=P(A)+P(B)−P(A)P(B) when independent); pairwise vs mutual; independence vs conditional independence (neither implies other; hidden common cause); Bin vs Hg; Geom vs NB; Bin vs Poisson; pmf/pdf/cdf; σx² vs s²; type I vs II (false alarm vs missed detection); one vs two-sided (1.96, 1.645); CI vs test (variance uses x̄(1−x̄) vs p0(1−p0)).
- Processes: solving any probability question (read/classify, translate, choose tool, compute, check); disjoint-union proof machine table; identify distribution flowchart; normal calcs; CLT; CI; hypothesis test 5 steps ("never accept H0"); binomial mean/var via indicators.
- Relationships: n↑ ⇒ CI narrower ∝1/√n (quadruple n to halve width); confidence↑ ⇒ wider; α↓ ⇒ β↑; only n↑ improves both. Probability vs statistics analogues table (E↔x̄, Var↔s², Cov↔s_xy, Corr↔r, LTP↔stratified estimate).
- Memory: 9 formulas; hooks ("ORU"; "σ over root n"; "1.96 two tails 1.645 one"; "n−1 because x̄ used a degree of freedom" [additional]; "reject or fail to reject"; "small P big surprise"); distribution facts anchored on Bernoulli; Geometric & Exponential memoryless.
