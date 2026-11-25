"""Builds MA3354_Exam_Pattern_Analysis.html (render to PDF with to_pdf.js / build.sh)."""
import sys, os, html
from collections import defaultdict
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'analysis')); sys.path.insert(0, HERE)
from papers import P, SKILL
from questions import U, PART_A

# ---------------------------------------------------------------- links to the papers
REPO = os.environ.get('REPO_URL', 'https://github.com/OWNER/REPO').rstrip('/')
FILES = {  # session label -> (regulation, path under question-papers/, QP code)
 '2016 M/J': ('R2013 · MA6566', 'R2013_MA6566/MA6566_2016_May-Jun_QP57517.pdf', '57517'),
 '2016 N/D': ('R2013 · MA6566', 'R2013_MA6566/MA6566_2016_Nov-Dec_QP80615.pdf', '80615'),
 '2017 A/M': ('R2013 · MA6566', 'R2013_MA6566/MA6566_2017_Apr-May_QP72078.pdf', '72078'),
 '2017 N/D': ('R2013 · MA6566', 'R2013_MA6566/MA6566_2017_Nov-Dec_QP50789.pdf', '50789'),
 '2018 A/M': ('R2013 · MA6566', 'R2013_MA6566/MA6566_2018_Apr-May_QP41320.pdf', '41320'),
 '2018 N/D': ('R2017 · MA8351', 'R2017_MA8351/MA8351_2018_Nov-Dec_QP25139.pdf', '25139'),
 '2019 A/M': ('R2017 · MA8351', 'R2017_MA8351/MA8351_2019_Apr-May_QP80212.pdf', '80212'),
 '2019 N/D': ('R2017 · MA8351', 'R2017_MA8351/MA8351_2019_Nov-Dec_QP90336.pdf', '90336'),
 '2020 N/D': ('R2017 · MA8351', 'R2017_MA8351/MA8351_2020_Nov-Dec_QPX10657.pdf', 'X10657'),
 '2021 N/D': ('R2017 · MA8351', 'R2017_MA8351/MA8351_2021_Nov-Dec_QP40784.pdf', '40784'),
 '2022 N/D': ('R2021 · MA3354', 'R2021_MA3354/MA3354_2022_Nov-Dec_QP70141.pdf', '70141'),
 '2023 A/M': ('R2021 · MA3354', 'R2021_MA3354/MA3354_2023_Apr-May_QP30243.pdf', '30243'),
 '2023 N/D': ('R2021 · MA3354', 'R2021_MA3354/MA3354_2023_Nov-Dec_QP21282.pdf', '21282'),
 '2024 A/M': ('R2021 · MA3354', 'R2021_MA3354/MA3354_2024_Apr-May_QP51325.pdf', '51325'),
}
FULL = {'M/J': 'May/June', 'A/M': 'April/May', 'N/D': 'Nov/Dec'}
def purl(s): return f'{REPO}/blob/main/question-papers/{FILES[s][1]}'
def chips(seen):
    return ''.join(f'<a class="chip{" r21c" if s >= "2022" else ""}" href="{purl(s)}">{s}</a>' for s in seen)

# ---------------------------------------------------------------- skill display names
NAME = {
 'U1 PDNF/PCNF': 'PDNF / PCNF',
 'U1 Equivalence/tautology without truth table': 'Equivalence & tautology without truth table',
 'U1 Rules of inference (indirect, CP, quantifiers)': 'Rules of inference (indirect, CP rule, quantifiers)',
 'U1 Proof methods & quantifier translation': 'Proof methods',
 'U2 Induction (incl. product of primes)': 'Mathematical induction',
 'U2 Recurrence relations (generating fn + characteristic eq.)': 'Recurrence relations',
 'U2 Inclusion-Exclusion': 'Inclusion–exclusion',
 'U2 Permutation/Combination/Pigeonhole': 'Permutations, combinations, pigeonhole',
 'U3 Isomorphism': 'Graph isomorphism',
 'U3 Handshake/odd-degree + max-edge theorems': 'Handshaking & maximum-edge theorems',
 'U3 Euler (theorem + find path/circuit)': 'Euler paths & circuits',
 'U3 Hamiltonian (Dirac n/2, K_mn)': 'Hamiltonian graphs (Dirac)',
 'U3 Self-complementary n≡0,1 mod 4': 'Self-complementary graphs',
 'U3 Bipartite iff no odd cycle': 'Bipartite graphs',
 'U3 A^r walks theorem': 'Walks and powers of A',
 'U4 Lagrange & cosets': "Lagrange's theorem & cosets",
 'U4 Homomorphism (kernel normal, preserves e & inverse)': 'Homomorphisms & kernel',
 'U4 Normal subgroup (intersection, coset/xHx^-1 criteria)': 'Normal subgroups',
 'U4 Cyclic (subgroup cyclic, generators)': 'Cyclic groups',
 'U4 Prove a given set is a group/abelian': 'Prove a set is a group',
 'U4 Ring problems': 'Rings',
 'U5 Every chain is distributive': 'Every chain is distributive',
 'U5 De Morgan in Boolean algebra': "De Morgan's laws in Boolean algebra",
 "U5 a≤b ⇔ a∧b'=0 ⇔ a'∨b=1 ⇔ b'≤a' / a≤b⇔a∧b=a": 'a ≤ b equivalences',
 'U5 Hasse diagram problems (D_n, lub/glb, is-it-a-lattice)': 'Hasse diagram problems',
 'U5 Distributive inequalities / isotonicity': 'Distributive inequalities',
 'U5 Complement unique + cancellation law': 'Unique complement & cancellation',
 'U5 Modular lattice': 'Modular lattices',
 'U5 Prove a relation is a poset': 'Prove a relation is a poset',
}
def nm(s): return html.escape(NAME.get(s, s[3:]))
def unit_of(s): return 'Unit ' + ['I', 'II', 'III', 'IV', 'V'][int(s[1]) - 1]

