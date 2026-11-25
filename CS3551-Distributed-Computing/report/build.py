"""CS3551 Distributed Computing — exam pattern analysis PDF (HTML; render with ../../report/to_pdf.js)."""
import sys, os, html
from collections import defaultdict
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'analysis'))
from papers import PAPERS, TOPICS          # noqa: E402
from run import score, tops                # noqa: E402
from validate import rank                  # noqa: E402

REPO = os.environ.get('REPO_URL', 'https://github.com/dev-pratapk/Exam').rstrip('/')
SUB = 'CS3551-Distributed-Computing'
FILES = {
 '2023 N/D': 'R2021_CS3551/CS3551_2023_Nov-Dec_QP20874.pdf',
 '2024 A/M': 'R2021_CS3551/CS3551_2024_Apr-May_QP50907.pdf',
 '2024 N/D': 'R2021_CS3551/CS3551_2024_Nov-Dec_QP40927.pdf',
 '2021 A/M': 'R2017_CS8603/CS8603_2021_Apr-May_QPX10324.pdf',
 '2021 N/D': 'R2017_CS8603/CS8603_2021_Nov-Dec_QP40400.pdf',
 '2023 N/D (R17)': 'R2017_CS8603/CS8603_2023_Nov-Dec_QP12155.pdf',
}
def purl(p): return f'{REPO}/blob/main/{SUB}/question-papers/{FILES[p]}'
def is21(p): return 'CS3551' in PAPERS[p]['reg']
def lab(p): return p.replace(' (R17)', '') + (' · CS8603' if not is21(p) else '')
def chip(p, extra=''): return f'<a class="chip{" r21c" if is21(p) else ""}" href="{purl(p)}">{lab(p)}{extra}</a>'

P = list(PAPERS)
FONT = os.path.join(HERE, '..', '..', 'report', 'fonts')
ROMAN = ['I', 'II', 'III', 'IV', 'V']
UNIT_NAME = {1: 'Introduction', 2: 'Logical Time and Global State', 3: 'Distributed Mutex and Deadlock',
             4: 'Consensus and Recovery', 5: 'Cloud Computing'}

# ---------------------------------------------------------------- stats
pap = defaultdict(set); papB = defaultdict(set); qs = defaultdict(list)
for p in P:
    for part, n, text, t, m in PAPERS[p]['Q']:
        for x in tops(t):
            pap[x].add(p)
            if part in 'BC': papB[x].add(p)
            if not x.startswith('x_'): qs[x].append((part, n, text, m, p))
TOP15 = rank(P, 3)
r21 = [p for p in P if is21(p)]
loo = {k: [(p, score(p, rank([q for q in P if q != p], k))) for p in P] for k in (2, 3)}
final = {p: score(p, TOP15) for p in P}

TIPS = {
 'design_issues': 'Heterogeneity, openness, security, scalability, failure handling, concurrency, transparency — plus algorithmic & system challenges. Also comes as a Part C case study.',
 'primitives': 'Send/Receive; blocking vs non-blocking; synchronous vs asynchronous (4 combinations with a timing diagram); MPI, RPC, RMI, sockets as standards.',
 'model_computation': 'Events, happens-before (→), concurrent events, cuts, consistent cut, past and future cones.',
 'snapshot': 'Global state, consistent global state, Chandy–Lamport marker algorithm for FIFO channels with an example.',
 'message_ordering': 'Non-FIFO, FIFO, causal order, synchronous order; total order (centralized and distributed / Lamport); group communication. Part C came twice from here.',
 'logical_clocks': 'Framework of logical clocks (R1, R2), scalar time, vector time and their properties; physical clock sync / NTP.',
 'deadlock_models': 'System model, wait-for graph, single-resource / AND / OR / AND-OR / p-out-of-q models, Knapp’s 4 classes, false/phantom deadlock.',
 'cmh': 'Probe messages for the AND model, query/reply for the OR model, with an example WFG.',
 'ricart_agrawala': 'REQUEST/REPLY with timestamps, deferred replies, 2(N−1) messages, example run.',
 'recovery_basics': 'Checkpoint, local checkpoint, consistent state, orphan/lost/in-transit messages, domino effect, livelock, cascaded rollback, issues in failure recovery.',
 'agreement_failures': 'Byzantine agreement: n > 3f, Lamport–Shostak–Pease (oral messages), phase-king; consensus with crash failures in f + 1 rounds.',
 'agreement_failure_free': 'Assumptions (failure model, synchronous/asynchronous, network, sender identification, authentication); agreement in failure-free systems.',
 'cloud_services': 'Compute (e.g. EC2), storage (S3, block / object / file), application services (e.g. Google App Engine, Salesforce).',
 'cloud_models': 'Public, private, hybrid, community clouds; IaaS, PaaS, SaaS — with advantages, disadvantages and how to choose for a case study.',
 'cloud_basics': 'Five essential characteristics (on-demand self-service, broad network access, pooling, rapid elasticity, measured service); scalability vs elasticity.',
}
ORDER = ['snapshot', 'logical_clocks', 'message_ordering', 'deadlock_models', 'cmh', 'recovery_basics', 'agreement_failures',
         'cloud_services', 'cloud_models', 'primitives', 'design_issues', 'ricart_agrawala', 'agreement_failure_free',
         'model_computation', 'cloud_basics']
