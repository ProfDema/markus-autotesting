#!/usr/bin/env python3

import os
import sys

from markus_pam_tester import MarkusPAMTester
from markus_tester import MarkusTestSpecs
from markusapi import Markus


if __name__ == '__main__':

    # Markus identifiers
    root_url = sys.argv[1]
    api_key = sys.argv[2]
    assignment_id = sys.argv[3]
    group_id = sys.argv[4]
    repo_name = sys.argv[5]
    SPECS = MarkusTestSpecs()

    # The test files to run (uploaded as support files), and the points assigned:
    # points can be assigned per test function, or per test class (every test function in the class will be worth those
    # points); if a test function/class is missing, it is assigned a default of 1 point (use POINTS = {} for all 1s).
    POINTS = {'test_passes': 1, 'test_fails': 2, 'Test2': 1}
    SPECS['test_points'] = {'test.py': POINTS}

    # The max time to run a single test (defaults to 10 seconds if commented out).
    # SPECS['test_timeout'] = 10

    # The max time to run all tests (defaults to 30 seconds if commented out).
    # SPECS['global_timeout'] = 30

    # The feedback file name (defaults to no feedback file if commented out).
    # SPECS['feedback_file'] = 'feedback_python.txt'

    tester = MarkusPAMTester(specs=SPECS)
    tester.run()
    # Use markus apis if needed
    # if os.path.isfile(FEEDBACK_FILE):
    #     api = Markus(api_key, root_url)
    #     with open(FEEDBACK_FILE) as feedback_open:
    #         api.upload_feedback_file(assignment_id, group_id, FEEDBACK_FILE, feedback_open.read())