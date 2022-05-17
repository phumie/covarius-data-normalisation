import enum
from sys import stderr, stdout

import pandas as pd
from pandas import DataFrame


class AccountNumberType(str, enum.Enum):
    iban = "iban"
    gb_domestic = "gbDomestic"
    unstructured = "unstructured"


class InputFields(str, enum.Enum):
    iban_number = "ibanNumber"
    sort_code = "sortCode"
    account_number = "accountNumber"
    unstructured_account_number = "unstructuredAccountNumber"
    bank_name = "bankName"
    name_1 = "name1"
    name_2 = "name2"
    notes = "notes"


class OutputFields(str, enum.Enum):
    account_number = "accountNumber"
    account_number_type = "accountNumberType"
    bank_name = "bankName"
    branch_country = "branchCountry"
    name_1 = "name1"
    name_2 = "name2"
    user_comments = "userComments"


def cleanup_data(data: DataFrame) -> DataFrame:
    for index in range(len(data)):
        # remove white spaces from bank name
        data[InputFields.bank_name][index] = data[InputFields.bank_name][index].replace(" ", "")
        data[InputFields.notes][index] = data[InputFields.notes][index].encode(encoding="ascii", errors="ignore")
    return data


def process_data(data: DataFrame):
    output_data = []

    # cleanup data
    data = cleanup_data(data)

    for index in range(len(data)):
        processed_data = {}

        # if ibanNumber is not empty
        if data[InputFields.iban_number][index]:
            processed_data = {
                OutputFields.account_number: data[InputFields.iban_number][index],
                OutputFields.account_number_type: AccountNumberType.iban
            }
        # if sortCode and accountNumber are not empty
        elif data[InputFields.sort_code][index] and data[InputFields.account_number][index]:
            processed_data = {
                OutputFields.account_number: data[InputFields.sort_code][index] + data[InputFields.account_number][
                    index],
                OutputFields.account_number_type: AccountNumberType.gb_domestic
            }
        # if unstructuredAccountNumber is not empty
        elif data[InputFields.unstructured_account_number][index]:
            processed_data = {
                OutputFields.account_number: data[InputFields.unstructured_account_number][index],
                OutputFields.account_number_type: AccountNumberType.unstructured
            }
        # if conditions not met, throw error and skip account record
        else:
            stderr.write(
                'DataError: Account record at index {} has been removed - required fields missing \n'.format(index))
            continue

        # find last '-' character to get bank name and branch country
        dash_index = data[InputFields.bank_name][index].rfind("-")

        # get branch name and branch country
        bank_name_str = data[InputFields.bank_name][index]
        bank_name = bank_name_str[:dash_index]
        branch_country = bank_name_str[dash_index + 1:]

        processed_data.update({
            OutputFields.bank_name: bank_name,
            OutputFields.branch_country: branch_country,
            OutputFields.name_1: data[InputFields.name_1[0:30]][index],
            OutputFields.name_2: data[InputFields.name_2[0:20]][index],
            OutputFields.user_comments: data[InputFields.notes][index],
        })

        output_data.append(processed_data)
    return output_data


def create_output_cvs_file(output_data, output_filename):
    data = pd.DataFrame(output_data)
    data.to_csv(output_filename, index=False)
    stdout.write("Process complete: '{}' file created successfully".format(output_filename))
    return
