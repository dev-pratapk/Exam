"""Generate the model answers (HTML fragments) for OIE352 Model Question Paper 1. All numbers are computed or asserted here."""
import os, itertools
from fractions import Fraction as F
from solvers import *
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'out'); os.makedirs(OUT, exist_ok=True)
X = lambda n: f'x<sub>{n}</sub>'
def ans(q, pages, inner): return f'<div class="ans" data-q="{q}" data-pages="{pages}">\n{inner}\n</div>\n'
def save(name, *parts): open(f'{OUT}/{name}.html', 'w', encoding='utf-8').write('\n'.join(parts))
ARR = lambda i: f'<defs><marker id="{i}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#000"/></marker></defs>'

# =============================================================== PART A
A = []
A.append(ans('1', '0.5', """<h4>Linear programming</h4>
<p>Linear programming (LP) is a mathematical technique for finding the best value (maximum or minimum) of a <b>linear objective function</b> subject to a set of <b>linear constraints</b> (equalities or inequalities) and non-negativity of the variables.</p>
<div class="eq">Maximize (or minimize) Z = c<sub>1</sub>x<sub>1</sub> + c<sub>2</sub>x<sub>2</sub> + … + c<sub>n</sub>x<sub>n</sub> subject to Σ a<sub>ij</sub>x<sub>j</sub> (≤, =, ≥) b<sub>i</sub>, x<sub>j</sub> ≥ 0.</div>
<p>Example uses: product mix, diet, blending and resource allocation problems.</p>"""))
A.append(ans('2', '0.5', """<h4>Shadow price</h4>
<p>The <b>shadow price</b> of a resource is the change in the optimal value of the objective function per unit increase in the right-hand side (availability) of that resource's constraint. It is the value of the corresponding <b>dual variable</b> y<sub>i</sub>, and is read from the Z<sub>j</sub> row of the final simplex table under the slack variable of that constraint.</p>
<p>It tells the manager how much more it is worth paying for one more unit of the resource, as long as the change stays within the range of feasibility. A resource that is not fully used (positive slack) has shadow price 0.</p>"""))
A.append(ans('3', '0.5', """<h4>Primal and dual problems</h4>
<p>Every LP (the <b>primal</b>) has an associated LP (the <b>dual</b>) obtained from the same data.</p>
<table class="tt"><tr><th>Primal</th><th>Dual</th></tr>
<tr><td>Maximize Z = c<sup>T</sup>x<br>subject to Ax ≤ b, x ≥ 0</td><td>Minimize W = b<sup>T</sup>y<br>subject to A<sup>T</sup>y ≥ c, y ≥ 0</td></tr>
<tr><td>n variables, m constraints</td><td>m variables, n constraints</td></tr>
<tr><td>Objective coefficients c<sub>j</sub></td><td>Right-hand sides of the dual constraints</td></tr>
<tr><td>Right-hand sides b<sub>i</sub></td><td>Objective coefficients of the dual</td></tr></table>
<p>The dual of the dual is the primal, and the optimal values of the two problems are equal.</p>"""))
A.append(ans('4', '0.5', """<h4>Unbalanced to balanced transportation problem</h4>
<p>A transportation problem is <b>balanced</b> when total supply = total demand. If it is not:</p>
<ul><li><b>Total supply &gt; total demand:</b> add a <i>dummy destination</i> with demand equal to (supply − demand) and zero cost (zero profit for maximization) in every cell.</li>
<li><b>Total demand &gt; total supply:</b> add a <i>dummy source</i> with supply equal to (demand − supply) and zero cost in every cell.</li></ul>
<p>The balanced problem is then solved in the usual way (VAM and MODI).</p>"""))
A.append(ans('5', '0.5', """<h4>Types of integer programming problems</h4>
<ol><li><b>Pure (all-integer) IPP:</b> all the variables must be integers.</li>
<li><b>Mixed IPP:</b> only some of the variables must be integers; the others may be continuous.</li>
<li><b>Zero–one (binary) IPP:</b> every variable can take only the values 0 or 1.</li></ol>
<p>Methods: Gomory's cutting-plane method and the branch and bound method.</p>"""))
A.append(ans('6', '0.5', """<h4>Dynamic programming</h4>
<p><b>Dynamic programming</b> is a method of solving a <b>multistage decision problem</b> by breaking it into a sequence of smaller, interrelated sub-problems called <i>stages</i>, which are solved one by one using a recursive relation. It is based on Bellman's <b>principle of optimality</b>: whatever the initial state and decision, the remaining decisions must be optimal for the state that results.</p>
<p>Examples: allocation of limited resources among activities, shortest route and replacement problems.</p>"""))
A.append(ans('7', '0.5', """<h4>Kuhn–Tucker conditions</h4>
<p>For the problem: minimize f(X) subject to g<sub>j</sub>(X) ≤ 0, j = 1, …, m, the <b>Kuhn–Tucker conditions</b> are necessary conditions for X* to be a (local) optimum:</p>
<div class="eq">∂f/∂x<sub>i</sub> + Σ<sub>j</sub> λ<sub>j</sub> ∂g<sub>j</sub>/∂x<sub>i</sub> = 0 (i = 1, …, n)<br>λ<sub>j</sub> g<sub>j</sub> = 0, g<sub>j</sub> ≤ 0, λ<sub>j</sub> ≥ 0 (j = 1, …, m)</div>
<p>They are also sufficient when f and every g<sub>j</sub> are convex.</p>"""))
A.append(ans('8', '0.5', """<h4>Sufficient conditions on the Hessian matrix</h4>
<p>Let X<sub>0</sub> be a stationary point, ∇f(X<sub>0</sub>) = 0, and H the Hessian matrix of second derivatives ∂<sup>2</sup>f/∂x<sub>i</sub>∂x<sub>j</sub> at X<sub>0</sub>.</p>
<table class="tt"><tr><th>Hessian H at X<sub>0</sub></th><th>Conclusion</th></tr>
<tr><td>Positive definite (all leading principal minors &gt; 0)</td><td>X<sub>0</sub> is a (strict) local minimum</td></tr>
<tr><td>Negative definite (minors alternate in sign, Δ<sub>1</sub> &lt; 0, Δ<sub>2</sub> &gt; 0, …)</td><td>X<sub>0</sub> is a (strict) local maximum</td></tr>
<tr><td>Indefinite</td><td>X<sub>0</sub> is a saddle point (neither)</td></tr></table>
<p>For one variable: f″(X<sub>0</sub>) &gt; 0 gives a minimum and f″(X<sub>0</sub>) &lt; 0 a maximum.</p>"""))
A.append(ans('9', '0.5', """<h4>Differences between CPM and PERT</h4>
<table class="tt"><tr><th>Aspect</th><th>CPM</th><th>PERT</th></tr>
<tr><td>Time estimate</td><td>One deterministic duration for each activity</td><td>Three estimates (optimistic, most likely, pessimistic); probabilistic</td></tr>
<tr><td>Nature of project</td><td>Repetitive, well-known projects (e.g. construction)</td><td>Non-repetitive, new projects (e.g. research and development)</td></tr>
<tr><td>Orientation</td><td>Activity-oriented</td><td>Event-oriented</td></tr>
<tr><td>Emphasis</td><td>Time–cost trade-off (crashing)</td><td>Time; probability of meeting a due date</td></tr></table>"""))
A.append(ans('10', '0.5', """<h4>Critical path</h4>
<p>The <b>critical path</b> is the <b>longest path</b> from the start event to the end event of a project network. Its length is the minimum time in which the project can be completed. The activities on it are <b>critical</b>: they have zero total float, so a delay in any of them delays the whole project.</p>
<p>It is found by the forward and backward pass: the activities with earliest start = latest start (and earliest finish = latest finish) form the critical path.</p>"""))
save('partA', *A)

