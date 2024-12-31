
# Interim Report for AlphaCare Insurance Solutions (ACIS)

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

1. **GitHub Repository Setup**
   - Created a repository and established a branch named `task-1`.
   - Committed work consistently with descriptive messages.

2. **Exploratory Data Analysis (EDA)**
   - **Data Summarization**: Conducted descriptive statistics and reviewed data structure.
   - **Data Quality Assessment**: Identified and handled missing values through dropping, imputation, and standard practices.
   - **Univariate Analysis**: Analyzed distributions of numerical and categorical variables.
   - **Bivariate Analysis**: Explored relationships between total premiums and claims using scatter plots and correlation matrices.
   - **Data Comparison**: Examined trends over geography in insurance cover types and premiums.
   - **Outlier Detection**: Utilized box plots to identify outliers.

3. **Visualizations**
   - Created insightful visualizations to capture key findings from the EDA.

## Insights from Analysis

### Data Quality Management
- **Dropped Columns**: Removed columns with high missing data to enhance dataset integrity.
- **Imputation**: Employed mode and median imputation for moderate and low missing data, respectively.

### Dataset Overview
- **Total Records**: Approximately 1,000,098 entries.
- **Key Features**: Significant variability in premiums, claims, and insured sums, indicating complex risk profiles.

### Univariate and Bivariate Insights
- **Numerical Variables**: Right-skewed distributions for sums insured and premiums, indicating diverse policy values.
- **Correlation Analysis**: Weak correlation (0.12) between total premiums and claims suggests other influencing factors are at play.

### Cover Type Preferences
- **Dominant Choices**: Common selections like "Own Damage" and "Passenger Liability" highlight key customer needs.
- **Marketing Opportunities**: Potential to bundle less popular cover types with core offerings to enhance customer engagement.

### Outlier Detection
- **Box Plot Analysis**: Identified significant outliers in total premiums and claims, suggesting high variance and potential data quality issues.

## Recommendations
- **Targeted Marketing**: Focus on popular cover types and consider bundling less common options to increase uptake.
- **Risk Assessment Refinement**: Incorporate additional variables such as demographic data to enhance modeling and improve pricing strategies.
- **Outlier Management**: Implement capping strategies for outliers to maintain data integrity while minimizing distortion.

## Next Steps
- Conduct further analysis on identified outliers and explore their characteristics.
- Investigate regional variations in cover type preferences and premium levels.
- Enhance predictive models by incorporating additional influencing factors.

