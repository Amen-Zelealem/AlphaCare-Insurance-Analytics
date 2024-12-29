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

    def _chi_squared_test(self, feature, metric):
        """
        Perform chi-squared test for categorical data.
        """
        contingency_table = pd.crosstab(self.data[feature], self.data[metric])
        chi2, p_value, _, _ = stats.chi2_contingency(contingency_table)
        return chi2, p_value

    def _t_test(self, group_a, group_b, metric):
        """
        Perform a t-test between two groups on a given metric.
        """
        if self._check_identical_values(metric):
            print(f"Warning: All values for {metric} are identical. Skipping t-test.")
            return None, None

        t_stat, p_value = stats.ttest_ind(group_a[metric].dropna(), group_b[metric].dropna(), nan_policy='omit')
        return t_stat, p_value

    def _z_test(self, group_a, group_b, metric):
        """
        Perform a z-test between two groups if sample size is large (>30).
        """
        mean_a, mean_b = group_a[metric].mean(), group_b[metric].mean()
        std_a, std_b = group_a[metric].std(), group_b[metric].std()
        n_a, n_b = group_a[metric].count(), group_b[metric].count()

        z_stat = (mean_a - mean_b) / np.sqrt((std_a**2 / n_a) + (std_b**2 / n_b))
        p_value = 2 * (1 - stats.norm.cdf(abs(z_stat)))
        return z_stat, p_value

    def _interpret_p_value(self, p_value, alpha=0.05):
        """
        Interpret the null hypothesis based on the p-value.
        """
        if p_value is None:
            return "Test skipped due to identical values."
        return "Reject the null hypothesis." if p_value < alpha else "Fail to reject the null hypothesis."

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