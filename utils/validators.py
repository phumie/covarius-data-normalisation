import os
from sys import stderr

import pandas as pd


def cli_input_validator(input_filename: str, output_filename: str) -> bool:
    if not input_filename.endswith('.json') and not output_filename.endswith('.cvs'):
        stderr.write('InputValidationError: input file name must contain .json extension and output file name must contain .cvs extension\n')
        return False
    elif not input_filename.endswith('.json'):
        stderr.write('InputValidationError: input file name must contain .json extension\n')
        return False
    elif not output_filename.endswith('.cvs'):
        stderr.write('InputValidationError: output file name must contain .cvs extension\n')
        return False
    return True


def does_input_file_exists(input_filename: str):
    if not os.path.exists(input_filename):
        stderr.write('InputFileError: file with name "{}" does not exist.\n'.format(input_filename))
        return False
    return True


def is_input_file_is_empty(input_filename: str):
    if os.stat(input_filename).st_size == 0:
        stderr.write('InputFileError: input file cannot be empty.\n')
        return True
    return False


def is_json(input_filename: str):
    try:
        data_obj = pd.read_json(input_filename, encoding='utf-8-sig')
    except ValueError as e:
        stderr.write('FileContentError: input file contents should be in json format.\n')
        return False
    return True


def validate_cli_inputs(input_filename, output_filename):
    validation_passed = True
    if not cli_input_validator(input_filename, output_filename):
        validation_passed = False

    if validation_passed and not does_input_file_exists(input_filename):
        validation_passed = False

    if validation_passed and is_input_file_is_empty(input_filename):
        validation_passed = False

    if validation_passed and not is_json(input_filename):
        validation_passed = False
    return validation_passed
