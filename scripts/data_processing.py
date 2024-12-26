import pandas as pd

class DataProcessing:
    def __init__(self, data: pd.DataFrame):
        """
        Initialize the DataProcessing class with the data.

        Args:
            data (pd.DataFrame): The input DataFrame to process.
        """
        self.data = data

    def missing_data_summary(self) -> pd.DataFrame:
        """
        Returns a summary of columns with missing data, including count and percentage of missing values.

        Returns:
            pd.DataFrame: A DataFrame with columns 'Missing Count' and 'Percentage (%)' for columns with missing values.
        """
        missing_data = self.data.isnull().sum()
        missing_data = missing_data[missing_data > 0]
        missing_percentage = (missing_data / len(self.data)) * 100
        missing_df = pd.DataFrame({
            'Missing Count': missing_data, 
            'Percentage (%)': missing_percentage
        }).sort_values(by='Percentage (%)', ascending=False)
        return missing_df

    def handle_missing_data(self, missing_type: str, missing_cols: list) -> pd.DataFrame:
        """
        Handles missing data based on predefined strategies.
        """
        if missing_type == 'high':
            self.data = self.data.drop(columns=missing_cols, errors='ignore')
        elif missing_type == 'moderate':
            for col in missing_cols:
                if col in self.data.columns:
                    if self.data[col].dtype == 'object':
                        self.data[col] = self.data[col].fillna(self.data[col].mode()[0] if not self.data[col].mode().empty else 'Unknown')
                    else:
                        self.data[col] = self.data[col].fillna(self.data[col].median() if not self.data[col].isnull().all() else 0)
        else:
            for col in missing_cols:
                if col in self.data.columns:
                    if self.data[col].dtype == 'object':
                        self.data[col] = self.data[col].fillna(self.data[col].mode()[0] if not self.data[col].mode().empty else 'Unknown')
                    else:
                        self.data[col] = self.data[col].fillna(self.data[col].median() if not self.data[col].isnull().all() else 0)
        return self.data
