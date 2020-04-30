#!/usr/bin/env python
"""Run Python code automatically within virtualenv

Search for a virtualenv and run the code within that."""
import os
import pathlib
import sys
import datetime

current_dir = pathlib.Path(os.getcwd())
while current_dir:
    python_executable = current_dir / ".venv" / "Scripts" / "python.exe"
    if python_executable.is_file():
        break
    if current_dir == current_dir.parent:
        break
    current_dir = current_dir.parent

if not python_executable.is_file():
    python_executable = pathlib.Path(sys.executable)

with pathlib.Path(__file__).with_suffix(".log").open("a") as log_file:
    date = str(datetime.datetime.now())
    args = " ".join(sys.argv[1:])
    cwd = os.getcwd()
    current_dir = current_dir.as_posix()
    log_file.write(f"{date} {args} # {cwd} # {current_dir}\n")

os.spawnv(os.P_WAIT, python_executable, sys.argv)
