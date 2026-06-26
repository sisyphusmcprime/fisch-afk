"""

    -- config.py --

    Imports all the stored json data into Python.

"""
import json

def init_pos(run_path):
    with open(f'{run_path}/json/position.jsonc', 'r') as pos_json:
        global pos_consts
        pos_consts = json.load(pos_json)

def init(run_path):
    init_pos(run_path)