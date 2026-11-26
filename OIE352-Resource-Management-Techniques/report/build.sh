#!/usr/bin/env bash
# Usage: OIE352-Resource-Management-Techniques/report/build.sh  (python3 + Node with Playwright; set NODE_PATH if needed)
set -e
cd "$(dirname "$0")"
python3 build.py
node ../../report/to_pdf.js "$PWD/OIE352_Exam_Pattern_Analysis.html" "$PWD/../OIE352_Exam_Pattern_Analysis.pdf" "OIE352 Resource Management Techniques — Exam Pattern Analysis"
rm -f OIE352_Exam_Pattern_Analysis.html
