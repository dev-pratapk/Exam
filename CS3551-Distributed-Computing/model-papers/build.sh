#!/usr/bin/env bash
# Usage: CS3551-Distributed-Computing/model-papers/build.sh  (python3 + Node with Playwright; set NODE_PATH if needed)
set -e
cd "$(dirname "$0")"
python3 build_model.py
node ../../report/to_pdf.js "$PWD/CS3551_Model_Question_Papers.html" "$PWD/../CS3551_Model_Question_Papers.pdf" "CS3551 Model Question Papers (built from previous year questions, not official)"
rm -f CS3551_Model_Question_Papers.html
