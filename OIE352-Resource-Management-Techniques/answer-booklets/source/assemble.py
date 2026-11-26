"""Assemble the DeepSeek answer fragments into two exam-style answer booklets (HTML -> PDF via to_pdf.js)."""
import os, re, sys, html
HERE = os.path.dirname(os.path.abspath(__file__))
REPO = '/home/ubuntu/work/lab/ma3354/repo'
sys.path.insert(0, f'{REPO}/OIE352-Resource-Management-Techniques/model-papers')
import build_model as bm  # noqa: E402
P1 = bm.PAPERS[0]
FONT = f'{REPO}/report/fonts'

def frag(job):
    s = open(f'{HERE}/out/{job}.html', encoding='utf-8').read()
    s = re.sub(r'^```\w*|```$', '', s.strip(), flags=re.M)
    def fix_svg(m):  # HTML <sub>/<sup> are invalid inside SVG <text>; use tspans
        t = m.group(0)
        t = re.sub(r'<sub>(.*?)</sub>', r'<tspan baseline-shift="sub" font-size="10">\1</tspan>', t)
        t = re.sub(r'<sup>(.*?)</sup>', r'<tspan baseline-shift="super" font-size="10">\1</tspan>', t)
        return t
    return re.sub(r'<svg.*?</svg>', fix_svg, s, flags=re.S)

def split_ans(s):
    """-> list of (label, pages, inner_html) for each <div class="ans">"""
    out = []
    for m in re.finditer(r'<div class="ans" data-q="([^"]+)"(?: data-pages="([^"]+)")?>(.*?)</div>\s*(?=<div class="ans"|\Z)', s, re.S):
        out.append((m.group(1).strip(), m.group(2), m.group(3)))
    return out

def qtext_B(q, side, sub):
    for sb, text, marks, src in P1['B'][q][side]:
        if sb == sub: return text, marks
    return '', ''

def block(label, pages, inner, qhtml, marks):
    pg = f'<div class="pg">write ≈ {pages} page{"s" if pages not in ("0.5","1") else ""}</div>' if pages else ''
    mk = f' <span class="mk">({marks} marks)</span>' if marks else ''
    return (f'<div class="row"><div class="mar"><div class="ql">{html.escape(label)}</div>{pg}</div>'
            f'<div class="body"><div class="qq">{qhtml}{mk}</div>{inner}</div></div>')

def part_a():
    out = ['<div class="parth">PART A — (10 × 2 = 20 marks)</div>']
    for label, pages, inner in split_ans(frag('partA')):
        k = int(re.sub(r'\D', '', label) or 0)
        q = P1['A'][k-1][0] if 1 <= k <= 10 else ''
        out.append(block(f'{k}.', pages or '0.5', inner, q, 2))
    return '\n'.join(out)

def part_b(side):
    out = []
    for q in range(11, 17):
        head = ''
        if q == 11: head = '<div class=parth>PART B — (5 × 13 = 65 marks)</div>'
        if q == 16: head = '<div class=parth>PART C — (1 × 15 = 15 marks)</div>'
        out.append(f'<div class="newq">{head}</div>')
        for label, pages, inner in split_ans(frag(f'{q}{side}')):
            sub, text, marks, src = P1['B'][q][side]
            out.append(block(f'{q} ({side})', pages, inner, text, marks))
    return '\n'.join(out)

