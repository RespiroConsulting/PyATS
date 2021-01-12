"""
<PYATS_JOBFILE>
"""
# To run the job:
# pyats run job example_job.py

import os
import time
from pyats.easypy import run

# All run() must be inside a main function
def main():
    run('task1_script.py')
