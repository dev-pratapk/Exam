import sys; sys.path.insert(0, '.')
from papers import PAPERS, TOPICS
from collections import defaultdict
P = list(PAPERS)

def score(p, S):
    """Part B + C marks (out of 80) if you can solve every question whose topic is in S; each (a) OR (b) pair scores the better side."""
    qs = {q[1]: q for q in PAPERS[p]['Q'] if q[0] in 'BC'}
    tot = 0
    for k in ['11', '12', '13', '14', '15', '16']:
        tot += max((qs[k + s][4] if qs[k + s][3] in S else 0) for s in 'ab')
    return tot

def rank(train, per_unit):
    f = defaultdict(float)
    for p in train:
        for part, n, t, topic, m in PAPERS[p]['Q']:
            f[topic] += (1.0 if part in 'BC' else 0.25)
    S = []
    for u in range(1, 6):
        S += sorted([x for x in TOPICS if TOPICS[x][0] == u], key=lambda x: (-f[x], x))[:per_unit]
    return S

if __name__ == '__main__':
    pap = defaultdict(set); papB = defaultdict(set)
    for p in P:
        for part, n, t, topic, m in PAPERS[p]['Q']:
            pap[topic].add(p)
            if part in 'BC': papB[topic].add(p)
    print('topic frequency (papers of 2; part B/C papers)')
    for x in sorted(TOPICS, key=lambda x: (TOPICS[x][0], -len(papB[x]))):
        print(f'U{TOPICS[x][0]} {len(pap[x])}/2 B/C {len(papB[x])}/2  {TOPICS[x][1]}')
    print('\nleave-one-out (Part B+C /80):')
    for k in (1, 2):
        print(f' top {k} per unit:', {p: score(p, rank([q for q in P if q != p], k)) for p in P})
    print(' all B/C topics seen in the other paper:', {p: score(p, {x for q in P if q != p for part, n, t, x, m in PAPERS[q]['Q'] if part in 'BC'}) for p in P})
    print(' every topic of both papers:', {p: score(p, set(TOPICS)) for p in P})