assert set(ORDER) == set(TOP15), (set(ORDER) ^ set(TOP15))

def nm(x): return html.escape(TOPICS[x][1])
prio_html = ''.join(
    f'<tr class="{"top" if i < 10 else ""}"><td class="num rk">{i+1}</td><td><b>{nm(x)}</b><div class="tip">{TIPS[x]}</div></td>'
    f'<td class="ctr">{ROMAN[TOPICS[x][0]-1]}</td><td class="num">{len(pap[x])}/6</td><td class="num">{sum(is21(p) for p in pap[x])}/3</td></tr>'
    for i, x in enumerate(ORDER))

def bar_chart():
    rows = sorted([x for x in TOPICS], key=lambda x: (-len(pap[x]), -len(papB[x]), x))
    out = ['<div class="chart"><div class="crow chead"><div class="cl">Topic</div><div class="cu">Unit</div>'
           '<div class="cb">Papers it appeared in (out of 6)</div><div class="cr">CS3551 (of 3)</div></div>']
    for x in rows:
        n = len(pap[x]); r = sum(is21(p) for p in pap[x])
        out.append(f'<div class="crow"><div class="cl">{nm(x)}</div><div class="cu">{ROMAN[TOPICS[x][0]-1]}</div>'
                   f'<div class="cb"><div class="bar" style="width:{n/6*80:.1f}%"></div><span class="bv">{n}</span></div><div class="cr">{r}</div></div>')
    out.append('</div>'); return '\n'.join(out)

PARTNAME = {'A': 'Part A · 2 marks', 'B': 'Part B · 13 marks', 'C': 'Part C · 15 marks'}
def qcard(i, part, n, text, m, p):
    cls = {'A': 'pa', 'B': 'pb', 'C': 'pc'}[part]
    return (f'<div class="qcard {cls}"><div class="qn">{i}</div><div class="qbody"><div class="qt">{text}</div>'
            f'<div class="qmeta"><span class="bd {cls}b">{PARTNAME[part]}</span><span class="seenlbl">Q{n} in</span>{chip(p)}</div></div></div>')

def unit_pages():
    out = []
    for u in range(1, 6):
        ts = sorted([x for x in TOPICS if TOPICS[x][0] == u], key=lambda x: (-len(pap[x]), -len(papB[x])))
        must = ''.join(f'<li><b>{nm(x)}</b> <span class="muted">— {len(pap[x])} of 6 papers</span></li>' for x in ts if x in TOP15)
        brk = ' style="break-before:auto;margin-top:16pt"' if u == 1 else ''
        out.append(f'<section{brk}><div class="unitband"><div class="unum">{u+2} · Unit {ROMAN[u-1]}</div><div class="utitle">{UNIT_NAME[u]}</div></div>'
                   f'<div class="must"><div class="musth">Must-do in this unit</div><ol>{must}</ol></div>')
        i = 0
        for x in ts:
            if not qs[x]: continue
            star = ' <span class="bd hot">Top 15</span>' if x in TOP15 else ''
            out.append(f'<h3>{nm(x)}{star} <span class="muted small">· {len(pap[x])} of 6 papers</span></h3>')
            for part, n, text, m, p in sorted(qs[x], key=lambda q: ('BCA'.index(q[0]), -is21(q[4]))):
                i += 1; out.append(qcard(i, part, n, text, m, p))
        out.append('</section>')
    return '\n'.join(out)

