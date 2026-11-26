"""Two OIE352 model question papers in the Anna University layout (Part A 10x2, Part B 5x13, Part C 1x15).
Every question is a real question of the CS6704 papers (Nov/Dec 2020 or Nov/Dec 2021). Output: OIE352_Model_Question_Papers.html"""
import os, re
HERE = os.path.dirname(os.path.abspath(__file__))

def T(rows, head=None):
    h = '<table class="qtb">'
    if head: h += '<tr>' + ''.join(f'<th>{c}</th>' for c in head) + '</tr>'
    for r in rows: h += '<tr>' + ''.join(f'<td>{c}</td>' for c in r) + '</tr>'
    return h + '</table>'
x = lambda n: f'x<sub>{n}</sub>'
SALES = T([['P1', 5, 6, 4, 2, 6, 40], ['P2', 7, 9, 5, 2, 5, 50], ['P3', 3, 3, 3, 2, 4, 60], ['P4', 7, 8, 5, 4, 4, 50], ['Demand', 40, 30, 40, 40, 30, '']], ['', 'S1', 'S2', 'S3', 'S4', 'S5', 'Available'])
Q16 = {'a': ('', 'Unit profit of five salesmen in four places is given below. ' + SALES + 'Solve the problem to maximize the profit.', 15, '2020 N/D and 2021 N/D (same question)'),
       'b': ('', f'Solve the integer programming problem. Maximize Z = 80{x(1)} + 45{x(2)} subject to {x(1)} + {x(2)} ≤ 7, 12{x(1)} + 5{x(2)} ≤ 60 and {x(1)}, {x(2)} ≥ 0 and integers.', 15, '2020 N/D and 2021 N/D (2021 prints 600 for 60)')}