# ---------------------------------------------------------------- statistics
papers = list(P)
def score(p, S):
    return sum(max(sum(m for c, m in side if SKILL[c] in S) for side in q.values()) for q in P[p].values())
freq = defaultdict(set)
for p in papers:
    for q in P[p].values():
        for side in q.values():
            for c, m in side: freq[SKILL[c]].add(p)
skills = [s for s in freq if 'other' not in s]
r21 = [p for p in papers if 'R21' in p]

order = []
while len(order) < 15:
    order.append(max((s for s in skills if s not in order), key=lambda s: sum(score(p, order + [s]) for p in papers)))
greedy = []
for i in range(len(order)):
    S = order[:i+1]; sc = [score(p, S) for p in papers]
    greedy.append((i+1, order[i], sum(sc)/len(sc), min(sc), [score(p, S) for p in r21]))
top10 = greedy[9]

train = [p for p in papers if 'R21' not in p]
ftr = defaultdict(int)
for p in train:
    for s in {SKILL[c] for q in P[p].values() for side in q.values() for c, m in side}: ftr[s] += 1
rank = [s for s in sorted(ftr, key=lambda s: (-ftr[s], s)) if 'other' not in s]
oos = [(k, [score(p, rank[:k]) for p in r21]) for k in (6, 8, 10, 12, 15)]

# ---------------------------------------------------------------- html helpers
def badges(seen, note, text=''):
    n = len(seen); b = ''
    if ' / ' in text and n >= 2: b += f'<span class="bd type">Same type {n}×</span>'
    elif n >= 3: b += f'<span class="bd hot">Repeated {n}×</span>'
    elif n == 2: b += '<span class="bd rep">Repeated 2×</span>'
    if note == 'due': b += '<span class="bd due">Due — not yet in R2021</span>'
    if note == 'r21': b += '<span class="bd r21">R2021 favourite</span>'
    return b

def qcard(i, text, seen, note):
    hot = len(seen) >= 3 and ' / ' not in text
    return (f'<div class="qcard{" hotcard" if hot else ""}"><div class="qn">{i}</div><div class="qbody">'
            f'<div class="qt">{text}</div><div class="qmeta">{badges(seen, note, text)}'
            f'<span class="seenlbl">Seen in</span>{chips(seen)}</div></div></div>')

ROMAN = ['I', 'II', 'III', 'IV', 'V']
def unit_pages():
    out = []
    for i, (unit, secs) in enumerate(U):
        title = unit.split('—', 1)[1].strip()
        ranked = sorted([s for s in skills if s[1] == str(i+1)], key=lambda s: -len(freq[s]))[:4]
        must = ''.join(f'<li><b>{nm(s)}</b> <span class="muted">— {len(freq[s])} of 14 papers</span></li>' for s in ranked)
        brk = ' style="break-before:auto;margin-top:16pt"' if i == 0 else ''
        out.append(f'<section class="unitpage"{brk}><div class="unitband"><div class="unum">{i+3} · Unit {ROMAN[i]}</div>'
                   f'<div class="utitle">{title}</div></div>'
                   f'<div class="must"><div class="musth">Must-do in this unit</div><ol>{must}</ol></div>')
        n = 0
        for sec, items in secs:
            out.append(f'<h3>{sec}</h3>')
            for text, seen, note in sorted(items, key=lambda it: -len(it[1])):
                n += 1; out.append(qcard(n, text, seen, note))
        out.append('</section>')
    return '\n'.join(out)

def parta_cards():
    out = []
    for i, (t, s) in enumerate(sorted(PART_A, key=lambda t: -len(t[1]))):
        out.append(f'<div class="qcard{" hotcard" if len(s) >= 6 else ""}"><div class="qn">{i+1}</div><div class="qbody"><div class="qt">{t}</div>'
                   f'<div class="qmeta"><span class="bd hot">In {len(s)} papers</span><span class="seenlbl">Seen in</span>{chips(s)}</div></div></div>')
    return '\n'.join(out)