def cover(letter, side):
    rows = ''.join(f'<td>{k}</td>' for k in range(1, 11))
    brow = ''.join(f'<td>{q} ({side})</td>' for q in range(11, 17))
    return f"""
<div class="cover">
 <div class="ct">ANSWER BOOKLET</div>
 <div class="cs">Model answers · Booklet {letter}</div>
 <table class="info">
  <tr><th>Subject</th><td>OIE352 — Resource Management Techniques (Regulations 2021)</td></tr>
  <tr><th>Question paper</th><td>OIE352 Model Question Paper 1 (questions of the 2021 paper and the repeated Part C)</td></tr>
  <tr><th>Questions answered</th><td>Part A: all 10 · Part B and C: option <b>({side})</b> of Q11–Q16</td></tr>
  <tr><th>Other options</th><td>Booklet {'B' if letter == 'A' else 'A'} answers option ({'b' if side == 'a' else 'a'}) of every Part B and Part C question</td></tr>
 </table>
 <div class="qa">
  <div class="qah">Question numbers answered</div>
  <table class="grid"><tr><th>Part A</th>{rows}</tr><tr><th>Marks</th>{''.join('<td>2</td>' for _ in range(10))}</tr></table>
  <table class="grid"><tr><th>Part B / C</th>{brow}</tr><tr><th>Marks</th>{''.join('<td>13</td>' for _ in range(5))}<td>15</td></tr></table>
 </div>
 <div class="plan">
  <div class="qah">How much to write (42-page answer booklet, 3 hours)</div>
  <table class="grid2">
   <tr><th>Section</th><th>Pages to write</th><th>Time</th></tr>
   <tr><td>Part A — 10 × 2 marks</td><td>about 4 pages (½ page each)</td><td>25 min</td></tr>
   <tr><td>Part B — each 13-mark question</td><td>about 4 pages</td><td>25–27 min each</td></tr>
   <tr><td>Part C — 15-mark question</td><td>about 5 pages</td><td>25 min</td></tr>
   <tr><td>Total</td><td><b>about 28–32 pages</b> — you do not need all 42</td><td>2 h 50 min + 10 min to check</td></tr>
  </table>
  <p>The grey note under each question number says how many handwritten pages that answer should take. Start every Part B question on a new page. Draw graphs and networks with a pencil and a scale, and show every table: in this subject the marks follow the steps.</p>
 </div>
 <div class="note">These answers were written with Claude. Every number was computed with exact-fraction programs (simplex, dual simplex, transportation, branch and bound, dynamic programming, PERT) and checked: the transportation and integer-programming results were also verified by exhaustive search. Check the method and the notation against your textbook and your teacher’s notes before memorising. Unofficial; not affiliated with Anna University.</div>
</div>"""

