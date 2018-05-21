
# Run this file from project root to see if paths are relative to CWD
# or the script location.

from pathlib import Path
import os
import sys

p = Path('.')

print("full CWD: " + os.path.abspath('.'))
print("prog path rel to CWD: " + os.path.dirname(sys.argv[0]))
print("prog path rel to CWD 2: " + os.path.dirname(__file__))
print("full prog path: " + os.path.abspath(os.path.dirname(sys.argv[0])))
print("full prog path 2: " + os.path.abspath(os.path.dirname(__file__)))