def bar_chart():
    rows = sorted(skills, key=lambda s: (-len(freq[s]), s))
    out = ['<div class="chart">',
           '<div class="crow chead"><div class="cl">Topic</div><div class="cu">Unit</div><div class="cb">Papers it appeared in (out of 14)</div><div class="cr">R2021 (of 4)</div></div>']
    for s in rows:
        n = len(freq[s]); r = sum('R21' in p for p in freq[s])
        out.append(f'<div class="crow"><div class="cl">{nm(s)}</div><div class="cu">{ROMAN[int(s[1])-1]}</div>'
                   f'<div class="cb"><div class="bar" style="width:{n/14*82:.1f}%"></div><span class="bv">{n}</span></div>'
                   f'<div class="cr">{r}</div></div>')
    out.append('</div>'); return '\n'.join(out)

greedy_html = ''.join(
    f'<tr><td class="num">{n}</td><td>{nm(s)}</td><td>{unit_of(s)}</td><td class="num">{a:.0f}</td><td class="num">{w}</td>'
    f'<td class="num">{" · ".join(map(str, r))}</td></tr>' for n, s, a, w, r in greedy)
oos_html = ''.join(f'<tr><td>Top {k} topics</td>' + ''.join(f'<td class="num">{v}</td>' for v in r) + '</tr>' for k, r in oos)
rank_html = ', '.join(f'{nm(s)}' for s in rank[:10])
papers_table = ''.join(
    f'<tr><td>{s[:4]} {FULL[s[5:]]}</td><td>{reg}</td><td class="num">{code}</td><td><a href="{purl(s)}">{path.split("/")[-1]}</a></td></tr>'
    for s, (reg, path, code) in sorted(FILES.items(), key=lambda kv: kv[0], reverse=True))

PRIORITY = [
 ("Recurrence relations", "II", "14", "Every paper. Practise 6–8 problems, both generating-function and characteristic-equation methods."),
 ("Rules of inference — indirect method, CP rule, quantifiers", "I", "13", "“Student has not read the book”, “It rained”, (∀x)(P ∨ Q) ⇒ (∀x)P ∨ (∃x)Q."),
 ("Graph isomorphism", "III", "13", "Missing from only one paper in nine years."),
 ("Lagrange's theorem & cosets", "IV", "11", "Sometimes a full 16-mark question."),
 ("Handshaking & maximum-edge theorems", "III", "12", "Odd-degree vertices are even; n(n−1)/2; (n−k)(n−k+1)/2."),
 ("Hasse diagram problems", "V", "9", "In all four R2021 papers: D<sub>n</sub>, LUB/GLB, “is this a lattice?”"),
 ("Equivalence & tautology without truth table", "I", "10", "The “… ⇔ R” problem came four times."),
 ("a ≤ b equivalences", "V", "7", "a ≤ b ⇔ a ∧ b′ = 0 ⇔ a′ ∨ b = 1 ⇔ b′ ≤ a′. Five times in old papers — due."),
 ("Mathematical induction", "II", "14", "Sum of squares, 3 | n³ − n, product of primes."),
 ("Every chain is distributive", "V", "8", "Short proof, safe 8 marks."),
 ("Normal subgroups", "IV", "6", "Intersection of two normal subgroups; xHx<sup>−1</sup> ⊆ H."),
 ("Permutations, combinations, pigeonhole", "II", "9", "Committees, bit strings, “six men and five women”."),
 ("PDNF / PCNF", "I", "11", "In all four R2021 papers."),
 ("Inclusion–exclusion", "II", "12", "“Not divisible by 2, 3, 5, 7” came 5 times; missing from the last two papers — due."),
 ("Kernel is normal · De Morgan's laws · Dirac's theorem", "IV · V · III", "6 · 6 · 4", "High-repeat proofs. Learn them word by word."),
]
prio_html = ''.join(
    f'<tr class="{"top" if i < 10 else ""}"><td class="num rk">{i+1}</td><td><b>{a}</b><div class="tip">{d}</div></td>'
    f'<td class="ctr">{u}</td><td class="num">{c}</td></tr>' for i, (a, u, c, d) in enumerate(PRIORITY))

