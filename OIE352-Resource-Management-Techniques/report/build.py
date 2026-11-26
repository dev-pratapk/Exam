"""OIE352 Resource Management Techniques — exam pattern analysis PDF (built from the two public CS6704 papers)."""
import sys, os, html
from collections import defaultdict
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'analysis'))
from papers import PAPERS, TOPICS        # noqa: E402
from run import score, rank              # noqa: E402

REPO = os.environ.get('REPO_URL', 'https://github.com/dev-pratapk/Exam').rstrip('/')
SUB = 'OIE352-Resource-Management-Techniques'
FILES = {'2020 N/D': 'R2013_CS6704/CS6704_2020_Nov-Dec_QPX20411.pdf', '2021 N/D': 'R2013_CS6704/CS6704_2021_Nov-Dec_QP70398.pdf'}
def purl(p): return f'{REPO}/blob/main/{SUB}/question-papers/{FILES[p]}'
def chip(p): return f'<a class="chip" href="{purl(p)}">{p} · CS6704</a>'
P = list(PAPERS)
ROMAN = ['I', 'II', 'III', 'IV', 'V']
UNIT_NAME = {1: 'Linear Programming', 2: 'Duality and Networks', 3: 'Integer Programming', 4: 'Classical Optimisation Theory', 5: 'Project (Object) Scheduling'}
def nm(x): return TOPICS[x][1]

pap = defaultdict(set); papB = defaultdict(set); qs = defaultdict(list)
for p in P:
    for part, n, text, topic, m in PAPERS[p]['Q']:
        pap[topic].add(p)
        if part in 'BC': papB[topic].add(p)
        qs[topic].append((part, n, text, m, p))

top2 = rank(P, 2)
loo = {k: [(p, score(p, rank([q for q in P if q != p], k))) for p in P] for k in (1, 2)}
final = {p: score(p, top2) for p in P}
order = []   # study order: Part B/C problem types first (by units 1..5 interleaved by frequency), then the basics
for x in sorted([t for t in TOPICS if papB[t]], key=lambda t: (-len(papB[t]), TOPICS[t][0], t)): order.append(x)
basics = [t for t in TOPICS if not papB[t]]

def qcard(i, part, n, text, m, p):
    cls = {'A': 'pa', 'B': 'pb', 'C': 'pc'}[part]; label = {'A': 'Part A · 2 marks', 'B': 'Part B · 13 marks', 'C': 'Part C · 15 marks'}[part]
    return (f'<div class="qcard {cls}"><div class="qn">{i}</div><div class="qbody"><div class="qt">{text}</div>'
            f'<div class="qmeta"><span class="bd {cls}b">{label}</span><span class="seenlbl">Q{n} in</span>{chip(p)}</div></div></div>')

def unit_pages():
    out = []
    for u in range(1, 6):
        ts = sorted([x for x in TOPICS if TOPICS[x][0] == u], key=lambda x: (-len(papB[x]), -len(pap[x]), x))
        must = ''.join(f'<li><b>{nm(x)}</b> <span class="muted">— {len(pap[x])} of 2 papers</span></li>' for x in ts if papB[x])
        brk = ' style="break-before:auto;margin-top:16pt"' if u == 1 else ''
        out.append(f'<section{brk}><div class="unitband"><div class="unum">{u+2} · Unit {ROMAN[u-1]}</div><div class="utitle">{UNIT_NAME[u]}</div></div>'
                   f'<div class="must"><div class="musth">Problem types that came in Part B / C</div><ol>{must}</ol></div>')
        i = 0
        for x in ts:
            out.append(f'<h3>{nm(x)} <span class="muted small">· {len(pap[x])} of 2 papers</span></h3><p class="small">{TOPICS[x][2]}</p>')
            for part, n, text, m, p in sorted(qs[x], key=lambda q: ('BCA'.index(q[0]), q[4])):
                i += 1; out.append(qcard(i, part, n, text, m, p))
        out.append('</section>')
    return '\n'.join(out)

prio_html = ''.join(
    f'<tr class="{"top" if i < 10 else ""}"><td class="num rk">{i+1}</td><td><b>{nm(x)}</b><div class="tip">{TOPICS[x][2]}</div></td>'
    f'<td class="ctr">{ROMAN[TOPICS[x][0]-1]}</td><td class="num">{len(papB[x])}/2</td></tr>' for i, x in enumerate(order))
