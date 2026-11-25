#!/usr/bin/env bash
# Usage: CS3551-Distributed-Computing/report/build.sh  (python3 + Node with Playwright; set NODE_PATH if needed)
set -e
cd "$(dirname "$0")"
python3 build.py
node ../../report/to_pdf.js "$PWD/CS3551_Exam_Pattern_Analysis.html" "$PWD/../CS3551_Exam_Pattern_Analysis.pdf" "CS3551 Distributed Computing — Exam Pattern Analysis"
rm -f CS3551_Exam_Pattern_Analysis.html
