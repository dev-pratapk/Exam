#!/usr/bin/env bash
# Usage: model-papers/build.sh   (needs python3 and Node with Playwright; set NODE_PATH if needed)
set -e
cd "$(dirname "$0")"
python3 build_model.py
node ../report/to_pdf.js "$PWD/MA3354_Model_Question_Papers.html" "$PWD/../MA3354_Model_Question_Papers.pdf" "MA3354 Model Question Papers (built from previous year questions, not official)"
rm -f MA3354_Model_Question_Papers.html
echo "wrote MA3354_Model_Question_Papers.pdf"
