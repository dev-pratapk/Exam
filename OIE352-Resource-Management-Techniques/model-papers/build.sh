#!/usr/bin/env bash
# Usage: OIE352-Resource-Management-Techniques/model-papers/build.sh  (python3 + Node with Playwright; set NODE_PATH if needed)
set -e
cd "$(dirname "$0")"
python3 build_model.py
node ../../report/to_pdf.js "$PWD/OIE352_Model_Question_Papers.html" "$PWD/../OIE352_Model_Question_Papers.pdf" "OIE352 Model Question Papers (built from previous year questions, not official)"
rm -f OIE352_Model_Question_Papers.html
