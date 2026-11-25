"""Builds three MA3354 model question papers in the exact Anna University layout,
using only real questions from previous papers (2016-2024). Output: MA3354_Model_Question_Papers.html"""
import os
HERE = os.path.dirname(os.path.abspath(__file__))
FIG = lambda n: f'file://{HERE}/figs/clean_{n}.png'

def mat(rows):  # small bracketed matrix
    body = ''.join('<tr>' + ''.join(f'<td>{c}</td>' for c in r) + '</tr>' for r in rows)
    return f'<span class="mat"><table>{body}</table></span>'
M4 = mat(['0110', '1001', '1001', '0110'])

# Each Part B entry: unit -> {'a': [(sub, text, marks, source)], 'b': [...]}; sub '' = whole question.
PAPERS = [
{
 'name': 'Model Question Paper 1', 'focus': 'Most-repeated questions',
 'A': [
  ('Show that p → q and ¬p ∨ q are equivalent.', '2024 A/M'),
  ('Symbolize the statement “All men are mortal”.', '2022 N/D'),
  ('State the pigeonhole principle.', '2021 N/D, 2023 A/M, 2024 A/M'),
  ('How many different bit strings are there of length 9?', '2023 N/D'),
  ('Does there exist a simple graph with the degree sequence {3, 3, 3, 3, 2}?', '2021 N/D'),
  (f'Draw a graph with the adjacency matrix {M4}.', '2023 A/M'),
  ('Prove that the identity element of a group is unique.', '2019 N/D, 2021 N/D'),
  ('Define a field.', '2023 A/M'),
  ('Draw the Hasse diagram for (D<sub>24</sub>, /), where D<sub>24</sub> = {1, 2, 3, 4, 6, 8, 12, 24}.', '2023 A/M'),
  ('State De Morgan’s law in any Boolean algebra.', '2023 A/M'),
 ],
 'B': {
  11: {'a': [('(i)', 'Show that (¬P ∧ (¬Q ∧ R)) ∨ (Q ∧ R) ∨ (P ∧ R) ⇔ R, without using truth table.', 8, '2016 N/D, 2018 A/M, 2023 A/M, 2024 A/M'),
             ('(ii)', 'Show that the premises “A student in this class has not read the book” and “Everyone in this class passed the first exam” imply the conclusion “Someone who passed the first exam has not read the book”.', 8, '2017 N/D, 2018 N/D, 2019 A/M, 2020 N/D')],
       'b': [('(i)', 'Obtain the principal disjunctive and principal conjunctive normal forms of (¬P → R) ∧ (Q ↔ P).', 8, '2016 M/J, 2017 A/M, 2019 N/D'),
             ('(ii)', 'Using the indirect method, show that (∀x)(P(x) ∨ Q(x)) ⇒ (∀x)P(x) ∨ (∃x)Q(x).', 8, '2018 A/M, 2023 A/M, 2024 A/M')]},
  12: {'a': [('(i)', 'Solve: T(k) − 7T(k − 1) + 10T(k − 2) = 6 + 8k, T(0) = 1, T(1) = 2.', 8, '2016 N/D, 2018 A/M, 2023 A/M'),
             ('(ii)', 'Find the number of integers between 1 and 250 that are not divisible by any of the integers 2, 3, 5 and 7.', 8, '2016 N/D, 2018 A/M')],
       'b': [('(i)', 'Use mathematical induction to show that 1<sup>2</sup> + 2<sup>2</sup> + 3<sup>2</sup> + ⋯ + n<sup>2</sup> = n(n + 1)(2n + 1)/6, whenever n is a positive integer.', 8, '2018 N/D, 2023 A/M'),
             ('(ii)', 'Show that if n is an integer greater than 1, then n can be written as the product of primes.', 8, '2019 A/M, 2020 N/D, 2024 A/M')]},
  13: {'a': [('(i)', 'Prove that the number of vertices of odd degree in a graph G is always even.', 8, '2016 M/J, 2017 A/M, 2021 N/D, 2022 N/D, 2023 A/M'),
             ('(ii)', f'Check whether the graphs are isomorphic or not.<div class="fig"><img src="{FIG("iso_2024AM")}" style="width:62mm"></div>', 8, '2024 A/M')],
       'b': [('(i)', 'If G is a connected simple graph with n vertices, n ≥ 3, such that the degree of every vertex in G is at least n/2, then prove that G has a Hamilton cycle.', 8, '2016 M/J, 2017 A/M, 2020 N/D, 2024 A/M'),
             ('(ii)', f'Find an Euler path or an Euler circuit, if it exists, in each of the following three graphs. If it does not exist, explain why.<div class="fig"><img src="{FIG("euler_2022ND")}" style="width:100mm"></div>', 8, '2022 N/D, 2023 A/M')]},
  14: {'a': [('(i)', 'State and prove Lagrange’s theorem.', 8, '10 papers, 2016–2024'),
             ('(ii)', 'Prove that the kernel of a homomorphism f from a group ⟨G, *⟩ to a group ⟨H, Δ⟩ is a normal subgroup of the group ⟨G, *⟩.', 8, '2016 M/J, 2017 A/M, 2018 A/M, 2019 N/D, 2021 N/D, 2024 A/M')],
       'b': [('(i)', 'Prove that the intersection of two normal subgroups of a group G is again a normal subgroup of G.', 8, '2016 N/D, 2018 A/M, 2018 N/D, 2023 A/M'),
             ('(ii)', 'Prove that every subgroup of a cyclic group is cyclic.', 8, '2016 M/J, 2017 A/M, 2019 A/M, 2024 A/M')]},
  15: {'a': [('(i)', 'Prove that every chain is a distributive lattice.', 8, '8 papers, 2016–2024'),
             ('(ii)', 'In a distributive complemented lattice, show that the following are equivalent: (1) a ≤ b (2) a ∧ b̄ = 0 (3) ā ∨ b = 1 (4) b̄ ≤ ā.', 8, '2016 M/J, 2016 N/D, 2017 A/M, 2017 N/D, 2020 N/D')],
       'b': [('(i)', 'State and prove De Morgan’s laws in any Boolean algebra.', 8, '2016 M/J, 2019 N/D, 2022 N/D, 2023 N/D, 2024 A/M'),
             ('(ii)', 'Let D<sub>30</sub> = {1, 2, 3, 5, 6, 10, 15, 30} with the relation x ≤ y if and only if x divides y. Find (1) all lower bounds of 10 and 15 (2) GLB of 10 and 15 (3) all upper bounds of 10 and 15 (4) LUB of 10 and 15 (5) draw the Hasse diagram for D<sub>30</sub>.', 8, '2018 A/M')]},
 }},
{
 'name': 'Model Question Paper 2', 'focus': 'Next most frequent questions',
 'A': [
  ('Construct the truth table for (¬p) ∨ (¬q).', '2023 A/M'),
  ('Translate the statement “Every real number except zero has a multiplicative inverse” into a statement involving nested quantifiers.', '2024 A/M'),
  ('How many ways are there to select five players from a 10-member tennis team to make a trip to a match at another school?', '2023 A/M'),
  ('Find the first four terms of the sequence defined by the recurrence relation and initial condition a<sub>n</sub> = a<sub>n−1</sub><sup>2</sup>, a<sub>1</sub> = 2.', '2022 N/D'),
  ('Define a complete graph.', '2016 N/D, 2021 N/D, 2023 N/D'),
  ('When is a graph called an Eulerian graph?', '2023 N/D'),
  ('Is the set of integers under ordinary multiplication a group?', '2024 A/M'),
  ('Prove that in any group, the identity element is the only idempotent element.', '2018 A/M, 2018 N/D'),
  ('Show that the “greater than or equal” relation (≥) is a partial ordering on the set of integers.', '2024 A/M'),
  ('Is the poset (Z<sup>+</sup>, |) a lattice?', '2024 A/M'),
 ],
 'B': {
  11: {'a': [('(i)', 'Find the principal disjunctive normal form of p → [(p → q) ∧ ¬(¬q ∨ ¬p)].', 8, '2022 N/D, 2023 N/D'),
             ('(ii)', 'Show that “It rained” is a conclusion obtained from the statements: “If it does not rain or if there is no traffic dislocation, then the sports day will be held and the cultural programme will go on”, “If the sports day is held, the trophy will be awarded” and “The trophy was not awarded”.', 8, '2016 M/J, 2019 N/D, 2020 N/D')],
       'b': [('(i)', 'Using the indirect method, show that R → ¬Q, R ∨ S, S → ¬Q, P → Q ⇒ ¬P.', 8, '2019 A/M, 2020 N/D'),
             ('(ii)', 'Show that the following argument is valid: “Every microcomputer has a serial interface port. Some microcomputers have a parallel port. Therefore some microcomputers have both serial interface port and parallel port”.', 8, '2023 A/M')]},
  12: {'a': [('(i)', 'Use generating functions to solve the recurrence relation a<sub>n</sub> − 2a<sub>n−1</sub> − 3a<sub>n−2</sub> = 0, n ≥ 2, with a<sub>0</sub> = 3, a<sub>1</sub> = 1.', 8, '2022 N/D'),
             ('(ii)', 'Determine the number of positive integers n, 1 ≤ n ≤ 2000, that are not divisible by 2, 3 or 5 but are divisible by 7.', 8, '2019 A/M, 2020 N/D')],
       'b': [('(i)', 'Use mathematical induction to prove that 3<sup>n</sup> + 7<sup>n</sup> − 2 is divisible by 8, for n ≥ 1.', 8, '2023 N/D'),
             ('(ii)', 'There are six men and five women in a room. Find the number of ways four persons can be drawn from the room if (1) they can be male or female, (2) two must be men and two women, (3) they must all be of the same sex.', 8, '2016 M/J, 2017 A/M')]},
  13: {'a': [('(i)', 'State and prove the handshaking theorem. Hence prove that for any simple graph G with n vertices, the number of edges of G is less than or equal to n(n − 1)/2.', 8, '2016 N/D, 2018 A/M, 2020 N/D, 2022 N/D'),
             ('(ii)', f'Determine whether the following pairs of graphs G<sub>1</sub> and G<sub>2</sub> are isomorphic.<div class="fig"><img src="{FIG("iso_2023AM")}" style="width:52mm"></div>', 8, '2023 A/M')],
       'b': [('(i)', 'Prove that the maximum number of edges in a simple disconnected graph G with n vertices and k components is (n − k)(n − k + 1)/2.', 8, '2017 N/D, 2023 N/D'),
             ('(ii)', 'Define a self-complementary graph. Show that if G is a self-complementary simple graph with n vertices, then n ≡ 0 or 1 (mod 4).', 8, '2016 M/J, 2019 N/D, 2020 N/D')]},
  14: {'a': [('(i)', 'Let f : (G, *) → (G′, Δ) be a group homomorphism. Then prove that (1) [f(a)]<sup>−1</sup> = f(a<sup>−1</sup>) for all a ∈ G, (2) f(e) is the identity of G′, when e is the identity of G.', 8, '2016 N/D, 2020 N/D, 2021 N/D'),
             ('(ii)', 'Show that (Q<sup>+</sup>, *) is an abelian group, where * is defined by a * b = ab/2, for all a, b ∈ Q<sup>+</sup>.', 8, '2016 N/D, 2018 A/M')],
       'b': [('(i)', 'Prove that a subgroup H of G is normal in G if and only if xHx<sup>−1</sup> ⊆ H for all x in G.', 8, '2024 A/M'),
             ('(ii)', 'Show that the set Z<sub>4</sub> = {0, 1, 2, 3} is a commutative ring with respect to the binary operations addition modulo 4 (+<sub>4</sub>) and multiplication modulo 4 (×<sub>4</sub>).', 8, '2022 N/D')]},
  15: {'a': [('(i)', 'Let (L, ≤) be a lattice in which ∧ and ∨ denote the operations of meet and join respectively. For any a, b ∈ L, prove that a ≤ b ⇔ a ∧ b = a ⇔ a ∨ b = b.', 8, '2017 N/D, 2021 N/D, 2023 A/M'),
             ('(ii)', f'Determine whether the following partial ordering sets with the Hasse diagrams are lattices.<div class="fig"><img src="{FIG("hasse_2023AM")}" style="width:84mm"></div>', 8, '2023 A/M')],
       'b': [('(i)', 'In a complemented and distributive lattice, prove that the complement of each element is unique.', 8, '2016 N/D, 2018 A/M, 2020 N/D'),
             ('(ii)', 'State and prove the distributive inequalities in lattices.', 8, '2018 N/D, 2019 A/M, 2020 N/D')]},
 }},
{
 'name': 'Model Question Paper 3', 'focus': '“Due” topics and R2021-style questions',
 'A': [
  ('Prove that (p → (p ∨ q)) is a tautology.', '2022 N/D'),
  ('Write the symbolic form of the statement “The automated reply cannot be sent when the file system is full”.', '2023 N/D'),
  ('Among 200 people, how many of them were born in the same month?', '2022 N/D'),
  ('Determine n if P(n, 2) = 72.', '2023 N/D'),
  ('Define the pseudograph with an example.', '2022 N/D'),
  ('Give an example of a graph which is Eulerian but not Hamiltonian.', '2017 N/D, 2019 N/D'),
  ('Define monoid.', '2022 N/D'),
  ('Given G = {1, −1, i, −i} be a group and H = {−1, 1} be a subgroup of G. Find the index of H in G.', '2023 N/D'),
  ('Draw the Hasse diagram of (D<sub>20</sub>, /), where D<sub>20</sub> denotes the set of positive divisors of 20 and / is the relation “division”.', '2019 N/D'),
  ('Prove that (a′)′ = a, for all a ∈ B, where B is a Boolean algebra.', '2023 N/D'),
 ],
 'B': {
  11: {'a': [('(i)', 'Construct the truth table for the statement ¬(p ∨ (q ∧ r)) ↔ ((p ∨ q) ∧ (p ∨ r)).', 8, '2023 N/D'),
             ('(ii)', '“If there was a ball game, then travelling was difficult. If they arrived on time, then travelling was not difficult. They arrived on time. Therefore, there was no ball game”. Show that these statements constitute a valid argument.', 8, '2023 N/D')],
       'b': [('(i)', 'Prove that if n = ab, where a and b are positive integers, then a ≤ √n or b ≤ √n.', 8, '2020 N/D, 2024 A/M'),
             ('(ii)', 'Use the indirect method to prove that the conclusion ∃z Q(z) follows from the premises ∀x(P(x) → Q(x)) and ∃y P(y).', 8, '2023 N/D')]},
  12: {'a': [('(i)', 'Use generating functions to solve the recurrence relation a<sub>n</sub> = 3a<sub>n−1</sub> + 1, n ≥ 1, with a<sub>0</sub> = 1.', 8, '2023 N/D'),
             ('(ii)', 'In a survey of 100 students, it was found that 40 studied Mathematics, 64 studied Physics, 35 studied Chemistry, 1 studied all the three subjects, 25 studied Mathematics and Physics, 3 studied Mathematics and Chemistry, 20 studied Physics and Chemistry. Use the principle of inclusion and exclusion to find the number of students who studied Chemistry only and the number who studied none of these subjects.', 8, '2023 A/M')],
       'b': [('(i)', 'Prove that n<sup>3</sup> − n is divisible by 3 for n ≥ 1.', 8, '2018 A/M, 2021 N/D'),
             ('(ii)', 'Solve s(n + 2) − 5s(n + 1) + 6s(n) = 0 for n ≥ 0 with s(0) = 1, s(1) = 1.', 8, '2024 A/M')]},
  13: {'a': [('(i)', 'Prove that a simple connected graph is bipartite if and only if it contains no odd cycle.', 8, '2017 N/D, 2024 A/M'),
             ('(ii)', 'Prove that a connected graph G is an Euler graph if and only if all vertices of G are of even degree.', 8, '2018 A/M, 2019 N/D')],
       'b': [('(i)', 'Prove that there is a simple path between every pair of distinct vertices of a connected undirected graph.', 8, '2023 A/M'),
             ('(ii)', 'Show that the complete bipartite graph K<sub>m,n</sub>, with m, n ≥ 2, is Hamiltonian if and only if m = n. Also show that the complete graph K<sub>n</sub> is Hamiltonian for all n ≥ 3.', 8, '2019 A/M')]},
  14: {'a': [('(i)', 'Show that any two right (left) cosets of H in G are either disjoint or identical.', 8, '2017 N/D, 2023 A/M'),
             ('(ii)', 'If (G, *) is a group, prove that (a * b)<sup>−1</sup> = b<sup>−1</sup> * a<sup>−1</sup> for all a, b ∈ G.', 8, '2016 M/J, 2023 N/D')],
       'b': [('', 'Show that (Z, ⊕, ⊙) is a commutative ring with identity, where the operations ⊕ and ⊙ are defined, for any a, b ∈ Z, as a ⊕ b = a + b − 1 and a ⊙ b = a + b − ab.', 16, '2023 N/D')]},
  15: {'a': [('(i)', 'Let (L, ≤) be a lattice and a, b, c, d ∈ L. If a ≤ c and b ≤ d, then prove that (1) a ∨ b ≤ c ∨ d (2) a ∧ b ≤ c ∧ d.', 8, '2019 A/M, 2023 N/D'),
             ('(ii)', 'Let D<sub>100</sub> = {1, 2, 4, 5, 10, 20, 25, 50, 100} be the divisors of 100. Draw the Hasse diagram of (D<sub>100</sub>, /), where / is the relation “division”. Find (I) glb {10, 20} (II) lub {10, 20} (III) glb {5, 10, 20, 25} (IV) lub {5, 10, 20, 25}.', 8, '2019 N/D')],
       'b': [('(i)', 'Define a modular lattice and prove that every distributive lattice is modular but not conversely.', 8, '2016 M/J, 2019 A/M, 2019 N/D'),
             ('(ii)', 'If a, b ∈ S = {1, 2, 4, 8, 16} and a ∨ b = lcm of {a, b}, a ∧ b = gcd of {a, b} and a′ = 16/a, then show that {S, ∨, ∧, ′, 1, 16} is not a Boolean algebra.', 8, '2023 N/D')]},
 }},
]

