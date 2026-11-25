"""Two CS3551 model question papers in the exact Anna University layout (Part A 10x2, Part B 5x13, Part C 1x15),
using only real questions from previous papers. Output: CS3551_Model_Question_Papers.html"""
import os
HERE = os.path.dirname(os.path.abspath(__file__))

# Part B / C: unit -> {'a': [(sub, text, marks, source)], 'b': [...]}
PAPERS = [
{
 'name': 'Model Question Paper 1', 'focus': 'Most-repeated questions',
 'A': [
  ('Distinguish between message passing systems and shared memory systems.', '2024 A/M, 2021 N/D'),
  ('What are the motivations for distributed systems?', '2024 A/M'),
  ('How do you define the scalar time and vector time?', '2023 N/D'),
  ('Define global state and consistent global state.', '2024 A/M'),
  ('List down the three requirements of mutual exclusion algorithms.', '2024 N/D'),
  ('What is a false deadlock and when does it occur?', '2024 A/M'),
  ('List down any four issues in failure recovery.', '2024 N/D'),
  ('What is a checkpoint in the recovery system? How is it useful?', '2023 N/D'),
  ('What is virtualization in cloud computing?', '2024 A/M'),
  ('List the characteristics of cloud computing.', '2024 A/M'),
 ],
 'B': {
  11: {'a': [('', 'Explain blocking, non-blocking, synchronous and asynchronous primitives for distributed communication. Also summarize major libraries and standards for building distributed applications.', 13, '2024 A/M')],
       'b': [('', 'Explain the design issues and challenges in the design of distributed operating systems.', 13, '2024 A/M')]},
  12: {'a': [('', 'What is snapshot and what are the needs of taking snapshot in distributed systems? Outline Chandy–Lamport algorithm for snapshot and illustrate the algorithm.', 13, '2024 A/M')],
       'b': [('', 'Describe the physical clock synchronization and logical clock synchronization and explain the framework of a system of logical clock.', 13, '2023 N/D')]},
  13: {'a': [('', 'Outline Ricart and Agrawala’s algorithm for implementing mutual exclusion in distributed systems and illustrate the algorithm.', 13, '2024 A/M')],
       'b': [('', 'Compare and contrast Chandy–Misra–Haas algorithm for the AND model and OR model.', 13, '2024 N/D')]},
  14: {'a': [('', 'What are the different check pointing based recovery systems available? Explain the coordinated check pointing algorithm with illustration.', 13, '2023 N/D')],
       'b': [('', 'What is agreement in a failure free system? Explain how agreement is reached in message-passing synchronous systems with failures.', 13, '2024 A/M')]},
  15: {'a': [('', 'Explain the types of cloud computing deployment models with their relative advantages and disadvantages.', 13, '2024 A/M')],
       'b': [('', 'Explain the different cloud services and the platforms that support these services. Give an example for application service adapted by any organization.', 13, '2023 N/D')]},
  16: {'a': [('', 'The management of an autonomous education institution decided to migrate its website and database from on-premises infrastructure to the Cloud. As an expert of cloud computing you are contacted by management to identify the best suited cloud deployment model and service model for the institution. Describe the important factors you can consider for selecting the cloud deployment model and service model for the institution. Also justify, in what way the selected models are best suited for the institution compared to other models.', 15, '2024 A/M')],
       'b': [('', 'Illustrate centralized and distributed algorithms for total order in message and group communication systems.', 15, '2024 N/D')]},
 }},
{
 'name': 'Model Question Paper 2', 'focus': 'Next most frequent questions',
 'A': [
  ('Name the primitives for distributed communication.', '2021 N/D'),
  ('List out the distributed system challenges.', '2021 A/M'),
  ('What are the limitations of logical clock?', '2024 A/M'),
  ('Distinguish causal order and total order in group communication.', '2024 N/D'),
  ('List down the modifications that need to be done to the Chandy–Lamport snapshot algorithm so that it records a strongly consistent snapshot (i.e., all channel states are recorded empty).', '2024 N/D'),
  ('What is the purpose of the wait-for-graph (WFG)? Give an example for WFG.', '2021 A/M'),
  ('List the advantages and limitations of token-based algorithms for implementing mutual exclusion.', '2024 A/M'),
  ('What is meant by cascaded rollback?', '2024 N/D'),
  ('What are the advantages and disadvantages of asynchronous checkpointing?', '2024 A/M'),
  ('Distinguish scalability and elasticity in cloud computing.', '2024 N/D'),
 ],
 'B': {
  11: {'a': [('', 'Explain message passing systems and discuss on the message oriented middleware and its types. Also explain their functionality in distributed computing.', 13, '2023 N/D')],
       'b': [('', 'Prove that in a distributed computation, for an event, the surface of the past cone (i.e., all the events on the surface) form a consistent cut. Does it mean that all events on the surface of the past cone are always concurrent? Give an example to make your case.', 13, '2024 N/D')]},
  12: {'a': [('', 'Give a real time scenario where FIFO message queue is used. Write and describe the snapshot algorithms for FIFO channels.', 13, '2023 N/D')],
       'b': [('', 'Explain various ways of ordering messages in group communications. Also illustrate distributed algorithm to implement total order and causal order of messages.', 13, '2024 A/M')]},
  13: {'a': [('', 'Outline the Chandy–Misra–Haas algorithm to detect deadlock in OR model and illustrate the algorithm with an example.', 13, '2024 A/M')],
       'b': [('', 'State the Lamport’s algorithm and its use and also the limitations and benefits. Compare this with any two token based algorithms.', 13, '2023 N/D')]},
  14: {'a': [('', 'What is check pointing and why it is needed in distributed systems? Illustrate the algorithm proposed by Juang and Venkatesan for asynchronous check pointing and recovery.', 13, '2024 A/M')],
       'b': [('', 'Explain in detail consensus algorithm for Byzantine failures.', 13, '2024 N/D')]},
  15: {'a': [('', 'A company like to have an advanced collaboration services like video, chat and web conferences for their employees, but their system does not support any of the IT resources due to insufficient infrastructure. If they could leverage cloud computing technology in their system, suggest a suitable cloud type with proper justification. List the characteristic of cloud computing.', 13, '2023 N/D')],
       'b': [('', 'Explain in detail the various storage services in cloud computing.', 13, '2024 N/D')]},
  16: {'a': [('', 'Outline the Koo and Toueg coordinated check pointing and recovery technique and apply this algorithm to a specific case study to demonstrate how this algorithm avoids the domino effect and live lock problems during the recovery.', 15, '2024 A/M')],
       'b': [('', 'Consider an e-shopping system capable of handling more user requests at a time from various geographic locations. The system will fail as it is designed to handle only minimal count of requests at delayed time intervals. Propose at least 3 design constraints for enhancing the current system and discuss 3 associated challenges.', 15, '2021 N/D (CS8603)')]},
 }},
]