REPEATS = [
 ("(¬P ∧ (¬Q ∧ R)) ∨ (Q ∧ R) ∨ (P ∧ R) ⇔ R", ["2016 N/D", "2018 A/M", "2023 A/M", "2024 A/M"]),
 ("Integers 1–250 (or 500 / 100) not divisible by 2, 3, 5, 7", ["2016 M/J", "2016 N/D", "2017 A/M", "2018 A/M", "2018 N/D"]),
 ("a ≤ b ⇔ a ∧ b′ = 0 ⇔ a′ ∨ b = 1 ⇔ b′ ≤ a′", ["2016 M/J", "2016 N/D", "2017 A/M", "2017 N/D", "2020 N/D"]),
 ("“A student in this class has not read the book …”", ["2017 N/D", "2018 N/D", "2019 A/M", "2020 N/D"]),
 ("Dirac: degree ≥ n/2 ⇒ Hamiltonian", ["2016 M/J", "2017 A/M", "2020 N/D", "2024 A/M"]),
 ("G(k) − 7G(k−1) + 10G(k−2) = 8k + 6", ["2016 N/D", "2018 A/M", "2023 A/M"]),
 ("(∀x)(P(x) ∨ Q(x)) ⇒ (∀x)P(x) ∨ (∃x)Q(x)", ["2018 A/M", "2023 A/M", "2024 A/M"]),
 ("“It rained” (sports day / trophy)", ["2016 M/J", "2019 N/D", "2020 N/D"]),
 ("PDNF & PCNF of (¬P → R) ∧ (Q ↔ P)", ["2016 M/J", "2017 A/M", "2019 N/D"]),
 ("Every integer n ≥ 2 is a prime or a product of primes", ["2019 A/M", "2020 N/D", "2024 A/M"]),
 ("Self-complementary ⇒ n ≡ 0 or 1 (mod 4)", ["2016 M/J", "2019 N/D", "2020 N/D"]),
 ("Complement is unique in a complemented distributive lattice", ["2016 N/D", "2018 A/M", "2020 N/D"]),
]
rep_html = ''.join(f'<tr><td>{q}</td><td class="num big">{len(s)}×</td><td>{chips(s)}</td></tr>' for q, s in REPEATS)

