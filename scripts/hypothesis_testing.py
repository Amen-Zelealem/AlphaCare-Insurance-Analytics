import pandas as pd
import numpy as np
from scipy import stats

class ABHypothesisTesting:
    def __init__(self, data):
        """
        Initialize the class with the dataset.
        """
        self.data = data

    def _segment_data(self, feature, value=None, exclude_values=None):
        """
        Segment the data based on a feature. Optionally filter by value or exclude certain values.
        """
        if exclude_values is not None:
            data_segment = self.data[~self.data[feature].isin(exclude_values)]
        else:
            data_segment = self.data.copy()

        if value is not None:
            data_segment = data_segment[data_segment[feature] == value]
        
        return data_segment

    def _check_identical_values(self, metric):
        """
        Check if all values for a metric are identical.
        """
        unique_values = self.data[metric].dropna().unique()
        return len(unique_values) == 1