PAPERS = [
{'name': 'Model Question Paper 1', 'focus': 'Questions from the 2021 paper, with the repeated Part C',
 'A': [('What is linear programming?', '2020 N/D'), ('What do you mean by shadow pricing?', '2021 N/D'), ('Define primal and dual problem.', '2020 N/D'),
       ('How do you convert an unbalanced transportation problem into a balanced one?', '2021 N/D'), ('List different types of integer programming problems.', '2021 N/D'),
       ('Define Dynamic Programming.', '2020 N/D'), ('Define Kuhn–Tucker conditions.', '2020 N/D'),
       ('Write the sufficient conditions for the Hessian matrix (H) evaluated at a stationary point (X<sub>0</sub>).', '2021 N/D'),
       ('Bring out any four differences between CPM and PERT.', '2021 N/D'), ('Define critical path.', '2020 N/D')],
 'B': {
  11: {'a': ('', 'An automobile manufacturer makes automobiles and trucks in a factory that is divided into two shops. Shop A, which performs the basic assembly operation, must work 5 man-days on each truck but only 2 man-days on each automobile. Shop B, which performs the finishing operation, must work 3 man-days for each truck or automobile that it produces. Because of men and machine limitations shop A has 180 man-days per week available while shop B has 135 man-days per week. If the manufacturer makes a profit of Rs. 300 on each truck and Rs. 200 on each automobile, how many of each should he produce to maximize his profit?', 13, '2021 N/D'),
       'b': ('', f'Solve the following LPP using Simplex method. Max Z = 2{x(1)} + {x(2)} + {x(3)} subject to 4{x(1)} + 6{x(2)} + 3{x(3)} ≤ 8, 3{x(1)} − 6{x(2)} − 4{x(3)} ≤ 1, 2{x(1)} + 3{x(2)} − 5{x(3)} ≥ 4 and {x(1)}, {x(2)}, {x(3)} ≥ 0.', 13, '2020 N/D')},
  12: {'a': ('', f'Using dual simplex method solve the LPP: Minimize z = 2{x(1)} + {x(2)} subject to 3{x(1)} + {x(2)} ≥ 3, 4{x(1)} + 3{x(2)} ≥ 6, {x(1)} + 2{x(2)} ≥ 3 and {x(1)}, {x(2)} ≥ 0.', 13, '2021 N/D'),
       'b': ('', 'Solve the transportation problem.' + T([['I', 21, 16, 25, 13, 11], ['II', 17, 18, 14, 23, 13], ['III', 32, 27, 18, 41, 19], ['Demand', 6, 10, 12, 15, '']], ['', '1', '2', '3', '4', 'Supply']), 13, '2021 N/D')},
  13: {'a': ('', f'Solve the following IPP: Minimize Z = −2{x(1)} − 3{x(2)} subject to 2{x(1)} + 2{x(2)} ≤ 7, {x(1)} ≤ 2, {x(2)} ≤ 2 and {x(1)}, {x(2)} ≥ 0 and integers.', 13, '2021 N/D'),
       'b': ('', 'A student has to take examinations in three courses A, B and C. He has three days available for study. He feels it would be best to devote a whole day to the study of the same course, so that he may study a course for one day, two days or three days or not at all. His estimates of the grade he may get by study are as follows:' + T([[0, 0, 1, 0], [1, 1, 1, 1], [2, 1, 3, 3], [3, 3, 4, 3]], ['Study days / Course', 'A', 'B', 'C']) + 'How should he plan to study so that he maximizes the sum of the grades?', 13, '2021 N/D')},
  14: {'a': ('', 'Describe Kuhn–Tucker conditions with a suitable example.', 13, '2021 N/D'),
       'b': ('', 'Solve 2x<sup>3</sup> − 2.5x − 5 = 0 for the root in [1, 2] by Newton Raphson method.', 13, '2020 N/D')},
  15: {'a': ('', '(i) What is the critical path method and what is its usefulness? (5) (ii) Draw the network diagram exactly with two dummies. (8)' + T([['A', '–'], ['B', '–'], ['C', 'B'], ['D', 'A, C'], ['E', 'A'], ['F', 'E'], ['G', 'E'], ['H', 'G'], ['I', 'D, F'], ['J', 'G, I'], ['K', 'G, I'], ['L', 'H, K']], ['Activity', 'Must be preceded by']), 13, '2021 N/D'),
       'b': ('', 'A small project is composed of 7 activities whose time estimates are listed below. Activities are identified by their beginning (i) and ending (j) node numbers.' + T([[1, 2, 1, 1, 7], [1, 3, 1, 4, 7], [1, 4, 2, 2, 8], [2, 5, 1, 1, 1], [3, 5, 2, 5, 14], [4, 6, 2, 5, 8], [5, 6, 3, 6, 15]], ['i', 'j', 't<sub>0</sub>', 't<sub>1</sub>', 't<sub>p</sub>']) + '(i) Draw the network. (ii) Calculate the expected variances for each. (iii) Find the expected project completion time. (iv) Calculate the probability that the project will be completed at least 3 weeks earlier than expected. (v) If the project due date is 18 weeks, what is the probability?', 13, '2021 N/D')},
  16: Q16}},
{'name': 'Model Question Paper 2', 'focus': 'Questions from the 2020 paper, with the repeated Part C',
 'A': [('What is meant by optimal solution of LPP?', '2020 N/D'), ('Define feasible solution and optimal solution to the linear programming problem.', '2021 N/D'),
       ('Write the difference between the transportation problem and the assignment problem.', '2020 N/D'), ('What do you understand by degeneracy in a transportation problem?', '2021 N/D'),
       ('Write the ILP algorithms based on exploiting the tremendous computational success of Linear Programming.', '2020 N/D'),
       ('Write the Gomory’s constraint for the all-integer programming problem whose simplex table (with non-integer solution) is given.', '2021 N/D'),
       ('What is Newton Raphson method?', '2020 N/D'), ('List the uses of classical optimization theory.', '2021 N/D'),
       ('If there are five activities P, Q, R, S and T such that P, Q, R have no immediate predecessors but S and T have immediate predecessors P, Q and R respectively, represent this situation by a network.', '2020 N/D'),
       ('List out the advantages of PERT.', '2021 N/D')],
 'B': {
  11: {'a': ('', f'Solve the LPP using graphical method. Maximize Z = 3{x(1)} + 4{x(2)} subject to the constraints 2{x(1)} + 5{x(2)} ≤ 120, 4{x(1)} + 2{x(2)} ≤ 80 and {x(1)}, {x(2)} ≥ 0.', 13, '2020 N/D'),
       'b': ('', 'Garden Ltd. has two products, Rose and Lotus. To produce one unit of Rose, 2 units of material X and 4 units of material Y are required. To produce one unit of Lotus, 3 units of material X and 2 units of material Y are required. At least 16 units of each material must be used in order to meet the committed sales of Rose and Lotus. Cost per unit of material X and material Y are Rs. 2.50 and Rs. 0.25 respectively. You are required (i) to formulate the mathematical model (6) and (ii) to solve it for the minimum cost (graphically) (7).', 13, '2021 N/D')},
  12: {'a': ('', f'Use dual simplex method to solve the LPP. Maximize Z = −3{x(1)} − 2{x(2)} subject to {x(1)} + {x(2)} ≥ 1, {x(1)} + {x(2)} ≤ 7, {x(1)} + 2{x(2)} ≥ 10, {x(2)} ≤ 3 and {x(1)}, {x(2)} ≥ 0.', 13, '2020 N/D'),
       'b': ('', 'Consider the problem of assigning four sales persons to four different sales regions as shown in the following table such that the total sales is maximized.' + T([['1', 10, 22, 12, 14], ['2', 16, 18, 22, 10], ['3', 24, 20, 12, 18], ['4', 16, 14, 24, 20]], ['Salesman / Region', '1', '2', '3', '4']) + 'The cell entries represent annual sales figures in lakhs of rupees. Find the optimal allocation of the sales persons to the different regions.', 13, '2020 N/D')},
  13: {'a': ('', f'Find the optimum integer solution to the following linear programming problem: Maximize z = {x(1)} + 2{x(2)} subject to 2{x(2)} ≤ 7, {x(1)} + {x(2)} ≤ 7, 2{x(1)} ≤ 11 and {x(1)}, {x(2)} ≥ 0 and integers.', 13, '2020 N/D (printed 2x<sub>1</sub> = 11; the intended constraint is ≤ 11)'),
       'b': ('', f'Use Branch and Bound method to solve the following: Maximize z = 2{x(1)} + 2{x(2)} subject to 5{x(1)} + 3{x(2)} ≤ 8, {x(1)} + 2{x(2)} ≤ 4 and {x(1)}, {x(2)} ≥ 0 and integers.', 13, '2020 N/D')},
  14: {'a': ('', f'Minimize f = {x(1)}<sup>2</sup> + 2{x(2)}<sup>2</sup> + 3{x(3)}<sup>2</sup> subject to the constraints g<sub>1</sub> = {x(1)} − {x(2)} − 2{x(3)} ≤ 12 and g<sub>2</sub> = {x(1)} + 2{x(2)} − 3{x(3)} ≤ 8, using Kuhn–Tucker conditions.', 13, '2020 N/D'),
       'b': ('', 'Illustrate the sensitivity analysis in the Jacobian method.', 13, '2021 N/D')},
  15: {'a': ('', 'Draw the network from the following activities and find the critical path and the total duration of the project.' + T([['A', '–', 3], ['B', '–', 8], ['C', 'A', 9], ['D', 'B', 6], ['E', 'C', 10], ['F', 'C', 14], ['G', 'C, D', 11], ['H', 'F, G', 10], ['I', 'E', 5], ['J', 'I', 4], ['K', 'H', 1]], ['Activity', 'Immediate predecessors', 'Duration (weeks)']), 13, '2020 N/D'),
       'b': ('', 'A project has the following activities and other characteristics:' + T([['A', '–', 4, 7, 16], ['B', '–', 1, 5, 15], ['C', 'A', 6, 12, 30], ['D', 'A', 2, 5, 8], ['E', 'C', 5, 11, 17], ['F', 'D', 3, 6, 15], ['G', 'B', 3, 9, 27], ['H', 'E, F', 1, 4, 7], ['I', 'G', 4, 19, 28]], ['Activity', 'Preceding activity', 'Most optimistic', 'Most likely', 'Most pessimistic']) + 'Required: (i) draw the PERT network diagram; (ii) identify the critical path; (iii) prepare the activity schedule for the project; (iv) determine the mean project completion time; (v) find the probability that the project is completed in 36 weeks.', 13, '2020 N/D')},
  16: Q16}},
]

