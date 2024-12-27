import unittest
import pandas as pd
from scripts.data_processing import DataProcessing  # Update the import path as needed

class TestDataProcessing(unittest.TestCase):
    def setUp(self):
        """
        Set up sample data and initialize the DataProcessing instance 
        for testing. This sample data includes missing values in 
        different columns for testing various scenarios.
        """
        data = {
            'A': [1, 2, None, 4],  # Column A has one missing value
            'B': ['x', None, 'y', 'z'],  # Column B has one missing value
            'C': [None, None, 3, 4],  # Column C has two missing values
            'D': ['a', 'b', 'c', 'd']  # Column D has no missing values
        }
        self.df = pd.DataFrame(data)  # Create a DataFrame from the sample data
        self.processor = DataProcessing(self.df)  # Initialize the DataProcessing class

    def test_missing_data_summary(self):
        """
        Test the `missing_data_summary` method to ensure it accurately
        calculates the count and percentage of missing data for each column.
        """
        summary = self.processor.missing_data_summary()

        # Verify the result is a DataFrame
        self.assertIsInstance(summary, pd.DataFrame)

        # Check if the summary contains the expected columns
        self.assertListEqual(list(summary.columns), ['Missing Count', 'Percentage (%)'])

        # Verify the missing count and percentage for column C
        self.assertEqual(summary.loc['C', 'Missing Count'], 2)
        self.assertAlmostEqual(summary.loc['C', 'Percentage (%)'], 50.0)

    def test_handle_missing_data_high(self):
        """
        Test the `handle_missing_data` method with the 'high' type,
        ensuring columns with high missing percentages are dropped.
        """
        result = self.processor.handle_missing_data('high', ['C'])

        # Verify column C is dropped from the DataFrame
        self.assertNotIn('C', result.columns)

        # Check the shape of the DataFrame to ensure one column is removed
        self.assertEqual(result.shape[1], 3)

    def test_handle_missing_data_moderate(self):
        """
        Test the `handle_missing_data` method with the 'moderate' type,
        ensuring missing values are appropriately handled (e.g., filled)
        for columns with moderate missing percentages.
        """
        result = self.processor.handle_missing_data('moderate', ['A', 'B'])

        # Verify there are no missing values in columns A and B
        self.assertFalse(result['A'].isnull().any())
        self.assertFalse(result['B'].isnull().any())

        # Check if columns A and B are still in the DataFrame
        self.assertIn('A', result.columns)
        self.assertIn('B', result.columns)

    def test_handle_missing_data_low(self):
        """
        Test the `handle_missing_data` method with the 'low' type,
        ensuring missing values in columns with low missing percentages
        are appropriately handled (e.g., filled).
        """
        result = self.processor.handle_missing_data('low', ['A', 'B'])

        # Verify there are no missing values in columns A and B
        self.assertFalse(result['A'].isnull().any())
        self.assertFalse(result['B'].isnull().any())

        # Check if columns A and B are still in the DataFrame
        self.assertIn('A', result.columns)
        self.assertIn('B', result.columns)

if __name__ == '__main__':
    unittest.main()
