
# AlphaCare Insurance Solutions (ACIS)

## Project Overview


### Business Objective
AlphaCare Insurance Solutions (ACIS) aims to enhance risk and predictive analytics in car insurance planning and marketing in South Africa. The focus of this project is to analyze historical insurance claim data to optimize marketing strategies and identify low-risk targets for premium reductions, ultimately attracting new clients.

## **Project Structure**

   ``` bash
+---.dvc
|   |   .gitignore
|   |   config           
+---.github
|   \---workflows
|           blank.yml
|           
+---.vscode
|       settings.json
|                          
         
+---notebooks
|       data_preparation.ipynb
|       eda_analysis.ipynb
|       hypothesis_testing.ipynb
|       model_training.ipynb
|       README.md
|       __init__.py
|       
+---Screenshots
|       correlation_heatmap.png
|       geographical_trends.png
|       outliers_boxplot.png
|       premium_by_cover.png
|       
+---scripts
|   |   data_processing.py
|   |   data_visualization.py
|   |   extract_zip.py
|   |   hypothesis_testing.py
|   |   model_building.py
|   |   README.md
|   |   __init__.py         
+---src
|       README.md
|       __init__.py
|       
|---tests
    |   README.md
    |   test_data_processing.py
    |   test_extract_zip.py
    |   __init__.py
    |   
|   .dvcignore
|   .gitignore
|   dvc.lock
|   dvc.yaml
|   README.md
|   requirements.txt
 
```

## Completed Tasks

## Task 1: Exploratory Data Analysis (EDA)

### Overview
EDA is essential for understanding datasets. In this analysis of a car insurance claims dataset (1,000,098 rows, 52 columns), data quality checks revealed:

- **Missing Values**: High missing data in critical columns led to their removal (e.g., NumberOfVehiclesInFleet). Columns with lower missing data were imputed.
- **Statistical Summary**: Significant skewness in key variables (e.g., SumInsured, TotalClaims) indicated few high-value entries influence averages.
- **Univariate Analysis**: Identified distributions of numerical and categorical variables, revealing insights into policy values and demographics.

### Key Insights
- **Policy Distribution**: Most policies have low insured sums, while a small subset drives metrics.
- **Outlier Detection**: Box plots identified outliers in TotalPremium and TotalClaims, suggesting further investigation.

## Task 2: A/B Hypothesis Testing

### Findings
- **Risk Differences**: Significant variations in risk across provinces (p < 0.05) and zip codes (p < 0.05); gender showed no significant risk differences (p > 0.05).

## Task 3: Statistical Modeling

### Data Preprocessing
Key steps included cleaning the dataset, handling missing values, encoding categorical features, and feature selection.

### Task 4: Model Training
Models trained: Linear Regression, Decision Tree, Random Forest, XGBoost. Random Forest and XGBoost performed best, capturing complex patterns with reasonable accuracy.

### Conclusion
Random Forest and XGBoost are recommended for deployment, providing strong predictive power and interpretability for car insurance analytics.