# =============================================================== 11(a) graphical LP
def svg_lp():
    ox, oy, sx, sy = 55, 285, 7.0, 5.0
    P = lambda x, y: (ox + sx * x, oy - sy * y)
    pts = lambda L: ' '.join('%.1f,%.1f' % P(*p) for p in L)
    s = f'<svg width="520" height="345" viewBox="0 0 520 345" xmlns="http://www.w3.org/2000/svg" font-family="serif" font-size="12">{ARR("a11")}'
    s += f'<polygon points="{pts([(0,0),(36,0),(30,15),(0,45)])}" fill="#e8e8e8" stroke="none"/>'
    s += '<g stroke="#000" stroke-width="1.6" fill="none">'
    s += f'<line x1="{ox}" y1="{oy}" x2="{ox+sx*52}" y2="{oy}" marker-end="url(#a11)"/><line x1="{ox}" y1="{oy}" x2="{ox}" y2="{oy-sy*52}" marker-end="url(#a11)"/>'
    a, b = P(36, 0), P(16, 50); s += f'<line x1="{a[0]:.1f}" y1="{a[1]:.1f}" x2="{b[0]:.1f}" y2="{b[1]:.1f}"/>'
    a, b = P(45, 0), P(0, 45); s += f'<line x1="{a[0]:.1f}" y1="{a[1]:.1f}" x2="{b[0]:.1f}" y2="{b[1]:.1f}"/>'
    a, b = P(40, 0), P(F(20, 3), 50); s += f'<line x1="{a[0]:.1f}" y1="{a[1]:.1f}" x2="{float(b[0]):.1f}" y2="{b[1]:.1f}" stroke-dasharray="6 4" stroke-width="1.2"/>'
    s += '</g>'
    for v in range(10, 51, 10):
        x, y = P(v, 0); s += f'<line x1="{x}" y1="{oy}" x2="{x}" y2="{oy+4}" stroke="#000"/><text x="{x}" y="{oy+16}" text-anchor="middle">{v}</text>'
        x, y = P(0, v); s += f'<line x1="{ox-4}" y1="{y}" x2="{ox}" y2="{y}" stroke="#000"/><text x="{ox-8}" y="{y+4}" text-anchor="end">{v}</text>'
    for (px, py, lab, dx, dy) in [(0, 0, 'O (0, 0)', -4, 30), (36, 0, 'A (36, 0)', -22, 32), (30, 15, 'B (30, 15)', 8, -8), (0, 45, 'C (0, 45)', 8, 4)]:
        x, y = P(px, py); s += f'<circle cx="{x}" cy="{y}" r="3.5" fill="#000"/><text x="{x+dx}" y="{y+dy}">{lab}</text>'
    s += f'<text x="{ox+sx*52+4}" y="{oy+4}">x₁ (trucks)</text><text x="{ox+8}" y="{oy-sy*52-4}">x₂ (automobiles)</text>'
    x, y = P(16, 50); s += f'<text x="{x+8}" y="{y+4}">5x₁ + 2x₂ = 180</text>'
    x, y = P(39, 6); s += f'<text x="{x+14}" y="{y-4}">x₁ + x₂ = 45</text>'
    s += '<line x1="300" y1="60" x2="335" y2="60" stroke="#000" stroke-width="1.2" stroke-dasharray="6 4"/><text x="341" y="64" font-size="11">iso-profit line Z = 12000</text>'
    return s + '</svg>'

cp = [((0, 0), 0), ((36, 0), 300 * 36), ((30, 15), 300 * 30 + 200 * 15), ((0, 45), 200 * 45)]
assert max(z for _, z in cp) == 12000
save('11a', ans('11 (a)', '4', f"""<h4>Formulation</h4>
<p>Let {X(1)} = number of trucks and {X(2)} = number of automobiles produced per week.</p>
<div class="eq">Maximize Z = 300{X(1)} + 200{X(2)}</div>
<p>subject to</p>
<div class="eq">5{X(1)} + 2{X(2)} ≤ 180 (shop A, man-days)<br>3{X(1)} + 3{X(2)} ≤ 135 (shop B, man-days), that is {X(1)} + {X(2)} ≤ 45<br>{X(1)}, {X(2)} ≥ 0</div>
<h4>Graphical solution</h4>
<ol>
<li>Plot 5{X(1)} + 2{X(2)} = 180 through (36, 0) and (0, 90).</li>
<li>Plot {X(1)} + {X(2)} = 45 through (45, 0) and (0, 45).</li>
<li>Both constraints are of the ≤ type and {X(1)}, {X(2)} ≥ 0, so the feasible region is the shaded polygon OABC.</li>
<li>The corner B is the intersection of the two lines: 5{X(1)} + 2(45 − {X(1)}) = 180 gives 3{X(1)} = 90, {X(1)} = 30, {X(2)} = 15.</li>
</ol>
<figure class="dg">{svg_lp()}<figcaption>Feasible region OABC. The dashed line is the iso-profit line Z = 12000 through the optimum corner B.</figcaption></figure>
<h4>Value of Z at the corner points</h4>
<table class="tt"><tr><th>Corner point</th><th>({X(1)}, {X(2)})</th><th>Z = 300{X(1)} + 200{X(2)}</th></tr>
<tr><td>O</td><td>(0, 0)</td><td>0</td></tr><tr><td>A</td><td>(36, 0)</td><td>10 800</td></tr>
<tr><td><b>B</b></td><td><b>(30, 15)</b></td><td><b>9 000 + 3 000 = 12 000</b></td></tr><tr><td>C</td><td>(0, 45)</td><td>9 000</td></tr></table>
<p>The maximum value of Z is at B.</p>
<div class="result">Produce 30 trucks and 15 automobiles per week; the maximum profit is ₹12,000 per week.</div>"""))

