#!/bin/bash
pip3 -V
pip3 install --force-reinstall --upgrade -t local_lib git+https://github.com/jaraco/path.py.git --log file.log
python3 my_program.py