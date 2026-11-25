"""Send each part of Model Question Paper 1 to DeepSeek (via opencode) as a separate job."""
import os, re, sys, subprocess, concurrent.futures as cf
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, '/home/ubuntu/work/lab/ma3354/repo/model-papers')
import build_model as bm   # noqa: E402  (imports PAPERS; writes an html file we ignore)

P1 = bm.PAPERS[0]
def plain(t):  # strip html/figure tags for the prompt
    t = re.sub(r'<div class="fig">.*?</div>', '', t)
    t = re.sub(r'<span class="mat">.*?</span>', '[[0,1,1,0],[1,0,0,1],[1,0,0,1],[0,1,1,0]] (rows = vertices v1..v4)', t)
    t = t.replace('<sub>', '_').replace('</sub>', '').replace('<sup>', '^').replace('</sup>', '')
    return re.sub(r'<[^>]+>', '', t)

FIGS = {
 (13, 'a', '(ii)'): """FIGURE (draw it yourself in SVG; the reader of the question sees this picture):
G1: 8 vertices. Outer square TL, TR, BR, BL (edges TL–TR, TR–BR, BR–BL, BL–TL). Inner square tl, tr, br, bl (edges tl–tr, tr–br, br–bl, bl–tl).
    Two connecting edges: TR–tr and BL–bl.  (10 edges)
G2: 8 vertices. Same outer square and inner square, but the two connecting edges are TL–tl and TR–tr.  (10 edges)
Correct conclusion: NOT isomorphic. Both have 8 vertices, 10 edges, degree sequence (3,3,3,3,2,2,2,2), but in G2 the four
degree-3 vertices TL, TR, tr, tl form a 4-cycle (4 edges among them), while in G1 the degree-3 vertices TR, tr, BL, bl have only
2 edges among them (TR–tr, BL–bl). An isomorphism preserves adjacency between degree-3 vertices, so no isomorphism exists.
(Name the vertices u1..u8 for G1 and v1..v8 for G2 in your answer and show the comparison table.)""",
 (13, 'b', '(ii)'): """FIGURE (draw all three graphs in SVG):
G1: vertices A, B, C, D, E. Edges: A–B, A–C, A–D, B–D, B–E, C–D, D–E (7 edges). Degrees: A3, B3, C2, D4, E2.
    Exactly two odd vertices (A, B) ⇒ Euler path but no Euler circuit. Example Euler path: A–C–D–A–B–D–E–B.
G2: regular hexagon A, B, C, D, E, F (edges AB, BC, CD, DE, EF, FA) plus the three long diagonals A–D, B–E, C–F which cross at the
    centre point labelled Q. Each of A..F has degree 3 (if Q is taken as a vertex, deg Q = 6 and A..F still have degree 3).
    Six odd vertices ⇒ neither an Euler path nor an Euler circuit.
G3: complete graph K5 on A, B, C, D, E (pentagon + all diagonals, 10 edges). Every vertex has degree 4 ⇒ Euler circuit
    (hence also an Euler path). Example circuit: A–B–C–D–E–A–C–E–B–D–A.""",
}
KEY = {
 (12, 'a', '(i)'): 'Check value: T(k) = −9·2^k + 2·5^k + 2k + 8 (T(2) = 26, T(3) = 192).',
 (12, 'a', '(ii)'): 'Check value: divisible by at least one of 2,3,5,7 = 293 − 117 + 18 − 1 = 193, so the answer is 250 − 193 = 57.',
 (15, 'b', '(ii)'): 'Check values: lower bounds of 10 and 15 = {1, 5}; GLB = 5; upper bounds = {30}; LUB = 30. Hasse diagram of D30 is a cube.',
}

def job_prompt(job):
    head = ('Read SPEC.md in the current directory and follow it exactly.\n'
            'Paper header: B.E./B.Tech. MA3354 Discrete Mathematics, Regulations 2021, Model Question Paper 1.\n')
    if job == 'partA':
        qs = '\n'.join(f'{k+1}. {plain(t)}' for k, (t, s) in enumerate(P1['A']))
        return head + (f'Your part: PART A (10 × 2 = 20 marks). Answer all ten 2-mark questions below.\n{qs}\n'
                       'Use data-q="1" … data-q="10" and data-pages="0.5" for each.\n'
                       'For Q5 construct an explicit simple graph (draw it) with degrees 3,3,3,3,2. For Q6 draw the 4-cycle v1–v2–v4–v3–v1. '
                       'For Q9 draw the Hasse diagram of D24 (covers: 1–2, 1–3, 2–4, 2–6, 3–6, 4–8, 4–12, 6–12, 8–24, 12–24).\n'
                       'Write the file out/partA.html.')
    q, side = int(job[:2]), job[2]
    subs = P1['B'][q][side]
    lines = []
    for sub, text, marks, src in subs:
        extra = '\n'.join(x for x in (FIGS.get((q, side, sub)), KEY.get((q, side, sub))) if x)
        lines.append(f'{q} ({side}) {sub} [{marks} marks]: {plain(text)}' + (f'\n{extra}' if extra else ''))
    body = '\n\n'.join(lines)
    return head + (f'Your part: PART B, Question {q} ({side}) — answer every sub-part below (one <div class="ans"> per sub-part, '
                   f'data-q like "{q} ({side}) (i)").\n\n{body}\n\nWrite the file out/{job}.html.')

def run(job):
    prompt = job_prompt(job)
    open(f'{HERE}/prompts/{job}.txt', 'w').write(prompt)
    with open(f'{HERE}/logs/{job}.log', 'w') as log:
        r = subprocess.run(['opencode', 'run', '-m', 'opencode/deepseek-v4.1-flash-free', prompt],
                           cwd=HERE, stdout=log, stderr=subprocess.STDOUT, timeout=1500,
                           env={**os.environ, 'PATH': os.path.expanduser('~/.local/bin') + ':' + os.environ['PATH']})
    ok = os.path.exists(f'{HERE}/out/{job}.html')
    return job, r.returncode, ok

if __name__ == '__main__':
    os.makedirs(f'{HERE}/out', exist_ok=True); os.makedirs(f'{HERE}/logs', exist_ok=True); os.makedirs(f'{HERE}/prompts', exist_ok=True)
    jobs = sys.argv[1:] or ['partA'] + [f'{q}{s}' for q in range(11, 16) for s in 'ab']
    with cf.ThreadPoolExecutor(max_workers=4) as ex:
        for job, rc, ok in ex.map(run, jobs):
            print(f'{job}: exit={rc} file={"yes" if ok else "NO"}', flush=True)