REPEATS = [
 ('Snapshot algorithm for FIFO channels (Chandy–Lamport)', ['2023 N/D', '2024 A/M', '2024 N/D', '2021 A/M', '2021 N/D'], 'Part B 12 — five of six papers'),
 ('Distributed algorithm for total order and causal order of messages', ['2024 A/M', '2024 N/D', '2023 N/D (R17)'], 'Part B 12 and Part C 16'),
 ('Primitives for distributed communication (blocking / non-blocking, sync / async)', ['2024 A/M', '2024 N/D', '2023 N/D (R17)', '2023 N/D', '2021 N/D'], 'Part B 11 + Part A'),
 ('Design issues and challenges of distributed systems', ['2023 N/D', '2024 A/M', '2021 A/M', '2021 N/D'], 'Part B 11 and Part C 16'),
 ('Chandy–Misra–Haas algorithm (AND / OR model)', ['2023 N/D', '2024 A/M', '2024 N/D'], 'every CS3551 paper'),
 ('Issues in failure recovery', ['2023 N/D', '2024 A/M', '2024 N/D', '2021 A/M', '2021 N/D'], 'Part A almost every time; Part B twice'),
 ('Ricart–Agrawala algorithm', ['2024 A/M', '2024 N/D'], 'Part B 13 in back-to-back papers'),
 ('Cloud storage services / cloud services and platforms', ['2023 N/D', '2024 A/M', '2024 N/D'], 'Part B 15 in every CS3551 paper'),
 ('Message passing vs shared memory systems', ['2024 A/M', '2021 N/D', '2021 A/M', '2023 N/D'], 'Part A favourite'),
 ('Virtualization; characteristics of cloud computing', ['2023 N/D', '2024 A/M', '2024 N/D'], 'Part A in every CS3551 paper'),
]
rep_html = ''.join(f'<tr><td>{q}<div class="tip">{w}</div></td><td class="num big">{len(s)}×</td><td>{"".join(chip(p) for p in s)}</td></tr>' for q, s, w in REPEATS)
loo_html = ''.join(f'<tr><td>{lab(p)}</td><td class="num">{a}</td><td class="num">{b}</td></tr>'
                   for (p, a), (_, b) in zip(loo[2], loo[3]))
papers_table = ''.join(f'<tr><td>{lab(p)}</td><td>{PAPERS[p]["reg"]}</td><td class="num">{PAPERS[p]["code"]}</td>'
                       f'<td><a href="{purl(p)}">{FILES[p].split("/")[-1]}</a></td></tr>' for p in P)
partc_html = ''.join(f'<tr><td>{lab(p)}</td><td>{html.escape(q[2][:150])}{"…" if len(q[2]) > 150 else ""}</td><td>{"Unit " + ROMAN[TOPICS[q[3]][0]-1] if q[3] in TOPICS else "not in CS3551"}</td></tr>'
                     for p in P for q in PAPERS[p]['Q'] if q[0] == 'C')
TOC = [("1", "Key findings", ""), ("2", "What to study first", "top 15 topics, 3 per unit"),
       ("3–7", "Question bank, Unit I to V", "every question from 6 papers, grouped by topic"),
       ("8", "Part C (15-mark) pattern", "case-study questions"), ("9", "Exam-hall tips", ""),
       ("10", "How the patterns were found", "method, repeats, chart, validation"),
       ("11", "Download the question papers", ""), ("12", "Limitations", "")]
toc_html = ''.join(f'<li><span class="n">{n}</span><span>{t}</span><span class="d">{d}</span></li>' for n, t, d in TOC)

CSS = open(os.path.join(HERE, 'style.css')).read().replace('{FONT}', FONT)