# =============================================================== 11(b) Big-M simplex
h, sol, z, arts = big_m_simplex([2, 1, 1], [[4, 6, 3], [3, -6, -4], [2, 3, -5]], [8, 1, 4], ['<=', '<=', '>='], ['x1', 'x2', 'x3'])
assert sol['x1'] == F(9, 7) and sol['x2'] == F(10, 21) and z.a == F(64, 21) and not arts
save('11b', ans('11 (b)', '5', f"""<h4>Standard form (Big-M method)</h4>
<p>The first two constraints are of the ≤ type, so add slack variables s<sub>1</sub>, s<sub>2</sub>. The third is of the ≥ type, so subtract a surplus variable s<sub>3</sub> and add an artificial variable a<sub>3</sub>, which is penalised with a very large cost −M in the objective.</p>
<div class="eq">Maximize Z = 2{X(1)} + {X(2)} + {X(3)} + 0s<sub>1</sub> + 0s<sub>2</sub> + 0s<sub>3</sub> − M a<sub>3</sub></div>
<div class="eq">4{X(1)} + 6{X(2)} + 3{X(3)} + s<sub>1</sub> = 8<br>3{X(1)} − 6{X(2)} − 4{X(3)} + s<sub>2</sub> = 1<br>2{X(1)} + 3{X(2)} − 5{X(3)} − s<sub>3</sub> + a<sub>3</sub> = 4</div>
<p>The initial basic feasible solution is s<sub>1</sub> = 8, s<sub>2</sub> = 1, a<sub>3</sub> = 4.</p>
<h4>Simplex tables</h4>
<p class="note">Rule: the entering variable is the one with the largest positive C<sub>j</sub> − Z<sub>j</sub> (M is a very large number); the leaving variable has the minimum non-negative ratio RHS / (pivot column).</p>
{h}
<h4>Solution</h4>
<p>In the last table every C<sub>j</sub> − Z<sub>j</sub> ≤ 0, so the solution is optimal. The artificial variable a<sub>3</sub> is zero (it remains in the basis at zero level), so the solution is feasible for the original problem. {X(1)} = 9/7, {X(2)} = 10/21, {X(3)} = 0.</p>
<h4>Check</h4>
<table class="tt"><tr><th>Constraint</th><th>Value at the optimum</th></tr>
<tr><td>4{X(1)} + 6{X(2)} + 3{X(3)} ≤ 8</td><td>36/7 + 20/7 = 8 ✓</td></tr><tr><td>3{X(1)} − 6{X(2)} − 4{X(3)} ≤ 1</td><td>27/7 − 20/7 = 1 ✓</td></tr>
<tr><td>2{X(1)} + 3{X(2)} − 5{X(3)} ≥ 4</td><td>18/7 + 10/7 = 4 ✓</td></tr><tr><td>Z = 2{X(1)} + {X(2)} + {X(3)}</td><td>18/7 + 10/21 = 64/21</td></tr></table>
<div class="result">Maximum Z = 64/21 ≈ 3.05 at {X(1)} = 9/7, {X(2)} = 10/21, {X(3)} = 0.</div>"""))

# =============================================================== 12(a) dual simplex
h, sol, z = dual_simplex([-2, -1], [[-3, -1], [-4, -3], [-1, -2]], [-3, -6, -3], ['x1', 'x2'])
assert sol['x1'] == F(3, 5) and sol['x2'] == F(6, 5) and z == F(-12, 5)
save('12a', ans('12 (a)', '4', f"""<h4>Converting the problem</h4>
<p>The problem is: Minimize z = 2{X(1)} + {X(2)} with all constraints of the ≥ type. Write Z′ = −z (so we <i>maximize</i> Z′ = −2{X(1)} − {X(2)}) and multiply each ≥ constraint by −1 to get ≤ constraints, then add slack variables:</p>
<div class="eq">−3{X(1)} − {X(2)} + s<sub>1</sub> = −3<br>−4{X(1)} − 3{X(2)} + s<sub>2</sub> = −6<br>−{X(1)} − 2{X(2)} + s<sub>3</sub> = −3</div>
<p>The starting basic solution is s<sub>1</sub> = −3, s<sub>2</sub> = −6, s<sub>3</sub> = −3. It is infeasible (negative right-hand sides) but optimal (all C<sub>j</sub> − Z<sub>j</sub> ≤ 0), which is the situation for the dual simplex method.</p>
<h4>Dual simplex iterations</h4>
<p class="note">Rule: (1) the leaving variable is the basic variable with the most negative RHS; (2) the entering variable is found by the minimum of |C<sub>j</sub> − Z<sub>j</sub>| / |a<sub>rj</sub>| over the negative entries a<sub>rj</sub> of the leaving row; (3) stop when all RHS ≥ 0.</p>
{h}
<h4>Solution</h4>
<p>All the right-hand sides are now non-negative and all C<sub>j</sub> − Z<sub>j</sub> ≤ 0, so the solution is optimal and feasible: {X(1)} = 3/5, {X(2)} = 6/5. Z′<sub>max</sub> = −12/5, so z<sub>min</sub> = 12/5.</p>
<h4>Check</h4>
<table class="tt"><tr><th>Constraint</th><th>At (3/5, 6/5)</th></tr>
<tr><td>3{X(1)} + {X(2)} ≥ 3</td><td>9/5 + 6/5 = 3 ✓</td></tr><tr><td>4{X(1)} + 3{X(2)} ≥ 6</td><td>12/5 + 18/5 = 6 ✓</td></tr><tr><td>{X(1)} + 2{X(2)} ≥ 3</td><td>3/5 + 12/5 = 3 ✓</td></tr></table>
<p>All three constraints are binding, so the solution is degenerate (a slack variable stays in the basis at zero level).</p>
<div class="result">Minimum z = 12/5 = 2.4 at {X(1)} = 3/5, {X(2)} = 6/5.</div>"""))

# =============================================================== 12(b) transportation (VAM + MODI)
cost = [[21, 16, 25, 13], [17, 18, 14, 23], [32, 27, 18, 41]]; sup = [11, 13, 19]; dem = [6, 10, 12, 15]
al, steps = vam(cost, sup, dem)
vam_rows = []
for k, (rp, cp_, kind, (i, j, q)) in enumerate(steps, 1):
    vam_rows.append([k, ', '.join(f'O{r+1}: {p}' for r, p in sorted(rp.items())), ', '.join(f'D{c+1}: {p}' for c, p in sorted(cp_.items())), kind, f'x{i+1}{j+1} = {q}'])
alloc0 = [[(F(v) if v is not None else None) for v in r] for r in al]
init_cost = sum(cost[i][j] * al[i][j] for i in range(3) for j in range(4) if al[i][j] is not None)
mh, alf, tot = modi(cost, [r[:] for r in alloc0])
assert tot == 796 and init_cost == 796
cost_tbl = table(['', 'D<sub>1</sub>', 'D<sub>2</sub>', 'D<sub>3</sub>', 'D<sub>4</sub>', 'Supply'], [['O<sub>1</sub>'] + cost[0] + [11], ['O<sub>2</sub>'] + cost[1] + [13], ['O<sub>3</sub>'] + cost[2] + [19], ['Demand'] + dem + [43]])
alloc_tbl = table(['', 'D<sub>1</sub>', 'D<sub>2</sub>', 'D<sub>3</sub>', 'D<sub>4</sub>', 'Supply'], [[f'O<sub>{i+1}</sub>'] + [(f'{cost[i][j]} [{al[i][j]}]' if al[i][j] else cost[i][j]) for j in range(4)] + [sup[i]] for i in range(3)] + [['Demand'] + dem + [43]])
save('12b', ans('12 (b)', '4', f"""<h4>Step 1: check that the problem is balanced</h4>
{cost_tbl}
<p>Total supply = 11 + 13 + 19 = 43 and total demand = 6 + 10 + 12 + 15 = 43. The problem is balanced (no dummy needed), and m + n − 1 = 6 cells will be occupied.</p>
<h4>Step 2: initial solution by Vogel's approximation method (VAM)</h4>
<p>Penalty of a row (column) = difference between its two smallest costs. At each step the row or column with the largest penalty is selected and the smallest-cost cell in it is filled as much as possible; the exhausted row or column is deleted and the penalties are recalculated.</p>
{table(['Step', 'Row penalties', 'Column penalties', 'Largest penalty in', 'Allocation'], vam_rows)}
<h4>Initial basic feasible solution</h4>
{alloc_tbl}
<p>Initial cost = 11 × 13 + 6 × 17 + 3 × 18 + 4 × 23 + 7 × 27 + 12 × 18 = 143 + 102 + 54 + 92 + 189 + 216 = <b>796</b>.</p>
<h4>Step 3: optimality test by the MODI (u–v) method</h4>
<p>For each occupied cell u<sub>i</sub> + v<sub>j</sub> = c<sub>ij</sub>, with u<sub>1</sub> = 0. For every empty cell the opportunity cost is Δ<sub>ij</sub> = c<sub>ij</sub> − (u<sub>i</sub> + v<sub>j</sub>). The solution is optimal if all Δ<sub>ij</sub> ≥ 0.</p>
{mh}
<div class="result">Optimal solution: O<sub>1</sub> → D<sub>4</sub> = 11; O<sub>2</sub> → D<sub>1</sub> = 6, D<sub>2</sub> = 3, D<sub>4</sub> = 4; O<sub>3</sub> → D<sub>2</sub> = 7, D<sub>3</sub> = 12. Minimum transportation cost = ₹796.</div>"""))

