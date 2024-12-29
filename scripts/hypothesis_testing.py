import pandas as pd
import numpy as np
from scipy import stats

class ABHypothesisTesting:
    def __init__(self, data):
        """
        Initialize the class with the dataset.
        """
        self.data = data

        """
        Run all hypothesis tests and return the results.
        """
        results = {
            'Risk Differences Across Provinces': self._risk_across_provinces(),
            'Risk Differences Between Postal Codes': self._risk_between_postalcodes(),
            'Margin Differences Between Postal Codes': self._margin_between_postalcodes(),
            'Risk Differences Between Women and Men': self._risk_between_genders(),
        }
        return results