def header(i):
    boxes = ''.join('<span></span>' for _ in range(12))
    return f"""
<div class="reg">Reg. No. : <span class="boxes">{boxes}</span></div>
<div class="qpc">Model Question Paper : {i}</div>
<div class="c">B.E./B.Tech. DEGREE EXAMINATIONS — MODEL PAPER</div>
<div class="c">Open Elective II</div>
<div class="c">OIE 352 — RESOURCE MANAGEMENT TECHNIQUES</div>
<div class="c">(Regulations 2021)</div>
<div class="tm"><span>Time : Three hours</span><span>Maximum : 100 marks</span></div>
<div class="c">(Use of normal table is permitted)</div>
<div class="c">Answer ALL questions.</div>
<div class="c part">PART A — (10 × 2 = 20 marks)</div>"""

def rows_for(p, qnos):
    rows = []
    for q in qnos:
        for side in ('a', 'b'):
            sub, text, marks, src = p['B'][q][side]
            qno = f'{q}.' if side == 'a' else ''
            rows.append(f'<div class="pb{" first" if qno else ""}"><span class="q">{qno}</span><span class="ab">({side})</span><span class="sub"></span><span class="tx">{text}</span><span class="mk">({marks})</span></div>')
            if side == 'a': rows.append('<div class="or">Or</div>')
    return ''.join(rows)