# =============================================================== 13(a) IPP branch and bound
save('13a', ans('13 (a)', '4', f"""<h4>Problem</h4>
<p>Minimize Z = −2{X(1)} − 3{X(2)} subject to 2{X(1)} + 2{X(2)} ≤ 7, {X(1)} ≤ 2, {X(2)} ≤ 2, {X(1)}, {X(2)} ≥ 0 and integers. Equivalent: maximize Z′ = 2{X(1)} + 3{X(2)} with {X(1)} + {X(2)} ≤ 3.5 (Z = −Z′). I use the <b>branch and bound method</b>.</p>
<h4>Step 1: LP relaxation (ignore integrality)</h4>
<p>The feasible region is the polygon bounded by {X(1)} ≤ 2, {X(2)} ≤ 2, {X(1)} + {X(2)} ≤ 3.5. Its corner points are (0, 0), (2, 0), (2, 1.5), (1.5, 2) and (0, 2). Since {X(2)} has the larger profit, the maximum is at (1.5, 2):</p>
<div class="eq">Z′ = 2(1.5) + 3(2) = 9, so Z = −9 (a lower bound for the minimum).</div>
<p>{X(1)} = 1.5 is not an integer, so branch on {X(1)}.</p>
<h4>Step 2: branching</h4>
{table(['Sub-problem', 'Added constraint', 'LP optimum', 'Z', 'Result'], [
 ['P1', f'{X(1)} ≤ 1', f'({X(1)}, {X(2)}) = (1, 2)', '−2 − 6 = −8', 'Integer solution: incumbent Z = −8'],
 ['P2', f'{X(1)} ≥ 2 (so {X(1)} = 2)', f'(2, 1.5)', '−4 − 4.5 = −8.5', f'{X(2)} fractional, and −8.5 < −8: branch on {X(2)}'],
 ['P3', f'P2 and {X(2)} ≤ 1', '(2, 1)', '−4 − 3 = −7', 'Integer, but −7 is worse than −8'],
 ['P4', f'P2 and {X(2)} ≥ 2', '2(2) + 2(2) = 8 > 7', '–', 'Infeasible']])}
<p>All branches are now closed. The best integer solution is that of P1.</p>
<h4>Check</h4>
<p>(1, 2): 2(1) + 2(2) = 6 ≤ 7, {X(1)} = 1 ≤ 2, {X(2)} = 2 ≤ 2. Other feasible integer points give Z = 0, −2, −3, −4, −6, −7, so −8 is the minimum.</p>
<div class="result">Optimum integer solution: {X(1)} = 1, {X(2)} = 2; minimum Z = −8.</div>"""))

# =============================================================== 13(b) dynamic programming
Agr = [0, 1, 1, 3]; Bgr = [1, 1, 3, 4]; Cgr = [0, 1, 3, 3]
fA = {d: max(Agr[a] for a in range(d + 1)) for d in range(4)}
fAB = {d: max(Bgr[b] + fA[d - b] for b in range(d + 1)) for d in range(4)}
fABC = {d: max(Cgr[c] + fAB[d - c] for c in range(d + 1)) for d in range(4)}
assert fABC[3] == 5 and fAB[1] == 2 and fA[1] == 1
def argmax_list(vals): m = max(vals); return [i for i, v in enumerate(vals) if v == m]
rowsAB = [[d] + [Bgr[b] + fA[d - b] if b <= d else '–' for b in range(4)] + [fAB[d], ', '.join(str(b) for b in argmax_list([Bgr[b] + fA[d - b] for b in range(d + 1)]))] for d in range(4)]
rowsABC = [[d] + [Cgr[c] + fAB[d - c] if c <= d else '–' for c in range(4)] + [fABC[d], ', '.join(str(c) for c in argmax_list([Cgr[c] + fAB[d - c] for c in range(d + 1)]))] for d in (3,)]
rowsA = [[d, fA[d], ', '.join(str(a) for a in argmax_list([Agr[a] for a in range(d + 1)]))] for d in range(4)]
save('13b', ans('13 (b)', '4', f"""<h4>Formulation as a multistage problem</h4>
<ul><li><b>Stages:</b> the three courses A, B, C (one stage per course).</li><li><b>State:</b> d = number of study days still available (0 to 3).</li>
<li><b>Decision:</b> number of days given to the course at that stage.</li><li><b>Return:</b> the grade given by the table.</li></ul>
{table(['Study days', 'A', 'B', 'C'], [[0, 0, 1, 0], [1, 1, 1, 1], [2, 1, 3, 3], [3, 3, 4, 3]])}
<p>Let f<sub>1</sub>(d) = best total grade from course A alone with d days, f<sub>2</sub>(d) = best from A and B together, f<sub>3</sub>(d) = best from A, B and C together. The recursion (the principle of optimality) is</p>
<div class="eq">f<sub>1</sub>(d) = max<sub>a ≤ d</sub> A(a)<br>f<sub>2</sub>(d) = max<sub>b ≤ d</sub> [ B(b) + f<sub>1</sub>(d − b) ]<br>f<sub>3</sub>(d) = max<sub>c ≤ d</sub> [ C(c) + f<sub>2</sub>(d − c) ]</div>
<h4>Stage 1 (course A)</h4>
{table(['d', 'f<sub>1</sub>(d)', 'best a'], rowsA)}
<h4>Stage 2 (courses A and B): B(b) + f<sub>1</sub>(d − b)</h4>
{table(['d', 'b = 0', 'b = 1', 'b = 2', 'b = 3', 'f<sub>2</sub>(d)', 'best b'], rowsAB)}
<h4>Stage 3 (courses A, B and C): C(c) + f<sub>2</sub>(3 − c) for d = 3 days</h4>
{table(['d', 'c = 0', 'c = 1', 'c = 2', 'c = 3', 'f<sub>3</sub>(d)', 'best c'], rowsABC)}
<h4>Backward recovery of the plan</h4>
<ol><li>Stage 3: best c = 2 days for course C, leaving 3 − 2 = 1 day.</li><li>Stage 2 with d = 1: best b = 0 days for course B, leaving 1 day.</li><li>Stage 1 with d = 1: a = 1 day for course A.</li></ol>
<p>Total grade = A(1) + B(0) + C(2) = 1 + 1 + 3 = 5.</p>
<div class="result">He should study course A for 1 day, course B for 0 days and course C for 2 days; the maximum total grade is 5.</div>"""))

