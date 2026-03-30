#!/usr/bin/env python3

# This script generate the combined output from files with the given extensions.
# Author: David HEURTEVENT <david@heurtevent.org> - frua.fr
# License: Apache-2.0

import os
import datetime

# Define the input and output file paths
input_dir = '../doc/'  # current directory
output_file = '../incus-git-doc.txt'

# Define the extensions to consider
extensions = ['.md', '.txt', '.yaml']

# Get the current date
date = datetime.datetime.now().strftime("%Y-%m-%d")

# Write the metadata - deletes the file if pre-existing
with open(output_file, 'w') as out:
    out.write('--- Metadata ---\n')
    out.write('Content: Combination of the incus documentation files from the git repo\n')
    out.write('Source: https://github.com/lxc/incus/doc\n')
    out.write('Date: %s\n'%date)
    out.write('Author: lxc/incus (linuxcontainers)\n')
    out.write('License: Apache-2.0\n')
    out.write('GeneratedBy: https://github.com/fruafr/incus-doc-git\n')
    out.write('---\n')

# Walk through the directory and subdirectories
for root, dirs, files in os.walk(input_dir):
    for file in files:
        # Check if the file has one of the desired extensions
        if os.path.splitext(file)[1].lower() in extensions:
            # Construct the relative path of the file
            rel_path = os.path.relpath(os.path.join(root, file), input_dir)
            print(rel_path)

            # Read the file content
            with open(os.path.join(root, file), 'r') as f:
                content = f.read()

            # Write the content to the output file
            with open(output_file, 'a') as out:
                out.write('--- {} ---\n'.format(file))
                out.write(content)
                out.write('\n')


