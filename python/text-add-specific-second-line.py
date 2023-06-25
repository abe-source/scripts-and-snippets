# Usage: python3 text-add-specific-second-line.py <input_file>.txt > output.txt

from itertools import chain,repeat
import sys

file_name = sys.argv[1]

with open(file_name) as f:
    lines = f.readlines()
    modified_list = list(chain.from_iterable(zip(lines, repeat("peter"))))
    for item in modified_list:
        print(item.strip())