FONT = os.path.join(HERE, 'fonts')
CSS = f"""
@font-face {{ font-family: 'NS'; src: url('file://{FONT}/NotoSans-Regular.ttf'); font-weight: 400; }}
@font-face {{ font-family: 'NS'; src: url('file://{FONT}/NotoSans-Italic.ttf'); font-weight: 400; font-style: italic; }}
@font-face {{ font-family: 'NS'; src: url('file://{FONT}/NotoSans-SemiBold.ttf'); font-weight: 600; }}
@font-face {{ font-family: 'NS'; src: url('file://{FONT}/NotoSans-Bold.ttf'); font-weight: 700; }}
@font-face {{ font-family: 'NSM'; src: url('file://{FONT}/NotoSansMath-Regular.ttf'); }}
@page {{ size: A4; margin: 17mm 17mm 19mm 17mm; }}
:root {{ --ink:#1b1b1a; --sub:#55534e; --mute:#7a7872; --line:#e4e2dc; --blue:#2a78d6; --blue-d:#1c5cab; --blue-l:#eef4fc;
        --orange:#eb6834; --orange-d:#a8401a; --orange-l:#fdf1eb; --amber:#c98500; --amber-l:#fdf6e6; --green:#0f7a52; --green-l:#e9f7f1; --bg:#f7f7f5; }}
* {{ box-sizing: border-box; }}
body {{ font-family: 'NS', 'NSM', 'DejaVu Sans', sans-serif; color: var(--ink); font-size: 10.4pt; line-height: 1.55; margin: 0; }}
b, strong {{ font-weight: 600; }}
a {{ color: var(--blue-d); text-decoration: none; }}
p {{ margin: 0 0 8pt; }}
.muted {{ color: var(--mute); font-weight: 400; }}
.small {{ font-size: 8.8pt; color: var(--sub); }}
section {{ break-before: page; }}
h1 {{ font-weight: 700; }}
h2 {{ font-size: 17pt; font-weight: 700; margin: 0 0 4pt; letter-spacing: -0.2pt; }}
h2 .no {{ color: var(--blue); margin-right: 6pt; }}
.lede {{ color: var(--sub); font-size: 10.6pt; margin-bottom: 14pt; }}
h3 {{ font-size: 12pt; font-weight: 600; color: var(--blue-d); margin: 16pt 0 7pt; break-after: avoid; }}

/* cover */
.cover {{ height: 255mm; padding-top: 18mm; display: flex; flex-direction: column; break-after: page; }}
.kicker {{ font-size: 9.5pt; font-weight: 600; color: var(--blue-d); letter-spacing: 1.2pt; text-transform: uppercase; }}
.cover h1 {{ font-size: 36pt; line-height: 1.1; margin: 10pt 0 8pt; letter-spacing: -0.6pt; }}
.cover .subt {{ font-size: 13.5pt; color: var(--sub); margin-bottom: 30pt; max-width: 150mm; }}
.tiles {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 10pt; margin-bottom: 26pt; }}
.tile {{ background: var(--bg); border-radius: 8pt; padding: 12pt 13pt; }}
.tile .big {{ font-size: 27pt; font-weight: 700; line-height: 1.1; color: var(--ink); }}
.tile .lbl {{ font-size: 9pt; color: var(--sub); margin-top: 4pt; line-height: 1.4; }}
.inside h4 {{ font-size: 10pt; text-transform: uppercase; letter-spacing: 1pt; color: var(--sub); margin: 0 0 6pt; font-weight: 600; }}
.toc {{ list-style: none; padding: 0; margin: 0; }}
.toc li {{ display: flex; gap: 10pt; padding: 7.5pt 0; border-bottom: 0.7pt solid var(--line); font-size: 10.5pt; }}
.toc .n {{ color: var(--blue); font-weight: 700; width: 26pt; flex: none; }}
.toc .d {{ color: var(--mute); margin-left: auto; font-size: 9pt; }}
.cover .foot {{ margin-top: auto; font-size: 8.8pt; color: var(--sub); border-top: 0.7pt solid var(--line); padding-top: 8pt; }}

/* boxes */
.callout {{ border-radius: 7pt; padding: 10pt 13pt; margin: 10pt 0 12pt; background: var(--blue-l); break-inside: avoid; }}
.callout.warn {{ background: var(--amber-l); }}
.callout .t {{ font-weight: 600; margin-bottom: 2pt; }}
.findings {{ display: grid; grid-template-columns: 1fr 1fr; gap: 10pt; margin: 6pt 0 12pt; }}
.finding {{ border: 0.8pt solid var(--line); border-radius: 8pt; padding: 11pt 12pt; break-inside: avoid; }}
.finding .h {{ font-weight: 600; font-size: 11pt; margin-bottom: 3pt; }}
.finding p {{ font-size: 9.6pt; color: var(--sub); margin: 0; }}
.finding .num {{ font-size: 20pt; font-weight: 700; color: var(--blue-d); line-height: 1.1; }}

/* tables */
table {{ border-collapse: collapse; width: 100%; margin: 4pt 0 12pt; font-size: 9.4pt; }}
th {{ text-align: left; font-weight: 600; color: var(--sub); font-size: 8.6pt; text-transform: uppercase; letter-spacing: 0.5pt;
      border-bottom: 1.2pt solid var(--ink); padding: 5pt 6pt; }}
td {{ border-bottom: 0.7pt solid var(--line); padding: 6pt 6pt; vertical-align: top; }}
tr {{ break-inside: avoid; }}
.num {{ text-align: right; white-space: nowrap; font-variant-numeric: tabular-nums; }}
.ctr {{ text-align: center; white-space: nowrap; }}
td.big {{ font-weight: 700; font-size: 11pt; }}
.prio td {{ padding: 4.5pt 6pt; }}
.prio .rk {{ font-weight: 700; color: var(--blue-d); font-size: 11pt; width: 18pt; }}
.prio .tip {{ color: var(--sub); font-size: 8.6pt; margin-top: 0; line-height: 1.4; }}
.prio tr.top td {{ background: #fafbfd; }}
.prio tr:nth-child(11) td {{ border-top: 1.4pt dashed var(--blue); }}

/* chips & badges */
.chip {{ display: inline-block; font-size: 7.8pt; padding: 0.5pt 5pt; margin: 1.5pt 3pt 1.5pt 0; border-radius: 9pt;
         background: #f0efec; color: var(--sub); white-space: nowrap; }}
.chip.r21c {{ background: var(--green-l); color: var(--green); }}
.bd {{ display: inline-block; font-size: 7.8pt; font-weight: 600; padding: 0.5pt 6pt; margin: 1.5pt 5pt 1.5pt 0; border-radius: 3pt; white-space: nowrap; }}
.hot {{ background: var(--orange-l); color: var(--orange-d); }}
.rep {{ background: var(--blue-l); color: var(--blue-d); }}
.type {{ background: #f0efec; color: var(--sub); }}
.due {{ background: var(--amber-l); color: #8a5a00; }}
.r21 {{ background: var(--green-l); color: var(--green); }}
.seenlbl {{ font-size: 7.8pt; color: var(--mute); margin: 0 4pt 0 2pt; }}

/* unit pages */
.unitband {{ display: flex; align-items: baseline; gap: 12pt; border-bottom: 2pt solid var(--blue); padding-bottom: 6pt; margin-bottom: 10pt; }}
.unum {{ font-size: 10pt; font-weight: 700; color: #fff; background: var(--blue); padding: 2pt 9pt; border-radius: 4pt; letter-spacing: 0.5pt; }}
.utitle {{ font-size: 18pt; font-weight: 700; letter-spacing: -0.2pt; }}
.must {{ background: var(--bg); border-radius: 8pt; padding: 9pt 13pt 6pt; margin-bottom: 4pt; break-inside: avoid; }}
.musth {{ font-size: 8.6pt; font-weight: 600; text-transform: uppercase; letter-spacing: 0.8pt; color: var(--sub); margin-bottom: 2pt; }}
.must ol {{ margin: 0; padding-left: 16pt; }}
.must li {{ margin: 1pt 0; }}
.qcard {{ display: flex; gap: 9pt; padding: 8pt 10pt 7pt 9pt; margin: 0 0 7pt; border: 0.8pt solid var(--line); border-radius: 7pt; break-inside: avoid; }}
.qcard.hotcard {{ border-left: 3pt solid var(--orange); }}
.qn {{ flex: none; width: 17pt; height: 17pt; border-radius: 50%; background: #f0efec; color: var(--sub); font-size: 8pt; font-weight: 600;
       display: flex; align-items: center; justify-content: center; margin-top: 1pt; }}
.qbody {{ flex: 1; }}
.qt {{ font-size: 10.2pt; line-height: 1.5; }}
.qmeta {{ margin-top: 4pt; line-height: 1.3; }}
.legend {{ display: flex; flex-wrap: wrap; gap: 4pt 14pt; font-size: 8.8pt; color: var(--sub); margin: 6pt 0 4pt; }}

/* chart */
.chart {{ margin: 6pt 0 12pt; }}
.crow {{ display: flex; align-items: center; min-height: 17pt; border-bottom: 0.5pt solid #f0efec; break-inside: avoid; }}
.chead {{ font-size: 8pt; font-weight: 600; text-transform: uppercase; letter-spacing: 0.5pt; color: var(--sub); border-bottom: 1.2pt solid var(--ink); min-height: 18pt; }}
.cl {{ width: 41%; font-size: 9.2pt; padding-right: 6pt; }}
.cu {{ width: 7%; font-size: 8.6pt; color: var(--sub); text-align: center; }}
.cb {{ flex: 1; display: flex; align-items: center; }}
.bar {{ height: 9pt; background: var(--blue); border-radius: 0 4pt 4pt 0; }}
.bv {{ font-size: 8.6pt; font-weight: 600; margin-left: 5pt; font-variant-numeric: tabular-nums; }}
.cr {{ width: 14%; text-align: right; font-size: 9pt; color: var(--sub); font-variant-numeric: tabular-nums; }}

ol.steps {{ padding-left: 0; list-style: none; counter-reset: s; margin: 6pt 0 10pt; }}
ol.steps > li {{ counter-increment: s; position: relative; padding: 0 0 9pt 28pt; break-inside: avoid; }}
ol.steps > li::before {{ content: counter(s); position: absolute; left: 0; top: 0; width: 18pt; height: 18pt; border-radius: 50%;
        background: var(--blue); color: #fff; font-size: 8.6pt; font-weight: 700; display: flex; align-items: center; justify-content: center; }}
ul.tips {{ padding-left: 15pt; }} ul.tips li {{ margin-bottom: 6pt; }}
"""

