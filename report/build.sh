#!/usr/bin/env bash
# Usage: REPO_URL=https://github.com/<owner>/<repo> report/build.sh
# Needs python3 and Node with Playwright (set NODE_PATH if Playwright is installed elsewhere).
set -e
cd "$(dirname "$0")"
python3 build.py
node to_pdf.js "$PWD/MA3354_Exam_Pattern_Analysis.html" "$PWD/../MA3354_Exam_Pattern_Analysis.pdf"
rm -f MA3354_Exam_Pattern_Analysis.html
echo "wrote MA3354_Exam_Pattern_Analysis.pdf"
