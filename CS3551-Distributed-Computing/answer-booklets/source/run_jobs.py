"""Send each part of CS3551 Model Question Paper 1 to DeepSeek (via opencode) as a separate job."""
import os, re, sys, subprocess, concurrent.futures as cf
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, '/home/ubuntu/work/lab/ma3354/repo/CS3551-Distributed-Computing/model-papers')
import build_model as bm  # noqa: E402
P1 = bm.PAPERS[0]
def plain(t): return re.sub(r'<[^>]+>', '', t)

HINTS = {
 '11a': 'Must cover: Send()/Receive(); buffered vs unbuffered; the four Send variants (blocking synchronous, non-blocking synchronous, blocking asynchronous, non-blocking asynchronous) and blocking / non-blocking Receive, with the timing diagram showing when each call returns; handles and Wait(); processor synchrony; libraries & standards: sockets, MPI, PVM, RPC, Java RMI, CORBA, DCOM, message-oriented middleware.',
 '11b': 'Organise as Kshemkalyani & Singhal ch.1: (1) challenges from the system perspective (communication, processes, naming, synchronization, data storage and access, consistency and replication, fault tolerance, security, API and transparency, scalability and modularity); (2) algorithmic challenges (execution models, dynamic distributed graph algorithms, time and global state, synchronization/coordination, group communication and multicast, monitoring distributed events, program design and verification, debugging, data replication, load balancing, real-time scheduling, performance); (3) applications of distributed computing and newer challenges (mobile systems, sensor networks, ubiquitous computing, P2P, publish-subscribe, distributed agents, distributed data mining, grid computing, security).',
 '12a': 'Must cover: why snapshots are needed (checkpointing, deadlock/termination detection, garbage collection, debugging); global state = local states + channel states; consistent global state conditions C1 and C2; Chandy–Lamport assumptions (FIFO channels, reliable, strongly connected); Marker Sending Rule and Marker Receiving Rule exactly; termination; a worked example with a space-time diagram (2–3 processes, markers drawn as dashed arrows) showing the recorded local and channel states; properties (recorded state is consistent, may not be a state that actually occurred); complexity O(e) messages, O(d) time.',
 '12b': 'Must cover: physical clock synchronization (clock skew/drift; Cristian’s algorithm; Berkeley algorithm; NTP with offset θ = ((T2 − T1) + (T3 − T4))/2 and delay δ = (T4 − T1) − (T3 − T2)); logical clocks: the framework (time domain T, logical clock C : H → T, clock consistency condition e_i → e_j ⇒ C(e_i) < C(e_j), strong consistency), implementation via rules R1 and R2; scalar time (R1: C_i := C_i + d; R2: C_i := max(C_i, C_msg), then R1) with its properties (consistency, total ordering with process ids, event counting, no strong consistency); vector time rules and properties (isomorphism, strong consistency). Include one space-time diagram with scalar or vector timestamps (check every timestamp).',
 '13a': 'Must cover: assumptions (reliable communication channels as stated in Kshemkalyani & Singhal; Lamport timestamps to order requests); messages REQUEST and REPLY; request-deferred array RD_i; the algorithm in three parts: requesting the CS, executing the CS (after receiving REPLY from all other N−1 sites), releasing the CS (send all deferred REPLYs); the rule for deferring: defer if the site is executing the CS, or is requesting and its own request has a smaller (timestamp, site-id); a worked example with 3 sites and a space-time diagram; correctness (mutual exclusion, no starvation); performance: 2(N−1) messages per CS, synchronization delay T. Compare briefly with Lamport (3(N−1)).',
 '13b': 'Must cover: AND model vs OR model definitions with WFG examples; CMH for AND model (probe(i, j, k), dependent_k(i) array, a deadlock when probe(i, j, i) returns to initiator; one probe per WFG edge, at most m(n−1)/2 messages for m processes at n sites, delay O(n)); CMH for OR model (query(i, j, k) and reply(i, j, k) messages, num_k(i), wait_k(i); engaging query; deadlock declared when the initiator receives replies to all its queries; e query and e reply messages for e WFG edges); a comparison table (model, message types, what is propagated, detection condition, message complexity, false deadlocks). Draw one small WFG for each model.',
 '14a': 'Must cover: checkpoint definition; types of checkpoint-based recovery: uncoordinated checkpointing (domino effect, rollback-dependency graph), coordinated checkpointing (blocking and non-blocking), communication-induced checkpointing (model-based and index-based); then the coordinated checkpointing algorithm of Koo and Toueg in detail: tentative checkpoints, two-phase protocol (initiator asks, processes take tentative checkpoints, reply yes/no, initiator decides permanent or discard), only processes that communicated since last checkpoint take checkpoints (minimal), the rollback recovery part (two phases); diagram; correctness (consistent set, no domino effect).',
 '14b': 'Must cover: agreement problems (Byzantine agreement, consensus, interactive consistency) and the failure-free case (synchronous: every process broadcasts its value, after one round all apply the same decision function; asynchronous failure-free also solvable); then agreement in synchronous systems with failures: (1) consensus with crash failures — the f + 1 round algorithm (each round broadcast the current value if it has not been broadcast before, x := min(x, received)); correctness and f + 1 lower bound; (2) Byzantine agreement: impossible when n ≤ 3f (explain with the 3-process example), the Lamport–Shostak–Pease Oral Messages algorithm OM(f) with f + 1 rounds, (3) phase-king algorithm (n > 4f, f + 1 phases of two rounds). Give a small table of results (failure model × synchronous / asynchronous).',
 '15a': 'Must cover: definition of cloud computing (NIST); four deployment models — public, private (on-premise / hosted), hybrid, community — each with a diagram or box diagram, description, examples, advantages and disadvantages; a comparison table (ownership, cost, security, scalability, control, examples); conclusion on how to choose.',
 '15b': 'Must cover (Bahga & Madisetti): service models IaaS, PaaS, SaaS (with a layered diagram); cloud services and platforms: compute services (Amazon EC2, Google Compute Engine, Windows Azure VMs), storage services (Amazon S3, Google Cloud Storage, Azure Blob/Table/Queue storage), database services (Amazon RDS/DynamoDB, Google Cloud SQL), application services (application runtimes and frameworks such as Google App Engine and Azure Web Sites; queuing (Amazon SQS), email (Amazon SES), notification (Amazon SNS), media services, content delivery (CloudFront)), and examples of platforms that support them (AWS, Google Cloud Platform, Microsoft Azure). Give one concrete example of an application service used by an organization (e.g. a company using Amazon SES/SNS or Google App Engine) and explain it.',
 '16a': 'Recommend a deployment model and a service model for the institution (a reasonable answer: hybrid or public cloud; PaaS for the website, managed database / DBaaS or IaaS for the database), with an architecture diagram. Factors: cost, data sensitivity and compliance (student records), security, scalability for admission/result-day peaks, availability, control, in-house expertise, vendor lock-in, migration effort. Compare with the alternatives in a table and justify why the chosen models fit best. End with migration steps and a conclusion.',
 '16b': 'Must cover: total order definition; (1) centralized algorithm using a coordinator/sequencer (steps, diagram, pros/cons, single point of failure); (2) the distributed three-phase algorithm from Kshemkalyani & Singhal (sender multicasts REVISE_TS, receivers reply PROPOSED_TS (max of local clock and timestamps), sender multicasts FINAL_TS = max of proposed; receivers keep temp_Q and delivery_Q and deliver in timestamp order when the head is deliverable); a space-time diagram with two senders and two/three receivers; complexity 3(n − 1) messages per multicast; also mention causal order (Raynal–Schiper–Toueg) briefly and compare in a table.',
}
PARTA_HINT = 'Answer each in 4–8 lines; use a small comparison table for Q1. Q3: scalar time = single integer per process with rules R1/R2; vector time = vector of n integers. Q4: global state = collection of local states and channel states; consistent if it satisfies C1/C2 (every received message was sent; no message is in transit that is not recorded). Q5: safety, liveness, fairness. Q10: on-demand self-service, broad network access, resource pooling, rapid elasticity, measured service.'