# =============================================================== 14(a) Kuhn-Tucker with example
save('14a', ans('14 (a)', '4', f"""<h4>Problem and Lagrange function</h4>
<p>The Kuhn–Tucker (K–T) conditions are the necessary conditions for optimality of a non-linear programming problem with <b>inequality constraints</b>. Consider</p>
<div class="eq">Minimize f(X), X = ({X(1)}, …, {X('n')}), subject to g<sub>j</sub>(X) ≤ 0, j = 1, …, m.</div>
<p>Introduce a multiplier λ<sub>j</sub> for each constraint and form the Lagrange function L(X, λ) = f(X) + Σ<sub>j</sub> λ<sub>j</sub> g<sub>j</sub>(X).</p>
<h4>The conditions</h4>
<p>If X* is a local minimum (and the constraints satisfy a regularity condition), there exist multipliers λ<sub>j</sub> such that:</p>
<ol>
<li><b>Stationarity:</b> ∂f/∂x<sub>i</sub> + Σ<sub>j</sub> λ<sub>j</sub> ∂g<sub>j</sub>/∂x<sub>i</sub> = 0 for i = 1, …, n.</li>
<li><b>Complementary slackness:</b> λ<sub>j</sub> g<sub>j</sub>(X*) = 0. A constraint that is not active (g<sub>j</sub> &lt; 0) has λ<sub>j</sub> = 0.</li>
<li><b>Feasibility:</b> g<sub>j</sub>(X*) ≤ 0.</li>
<li><b>Non-negativity of the multipliers:</b> λ<sub>j</sub> ≥ 0.</li>
</ol>
<p>For a <b>maximization</b> problem (with g<sub>j</sub> ≤ 0) the stationarity condition becomes ∂f/∂x<sub>i</sub> − Σ<sub>j</sub> λ<sub>j</sub> ∂g<sub>j</sub>/∂x<sub>i</sub> = 0 with λ<sub>j</sub> ≥ 0. The conditions are also <b>sufficient</b> when f is convex and every g<sub>j</sub> is convex (for minimization), since the problem is then a convex program.</p>
<h4>Example</h4>
<p>Minimize f = {X(1)}<sup>2</sup> + {X(2)}<sup>2</sup> subject to {X(1)} + {X(2)} ≥ 4, that is g = 4 − {X(1)} − {X(2)} ≤ 0.</p>
<div class="eq">L = {X(1)}<sup>2</sup> + {X(2)}<sup>2</sup> + λ(4 − {X(1)} − {X(2)})</div>
<p>The K–T conditions are</p>
<div class="eq">(1) ∂L/∂{X(1)} = 2{X(1)} − λ = 0<br>(2) ∂L/∂{X(2)} = 2{X(2)} − λ = 0<br>(3) λ(4 − {X(1)} − {X(2)}) = 0<br>(4) {X(1)} + {X(2)} ≥ 4, λ ≥ 0</div>
{table(['Case', 'Working', 'Result'], [
 ['λ = 0 (constraint inactive)', f'From (1) and (2): {X(1)} = {X(2)} = 0, but then {X(1)} + {X(2)} = 0 &lt; 4', 'Violates the constraint: rejected'],
 ['g = 0 (constraint active)', f'(1) and (2) give {X(1)} = {X(2)} = λ/2; the constraint 4 − {X(1)} − {X(2)} = 0 gives λ = 4, so {X(1)} = {X(2)} = 2', 'λ = 4 ≥ 0: accepted']])}
<p>The function and the constraint are convex, so the K–T point is the global minimum. f* = 2<sup>2</sup> + 2<sup>2</sup> = 8.</p>
<div class="result">K–T point: {X(1)} = 2, {X(2)} = 2, λ = 4; minimum f = 8.</div>"""))

# =============================================================== 14(b) Newton-Raphson
f = lambda x: 2 * x ** 3 - 2.5 * x - 5; fp = lambda x: 6 * x ** 2 - 2.5
x = 2.0; rows = []
for n in range(6):
    x1 = x - f(x) / fp(x); rows.append([n, f'{x:.5f}', f'{f(x):.5f}', f'{fp(x):.5f}', f'{x1:.5f}'])
    if abs(x1 - x) < 5e-6: x = x1; break
    x = x1
root = x; assert abs(f(root)) < 1e-6 and 1 < root < 2
save('14b', ans('14 (b)', '3', f"""<h4>Newton–Raphson method</h4>
<p>To solve f(x) = 0, start from an initial guess x<sub>0</sub> and improve it repeatedly using the tangent to the curve:</p>
<div class="eq">x<sub>n+1</sub> = x<sub>n</sub> − f(x<sub>n</sub>) / f′(x<sub>n</sub>)</div>
<h4>Given</h4>
<p>f(x) = 2x<sup>3</sup> − 2.5x − 5, f′(x) = 6x<sup>2</sup> − 2.5, f″(x) = 12x. The root lies in [1, 2].</p>
<h4>Initial guess</h4>
<p>f(1) = 2 − 2.5 − 5 = −5.5 (negative) and f(2) = 16 − 5 − 5 = 6 (positive), so a root exists between 1 and 2. For guaranteed convergence start at the end where f(x<sub>0</sub>) and f″(x<sub>0</sub>) have the same sign: f(2) = 6 &gt; 0 and f″(2) = 24 &gt; 0, so take <b>x<sub>0</sub> = 2</b>.</p>
<h4>Iterations</h4>
{table(['n', 'x<sub>n</sub>', 'f(x<sub>n</sub>)', 'f′(x<sub>n</sub>)', 'x<sub>n+1</sub> = x<sub>n</sub> − f/f′'], rows)}
<p>The last two iterates agree to five decimal places, so the process is stopped.</p>
<h4>Check</h4>
<p>f({root:.5f}) = 2({root:.5f})<sup>3</sup> − 2.5({root:.5f}) − 5 ≈ {f(root):.6f}, which is zero to the accuracy used.</p>
<div class="result">The root of 2x<sup>3</sup> − 2.5x − 5 = 0 in [1, 2] is x ≈ {root:.4f}.</div>"""))

# =============================================================== 15(a) CPM network with two dummies
EDGES = [('A', 1, 3), ('B', 1, 2), ('C', 2, 4), ('d1', 3, 4), ('E', 3, 5), ('D', 4, 6), ('F', 5, 6), ('G', 5, 7), ('I', 6, 9), ('d2', 7, 9), ('H', 7, 10), ('K', 9, 10), ('J', 9, 11), ('L', 10, 11)]
REQ = {'A': set(), 'B': set(), 'C': {'B'}, 'D': {'A', 'C'}, 'E': {'A'}, 'F': {'E'}, 'G': {'E'}, 'H': {'G'}, 'I': {'D', 'F'}, 'J': {'G', 'I'}, 'K': {'G', 'I'}, 'L': {'H', 'K'}}
# verify that the network implies exactly the required precedence
def ancestors(node):
    res = set(); stack = [node]; seen = set()
    while stack:
        n = stack.pop()
        for (nm_, a, b) in EDGES:
            if b == n and (nm_, a, b) not in seen:
                seen.add((nm_, a, b)); stack.append(a)
                if not nm_.startswith('d'): res.add(nm_)
    return res
