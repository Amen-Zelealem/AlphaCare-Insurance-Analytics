import unittest
import os
import zipfile
import pandas as pd
from scripts.extract_zip import extract_file_from_zip, load_txt_from_zip, load_data

class TestExtractZip(unittest.TestCase):
    def setUp(self):
        """
        Set up the test environment by creating temporary directories, sample files, 
        and a ZIP archive to use in the tests.
        """
        self.test_dir = "test_data"  # Directory for temporary test files
        self.test_zip = "test.zip"  # Name of the ZIP file to create
        self.test_txt = "sample.txt"  # Name of the sample TXT file to create
        self.extracted_dir = "extracted_data"  # Directory for extracted files

        # Create directories for test and extracted data
        os.makedirs(self.test_dir, exist_ok=True)
        os.makedirs(self.extracted_dir, exist_ok=True)

        # Create a sample TXT file with sample data
        sample_data = "id|name|value\n1|John|100\n2|Doe|200"
        self.sample_txt_path = os.path.join(self.test_dir, self.test_txt)
        with open(self.sample_txt_path, "w") as f:
            f.write(sample_data)

        # Create a ZIP archive containing the sample TXT file
        self.sample_zip_path = os.path.join(self.test_dir, self.test_zip)
        with zipfile.ZipFile(self.sample_zip_path, "w") as zipf:
            zipf.write(self.sample_txt_path, self.test_txt)

    def tearDown(self):
        """
        Clean up the test environment by removing temporary files and directories 
        after the tests have completed.
        """
        # Remove files and directories in the test directory
        for root, dirs, files in os.walk(self.test_dir, topdown=False):
            for file in files:
                os.remove(os.path.join(root, file))
            for dir in dirs:
                os.rmdir(os.path.join(root, dir))
        os.rmdir(self.test_dir)

        # Remove files and directories in the extracted data directory
        for root, dirs, files in os.walk(self.extracted_dir, topdown=False):
            for file in files:
                os.remove(os.path.join(root, file))
            for dir in dirs:
                os.rmdir(os.path.join(root, dir))
        os.rmdir(self.extracted_dir)

    def test_extract_file_from_zip(self):
        """
        Test the `extract_file_from_zip` function to ensure that files are 
        correctly extracted from a ZIP archive to a specified directory.
        """
        # Extract the file from the ZIP archive
        extract_file_from_zip(self.sample_zip_path, self.extracted_dir)

        # Check if the extracted file exists in the target directory
        extracted_file = os.path.join(self.extracted_dir, self.test_txt)
        self.assertTrue(os.path.exists(extracted_file))

    def test_load_txt_from_zip(self):
        """
        Test the `load_txt_from_zip` function to ensure that a TXT file 
        extracted from a ZIP archive is correctly loaded into a pandas DataFrame.
        """
        # Extract the file from the ZIP archive
        extract_file_from_zip(self.sample_zip_path, self.extracted_dir)

        # Load the TXT file into a pandas DataFrame
        df = load_txt_from_zip(self.extracted_dir, self.test_txt)

        # Verify the DataFrame's structure and content
        self.assertIsInstance(df, pd.DataFrame)  # Check if the result is a DataFrame
        self.assertEqual(df.shape, (2, 3))  # Expect 2 rows and 3 columns
        self.assertListEqual(list(df.columns), ["id", "name", "value"])  # Verify column names

    def test_load_data(self):
        """
        Test the `load_data` function to ensure that the full pipeline, including 
        extraction and loading of data, works as expected.
        """
        # Load data directly from the ZIP archive into a pandas DataFrame
        df = load_data(self.sample_zip_path, self.test_txt, extract_to=self.extracted_dir)

        # Verify the DataFrame's structure and content
        self.assertIsInstance(df, pd.DataFrame)  # Check if the result is a DataFrame
        self.assertEqual(df.shape, (2, 3))  # Expect 2 rows and 3 columns
        self.assertListEqual(list(df.columns), ["id", "name", "value"])  # Verify column names

if __name__ == '__main__':
    unittest.main()