def paper_html(i, p):
    a = ''.join(f'<div class="pa"><span class="no">{k+1}.</span><span class="tx">{t}</span></div>' for k, (t, s) in enumerate(p['A']))
    return (f'<div class="paper">{header(i)}{a}<div class="c part">PART B — (5 × 13 = 65 marks)</div>{rows_for(p, range(11, 16))}'
            f'<div class="c part partc">PART C — (1 × 15 = 15 marks)</div>{rows_for(p, [16])}<div class="endline"></div></div>')

def sources_html():
    out = ['<div class="paper src"><h2>Where each question came from</h2>'
           '<p>OIE352 has no public question papers yet. Every question below is a real question from the two public papers of CS6704 Resource Management Techniques (Regulations 2013), the same subject: '
           'N/D 2020 (code X20411) and N/D 2021 (code 70398). The paper layout (Part A 10 × 2, Part B 5 × 13, Part C 1 × 15) follows those papers and the Regulation 2021 pattern. '
           'The real OIE352 paper may differ. N/D = Nov/Dec.</p>']
    for p in PAPERS:
        out.append(f'<h3>{p["name"]} — {p["focus"]}</h3><table><tr><th>Q</th><th>Seen in</th><th>Q</th><th>Seen in</th></tr>')
        cells = [(f'A{k+1}', s) for k, (t, s) in enumerate(p['A'])]
        for q in range(11, 17):
            for side in ('a', 'b'): cells.append((f'{q}({side})', p['B'][q][side][3]))
        half = (len(cells) + 1) // 2
        for l, r in zip(cells[:half], cells[half:] + [('', '')]):
            out.append(f'<tr><td class="k">{l[0]}</td><td>{l[1]}</td><td class="k">{r[0]}</td><td>{r[1]}</td></tr>')
        out.append('</table>')
    out.append('</div>'); return ''.join(out)

CSS_SRC = open(os.path.join(HERE, '..', '..', 'model-papers', 'build_model.py')).read()
CSS = re.search(r'CSS = """(.*?)"""', CSS_SRC, re.S).group(1) + """
.partc { margin-top: 6mm; }
.c.part { break-after: avoid; }
.qtb { border-collapse: collapse; margin: 2mm 0 2mm 4mm; font-size: 10pt; } .qtb td, .qtb th { border: 0.7pt solid #000; padding: 0.6mm 2.4mm; text-align: center; font-weight: normal; }
"""
H = ('<!doctype html><html><head><meta charset="utf-8"><title>OIE352 Resource Management Techniques — Model Question Papers</title>'
     f'<style>{CSS}</style></head><body>' + ''.join(paper_html(i, p) for i, p in enumerate(PAPERS, 1)) + sources_html() + '</body></html>')
if __name__ == '__main__':
    out = os.path.join(HERE, 'OIE352_Model_Question_Papers.html'); open(out, 'w', encoding='utf-8').write(H); print(out)
