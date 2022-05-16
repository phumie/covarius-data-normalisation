import unittest

from utils.validators import *


class MyTestCase(unittest.TestCase):
    def test_01_cli_input_validator(self):
        # test invalid file names
        self.assertEqual(cli_input_validator("input.jsn", "output.cvs"), False)
        self.assertEqual(cli_input_validator("input.json", "output.cv"), False)
        self.assertEqual(cli_input_validator("input.jsn", "output.cs"), False)
        self.assertEqual(cli_input_validator("input.json", "output.cvs"), True)

    def test_02_does_input_file_exists(self):
        # check if input file exists
        self.assertEqual(does_input_file_exists("does_not_exist.json"), False)
        self.assertEqual(does_input_file_exists("test_files/testing.json"), True)

    def test_03_is_input_file_is_empty(self):
        # check if input file is empty
        self.assertEqual(is_input_file_is_empty("test_files/empty.json"), True)
        self.assertEqual(is_input_file_is_empty("test_files/testing.json"), False)

    def test_04_is_json(self):
        # check if json file contents are in json format
        self.assertEqual(is_json("test_files/invalid_data.json"), False)
        self.assertEqual(is_json("test_files/testing.json"), True)


if __name__ == '__main__':
    unittest.main()
