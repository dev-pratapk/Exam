"""Exact (fraction) solvers that print HTML tableaux: Big-M simplex, dual simplex, transportation (VAM + MODI)."""
from fractions import Fraction as F

def fm(x):
    x = F(x)
    return str(x.numerator) if x.denominator == 1 else f'{x.numerator}/{x.denominator}'

class MN:
    """a + b*M with M a very large positive number (compared lexicographically)."""
    def __init__(self, b=0, a=0): self.b = F(b); self.a = F(a)
    def __add__(s, o): o = o if isinstance(o, MN) else MN(0, o); return MN(s.b + o.b, s.a + o.a)
    __radd__ = __add__
    def __sub__(s, o): o = o if isinstance(o, MN) else MN(0, o); return MN(s.b - o.b, s.a - o.a)
    def __mul__(s, k): k = F(k); return MN(s.b * k, s.a * k)
    __rmul__ = __mul__
    def __neg__(s): return MN(-s.b, -s.a)
    def key(s): return (s.b, s.a)
    def __lt__(s, o): return s.key() < o.key()
    def __gt__(s, o): return s.key() > o.key()
    def pos(s): return s.key() > (0, 0)
    def neg(s): return s.key() < (0, 0)
    def html(s):
        if s.b == 0: return fm(s.a)
        t = ('' if s.b == 1 else '−' if s.b == -1 else fm(s.b)) + 'M'
        if s.a == 0: return t
        return t + (' + ' if s.a > 0 else ' − ') + fm(abs(s.a))

def table(head, rows, caption=None, hl=None):
    h = '<table class="tt">' + (f'<caption>{caption}</caption>' if caption else '')
    h += '<tr>' + ''.join(f'<th>{c}</th>' for c in head) + '</tr>'
    for i, r in enumerate(rows):
        h += '<tr>' + ''.join(f'<td{" style=\"font-weight:700\"" if hl and (i, j) == hl else ""}>{c}</td>' for j, c in enumerate(r)) + '</tr>'
    return h + '</table>'

def sub(name):
    import re
    return re.sub(r'([a-z])(\d+)$', r'\1<sub>\2</sub>', name)

def big_m_simplex(c, A, b, senses, names, maximize=True, show=True):
    """c: objective coefficients (to maximize), A rows, b rhs>=0, senses in '<=','>=','='. Returns (html, solution dict, z)."""
    n, m = len(c), len(A)
    cols = list(names); cost = [MN(0, F(x)) for x in c]; rows = [[F(x) for x in r] for r in A]
    basis = []; art = []
    for i, s in enumerate(senses):
        for r in range(m): rows[r].append(F(0))
        if s == '<=':
            rows[i][-1] = F(1); cols.append(f's{i+1}'); cost.append(MN()); basis.append(len(cols) - 1)
        elif s == '>=':
            rows[i][-1] = F(-1); cols.append(f's{i+1}'); cost.append(MN())
            for r in range(m): rows[r].append(F(0))
            rows[i][-1] = F(1); cols.append(f'a{i+1}'); cost.append(MN(-1, 0)); basis.append(len(cols) - 1); art.append(len(cols) - 1)
        else:
            rows[i][-1] = F(1); cols.append(f'a{i+1}'); cost.append(MN(-1, 0)); basis.append(len(cols) - 1); art.append(len(cols) - 1)
    # pad rows to same length
    L = len(cols)
    rows = [r + [F(0)] * (L - len(r)) for r in rows]
    rhs = [F(x) for x in b]
    out = []; it = 0
    while True:
        zj = [MN() for _ in range(L)]; zval = MN()
        for i in range(m):
            for j in range(L): zj[j] = zj[j] + cost[basis[i]] * rows[i][j]
            zval = zval + cost[basis[i]] * rhs[i]
        d = [cost[j] - zj[j] for j in range(L)]
        ent = max(range(L), key=lambda j: d[j].key()) if any(x.pos() for x in d) else None
        head = ['Basis', 'C<sub>B</sub>'] + [sub(x) for x in cols] + ['RHS'] + (['Ratio'] if ent is not None else [])
        ratios = []
        leave = None
        if ent is not None:
            for i in range(m):
                if rows[i][ent] > 0: ratios.append(rhs[i] / rows[i][ent])
                else: ratios.append(None)
            valid = [(r, i) for i, r in enumerate(ratios) if r is not None]
            if not valid: out.append('<p>Unbounded.</p>'); return '\n'.join(out), None, None
            leave = min(valid)[1]
        body = []
        for i in range(m):
            body.append([sub(cols[basis[i]]), cost[basis[i]].html()] + [fm(x) for x in rows[i]] + [fm(rhs[i])] + ([fm(ratios[i]) if ratios[i] is not None else '–'] if ent is not None else []))
        body.append(['<b>C<sub>j</sub> − Z<sub>j</sub></b>', ''] + [x.html() for x in d] + [f'Z = {zval.html()}'] + ([''] if ent is not None else []))
        it += 1
        cap = f'Table {it}' + ('' if ent is not None else ' (optimal)')
        out.append(table(head, body, cap))
        if ent is not None:
            out.append(f'<p class="note">Entering variable: {sub(cols[ent])} (largest C<sub>j</sub> − Z<sub>j</sub> = {d[ent].html()}). Leaving variable: {sub(cols[basis[leave]])} (minimum ratio {fm(ratios[leave])}). Pivot element = {fm(rows[leave][ent])}.</p>')
        if ent is None: break
        p = rows[leave][ent]
        rows[leave] = [x / p for x in rows[leave]]; rhs[leave] /= p
        for i in range(m):
            if i != leave and rows[i][ent] != 0:
                f = rows[i][ent]; rows[i] = [a - f * bb for a, bb in zip(rows[i], rows[leave])]; rhs[i] -= f * rhs[leave]
        basis[leave] = ent
    sol = {cols[basis[i]]: rhs[i] for i in range(m)}
    arts_in = [cols[j] for j in art if cols[j] in sol and sol[cols[j]] != 0]
    return '\n'.join(out), sol, zval, arts_in