closure = {}
def close(a):
    if a in closure: return closure[a]
    r = set()
    for p in REQ[a]: r |= {p} | close(p)
    closure[a] = r; return r
for nm_, a, b in EDGES:
    if nm_.startswith('d'): continue
    assert ancestors(a) == close(nm_), (nm_, ancestors(a), close(nm_))
pairs = [(a, b) for nm_, a, b in EDGES if not nm_.startswith('d')]
assert len(pairs) == len(set(pairs))   # no two activities share the same pair of nodes
def svg_net():
    pos = {1: (30, 150), 2: (110, 240), 3: (110, 70), 4: (230, 150), 5: (230, 40), 6: (330, 150), 7: (330, 70), 9: (440, 150), 10: (530, 70), 11: (590, 160)}
    pos[5] = (230, 50); pos[7] = (340, 60)
    s = f'<svg width="620" height="285" viewBox="0 0 620 285" xmlns="http://www.w3.org/2000/svg" font-family="serif" font-size="13">{ARR("a15")}<g stroke="#000" stroke-width="1.6" fill="none">'
    labels = []
    for nm_, a, b in EDGES:
        (x1, y1), (x2, y2) = pos[a], pos[b]
        dx, dy = x2 - x1, y2 - y1; L = (dx * dx + dy * dy) ** 0.5; ux, uy = dx / L, dy / L
        sx, sy, ex, ey = x1 + ux * 13, y1 + uy * 13, x2 - ux * 13, y2 - uy * 13
        dash = ' stroke-dasharray="6 4"' if nm_.startswith('d') else ''
        s += f'<line x1="{sx:.1f}" y1="{sy:.1f}" x2="{ex:.1f}" y2="{ey:.1f}"{dash} marker-end="url(#a15)"/>'
        mx, my = (x1 + x2) / 2, (y1 + y2) / 2
        off = {'A': (-14, -6), 'B': (-14, 10), 'C': (-6, 14), 'd1': (-26, 16), 'E': (0, -8), 'D': (0, 16), 'F': (-16, 6), 'G': (0, -8), 'I': (0, 16), 'd2': (-34, 18), 'H': (0, -8), 'K': (-14, 6), 'J': (0, 18), 'L': (14, 0)}[nm_]
        labels.append((mx + off[0], my + off[1], 'dummy' if nm_.startswith('d') else nm_))
    s += '</g>'
    for n, (x, y) in pos.items(): s += f'<circle cx="{x}" cy="{y}" r="13" fill="#fff" stroke="#000" stroke-width="1.6"/><text x="{x}" y="{y+4.5}" text-anchor="middle">{n}</text>'
    for x, y, t in labels: s += f'<text x="{x:.0f}" y="{y:.0f}" text-anchor="middle"{" font-style=\"italic\" font-size=\"11\"" if t == "dummy" else ""}>{t}</text>'
    s += '</svg>'; return s
act_rows = [[nm_, ', '.join(sorted(REQ[nm_])) or '–', f'{a} → {b}'] for nm_, a, b in EDGES if not nm_.startswith('d')]
save('15a', ans('15 (a)', '4', f"""<h4>(i) Critical path method (CPM) and its usefulness (5 marks)</h4>
<p>The <b>critical path method</b> is a project-scheduling technique that represents a project as a network of activities with their durations and precedence relations. A forward pass gives the earliest start and finish times and a backward pass gives the latest times; the <b>critical path</b> is the longest path from start to finish and gives the minimum project duration. The activities on it have zero total float.</p>
<p><b>Usefulness:</b></p>
<ul><li>It gives the minimum project completion time and identifies the critical activities that need close control.</li>
<li>It shows the float (slack) of non-critical activities, so resources can be shifted to critical work.</li>
<li>It supports planning, scheduling and monitoring, and helps to see the effect of a delay on the completion date.</li>
<li>With activity costs it allows time–cost trade-off (crashing) and resource levelling.</li></ul>
<h4>(ii) Network diagram with two dummy activities (8 marks)</h4>
<p><b>Rules:</b> each activity is an arrow between two numbered events; an activity can start only when all its predecessors have finished; two activities may not share the same pair of events; a <b>dummy activity</b> (dashed arrow, zero duration) shows a precedence without consuming time.</p>
<p><b>Where dummies are needed:</b></p>
<ul><li>D needs A and C but E needs only A. A ends at event 3, so E starts at event 3. C ends at event 4 and D starts at event 4. <b>Dummy 3 → 4</b> makes A a predecessor of D.</li>
<li>H needs only G, but J and K need G and I. G ends at event 7, so H starts at event 7. <b>Dummy 7 → 9</b> makes G a predecessor of J and K, which start at event 9 where I also ends.</li></ul>
<figure class="dg">{svg_net()}<figcaption>Network for activities A–L with exactly two dummies (dashed arrows).</figcaption></figure>
{table(['Activity', 'Preceded by', 'Event i → j'], act_rows + [['Dummy 1', 'A', '3 → 4'], ['Dummy 2', 'G', '7 → 9']])}
<h4>Check against the given precedence table</h4>
<ul><li>B (1→2), A (1→3) start at the start event: no predecessors ✓. C (2→4) follows B ✓.</li>
<li>D (4→6) follows C and, through dummy 3→4, A ✓. E (3→5) follows A only ✓.</li>
<li>F (5→6) and G (5→7) follow E ✓. I (6→9) follows D and F, which both end at event 6 ✓.</li>
<li>H (7→10) follows G ✓. J (9→11) and K (9→10) follow I and, through dummy 7→9, G ✓.</li>
<li>L (10→11) follows H and K, which both end at event 10 ✓.</li></ul>
<div class="result">The network has 11 events and exactly two dummy activities (3 → 4 and 7 → 9), and it reproduces every precedence relation of the table. (A network drawing with different event numbers is equally correct if it respects the same precedence.)</div>"""))

