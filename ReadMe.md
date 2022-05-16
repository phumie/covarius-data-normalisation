# Covarius Data Normalisation

The covarius data normalisation application takes bank acount data in json format, processes the data according to the business rules, and generates a cvs file with the processed data.

## Installation
Follow the following steps to run the application.

1. Clone the project repository.
```bash
git clone https://github.com/phumie/covarius-data-normalisation.git
```

2. Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the packages in build_requirements.txt. The packages used for the project are *Typer* and *pandas*.
For more information on the packages, visit the [typer docs page](https://typer.tiangolo.com/) and the [pandas docs page](https://pandas.pydata.org/docs/). 

```bash
pip install -r build_requirements.txt
```

## Execution
To run the application, pass the command below in the terminal.

**Note

**input.json** is the name of the json file that contains data the application processes.  The input file must be located in the parent directory.

**output.cvs** is the name of the output file that will be generated after the input data has been processed.

```bash
python main.py input.json output.json
```


## Tests
To run the unit tests, run the following command in the terminal. Please note that the tests are based on the application validators.
```bash
python test_input_validators.py
```