CSS = f"""
@font-face {{ font-family: 'NS'; src: url('file://{FONT}/NotoSans-Regular.ttf'); font-weight: 400; }}
@font-face {{ font-family: 'NS'; src: url('file://{FONT}/NotoSans-Italic.ttf'); font-weight: 400; font-style: italic; }}
@font-face {{ font-family: 'NS'; src: url('file://{FONT}/NotoSans-SemiBold.ttf'); font-weight: 600; }}
@font-face {{ font-family: 'NS'; src: url('file://{FONT}/NotoSans-Bold.ttf'); font-weight: 700; }}
@font-face {{ font-family: 'NSM'; src: url('file://{FONT}/NotoSansMath-Regular.ttf'); }}
@page {{ size: A4; margin: 15mm 14mm 17mm 10mm; }}
body {{ font-family: 'NS', 'NSM', 'DejaVu Sans', sans-serif; font-size: 10.6pt; line-height: 1.6; color: #111; margin: 0; }}
b {{ font-weight: 600; }}
sub, sup {{ font-size: 72%; line-height: 0; }}
.cover {{ break-after: page; border: 1.4pt solid #000; padding: 8mm 12mm 6mm; }}
.ct {{ text-align: center; font-size: 26pt; font-weight: 700; letter-spacing: 3pt; }}
.cs {{ text-align: center; font-size: 13pt; color: #444; margin-bottom: 5mm; }}
table {{ border-collapse: collapse; }}
.info {{ width: 100%; margin-bottom: 5mm; font-size: 10pt; }}
.info th {{ text-align: left; width: 45mm; padding: 1.8mm 3mm; border: 0.8pt solid #000; background: #f3f3f1; font-weight: 600; }}
.info td {{ padding: 1.8mm 3mm; border: 0.8pt solid #000; }}
.qah {{ font-weight: 700; font-size: 11pt; margin: 0 0 2.5mm; }}
.grid {{ width: 100%; margin-bottom: 2mm; font-size: 9.5pt; text-align: center; }}
.grid th, .grid td {{ border: 0.8pt solid #000; padding: 1.2mm 1mm; }} .grid th {{ background: #f3f3f1; width: 22mm; }}
.plan {{ margin-top: 3mm; }}
.grid2 {{ width: 100%; font-size: 10pt; }} .grid2 th, .grid2 td {{ border: 0.8pt solid #000; padding: 1.3mm 3mm; text-align: left; }} .grid2 th {{ background: #f3f3f1; }}
.plan p {{ font-size: 9pt; color: #333; margin: 2mm 0 0; line-height: 1.45; }}
.note {{ margin-top: 3mm; font-size: 8pt; color: #555; border-top: 0.8pt solid #999; padding-top: 3mm; }}
.parth {{ text-align: center; font-weight: 700; font-size: 12pt; letter-spacing: 0.5pt; margin: 0 0 5mm; padding: 2mm 0; border-top: 1pt solid #000; border-bottom: 1pt solid #000; }}
.newq {{ break-before: page; }}
.newq:first-of-type {{ break-before: page; }}
.row {{ display: flex; margin-bottom: 7mm; }}
.mar, .qq, .body > h4:first-of-type {{ break-after: avoid; }}
.mar {{ width: 21mm; flex: none; border-right: 1.3pt solid #d33; padding-right: 2.5mm; text-align: right; }}
.ql {{ font-weight: 700; font-size: 10.5pt; line-height: 1.35; }}
.pg {{ font-size: 7.5pt; color: #2b7a3f; margin-top: 1.5mm; line-height: 1.25; }}
.body {{ flex: 1; padding-left: 5mm; min-width: 0; }}
.qq {{ break-after: avoid; background: #f4f4f2; border-radius: 3pt; padding: 2mm 3mm; font-size: 9.6pt; color: #333; font-style: italic; margin-bottom: 3mm; }}
.qq .mat {{ font-style: normal; }}
.qq .fig, .qq img {{ display: none; }}
.mk {{ font-style: normal; color: #666; white-space: nowrap; }}
h4 {{ font-size: 10.8pt; font-weight: 700; margin: 3.5mm 0 1.5mm; text-decoration: underline; text-underline-offset: 2pt; break-after: avoid; }}
p {{ margin: 0 0 2.2mm; }}
ol, ul {{ margin: 0 0 2.5mm; padding-left: 6mm; }} li {{ margin-bottom: 1.2mm; }}
.eq {{ margin: 1.5mm 0 2mm 6mm; }}
.result {{ border: 1.1pt solid #000; padding: 2mm 3mm; margin: 3mm 0 1mm; font-weight: 600; break-inside: avoid; }}
table.tt {{ border-collapse: collapse; margin: 2mm 0 3mm; font-size: 9.6pt; break-inside: avoid; }}
table.tt th, table.tt td {{ border: 0.7pt solid #000; padding: 1mm 2.5mm; text-align: center; vertical-align: top; }}
table.tt th {{ background: #f3f3f1; font-weight: 600; }}
table.tt caption {{ caption-side: top; text-align: left; font-weight: 600; font-size: 9pt; padding: 1mm 0; }}
.qq table.qtb {{ border-collapse: collapse; margin: 1mm 0 1mm 3mm; font-size: 8.4pt; font-style: normal; }} .qq table.qtb td, .qq table.qtb th {{ border: 0.6pt solid #666; padding: 0.3mm 1.6mm; font-weight: normal; }}
p.note {{ font-size: 9.2pt; color: #333; margin: 1mm 0 2.5mm; }}
figure.dg {{ margin: 3mm 0; text-align: center; break-inside: avoid; }}
figure.dg svg {{ max-width: 100%; height: auto; }}
figcaption {{ font-size: 9pt; color: #444; margin-top: 1mm; }}
.mat {{ display: inline-block; vertical-align: middle; border-left: 1pt solid #000; border-right: 1pt solid #000; padding: 0 2pt; margin: 0 2pt; }}
.mat table {{ border-collapse: collapse; }} .mat td {{ padding: 0 3pt; font-size: 9pt; line-height: 1.2; }}
"""

def booklet(letter, side):
    body = cover(letter, side) + '<div>' + part_a() + '</div>' + part_b(side)
    return (f'<!doctype html><html><head><meta charset="utf-8"><title>OIE352 Model Paper 1 — Answer Booklet {letter}</title>'
            f'<style>{CSS}</style></head><body>{body}</body></html>')

if __name__ == '__main__':
    for letter, side in (('A', 'a'), ('B', 'b')):
        p = f'{HERE}/Booklet_{letter}.html'; open(p, 'w', encoding='utf-8').write(booklet(letter, side)); print(p)
