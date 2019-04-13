import sys

# just insuring that you run the same version of python
assert sys.version_info[:2] == (3, 7)

import py_compile
from pathlib import Path

# compile `source_file.py` to byte-code
CWD = Path(__file__).parent.resolve()

source_file = CWD / "source_file.py"
compiled_file = CWD / "compiled_python_file.pyc"

print(f"compiling '{source_file.parts[-1]}' -> '{compiled_file.parts[-1]}'")
py_compile.compile(source_file, cfile=compiled_file)