def job_prompt(job):
    head = ('Read SPEC.md in the current directory and follow it exactly.\n'
            'Paper: B.E./B.Tech. CS3551 Distributed Computing, Regulations 2021, Model Question Paper 1.\n')
    if job == 'partA':
        qs = '\n'.join(f'{k+1}. {plain(t)}' for k, (t, s) in enumerate(P1['A']))
        return head + (f'Your part: PART A (10 × 2 = 20 marks). Answer all ten 2-mark questions.\n{qs}\n'
                       f'Use data-q="1" … data-q="10" and data-pages="0.5".\nHints: {PARTA_HINT}\nWrite the file out/partA.html.')
    q, side = int(job[:2]), job[2]
    sub, text, marks, src = P1['B'][q][side][0]
    part = 'PART C' if q == 16 else 'PART B'
    return head + (f'Your part: {part}, Question {q} ({side}) [{marks} marks]: {plain(text)}\n\n'
                   f'Write ONE <div class="ans" data-q="{q} ({side})" data-pages="{5 if marks == 13 else 6}">.\n'
                   f'Content checklist: {HINTS[job]}\n\nWrite the file out/{job}.html.')

JAIL_CFG = """{
  "$schema": "https://opencode.ai/config.json",
  "permission": {"bash": "deny", "webfetch": "deny", "websearch": "deny", "external_directory": "deny", "edit": "allow", "read": "allow"}
}
"""
def run(job, tries=2):
    """Run one job inside an empty jail folder: no shell, no web, no access outside the folder."""
    import shutil, tempfile
    prompt = job_prompt(job).replace('Write the file out/' + job + '.html.', 'Write the file answer.html in the current directory.')
    open(f'{HERE}/prompts/{job}.txt', 'w').write(prompt)
    for t in range(tries):
        jail = tempfile.mkdtemp(prefix=f'dcjail_{job}_')
        open(f'{jail}/opencode.json', 'w').write(JAIL_CFG); shutil.copy(f'{HERE}/SPEC.md', jail)
        try:
            with open(f'{HERE}/logs/{job}.log', 'w') as log:
                r = subprocess.run(['opencode', 'run', '-m', 'opencode/deepseek-v4.1-flash-free', prompt], cwd=jail, stdout=log,
                                   stderr=subprocess.STDOUT, timeout=900,
                                   env={**os.environ, 'PATH': os.path.expanduser('~/.local/bin') + ':' + os.environ['PATH'],
                                        'XDG_DATA_HOME': f'{jail}/.data', 'XDG_STATE_HOME': f'{jail}/.state'})
            rc = r.returncode
        except subprocess.TimeoutExpired:
            rc = 'timeout'
        if os.path.exists(f'{jail}/answer.html'):
            shutil.copy(f'{jail}/answer.html', f'{HERE}/out/{job}.html'); return job, rc, True
    return job, rc, False

if __name__ == '__main__':
    for d in ('out', 'logs', 'prompts'): os.makedirs(f'{HERE}/{d}', exist_ok=True)
    jobs = sys.argv[1:] or ['partA'] + [f'{q}{s}' for q in range(11, 17) for s in 'ab']
    with cf.ThreadPoolExecutor(max_workers=4) as ex:
        for job, rc, ok in ex.map(run, jobs): print(f'{job}: exit={rc} file={"yes" if ok else "NO"}', flush=True)