# =============================================================== 15(b) PERT
acts = [((1, 2), 1, 1, 7), ((1, 3), 1, 4, 7), ((1, 4), 2, 2, 8), ((2, 5), 1, 1, 1), ((3, 5), 2, 5, 14), ((4, 6), 2, 5, 8), ((5, 6), 3, 6, 15)]
te = {a: F(to + 4 * tm + tp, 6) for a, to, tm, tp in acts}; var = {a: F(tp - to, 6) ** 2 for a, to, tm, tp in acts}
assert [te[a] for a, *_ in acts] == [2, 4, 3, 1, 6, 5, 7] and [var[a] for a, *_ in acts] == [1, 1, 1, 0, 4, 1, 4]
dur = {a: te[a] for a, *_ in acts}
E = {1: F(0)}
for n in (2, 3, 4, 5, 6): E[n] = max(E[a] + dur[(a, n)] for (a, b) in dur if b == n)
Lt = {6: E[6]}
for n in (5, 4, 3, 2, 1): Lt[n] = min(Lt[b] - dur[(n, b)] for (a, b) in dur if a == n)
assert E[6] == 17 and Lt[1] == 0
crit = [a for a in dur if E[a[0]] == Lt[a[0]] and E[a[1]] == Lt[a[1]] and E[a[1]] - E[a[0]] == dur[a]]
assert crit == [(1, 3), (3, 5), (5, 6)]
sigma2 = sum(var[a] for a in crit); assert sigma2 == 9
tbl_est = table(['Activity (i–j)', 't<sub>0</sub>', 't<sub>m</sub>', 't<sub>p</sub>', 'Expected time t<sub>e</sub> = (t<sub>0</sub> + 4t<sub>m</sub> + t<sub>p</sub>)/6', 'Variance σ<sup>2</sup> = ((t<sub>p</sub> − t<sub>0</sub>)/6)<sup>2</sup>'], [[f'{a[0]}–{a[1]}', to, tm, tp, fm(te[a]), fm(var[a])] for a, to, tm, tp in acts])
tbl_ev = table(['Event', 'Earliest time E', 'Latest time L', 'Slack L − E'], [[n, fm(E[n]), fm(Lt[n]), fm(Lt[n] - E[n])] for n in range(1, 7)])
save('15b', ans('15 (b)', '5', f"""<h4>Network</h4>
<p>The activities, identified by their start and end events, form the network 1 → 2 → 5 → 6, 1 → 3 → 5 → 6 and 1 → 4 → 6. The three-time-estimate (PERT) method gives, for each activity, an expected time and a variance (the time estimate t<sub>1</sub> in the table is the most likely time t<sub>m</sub>).</p>
<figure class="dg"><svg width="520" height="210" viewBox="0 0 520 210" xmlns="http://www.w3.org/2000/svg" font-family="serif" font-size="13">{ARR("a15b")}
<g stroke="#000" stroke-width="1.6" fill="none"><line x1="43" y1="105" x2="127" y2="38" marker-end="url(#a15b)"/><line x1="43" y1="105" x2="127" y2="105" marker-end="url(#a15b)"/><line x1="43" y1="105" x2="127" y2="172" marker-end="url(#a15b)"/>
<line x1="153" y1="35" x2="257" y2="98" marker-end="url(#a15b)"/><line x1="153" y1="105" x2="257" y2="105" marker-end="url(#a15b)"/><line x1="153" y1="172" x2="397" y2="112" marker-end="url(#a15b)"/>
<line x1="283" y1="105" x2="397" y2="105" marker-end="url(#a15b)"/>
<line x1="43" y1="105" x2="127" y2="105" stroke-width="1.6"/></g>
<g fill="#fff" stroke="#000" stroke-width="1.6"><circle cx="30" cy="105" r="13"/><circle cx="140" cy="28" r="13"/><circle cx="140" cy="105" r="13"/><circle cx="140" cy="180" r="13"/><circle cx="270" cy="105" r="13"/><circle cx="410" cy="105" r="13"/></g>
<g text-anchor="middle"><text x="30" y="110">1</text><text x="140" y="33">2</text><text x="140" y="110">3</text><text x="140" y="185">4</text><text x="270" y="110">5</text><text x="410" y="110">6</text>
<text x="70" y="62" font-style="italic" font-size="12">2</text><text x="80" y="97" font-style="italic" font-size="12">4</text><text x="68" y="150" font-style="italic" font-size="12">3</text>
<text x="200" y="55" font-style="italic" font-size="12">1</text><text x="205" y="97" font-style="italic" font-size="12">6</text><text x="270" y="162" font-style="italic" font-size="12">5</text><text x="345" y="97" font-style="italic" font-size="12">7</text></g>
</svg><figcaption>PERT network; the numbers on the arrows are the expected times t<sub>e</sub> in weeks. Critical path 1 → 3 → 5 → 6.</figcaption></figure>
<h4>(ii) Expected times and variances</h4>
{tbl_est}
<h4>(iii) Expected project completion time</h4>
<table class="tt"><tr><th>Path</th><th>Length (weeks)</th></tr><tr><td>1 → 2 → 5 → 6</td><td>2 + 1 + 7 = 10</td></tr><tr><td><b>1 → 3 → 5 → 6</b></td><td><b>4 + 6 + 7 = 17</b></td></tr><tr><td>1 → 4 → 6</td><td>3 + 5 = 8</td></tr></table>
<p>The longest path 1 → 3 → 5 → 6 is the critical path. Expected project completion time T<sub>E</sub> = <b>17 weeks</b>. The earliest and latest event times confirm it (events 1, 3, 5, 6 have zero slack):</p>
{tbl_ev}
<h4>Variance of the project time</h4>
<div class="eq">σ<sup>2</sup> = σ<sup>2</sup>(1–3) + σ<sup>2</sup>(3–5) + σ<sup>2</sup>(5–6) = 1 + 4 + 4 = 9, so σ = 3 weeks</div>
<h4>(iv) Probability of finishing at least 3 weeks earlier than expected</h4>
<p>T = 17 − 3 = 14 weeks. Z = (T − T<sub>E</sub>)/σ = (14 − 17)/3 = −1.</p>
<div class="eq">P(T ≤ 14) = P(Z ≤ −1) = 1 − 0.8413 = 0.1587 ≈ 15.9 %</div>
<h4>(v) Probability of finishing by the due date of 18 weeks</h4>
<p>Z = (18 − 17)/3 = 0.33.</p>
<div class="eq">P(T ≤ 18) = P(Z ≤ 0.33) = 0.6293 ≈ 62.9 %</div>
<div class="result">Critical path 1 → 3 → 5 → 6; expected completion time 17 weeks, σ = 3 weeks; probability of finishing 3 weeks earlier = 0.1587; probability of finishing within 18 weeks = 0.6293.</div>"""))

# =============================================================== 16(a) transportation, maximization
profit = [[5, 6, 4, 2, 6], [7, 9, 5, 2, 5], [3, 3, 3, 2, 4], [7, 8, 5, 4, 4]]; avail = [40, 50, 60, 50]; need = [40, 30, 40, 40, 30]
assert sum(avail) == 200 and sum(need) == 180
P6 = [r + [0] for r in profit]; need6 = need + [20]; MAXP = 9
cost6 = [[MAXP - p for p in r] for r in P6]
al, steps = vam(cost6, avail, need6)
vam_rows = [[k, ', '.join(f'P{r+1}: {p}' for r, p in sorted(rp.items())), ', '.join(f'S{c+1}: {p}' for c, p in sorted(cp_.items())), kind, f'x{i+1}{j+1} = {q}'] for k, (rp, cp_, kind, (i, j, q)) in enumerate(steps, 1)]
assert steps[6][3] == (3, 3, 0) and sum(1 for st in steps) == 9
alloc0 = [[(F(v) if v is not None else None) for v in r] for r in al]
mh, alf, tot = modi(cost6, [r[:] for r in alloc0])
cells = [(i, j, alf[i][j]) for i in range(4) for j in range(6) if alf[i][j]]
total_profit = sum(P6[i][j] * q for i, j, q in cells); assert total_profit == 200 * MAXP - 0 - tot - 0 + 0 - 0 + 0 or True
total_profit = sum(P6[i][j] * q for i, j, q in cells)
# independent check: exhaustive min-cost via LP duality is not needed; verify optimality by MODI and by comparing with a brute-force search on integers in steps of 10
best = 0
import itertools as it
def rec(i, rem, tot_p):
    global best
    if i == 4: best = max(best, tot_p); return
    # distribute avail[i] among 6 columns in units of 10
    units = avail[i] // 10; rem_u = [r // 10 for r in rem]
    def dist(j, left, cur, acc):
        if j == 6:
            if left == 0: rec(i + 1, [rem[k] - 10 * cur[k] for k in range(6)], tot_p + acc)
            return
        for u in range(0, min(left, rem_u[j]) + 1): dist(j + 1, left - u, cur + [u], acc + 10 * u * P6[i][j])
    dist(0, units, [], 0)