def dual_simplex(c, A, b, names):
    """Maximize c.x s.t. A x <= b (b may be negative), x>=0, with all c_j <= 0 (dual feasible). Slack s_i added."""
    n, m = len(c), len(A)
    cols = list(names) + [f's{i+1}' for i in range(m)]
    rows = [[F(x) for x in A[i]] + [F(1) if k == i else F(0) for k in range(m)] for i in range(m)]
    rhs = [F(x) for x in b]; cost = [F(x) for x in c] + [F(0)] * m
    basis = [n + i for i in range(m)]; out = []; it = 0
    while True:
        zj = [sum(cost[basis[i]] * rows[i][j] for i in range(m)) for j in range(len(cols))]
        d = [cost[j] - zj[j] for j in range(len(cols))]; zval = sum(cost[basis[i]] * rhs[i] for i in range(m))
        neg = [(rhs[i], i) for i in range(m) if rhs[i] < 0]
        leave = min(neg)[1] if neg else None
        ent = None
        if leave is not None:
            cand = [(abs(d[j] / rows[leave][j]), j) for j in range(len(cols)) if rows[leave][j] < 0]
            if not cand: out.append('<p>Infeasible.</p>'); return '\n'.join(out), None, None
            ent = min(cand)[1]
        head = ['Basis', 'C<sub>B</sub>'] + [sub(x) for x in cols] + ['RHS']
        body = [[sub(cols[basis[i]]), fm(cost[basis[i]])] + [fm(x) for x in rows[i]] + [fm(rhs[i])] for i in range(m)]
        body.append(['<b>C<sub>j</sub> − Z<sub>j</sub></b>', ''] + [fm(x) for x in d] + [f'Z′ = {fm(zval)}'])
        it += 1; out.append(table(head, body, f'Table {it}' + ('' if leave is not None else ' (optimal)')))
        if leave is None: break
        out.append(f'<p class="note">Leaving variable: {sub(cols[basis[leave]])} (most negative RHS = {fm(rhs[leave])}). Entering variable: {sub(cols[ent])} (minimum of |C<sub>j</sub> − Z<sub>j</sub>| / |a<sub>rj</sub>| = {fm(abs(d[ent] / rows[leave][ent]))}). Pivot element = {fm(rows[leave][ent])}.</p>')
        p = rows[leave][ent]; rows[leave] = [x / p for x in rows[leave]]; rhs[leave] /= p
        for i in range(m):
            if i != leave and rows[i][ent] != 0:
                f = rows[i][ent]; rows[i] = [a - f * bb for a, bb in zip(rows[i], rows[leave])]; rhs[i] -= f * rhs[leave]
        basis[leave] = ent
    return '\n'.join(out), {cols[basis[i]]: rhs[i] for i in range(m)}, zval

# ---------------------------------------------------------------- transportation
def vam(cost, supply, demand):
    m, n = len(cost), len(cost[0]); s = list(supply); d = list(demand)
    alloc = [[None] * n for _ in range(m)]; rows = set(range(m)); cols = set(range(n)); steps = []
    while rows and cols:
        rp = {}; cp = {}
        for i in rows:
            v = sorted(cost[i][j] for j in cols); rp[i] = (v[1] - v[0]) if len(v) > 1 else v[0]
        for j in cols:
            v = sorted(cost[i][j] for i in rows); cp[j] = (v[1] - v[0]) if len(v) > 1 else v[0]
        mr = max(rp.values()); mc = max(cp.values())
        if mr >= mc:
            i = max([r for r in rows if rp[r] == mr], key=lambda r: -min(cost[r][j] for j in cols)); j = min(cols, key=lambda j: (cost[i][j], j))
            kind = f'row {i+1} (penalty {mr})'
        else:
            j = max([c for c in cols if cp[c] == mc], key=lambda c: -min(cost[i][c] for i in rows)); i = min(rows, key=lambda i: (cost[i][j], i))
            kind = f'column {j+1} (penalty {mc})'
        q = min(s[i], d[j]); alloc[i][j] = q; s[i] -= q; d[j] -= q
        steps.append((dict(rp), dict(cp), kind, (i, j, q)))
        if s[i] == 0 and (d[j] != 0 or len(rows) == 1): rows.discard(i)
        elif d[j] == 0: cols.discard(j)
        if s[i] == 0 and d[j] == 0 and len(rows) > 0 and len(cols) > 0:
            pass
    return alloc, steps