basic_html = ''.join(f'<tr><td><b>{nm(x)}</b><div class="tip">{TOPICS[x][2]}</div></td><td class="ctr">{ROMAN[TOPICS[x][0]-1]}</td><td class="num">{len(pap[x])}/2</td></tr>' for x in basics)
loo_html = ''.join(f'<tr><td>{p} · {PAPERS[p]["code"]}</td><td class="num">{a}</td><td class="num">{b}</td></tr>' for (p, a), (_, b) in zip(loo[1], loo[2]))
papers_table = ''.join(f'<tr><td>{p}</td><td>{PAPERS[p]["reg"]}</td><td class="num">{PAPERS[p]["code"]}</td><td><a href="{purl(p)}">{FILES[p].split("/")[-1]}</a></td></tr>' for p in P)
bar = ['<div class="chart"><div class="crow chead"><div class="cl">Problem type / topic</div><div class="cu">Unit</div><div class="cb">Papers (out of 2)</div><div class="cr">Part B / C</div></div>']
for x in sorted(TOPICS, key=lambda x: (-len(pap[x]), -len(papB[x]), TOPICS[x][0])):
    bar.append(f'<div class="crow"><div class="cl">{nm(x)}</div><div class="cu">{ROMAN[TOPICS[x][0]-1]}</div><div class="cb"><div class="bar" style="width:{len(pap[x])/2*80:.0f}%"></div><span class="bv">{len(pap[x])}</span></div><div class="cr">{len(papB[x])}</div></div>')
bar.append('</div>')

REPEATS = [
 ('Part C: transportation problem — maximize profit of five salesmen in four places (unbalanced, add a dummy)', ['2020 N/D', '2021 N/D'], 'Same question, same numbers'),
 ('Part C: integer programming — Maximize Z = 80x₁ + 45x₂ with x₁ + x₂ ≤ 7 and 12x₁ + 5x₂ ≤ 60 (printed 600 in 2021)', ['2020 N/D', '2021 N/D'], 'Same question; the 2021 paper has a typo'),
 ('Dual simplex method on a small two-variable LPP (Question 12a)', ['2020 N/D', '2021 N/D'], 'Question 12(a) both years'),
 ('Kuhn–Tucker conditions (Question 14)', ['2020 N/D', '2021 N/D'], 'A problem in 2020, “describe with an example” in 2021'),
 ('CPM / PERT network (Question 15)', ['2020 N/D', '2021 N/D'], 'PERT with probability of completion both years'),
 ('LP formulation and graphical solution (Question 11)', ['2020 N/D', '2021 N/D'], 'Max-profit problem each year, plus a minimum-cost one in 2021'),
]
rep_html = ''.join(f'<tr><td>{q}<div class="tip">{w}</div></td><td class="num big">{len(s)}×</td><td>{"".join(chip(p) for p in s)}</td></tr>' for q, s, w in REPEATS)
partc_html = ''.join(f'<tr><td>{p}</td><td>{q[1]}</td><td>{q[2][:170]}…</td><td>{nm(q[3])}</td></tr>' for p in P for q in PAPERS[p]['Q'] if q[0] == 'C')
TOC = [("1", "Key findings", ""), ("2", "What to study first", "problem types in priority order"),
       ("3–7", "Question bank, Unit I to V", "every question of the two papers, grouped by problem type"),
       ("8", "Part C pattern", "the same two questions came twice"), ("9", "Exam-hall tips", ""),
       ("10", "How the patterns were found", "method, repeats, chart, validation"),
       ("11", "Download the question papers", ""), ("12", "Limitations", "please read")]
toc_html = ''.join(f'<li><span class="n">{n}</span><span>{t}</span><span class="d">{d}</span></li>' for n, t, d in TOC)
CSS = open(os.path.join(HERE, 'style.css')).read().replace('{FONT}', os.path.join(HERE, '..', '..', 'report', 'fonts'))