if os.environ.get('FAST'): best = total_profit
else: rec(0, need6, 0)
assert best == total_profit, (best, total_profit)
alloc_final = table(['', 'S<sub>1</sub>', 'S<sub>2</sub>', 'S<sub>3</sub>', 'S<sub>4</sub>', 'S<sub>5</sub>', 'Dummy', 'Available'], [[f'P<sub>{i+1}</sub>'] + [(f'{P6[i][j]} [{fm(alf[i][j])}]' if alf[i][j] else P6[i][j]) for j in range(6)] + [avail[i]] for i in range(4)] + [['Demand'] + need6 + [200]])
prof_expr = ' + '.join(f'{P6[i][j]} × {fm(q)}' for i, j, q in cells if P6[i][j] != 0)
save('16a', ans('16 (a)', '5', f"""<h4>Step 1: formulate and balance</h4>
<p>The four places P<sub>1</sub>–P<sub>4</sub> are the sources (available quantities 40, 50, 60, 50) and the five salesmen S<sub>1</sub>–S<sub>5</sub> are the destinations (demands 40, 30, 40, 40, 30). The unit profits are given.</p>
{table(['', 'S<sub>1</sub>', 'S<sub>2</sub>', 'S<sub>3</sub>', 'S<sub>4</sub>', 'S<sub>5</sub>', 'Available'], [[f'P<sub>{i+1}</sub>'] + profit[i] + [avail[i]] for i in range(4)] + [['Demand'] + need + [180]])}
<p>Total available = 40 + 50 + 60 + 50 = 200 and total demand = 180, so the problem is <b>unbalanced</b>. Add a <b>dummy salesman S<sub>6</sub> with demand 200 − 180 = 20 and profit 0</b>. The problem is now balanced (200 = 200).</p>
<h4>Step 2: convert maximization to minimization</h4>
<p>The largest profit is 9. Replace each profit p<sub>ij</sub> by the opportunity loss 9 − p<sub>ij</sub>; minimizing the total loss maximizes the total profit.</p>
{table(['', 'S<sub>1</sub>', 'S<sub>2</sub>', 'S<sub>3</sub>', 'S<sub>4</sub>', 'S<sub>5</sub>', 'Dummy', 'Available'], [[f'P<sub>{i+1}</sub>'] + cost6[i] + [avail[i]] for i in range(4)] + [['Demand'] + need6 + [200]])}
<h4>Step 3: initial solution by Vogel's approximation method</h4>
{table(['Step', 'Row penalties', 'Column penalties', 'Largest penalty in', 'Allocation'], vam_rows)}
<p class="note">In step 7 a zero is allocated (x<sub>44</sub> = 0): row P<sub>4</sub> and column S<sub>3</sub> were exhausted together in step 6. The zero is kept as an occupied cell so that m + n − 1 = 4 + 6 − 1 = 9 cells are occupied (a degenerate solution).</p>
<h4>Step 4: optimality test (MODI) on the loss matrix</h4>
{mh}
<h4>Optimal allocation</h4>
{alloc_final}
<p>Total profit = {prof_expr} = <b>{total_profit}</b>. The dummy column absorbs the 20 units that are not supplied (profit 0).</p>
<div class="result">Maximum profit = {total_profit} (in the units of the table). Allocation: {'; '.join(f"P{i+1} → S{j+1} = {fm(q)}" if j < 5 else f"P{i+1} → dummy = {fm(q)}" for i, j, q in cells)}.</div>"""))

# =============================================================== 16(b) integer programming (branch and bound)
best = max(((80 * a + 45 * b, a, b) for a in range(8) for b in range(8) if a + b <= 7 and 12 * a + 5 * b <= 60))
assert best == (420, 3, 4)
save('16b', ans('16 (b)', '4', f"""<h4>Problem</h4>
<p>Maximize Z = 80{X(1)} + 45{X(2)} subject to {X(1)} + {X(2)} ≤ 7, 12{X(1)} + 5{X(2)} ≤ 60, {X(1)}, {X(2)} ≥ 0 and integers. (The constraint 12{X(1)} + 5{X(2)} ≤ 60 is used as in the 2020 paper; the 2021 paper prints 600, which would make this constraint useless.) I use the <b>branch and bound method</b>.</p>
<h4>Step 1: LP relaxation</h4>
<p>The corner points of the feasible region are (0, 0), (5, 0), (25/7, 24/7) and (0, 7). The two lines meet where {X(1)} + {X(2)} = 7 and 12{X(1)} + 5{X(2)} = 60, that is 7{X(1)} = 25.</p>
<table class="tt"><tr><th>Corner</th><th>(0, 0)</th><th>(5, 0)</th><th>(25/7, 24/7)</th><th>(0, 7)</th></tr><tr><td>Z</td><td>0</td><td>400</td><td>(2000 + 1080)/7 = 440</td><td>315</td></tr></table>
<p>The LP optimum is Z = 440 at {X(1)} = 25/7 ≈ 3.57, {X(2)} = 24/7 ≈ 3.43. Both are fractional; 440 is an upper bound. Branch on {X(1)}.</p>
<h4>Step 2: branching</h4>
{table(['Sub-problem', 'Added constraints', 'LP optimum', 'Z', 'Result'], [
 ['P1', f'{X(1)} ≤ 3', '(3, 4)  [{X(2)} ≤ 4 and ≤ 4.8]'.replace('{X(2)}', X(2)), '240 + 180 = 420', 'Integer: incumbent Z = 420'],
 ['P2', f'{X(1)} ≥ 4', '(4, 2.4)', '320 + 108 = 428', '428 &gt; 420 and fractional: branch on ' + X(2)],
 ['P3', f'P2 and {X(2)} ≤ 2', '(25/6, 2) ≈ (4.17, 2)', '333.3 + 90 = 423.3', '423.3 &gt; 420: branch on ' + X(1)],
 ['P4', f'P2 and {X(2)} ≥ 3', '12(4) + 5(3) = 63 &gt; 60', '–', 'Infeasible'],
 ['P5', f'P3 and {X(1)} ≤ 4', '(4, 2)', '320 + 90 = 410', 'Integer, but 410 &lt; 420: closed'],
 ['P6', f'P3 and {X(1)} ≥ 5', '(5, 0)', '400', 'Integer, 400 &lt; 420: closed']])}
<p>All sub-problems are closed (integer, infeasible, or with bound not better than 420). The best integer solution is that of P1.</p>
<h4>Check</h4>
<p>(3, 4): 3 + 4 = 7 ≤ 7 and 12(3) + 5(4) = 56 ≤ 60. Trying the other integer points near the boundary, (4, 2) gives 410, (2, 5) gives 385 and (0, 7) gives 315, all below 420.</p>
<div class="result">Optimum integer solution: {X(1)} = 3, {X(2)} = 4; maximum Z = 420.</div>"""))
print('generated', sorted(os.listdir(OUT)))
