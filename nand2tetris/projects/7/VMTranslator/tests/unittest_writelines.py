import unittest
import os

# Import the function to test
from your_module_name import writelines  # Replace 'your_module_name' with the actual name of your module

class TestWriteLines(unittest.TestCase):
    def setUp(self):
        # Create a temporary file for testing
        self.test_filename = "test_file.txt"
    
    def tearDown(self):
        # Remove the temporary file after each test
        if os.path.exists(self.test_filename):
            os.remove(self.test_filename)

    def test_write_string_to_file(self):
        # Test writing a string to a file
        input_data = "This is a test string."
        writelines(input_data, self.test_filename)
        with open(self.test_filename, 'r') as file:
            data_written = file.read()
        self.assertEqual(data_written, input_data)

    def test_write_list_to_file(self):
        # Test writing a list of strings to a file
        input_data = ["Line 1\n", "Line 2\n", "Line 3\n"]
        writelines(input_data, self.test_filename)
        with open(self.test_filename, 'r') as file:
            data_written = file.readlines()
        self.assertEqual(data_written, input_data)

    def test_invalid_input_data_type(self):
        # Test passing invalid input data type
        with self.assertRaises(TypeError):
            writelines(123, self.test_filename)

    def test_invalid_filename_type(self):
        # Test passing invalid filename type
        with self.assertRaises(TypeError):
            writelines("Test", 123)

    def test_empty_filename(self):
        # Test passing an empty filename
        with self.assertRaises(ValueError):
            writelines("Test", "")

if __name__ == '__main__':
    unittest.main()