def modi(cost, alloc, maximize_profit=None):
    """MODI optimisation. Returns (html, alloc, total_cost)."""
    m, n = len(cost), len(cost[0]); out = []; it = 0
    basic = {(i, j) for i in range(m) for j in range(n) if alloc[i][j] is not None}
    # degeneracy fix
    while len(basic) < m + n - 1:
        for i in range(m):
            for j in range(n):
                if (i, j) not in basic:
                    trial = basic | {(i, j)}
                    if not has_cycle(trial, m, n): basic = trial; alloc[i][j] = F(0); break
            else: continue
            break
    while True:
        u = [None] * m; v = [None] * n; u[0] = F(0)
        ch = True
        while ch:
            ch = False
            for (i, j) in basic:
                if u[i] is not None and v[j] is None: v[j] = F(cost[i][j]) - u[i]; ch = True
                elif v[j] is not None and u[i] is None: u[i] = F(cost[i][j]) - v[j]; ch = True
        delta = {(i, j): F(cost[i][j]) - u[i] - v[j] for i in range(m) for j in range(n) if (i, j) not in basic}
        it += 1
        head = [''] + [f'D<sub>{j+1}</sub>' for j in range(n)] + ['u<sub>i</sub>']
        body = []
        for i in range(m):
            body.append([f'O<sub>{i+1}</sub>'] + [(f'{cost[i][j]} [{fm(alloc[i][j])}]' if (i, j) in basic else f'{cost[i][j]} (Δ = {fm(delta[(i, j)])})') for j in range(n)] + [fm(u[i])])
        body.append(['v<sub>j</sub>'] + [fm(x) for x in v] + [''])
        total = sum(F(cost[i][j]) * alloc[i][j] for (i, j) in basic)
        out.append(table(head, body, f'Table {it}: cost in each cell, [allocation] for occupied cells, Δ<sub>ij</sub> = c<sub>ij</sub> − u<sub>i</sub> − v<sub>j</sub> for empty cells. Total cost = {fm(total)}'))
        neg = [(dv, k) for k, dv in delta.items() if dv < 0]
        if not neg:
            out.append('<p class="note">All Δ<sub>ij</sub> ≥ 0, so this solution is optimal.</p>'); break
        dv, (ei, ej) = min(neg)
        cyc = find_cycle(basic, (ei, ej), m, n)
        minus = cyc[1::2]; theta = min(alloc[i][j] for (i, j) in minus)
        out.append(f'<p class="note">Most negative Δ is Δ<sub>{ei+1}{ej+1}</sub> = {fm(dv)}. Loop: {" → ".join(f"({i+1},{j+1})" for i, j in cyc)}. Shift θ = {fm(theta)} units around the loop.</p>')
        for k, (i, j) in enumerate(cyc):
            alloc[i][j] = (alloc[i][j] or F(0)) + (theta if k % 2 == 0 else -theta)
        leave = next((c for c in minus if alloc[c[0]][c[1]] == 0), None)
        basic.add((ei, ej)); basic.discard(leave)
        for (i, j) in list(minus):
            if alloc[i][j] == 0 and (i, j) != leave: alloc[i][j] = F(0)
        for i in range(m):
            for j in range(n):
                if (i, j) not in basic: alloc[i][j] = None
    return '\n'.join(out), alloc, total

def has_cycle(cells, m, n):
    adj = {}
    for (i, j) in cells: adj.setdefault(('r', i), []).append(('c', j)); adj.setdefault(('c', j), []).append(('r', i))
    seen = set()
    def dfs(node, parent):
        seen.add(node)
        for nb in adj.get(node, []):
            if nb == parent: continue
            if nb in seen or dfs(nb, node): return True
        return False
    return any(dfs(x, None) for x in list(adj) if x not in seen)

def find_cycle(basic, start, m, n):
    cells = set(basic) | {start}
    def rec(path, horizontal):
        i, j = path[-1]
        cand = [(i, c) for c in range(n) if c != j and (i, c) in cells] if horizontal else [(r, j) for r in range(m) if r != i and (r, j) in cells]
        for nxt in cand:
            if nxt == start and len(path) >= 4 and len(path) % 2 == 0: return path
            if nxt in path: continue
            r = rec(path + [nxt], not horizontal)
            if r: return r
        return None
    return rec([start], True) or rec([start], False)