def header(i):
    boxes = ''.join('<span></span>' for _ in range(12))
    return f"""
<div class="reg">Reg. No. : <span class="boxes">{boxes}</span></div>
<div class="qpc">Model Question Paper : {i}</div>
<div class="c">B.E./B.Tech. DEGREE EXAMINATIONS — MODEL PAPER</div>
<div class="c">Fifth Semester</div>
<div class="c">Computer Science and Engineering</div>
<div class="c">CS 3551 — DISTRIBUTED COMPUTING</div>
<div class="c sm">(Common to Computer Science and Design/Computer Science and Engineering (Artificial Intelligence and Machine Learning)/Computer Science and Engineering (Cyber Security)/Computer and Communication Engineering/Artificial Intelligence and Data Science/Information Technology)</div>
<div class="c">(Regulations 2021)</div>
<div class="tm"><span>Time : Three hours</span><span>Maximum : 100 marks</span></div>
<div class="c">Answer ALL questions.</div>
<div class="c part">PART A — (10 × 2 = 20 marks)</div>"""

def rows_for(p, qnos):
    rows = []
    for q in qnos:
        for side in ('a', 'b'):
            for j, (sub, text, marks, src) in enumerate(p['B'][q][side]):
                qno = f'{q}.' if side == 'a' and j == 0 else ''
                ab = f'({side})' if j == 0 else ''
                rows.append(f'<div class="pb{" first" if qno else ""}"><span class="q">{qno}</span><span class="ab">{ab}</span>'
                            f'<span class="sub">{sub}</span><span class="tx">{text}</span><span class="mk">{"(" + str(marks) + ")" if sub else ""}</span></div>')
            if side == 'a': rows.append('<div class="or">Or</div>')
    return ''.join(rows)

def paper_html(i, p):
    a = ''.join(f'<div class="pa"><span class="no">{k+1}.</span><span class="tx">{t}</span></div>' for k, (t, s) in enumerate(p['A']))
    return (f'<div class="paper">{header(i)}{a}<div class="c part">PART B — (5 × 13 = 65 marks)</div>{rows_for(p, range(11, 16))}'
            f'<div class="c part partc">PART C — (1 × 15 = 15 marks)</div>{rows_for(p, [16])}<div class="endline"></div></div>')

def sources_html():
    out = ['<div class="paper src"><h2>Where each question came from</h2>'
           '<p>Every question is a real question from a previous Anna University paper: CS3551 (R2021) unless marked CS8603 (R2017). '
           'A/M = April/May, N/D = Nov/Dec.</p>']
    for p in PAPERS:
        out.append(f'<h3>{p["name"]} — {p["focus"]}</h3><table><tr><th>Q</th><th>Seen in</th><th>Q</th><th>Seen in</th></tr>')
        cells = [(f'A{k+1}', s) for k, (t, s) in enumerate(p['A'])]
        for q in range(11, 17):
            for side in ('a', 'b'):
                for sub, text, marks, src in p['B'][q][side]:
                    cells.append((f'{q}({side})', src))
        half = (len(cells) + 1) // 2
        for l, r in zip(cells[:half], cells[half:] + [('', '')]):
            out.append(f'<tr><td class="k">{l[0]}</td><td>{l[1]}</td><td class="k">{r[0]}</td><td>{r[1]}</td></tr>')
        out.append('</table>')
    out.append('</div>'); return ''.join(out)

CSS = open(os.path.join(HERE, '..', '..', 'model-papers', 'build_model.py')).read()
import re  # noqa: E402
CSS = re.search(r'CSS = """(.*?)"""', CSS, re.S).group(1) + '.partc { margin-top: 6mm; }\n'

H = ('<!doctype html><html><head><meta charset="utf-8"><title>CS3551 Distributed Computing — Model Question Papers</title>'
     f'<style>{CSS}</style></head><body>' + ''.join(paper_html(i, p) for i, p in enumerate(PAPERS, 1)) + sources_html() + '</body></html>')
if __name__ == '__main__':
    out = os.path.join(HERE, 'CS3551_Model_Question_Papers.html'); open(out, 'w', encoding='utf-8').write(H); print(out)