def header(i, p):
    boxes = ''.join('<span></span>' for _ in range(12))
    return f"""
<div class="reg">Reg. No. : <span class="boxes">{boxes}</span></div>
<div class="qpc">Model Question Paper : {i}</div>
<div class="c">B.E./B.Tech. DEGREE EXAMINATIONS — MODEL PAPER</div>
<div class="c">Third Semester</div>
<div class="c">Computer Science and Engineering</div>
<div class="c b">MA 3354 — DISCRETE MATHEMATICS</div>
<div class="c sm">(Common to Computer Science and Engineering (Artificial Intelligence and Machine Learning)/Computer Science and Engineering (Cyber Security)/Computer and Communication Engineering/Artificial Intelligence and Data Science/Computer Science and Business Systems/Information Technology)</div>
<div class="c">(Regulations 2021)</div>
<div class="tm"><span>Time : Three hours</span><span>Maximum : 100 marks</span></div>
<div class="c">Answer ALL questions.</div>
<div class="c part">PART A — (10 × 2 = 20 marks)</div>"""

def paper_html(i, p):
    a = ''.join(f'<div class="pa"><span class="no">{k+1}.</span><span class="tx">{t}</span></div>' for k, (t, s) in enumerate(p['A']))
    rows = []
    for q in range(11, 16):
        for side in ('a', 'b'):
            for j, (sub, text, marks, src) in enumerate(p['B'][q][side]):
                qno = f'{q}.' if side == 'a' and j == 0 else ''
                ab = f'({side})' if j == 0 else ''
                rows.append(f'<div class="pb{" first" if qno else ""}"><span class="q">{qno}</span><span class="ab">{ab}</span>'
                            f'<span class="sub">{sub}</span><span class="tx">{text}</span><span class="mk">({marks})</span></div>')
            if side == 'a': rows.append('<div class="or">Or</div>')
    return (f'<div class="paper">{header(i, p)}{a}<div class="c part">PART B — (5 × 16 = 80 marks)</div>'
            + ''.join(rows) + '<div class="endline"></div></div>')