H = f"""<!doctype html><html><head><meta charset="utf-8"><title>OIE352 Resource Management Techniques — Exam Pattern Analysis</title><style>{CSS}</style></head><body>
<div class="cover">
 <div class="kicker">Anna University · Regulation 2021 · Open Elective II</div>
 <h1>OIE352 Resource Management Techniques</h1>
 <div class="subt">Exam pattern analysis and must-study problem types. OIE352 has no public question papers yet, so this guide uses the two public papers of CS6704, the same subject under Regulation 2013 (same five units, same textbook).</div>
 <div class="tiles">
  <div class="tile"><div class="big">2/2</div><div class="lbl">papers asked the same two Part C problems (transportation maximization, integer programming)</div></div>
  <div class="tile"><div class="big">10</div><div class="lbl">problem types (2 per unit) covered every Part B and Part C mark of both papers in a cross-check</div></div>
  <div class="tile"><div class="big">0</div><div class="lbl">official OIE352 papers found online. Read “Limitations” in Section 12.</div></div>
 </div>
 <div class="inside"><h4>Inside this guide</h4><ul class="toc">{toc_html}</ul></div>
 <div class="foot">Papers, this PDF and the analysis code: <a href="{REPO}/tree/main/{SUB}">{REPO}/tree/main/{SUB}</a><br>Unofficial study aid, not affiliated with Anna University. Free to share.</div>
</div>

<section style="break-before:auto">
<h2><span class="no">1</span>Key findings</h2>
<div class="lede">The short version. Data and method are in Section 10.</div>
<div class="findings">
 <div class="finding"><div class="num">Numbers</div><div class="h">This subject is problem solving</div><p>Nearly all of Part B and C is a numerical problem: simplex, dual simplex, transportation, assignment, integer LP, dynamic programming, Kuhn–Tucker, CPM and PERT. Practise methods, not theory.</p></div>
 <div class="finding"><div class="num">Twice</div><div class="h">Part C repeated word for word</div><p>Both papers asked the same salesmen transportation (profit maximization) and the same integer programming problem. Learn both fully.</p></div>
 <div class="finding"><div class="num">2/2</div><div class="h">Same type every year</div><p>Dual simplex (Q12a), Kuhn–Tucker (Q14), CPM and PERT (Q15) and LP graphical (Q11) came in both papers; the numbers change.</p></div>
 <div class="finding"><div class="num">Printing errors</div><div class="h">Check the question</div><p>2020 Q13(a) prints “2x₁ = 11”, which has no integer solution (intended: ≤ 11). 2021 Part C prints 600 where 60 is intended. State your assumption in the answer.</p></div>
</div>
<div class="callout"><div class="t">How to prepare</div>For each problem type, solve one past problem completely, then one with different numbers. Write every step: formulation, table, iteration, final answer with units. Marks follow the steps.</div>
<div class="callout warn"><div class="t">Honest note</div>Only two public papers exist, both of the old subject code CS6704. Patterns from two papers are indicative, not proof. The syllabus of OIE352 matches CS6704 unit by unit, but the real OIE352 papers may use other problem types within each unit (for example shortest route in Unit II, Jacobian or Lagrangian problems in Unit IV). The study list in Section 2 therefore includes the basics for each unit.</div>
</section>

<section>
<h2><span class="no">2</span>What to study first</h2>
<div class="lede">Problem types that came in Part B or Part C, in priority order. The first 10 rows are the minimum plan.</div>
<table class="prio"><tr><th>#</th><th>Problem type and method</th><th class="ctr">Unit</th><th class="num">Papers</th></tr>{prio_html}</table>
<h3>Also learn for Part A (2 marks)</h3>
<table class="prio"><tr><th>Topic</th><th class="ctr">Unit</th><th class="num">Papers</th></tr>{basic_html}</table>
<p class="small">Not asked yet but in the syllabus: shortest route problem (Unit II), Lagrangian method and equality constraints (Unit IV), time charts and resource levelling (Unit V). Read them once.</p>
</section>

<section>
<h2><span class="no">3–7</span>Question bank, Unit by Unit</h2>
<div class="lede">Every question of the two papers, grouped by problem type. Click a tag to open that paper.</div>
<div class="legend"><span><span class="bd pbb">Part B · 13 marks</span></span><span><span class="bd pcb">Part C · 15 marks</span></span><span><span class="bd pab">Part A · 2 marks</span></span></div>
</section>
{unit_pages()}

<section>
<h2><span class="no">8</span>Part C (15-mark) pattern</h2>
<div class="lede">Part C is one question with an (a) OR (b) choice. In both papers it was the same pair.</div>
<table><tr><th>Paper</th><th>Q</th><th>Question</th><th>Problem type</th></tr>{partc_html}</table>
<div class="callout"><div class="t">What to do</div>Solve Part C 16(a) (unbalanced transportation, maximize profit) and 16(b) (integer LP, optimum 420 at x₁ = 3, x₂ = 4 when the constraint is 12x₁ + 5x₂ ≤ 60) from start to finish at least twice. They are the best use of preparation time.</div>

<h2 style="margin-top:20pt"><span class="no">9</span>Exam-hall tips</h2>
<ul class="tips">
<li><b>Choose the side you can finish.</b> Every question has an (a) OR (b) choice; a half-finished table earns fewer marks than a complete simpler problem.</li>
<li><b>Show the table at every step.</b> Simplex, dual simplex, transportation (MODI) and Hungarian tables carry the marks; write the entering and leaving variable at each step.</li>
<li><b>Check feasibility at the end.</b> Substitute the answer in each constraint.</li>
<li><b>Unbalanced transportation:</b> add a dummy row or column with zero cost (zero profit for maximization) and then solve.</li>
<li><b>PERT probability:</b> Z = (T − T<sub>E</sub>)/σ; use the normal table (the paper allows it).</li>
<li><b>If the printed constraint looks wrong</b> (for example an equality that makes the problem infeasible), say so in one line and solve with the intended constraint.</li>
</ul>
</section>

<section>
<h2><span class="no">10</span>How the patterns were found</h2>
<h3>10.1 Method</h3>
<ol class="steps">
<li><b>Looked for OIE352 papers.</b> None are public: EnggTree lists them as “Coming Soon”, Brainkart has none, and the Anna University library site could not be reached.</li>
<li><b>Used the predecessor subject.</b> CS6704 Resource Management Techniques (Regulations 2013) has the same five units and the same textbook (Taha). Its two public papers (Nov/Dec 2020 and Nov/Dec 2021) were read by hand.</li>
<li><b>Tagged every question with a problem type</b> and counted in how many of the two papers it appeared (10.2, 10.3).</li>
<li><b>Simulated a student.</b> Each Part B unit and Part C is “(a) OR (b)”. A study list scores a question if it covers either side. Total out of 80 (65 + 15).</li>
<li><b>Cross-checked.</b> A list built from one paper was scored on the other (10.4).</li>
</ol>
<h3>10.2 Questions that repeated</h3>
<table><tr><th>Question</th><th class="num">Times</th><th>Papers</th></tr>{rep_html}</table>
<h3>10.3 How often each topic appeared</h3>
{''.join(bar)}
<h3>10.4 Cross-check between the two papers</h3>
<p class="small">A study list built from the <i>other</i> paper only, scored on the paper named (Part B + C out of 80).</p>
<table><tr><th>Paper scored</th><th class="num">Top 1 problem type per unit</th><th class="num">Top 2 per unit (10 types)</th></tr>{loo_html}</table>
<div class="callout">Studying the top 2 problem types per unit from one paper covered all 80 marks of the other. With only two papers this shows consistency, not a guarantee.</div>
</section>

<section>
<h2><span class="no">11</span>Download the question papers</h2>
<table><tr><th>Session</th><th>Regulation · subject</th><th class="num">QP code</th><th>File</th></tr>{papers_table}</table>
<h2 style="margin-top:20pt"><span class="no">12</span>Limitations</h2>
<ul class="tips">
<li><b>No official OIE352 paper was available.</b> Everything here comes from two CS6704 papers. If you have OIE352 papers (Nov/Dec 2024 onwards), share them through the repository and the analysis will be redone.</li>
<li>Two papers cannot show reliable frequencies. The study list covers every unit so that a change of problem type does not leave you unprepared.</li>
<li>Questions were typed from the papers by hand; check the original through the links if something looks wrong. Two printing errors are noted in Section 1.</li>
<li>Paper sources: the library of St. Anne’s College of Engineering and Technology. Unofficial; not affiliated with Anna University.</li>
</ul>
</section>
</body></html>"""
out = os.path.join(HERE, 'OIE352_Exam_Pattern_Analysis.html'); open(out, 'w', encoding='utf-8').write(H); print(out)
