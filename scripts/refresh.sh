#!/bin/bash

# Perform a complete git doc refresh

echo "Cloning incus git repo"
bash ./1.clone-incus.sh
echo "Copying docs to git-doc folder and cleaning the output"
bash ./2.cp-git-doc-clean.sh
echo "Removing the copy of the git repo"
bash ./3.rm-incus-git.sh
echo "Combining the output of the documentation files in a single file"
python3 ./4.generate-combined-output.py
# Store the date of extraction
echo "extraction date: $(date +%F)" > ../extraction-date.txt
echo "Refresh performed"