H = f"""<!doctype html><html><head><meta charset="utf-8"><title>CS3551 Distributed Computing — Exam Pattern Analysis</title><style>{CSS}</style></head><body>
<div class="cover">
 <div class="kicker">Anna University · Regulation 2021 · Semester 5</div>
 <h1>CS3551 Distributed Computing</h1>
 <div class="subt">Exam pattern analysis and must-study questions, built from every previous paper we could get: 3 CS3551 papers (2023–2024) and 3 CS8603 Distributed Systems papers (2021–2023).</div>
 <div class="tiles">
  <div class="tile"><div class="big">15</div><div class="lbl">topics (3 per unit) cover the whole Part B + Part C of every CS3551 paper so far</div></div>
  <div class="tile"><div class="big">5/6</div><div class="lbl">papers asked the snapshot / global-state algorithm in Part B</div></div>
  <div class="tile"><div class="big">3/3</div><div class="lbl">CS3551 papers asked Chandy–Misra–Haas and cloud services</div></div>
 </div>
 <div class="inside"><h4>Inside this guide</h4><ul class="toc">{toc_html}</ul></div>
 <div class="foot">Papers, this PDF and the analysis code: <a href="{REPO}/tree/main/{SUB}">{REPO}/tree/main/{SUB}</a><br>Unofficial study aid, not affiliated with Anna University. Free to share.</div>
</div>

<section style="break-before:auto">
<h2><span class="no">1</span>Key findings</h2>
<div class="lede">The short version. Data and method are in Section 10.</div>
<div class="findings">
 <div class="finding"><div class="num">Unit II</div><div class="h">The heaviest unit</div><p>Logical clocks (6/6 papers), snapshot / global state (5/6) and message ordering (5/6). Part C of Nov/Dec 2024 was also from here.</p></div>
 <div class="finding"><div class="num">3 + 2 + 1</div><div class="h">Paper format</div><p>Part A 10 × 2, Part B 5 × 13 (one per unit, a OR b), Part C 1 × 15 (a OR b, usually a case study). Q11 = Unit I … Q15 = Unit V.</p></div>
 <div class="finding"><div class="num">15 topics</div><div class="h">3 per unit is the safe minimum</div><p>Studying 2 topics per unit gave 39–67/80 on unseen papers. Studying 3 per unit gave 67–80/80 on the CS3551 papers (Section 10.4).</p></div>
 <div class="finding"><div class="num">Cloud</div><div class="h">Unit V is new and predictable</div><p>Every CS3551 paper asked cloud services in Part B 15 and virtualization / cloud characteristics in Part A.</p></div>
</div>
<div class="callout"><div class="t">How to prepare each topic</div>Learn the definition, a neat diagram, the algorithm steps (with message types) and one worked example. Examiners in this subject give most marks for diagrams and step-by-step algorithms. For Part A, also learn: message passing vs shared memory, virtualization, cloud characteristics, issues in failure recovery, scalar vs vector time.</div>
<div class="callout warn"><div class="t">Honest note</div>Only 6 papers exist so far (CS3551 started in 2023), so the patterns are less certain than for older subjects. Papers from April/May 2025 onwards could not be downloaded (they sit behind Studocu and Scribd login walls). Use this to prioritise, not to skip units.</div>
</section>

<section>
<h2><span class="no">2</span>What to study first</h2>
<div class="lede">The top 15 topics, 3 per unit, in priority order. The first 10 rows are the minimum plan; all 15 is the safe plan.</div>
<table class="prio"><tr><th>#</th><th>Topic and what to cover</th><th class="ctr">Unit</th><th class="num">Papers</th><th class="num">CS3551</th></tr>{prio_html}</table>
</section>

<section>
<h2><span class="no">3–7</span>Question bank, Unit by Unit</h2>
<div class="lede">Every question from the 6 papers (Part A, B and C), grouped by topic. Topics are in order of frequency. Click a session tag to open that paper. CS8603 questions on P2P, distributed shared memory, Maekawa and rendezvous are left out because they are not in the CS3551 syllabus.</div>
<div class="legend"><span><span class="bd pbb">Part B · 13 marks</span></span><span><span class="bd pcb">Part C · 15 marks</span></span><span><span class="bd pab">Part A · 2 marks</span></span>
<span><span class="chip r21c">2024 A/M</span> CS3551 paper</span><span><span class="chip">2021 N/D · CS8603</span> older-syllabus paper</span><span><span class="bd hot">Top 15</span> in the study list</span></div>
</section>
{unit_pages()}

<section>
<h2><span class="no">8</span>Part C (15-mark) pattern</h2>
<div class="lede">Part C is one question with an (a) OR (b) choice. CS3551 papers mostly give a real-life case study (“a company wants…”) that tests a Unit I, IV or V topic, or a deep version of a Unit II algorithm.</div>
<table><tr><th>Paper</th><th>Question</th><th>Unit</th></tr>{partc_html}</table>
<div class="callout"><div class="t">How to answer a case study</div>Restate the scenario in one line, pick a model or algorithm and name it, draw the architecture, then justify with 4–5 points (cost, scalability, security, fault tolerance, maintenance) and end with a short conclusion.</div>

<h2 style="margin-top:20pt"><span class="no">9</span>Exam-hall tips</h2>
<ul class="tips">
<li><b>Read both (a) and (b)</b> of every question first, and pick the one where you can draw a diagram.</li>
<li><b>Algorithms</b> (Chandy–Lamport, Ricart–Agrawala, CMH, Koo–Toueg): write the system model and assumptions, the message types, the steps, a space-time or WFG diagram, an example, and the message complexity.</li>
<li><b>Comparisons</b> (shared memory vs message passing, AND vs OR model, scalability vs elasticity): answer in a table.</li>
<li><b>13 marks ≈ 4–5 handwritten pages</b>; Part C 15 marks ≈ 5–6 pages.</li>
</ul>
</section>

<section>
<h2><span class="no">10</span>How the patterns were found</h2>
<h3>10.1 Method</h3>
<ol class="steps">
<li><b>Collected every available paper.</b> CS3551 papers exist only from Nov/Dec 2023, so the three CS8603 Distributed Systems (R2017) papers were added. CS8603 shares Units I–IV with CS3551; its Unit V (P2P, distributed shared memory) is not in CS3551, so those questions were left out of the counts.</li>
<li><b>Read every question by hand</b> from the scans and tagged it with the CS3551 topic it needs.</li>
<li><b>Counted frequency</b> per topic: in how many of the 6 papers, and of the 3 CS3551 papers, it appeared (10.3).</li>
<li><b>Simulated a student.</b> Each Part B unit and Part C is “(a) OR (b)”. For a study list, each question scores the better side it covers. Total out of 80 (Part B 65 + Part C 15).</li>
<li><b>Tested on unseen papers (leave-one-out).</b> Hide one paper, build the list from the other five, score the hidden paper. Repeat for all six (10.4).</li>
</ol>
<h3>10.2 Questions that repeat</h3>
<table><tr><th>Question</th><th class="num">Times</th><th>Papers</th></tr>{rep_html}</table>
<h3>10.3 How often each topic appears</h3>
{bar_chart()}
<h3>10.4 Leave-one-out test</h3>
<p class="small">Part B + Part C marks (out of 80) on each hidden paper, using a list built only from the other five papers.</p>
<table><tr><th>Hidden paper</th><th class="num">Top 2 per unit (10 topics)</th><th class="num">Top 3 per unit (15 topics)</th></tr>{loo_html}</table>
<div class="callout">With 3 topics per unit, the hidden CS3551 papers scored {", ".join(str(b) for p, b in loo[3] if is21(p))} out of 80. The final 15-topic list (built from all six papers) covers <b>{", ".join(str(final[p]) for p in r21)}</b> out of 80 in the three CS3551 papers. The CS8603 papers score lower only because their Unit V is a different syllabus.</div>
</section>

<section>
<h2><span class="no">11</span>Download the question papers</h2>
<table><tr><th>Session</th><th>Regulation · subject</th><th class="num">QP code</th><th>File</th></tr>{papers_table}</table>
<h2 style="margin-top:20pt"><span class="no">12</span>Limitations</h2>
<ul class="tips">
<li>Only 6 papers, and only 3 from the current CS3551 syllabus. Patterns may shift as more papers appear.</li>
<li>April/May 2025, Nov/Dec 2025 and April/May 2026 papers are on Studocu / Scribd behind logins and were not used. If you have them, share them through the repository and the analysis will be updated.</li>
<li>Questions were typed by hand from scans; check the original paper through the links if something looks wrong.</li>
<li>Paper sources: EnggTree, Brainkart, Poriyaan, Learnskart, St. Anne’s CET and Sri Sairam EC libraries. Unofficial; not affiliated with Anna University.</li>
</ul>
</section>
</body></html>"""
out = os.path.join(HERE, 'CS3551_Exam_Pattern_Analysis.html'); open(out, 'w', encoding='utf-8').write(H); print(out)