def sources_html():
    out = ['<div class="paper src"><h2>Where each question came from</h2>'
           '<p>Every question in these model papers is a real question from a previous Anna University paper '
           '(MA3354 R2021, MA8351 R2017 or MA6566 R2013). Sessions: M/J = May/June, A/M = April/May, N/D = Nov/Dec.</p>']
    for i, p in enumerate(PAPERS, 1):
        out.append(f'<h3>{p["name"]} — {p["focus"]}</h3><table><tr><th>Q</th><th>Seen in</th><th>Q</th><th>Seen in</th></tr>')
        cells = [(f'A{k+1}', s) for k, (t, s) in enumerate(p['A'])]
        for q in range(11, 16):
            for side in ('a', 'b'):
                for sub, text, marks, src in p['B'][q][side]:
                    cells.append((f'{q}({side}){sub}', src))
        half = (len(cells) + 1) // 2
        for l, r in zip(cells[:half], cells[half:] + [('', '')]):
            out.append(f'<tr><td class="k">{l[0]}</td><td>{l[1]}</td><td class="k">{r[0]}</td><td>{r[1]}</td></tr>')
        out.append('</table>')
    out.append('</div>')
    return ''.join(out)

CSS = """
@page { size: A4; margin: 16mm 19mm 18mm 19mm; }
body { font-family: 'C059', 'Century Schoolbook L', 'DejaVu Serif', serif; font-size: 11.3pt; line-height: 1.42; color: #000; margin: 0; }
sub, sup { font-size: 70%; line-height: 0; }
.paper { break-after: page; }
.reg { text-align: right; font-weight: bold; font-size: 10.5pt; margin: 2mm 0 5mm; }
.boxes { display: inline-flex; vertical-align: middle; border: 0.8pt solid #000; }
.boxes span { width: 6.2mm; height: 6.2mm; border-right: 0.8pt solid #000; }
.boxes span:last-child { border-right: none; }
.qpc { width: fit-content; margin: 0 auto 6mm; border: 1.2pt solid #000; padding: 2.5mm 7mm; font-size: 15pt; font-weight: bold;
       box-shadow: 2pt 2pt 0 #000; }
.c { text-align: center; margin: 1.6mm 0; }
.b { font-weight: normal; letter-spacing: 0.2pt; }
.sm { font-size: 10.3pt; margin: 2mm 6mm; }
.tm { display: flex; justify-content: space-between; margin: 4mm 0 2mm; }
.part { margin: 4mm 0 3mm; }
.pa { display: flex; margin: 0 0 3.2mm; break-inside: avoid; }
.pa .no { width: 9mm; flex: none; }
.pa:has(.mat) { align-items: center; }
.pa .tx { flex: 1; text-align: justify; }
.pb { display: flex; margin: 0 0 2.6mm; break-inside: avoid; }
.pb.first { margin-top: 4mm; }
.pb .q { width: 9mm; flex: none; }
.pb .ab { width: 9mm; flex: none; }
.pb .sub { width: 9mm; flex: none; }
.pb .tx { flex: 1; text-align: justify; padding-right: 3mm; }
.pb .mk { width: 9mm; flex: none; text-align: right; align-self: flex-end; }
.or { text-align: center; margin: 1mm 0 2.6mm 18mm; break-after: avoid; }
.fig { margin: 2.5mm 0 1mm; text-align: center; }
.fig img { max-width: 100%; }
.mat { display: inline-block; vertical-align: middle; border-left: 1pt solid #000; border-right: 1pt solid #000; border-radius: 2pt; padding: 0 2pt; margin: 0 2pt; }
.mat table { border-collapse: collapse; } .mat td { padding: 0 3pt; font-size: 10pt; line-height: 1.25; }
.endline { width: 40mm; border-top: 0.8pt solid #000; margin: 8mm auto 0; }
.src { font-family: 'DejaVu Sans', sans-serif; font-size: 9pt; }
.src h2 { font-size: 15pt; margin: 0 0 3mm; } .src h3 { font-size: 11pt; margin: 6mm 0 2mm; }
.src table { width: 100%; border-collapse: collapse; } .src th, .src td { text-align: left; border-bottom: 0.5pt solid #ccc; padding: 1.4mm 2mm; vertical-align: top; }
.src td.k { white-space: nowrap; font-weight: bold; width: 18mm; }
"""

H = ('<!doctype html><html><head><meta charset="utf-8"><title>MA3354 Discrete Mathematics — Model Question Papers</title>'
     f'<style>{CSS}</style></head><body>' + ''.join(paper_html(i, p) for i, p in enumerate(PAPERS, 1)) + sources_html() + '</body></html>')
out = os.path.join(HERE, 'MA3354_Model_Question_Papers.html')
open(out, 'w', encoding='utf-8').write(H); print(out)
