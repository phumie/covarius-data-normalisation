import typer
import pandas as pd
from utils.data_processing import process_data, create_output_cvs_file
from utils.validators import validate_cli_inputs


def get_cli_inputs(input_filename, output_filename):
    if validate_cli_inputs(input_filename, output_filename):
        data_obj = pd.read_json(input_filename, encoding='utf-8-sig')
        output_data = process_data(data_obj)
        create_output_cvs_file(output_data, output_filename)
    return


if __name__ == '__main__':
    typer.run(get_cli_inputs)