TOC = [("1", "Key findings", "the 1-page summary"), ("2", "What to study first", "priority list + pass plan"),
       ("3–7", "Question bank, Unit I to V", "every Part B question, most-repeated first"),
       ("8", "Part A (2-mark) patterns", ""), ("9", "Exam-hall tips", ""),
       ("10", "How the patterns were found", "method, repeats, charts, backtest"),
       ("11", "Download the question papers", "links to all 14 papers"), ("12", "Limitations", "")]
toc_html = ''.join(f'<li><span class="n">{n}</span><span>{t}</span><span class="d">{d}</span></li>' for n, t, d in TOC)

H = f"""<!doctype html><html><head><meta charset="utf-8"><title>MA3354 Discrete Mathematics — Exam Pattern Analysis</title><style>{CSS}</style></head><body>

<div class="cover">
 <div class="kicker">Anna University · Regulation 2021 · Semester 3</div>
 <h1>MA3354 Discrete Mathematics</h1>
 <div class="subt">Exam pattern analysis and must-study questions, built from 14 previous end-semester papers (2016–2024).</div>
 <div class="tiles">
  <div class="tile"><div class="big">14</div><div class="lbl">question papers read by hand, across R2013, R2017 and R2021</div></div>
  <div class="tile"><div class="big">{top10[3]}<span style="font-size:15pt">/80</span></div><div class="lbl">Part B marks in the <b>worst</b> past paper, knowing only the top 10 topics (average {top10[2]:.0f}/80)</div></div>
  <div class="tile"><div class="big">4×</div><div class="lbl">the same logic question came word for word (2016, 2018, 2023, 2024)</div></div>
 </div>
 <div class="inside"><h4>Inside this guide</h4><ul class="toc">{toc_html}</ul></div>
 <div class="foot">Papers, this PDF and the analysis code: <a href="{REPO}">{REPO}</a><br>Unofficial study aid, not affiliated with Anna University. Free to share.</div>
</div>

<section style="break-before:auto">
<h2><span class="no">1</span>Key findings</h2>
<div class="lede">The short version. Everything below is backed by the data in Section 10.</div>
<div class="findings">
 <div class="finding"><div class="num">Reused</div><div class="h">Questions come back</div><p>Anna University reuses a small pool of questions. Whole papers are recycled: 2016 May/June and 2017 April/May are almost the same paper. Single questions cross regulations, too.</p></div>
 <div class="finding"><div class="num">5 slots</div><div class="h">The structure is fixed</div><p>Q11–Q15 always map to Units I–V, and each has an (a) OR (b) choice. You only need one side per unit, so 2–3 strong topics per unit go a long way.</p></div>
 <div class="finding"><div class="num">{top10[3]}/80</div><div class="h">Top 10 topics are enough to pass</div><p>In the worst of all 14 papers, the top 10 topics still cover {top10[3]} Part B marks. The average is {top10[2]:.0f}/80. Add Part A and you are near 60/100.</p></div>
 <div class="finding"><div class="num">Tested</div><div class="h">It predicted unseen papers</div><p>A list built only from 2016–2021 papers scored at least 48/80 in every R2021 paper (2022–2024). Old papers really do predict new ones.</p></div>
</div>
<div class="callout"><div class="t">How to prepare each topic</div>For every theorem, write the full proof once by hand. For every problem type, solve the most-repeated question from the question bank (Sections 3–7) with the same numbers — repeats often come back unchanged. Then do Section 8 for Part A.</div>
<div class="callout warn"><div class="t">Honest note</div>No one can guarantee a question paper. This is a data-based estimate to help you <i>prioritise</i>. Do not skip whole units. Papers from Nov/Dec 2024 to Apr/May 2026 were not available, so very recent repeats are not counted.</div>
</section>

<section>
<h2><span class="no">2</span>What to study first</h2>
<div class="lede">Study top to bottom. The first 10 rows are the minimum pass plan. “Papers” = how many of the 14 papers had this topic in Part B.</div>
<table class="prio"><tr><th>#</th><th>Topic</th><th class="ctr">Unit</th><th class="num">Papers</th></tr>{prio_html}</table>
</section>

<section>
<h2><span class="no">3–7</span>Question bank, Unit by Unit</h2>
<div class="lede">Every Part B question from the 14 papers, grouped by the method it needs. In each group, the most-repeated questions come first. Close variants are shown in [brackets] or separated by “/”. Tap a session tag to open that paper.</div>
<div class="legend">
 <span><span class="bd hot">Repeated 4×</span> same question, 3+ times</span>
 <span><span class="bd rep">Repeated 2×</span> same question, twice</span>
 <span><span class="bd type">Same type 3×</span> different questions, one method</span>
 <span><span class="bd due">Due — not yet in R2021</span> frequent before 2022, not yet asked in R2021</span>
 <span><span class="bd r21">R2021 favourite</span> new style that R2021 papers like</span>
 <span><span class="chip r21c">2023 A/M</span> R2021 paper</span><span><span class="chip">2017 N/D</span> older paper</span>
</div>
<div class="callout" style="margin-bottom:4pt"><div class="t">Tip</div>Cards with an orange edge are the questions that came three or more times. Do those first.</div>
</section>
{unit_pages()}

<section>
<h2><span class="no">8</span>Part A (2-mark) patterns</h2>
<div class="lede">Part A is mostly definitions and one-step applications. These types came again and again. The number shows how many papers had them.</div>
{parta_cards()}
</section>

<section style="break-before:auto;margin-top:18pt">
<h2><span class="no">9</span>Exam-hall tips</h2>
<ul class="tips">
<li><b>Read both (a) and (b) of every unit first.</b> Pick the side where you know more of the sub-parts. They are usually 8 + 8 marks.</li>
<li><b>Theorems</b> (Lagrange, kernel is normal, chain is distributive, De Morgan): write the statement, the definitions you use, then the proof. Partial proofs still earn marks.</li>
<li><b>Isomorphism:</b> first tabulate vertices, edges and degree sequence. If they differ, the graphs are not isomorphic — say so. If they match, give the vertex mapping and check edges or the adjacency matrix.</li>
<li><b>Recurrences:</b> use the method the question asks for (generating function or characteristic equation). Using the wrong one can lose marks.</li>
<li><b>Inference proofs:</b> number every step and write the rule used (P, T, CP, US, UG, ES, EG) on the right.</li>
</ul>
</section>

<section>
<h2><span class="no">10</span>How the patterns were found</h2>
<div class="lede">Why you can trust the lists in this guide.</div>
<h3>10.1 Method</h3>
<ol class="steps">
<li><b>Collected every available paper.</b> MA3354 (R2021) papers exist only from 2022. But the earlier subjects <b>MA8351</b> (R2017) and <b>MA6566</b> (R2013) have the same five units, so they were included: 5 + 5 + 4 = 14 unique papers. A duplicate scan of Nov/Dec 2023 was removed.</li>
<li><b>Read every question by hand</b> from the scanned papers and recorded each Part B sub-question with its marks.</li>
<li><b>Tagged each sub-question with the topic (method) it needs.</b> For example, “student has not read the book”, “it rained” and “Babu knows JAVA” all need <i>rules of inference</i>. Learning the method covers every variant, so topics are counted, not exact wordings.</li>
<li><b>Counted frequency:</b> how many of the 14 papers, and how many of the 4 R2021 papers, had each topic (10.4).</li>
<li><b>Simulated a student (backtest).</b> Each Part B unit is “(a) OR (b)”. For a study list, each unit scores the better of the two sides, counting only sub-parts whose topic is on the list. Topics were added one at a time, each time picking the one that raises the average the most (10.5).</li>
<li><b>Tested on unseen papers.</b> A list built only from 2016–2021 papers was scored on the four R2021 papers it never saw (10.6).</li>
</ol>

<h3>10.2 Whole papers get recycled</h3>
<table><tr><th>Paper</th><th>Re-used in</th><th>What repeated</th></tr>
<tr><td>2016 May/June</td><td>2017 Apr/May</td><td>Almost the whole paper: same PDNF problem, same 6×6 adjacency matrices, “six men and five women”, Σ3<sup>r</sup>, Dirac, Lagrange, subgroup of a cyclic group, kernel is normal, every chain is distributive, a ≤ b equivalences.</td></tr>
<tr><td>2016 Nov/Dec</td><td>2018 Apr/May</td><td>About half: “… ⇔ R”, the G(k) recurrence, 1–250 not divisible by 2, 3, 5, 7, handshaking + n(n−1)/2, (Q<sup>+</sup>, ab/2), intersection of normal subgroups, unique complement.</td></tr>
<tr><td>2019 Apr/May</td><td>2020 Nov/Dec</td><td>About half: indirect method R → ¬Q …, “student has not read the book”, m | 2<sup>n</sup> − 1, 1 ≤ n ≤ 2000 divisible by 7, product of primes, (A, R<sup>−1</sup>) poset, distributive inequalities.</td></tr>
<tr><td>2022 Nov/Dec</td><td>2023 (both)</td><td>p → [(p → q) ∧ ¬(¬q ∨ ¬p)] (CNF, then PDNF); “Find an Euler path or circuit in the three graphs”, word for word.</td></tr>
<tr><td>2023 Apr/May</td><td>2024 Apr/May</td><td>“… ⇔ R”; (∀x)(P ∨ Q) ⇒ (∀x)P ∨ (∃x)Q; the same 4×4 adjacency matrix (Part A, then Part B).</td></tr>
</table>

<h3>10.3 Exact questions that crossed regulations</h3>
<table><tr><th>Question</th><th class="num">Times</th><th>Sessions</th></tr>{rep_html}</table>
<p class="small">R2021 papers also added new styles: <b>rings</b> (Z<sub>4</sub>, (Z, ⊕, ⊙)), <b>“is this Hasse diagram a lattice / distributive?”</b> and <b>word-argument validity</b>. Each came in 2–3 of the 4 R2021 papers.</p>

<h3>10.4 How often each topic appears</h3>
<p class="small">Topics that appeared only once are left out.</p>
{bar_chart()}

<h3>10.5 Backtest: marks from studying the top topics</h3>
<p class="small">Part B score out of 80 if you knew only the topics up to that row. Average and worst are over all 14 papers. The last column lists the four R2021 papers in order: 2022 N/D · 2023 A/M · 2023 N/D · 2024 A/M.</p>
<table><tr><th class="num">#</th><th>Add this topic</th><th>Unit</th><th class="num">Average</th><th class="num">Worst</th><th class="num">R2021 papers</th></tr>{greedy_html}</table>

<h3>10.6 Test on unseen papers</h3>
<p class="small">Topics ranked using only the ten 2016–2021 papers, then scored on the four R2021 papers. Top 10 from old papers: {rank_html}.</p>
<table><tr><th>Study list</th><th class="num">2022 N/D</th><th class="num">2023 A/M</th><th class="num">2023 N/D</th><th class="num">2024 A/M</th></tr>{oos_html}</table>
<div class="callout">A top-10 list made from old papers alone would have given <b>at least 48/80</b> in Part B in every R2021 paper.</div>
</section>

<section>
<h2><span class="no">11</span>Download the question papers</h2>
<div class="lede">All 14 papers are on GitHub, with website ad pages removed. Click a file name to open it.</div>
<table><tr><th>Session</th><th>Regulation · subject</th><th class="num">QP code</th><th>File</th></tr>{papers_table}</table>
<p class="small">Repository: <a href="{REPO}">{REPO}</a></p>

<h2 style="margin-top:22pt"><span class="no">12</span>Limitations</h2>
<ul class="tips">
<li>Papers after April/May 2024 (Nov/Dec 2024, Apr/May 2025, Nov/Dec 2025, Apr/May 2026) could not be accessed. If you have them, please share them through the repository.</li>
<li>Ten of the papers are from R2013/R2017 subjects with the same units. A few of their topics (modular lattices, walks and powers of A) are lower priority for R2021.</li>
<li>Questions were typed by hand from scans. If a symbol looks wrong, check the original paper using the links.</li>
<li>Paper sources: Brainkart and EnggTree student sites. Unofficial; not affiliated with Anna University.</li>
</ul>
</section>
</body></html>"""

out = os.path.join(HERE, 'MA3354_Exam_Pattern_Analysis.html')
open(out, 'w', encoding='utf-8').write(H)
print(out)
