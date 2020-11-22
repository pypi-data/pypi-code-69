#!/usr/bin/env python
# coding: utf-8

# Copyright (c) Mito.
# Distributed under the terms of the Modified BSD License.

"""
Contains helpful utility functions for saving and reading
in analyses.
"""

import os
import json
from string import ascii_letters, digits

from mitosheet._version import __version__
from mitosheet.steps import STEPS
from mitosheet.profiling import timeit


# Where all global .mito files are stored
MITO_FOLDER = os.path.expanduser("~/.mito")

# The current version of the saved Mito analysis
# where we save all the analyses for this version
CURRENT_VERSION_MITO_FOLDER = os.path.join(MITO_FOLDER, __version__)


def read_analysis(analysis_name):
    """
    Given an analysis_name, reads the saved analysis in
    ~/.mito/{analysis_name}.json and returns a JSON object
    representing it.
    """
    analysis_path = f'{CURRENT_VERSION_MITO_FOLDER}/{analysis_name}.json'

    if not os.path.exists(analysis_path):
        return None

    with open(analysis_path) as f:
        try:
            # We try and read the file as JSON
            return json.load(f)
        except: 
            return None

def _get_all_analysis_filenames():
    """
    Returns the names of the files in the CURRENT_VERSION_MITO_FOLDER
    """
    if not os.path.exists(CURRENT_VERSION_MITO_FOLDER):
        return []

    file_names = set([
        f for f in os.listdir(CURRENT_VERSION_MITO_FOLDER) 
        if os.path.isfile(os.path.join(CURRENT_VERSION_MITO_FOLDER, f))
    ])

    return file_names

def _delete_analyses(analysis_filenames):
    """
    For bulk deleting analysis with file names. 
    """
    for filename in analysis_filenames:
        os.remove(os.path.join(CURRENT_VERSION_MITO_FOLDER, filename))

def read_saved_analysis_names():
    """
    Reads the names of all the analyses saved by the user.

    Does not return any of the auto-saved analyses!
    """
    if not os.path.exists(CURRENT_VERSION_MITO_FOLDER):
        return []

    file_names = [
        f for f in os.listdir(CURRENT_VERSION_MITO_FOLDER) 
        if os.path.isfile(os.path.join(CURRENT_VERSION_MITO_FOLDER, f))
        and not f.startswith('UUID-')
    ]

    # We make sure they are in alphabetical order!
    file_names.sort()

    return [
        file_name[:-5] for file_name in file_names 
        if file_name.endswith('.json')
    ]

@timeit
def saved_analysis_names_json():
    return json.dumps(read_saved_analysis_names())

def make_steps_json_obj(steps):
    """
    Given a steps dictonary from a widget_state_container, puts the steps
    into a format that can be saved and recreated. Necessary for saving an
    analysis to a file!
    """
    steps_json_obj = dict()
    for step_id, step in enumerate(steps):
        step_type = step['step_type']
        
        for new_step in STEPS:
            if step_type == new_step['step_type']:

                # Save the step type
                step_summary = {
                    'step_version': new_step['step_version'],
                    'step_type': step_type,
                }
                # As well as all of the parameters for the step
                step_summary.update({key: value for key, value in step.items() if key in new_step['params']})

                steps_json_obj[step_id] = step_summary

    return steps_json_obj

@timeit
def write_analysis(widget_state_container, analysis_name=None):
    """
    Writes the analysis saved in widget_state_container to
    ~/.mito/{analysis_name}. If analysis_name is none, gets the temporary
    name from the widget_state_container.

    NOTE: as the written analysis is from the widget_state_container,
    we assume that the analysis is valid when written and read back in!
    """

    if not os.path.exists(MITO_FOLDER):
        os.mkdir(MITO_FOLDER)

    if not os.path.exists(CURRENT_VERSION_MITO_FOLDER):
        os.mkdir(CURRENT_VERSION_MITO_FOLDER)

    if analysis_name is None:
        analysis_name = widget_state_container.analysis_name

    analysis_path = f'{CURRENT_VERSION_MITO_FOLDER}/{analysis_name}.json'

    with open(analysis_path, 'w+') as f:
        steps_json_obj = make_steps_json_obj(widget_state_container.steps)

        f.write(json.dumps({
            'version': __version__,
            'steps': steps_json_obj
        }))
