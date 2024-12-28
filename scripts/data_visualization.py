from numpy import vsplit
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Set global font style and additional customization
plt.rcParams.update({
    'font.family': 'Garamond',  # Set the font to Garamond
    'font.size': 12,            # Adjust global font size
    'axes.titlesize': 16,       # Title font size
    'axes.labelsize': 14,       # Label font size
    'xtick.labelsize': 12,      # X-axis tick font size
    'ytick.labelsize': 12,      # Y-axis tick font size
})

class DataVisualizer:
    def __init__(self, data: pd.DataFrame):
        """
        Initializes the DataVisualizer class with a dataset.

        Args:
            data (pd.DataFrame): The DataFrame containing the data to visualize.
        """
        self.data = data
        sns.set(style="whitegrid", font="Garamond")  # Seaborn style with Garamond font

    def univariate_analysis(self, num_cols=None, cat_cols=None):
        """
        Performs univariate analysis by plotting histograms for numerical columns 
        and bar charts for categorical columns.

        Args:
            num_cols (list): List of numerical columns to plot histograms. If None, automatically detect numerical columns.
            cat_cols (list): List of categorical columns to plot bar charts. If None, automatically detect categorical columns.
        """
        if num_cols is None:
            num_cols = self.data.select_dtypes(include=['float64', 'int64']).columns.tolist()
        
        if cat_cols is None:
            cat_cols = self.data.select_dtypes(include=['object', 'category']).columns.tolist()

        # Histograms for Numerical Columns
        for col in num_cols:
            plt.figure(figsize=(10, 4))
            sns.histplot(
                self.data[col].dropna(), kde=True, bins=30, 
                color='#6A5ACD', edgecolor='black', alpha=0.8
            )
            plt.title(f'Distribution of {col}', fontsize=18, fontweight='bold', color='#483D8B')
            plt.xlabel(col, fontsize=14, color='#4B0082')
            plt.ylabel('Frequency', fontsize=14, color='#4B0082')
            plt.grid(axis='y', linestyle='--', alpha=0.5)
            plt.tight_layout()
            plt.show()

        # Bar Charts for Categorical Columns
        for col in cat_cols:
            plt.figure(figsize=(10, 5))
            sns.countplot(
                x=col, data=self.data, hue=col, legend=False,  # Set hue to the same column and disable legend
                order=self.data[col].value_counts().index,
                palette='coolwarm'  # Use a color palette
            )
            plt.title(f'Distribution of {col}', fontsize=18, fontweight='bold', color='#8B0000')
            plt.xlabel(col, fontsize=14, color='#8B0000')
            plt.ylabel('Count', fontsize=14, color='#8B0000')
            plt.xticks(rotation=45, ha='right')
            plt.grid(axis='y', linestyle='--', alpha=0.5)
            plt.tight_layout()
            plt.show()

    def scatter_plot(self, x_col, y_col, hue_col=None):
        """
        Creates a scatter plot to visualize the relationship between two numerical variables.
        
        Args:
            x_col (str): Name of the column for the x-axis.
            y_col (str): Name of the column for the y-axis.
            hue_col (str): Column to color the points by (optional).
        """
        plt.figure(figsize=(10, 6))
        sns.scatterplot(
            data=self.data, x=x_col, y=y_col, hue=hue_col, 
            palette='viridis', s=100, edgecolor='black'
        )
        plt.title(f'Scatter Plot of {x_col} vs {y_col}', fontsize=18, fontweight='bold', color='#228B22')
        plt.xlabel(x_col, fontsize=14, color='#006400')
        plt.ylabel(y_col, fontsize=14, color='#006400')
        plt.legend(title=hue_col, fontsize=12, title_fontsize=14)
        plt.grid(linestyle='--', alpha=0.5)
        plt.tight_layout()
        plt.show()

    def correlation_matrix(self, cols):
        """
        Displays a heatmap of the correlation matrix for the specified columns.
        
        Args:
            cols (list): List of numerical columns to include in the correlation matrix.
        """
        corr_matrix = self.data[cols].corr()
        plt.figure(figsize=(12, 8))
        sns.heatmap(
            corr_matrix, annot=True, cmap='coolwarm', fmt='.2f', 
            linewidths=0.5, cbar_kws={'shrink': 0.75}
        )
        plt.title('Correlation Matrix', fontsize=18, fontweight='bold', color='#8B4513')
        plt.tight_layout()
        plt.show()
        plt.savefig("Screenshots/correlation_heatmap.png",dpi = 300)

    def plot_violin_premium_by_cover(self, x_col, y_col):
        """
        Creates a violin plot showing the distribution of TotalPremium by CoverType.
        
        Args:
            x_col (str): Categorical column for the x-axis.
            y_col (str): Numerical column for the y-axis.
        """
        plt.figure(figsize=(12, 6))
        sns.violinplot(
            x=x_col, y=y_col, data=self.data, palette='muted', inner='quartile'
        )
        plt.title(f'Distribution of {y_col} by {x_col}', fontsize=18, fontweight='bold', color='#4682B4')
        plt.xlabel(x_col, fontsize=14, color='#1E90FF')
        plt.ylabel(y_col, fontsize=14, color='#1E90FF')
        plt.xticks(rotation=45)
        plt.grid(axis='y', linestyle='--', alpha=0.5)
        plt.tight_layout()
        # plt.show()
        plt.savefig("Screenshots/premium_by_cover.png",dpi = 500)

    def plot_geographical_trends(self, cover_types):
        fig, axs = plt.subplots(2, 2, figsize=(16, 12))
        fig.suptitle('Geographical Trends in Insurance Data', fontsize=24, fontweight='bold', color='#2E8B57')

        # Filter the data to include only the specified cover types
        filtered_data = self.data[self.data['CoverType'].isin(cover_types)]

        # 1. Cover Type Distribution by Province (bar plot)
        sns.countplot(x='Province', hue='CoverType', data=filtered_data, palette='Set3', ax=axs[0, 0])
        axs[0, 0].set_title('Common Cover Types Across Provinces', fontsize=18, fontweight='bold')
        axs[0, 0].set_xlabel('Province', fontsize=14)
        axs[0, 0].set_ylabel('Count', fontsize=14)
        axs[0, 0].tick_params(axis='x', rotation=45)
        axs[0, 0].legend(title='Cover Type', loc='upper center', bbox_to_anchor=(0.5, 0.9), ncol=2)

        # 2. Car Make Distribution by Province (bar plot)
        car_make_counts = self.data.groupby('Province')['make'].count().reset_index()
        sns.barplot(x='Province', y='make', data=car_make_counts, ax=axs[0, 1])
        axs[0, 1].set_title('Car Make Distribution by Province', fontsize=18, fontweight='bold')
        axs[0, 1].set_xlabel('Province', fontsize=14)
        axs[0, 1].set_ylabel('Count of Car Makes', fontsize=14)
        axs[0, 1].tick_params(axis='x', rotation=45)

        # 3. Total Premium by Province (box plot)
        sns.boxplot(x='Province', y='TotalPremium', data=self.data, showmeans=True, ax=axs[1, 0])
        axs[1, 0].set_title('Distribution of Total Premium by Province', fontsize=18, fontweight='bold')
        axs[1, 0].set_xlabel('Province', fontsize=14)
        axs[1, 0].set_ylabel('Total Premium', fontsize=14)
        axs[1, 0].tick_params(axis='x', rotation=45)

        # 4. Vehicle Type Distribution by Province (count plot)
        sns.countplot(x='Province', hue='VehicleType', data=self.data, palette='Set1', ax=axs[1, 1])
        axs[1, 1].set_title('Vehicle Type Distribution by Province', fontsize=18, fontweight='bold')
        axs[1, 1].set_xlabel('Province', fontsize=14)
        axs[1, 1].set_ylabel('Count of Vehicle Types', fontsize=14)
        axs[1, 1].tick_params(axis='x', rotation=45)
        axs[1, 1].legend(title='Vehicle Type', loc='upper center', bbox_to_anchor=(0.5, 0.9), ncol=2)

        # # Adjust layout to prevent overlapping and enhance aesthetics
        # plt.tight_layout(rect=[0, 0.03, 1, 0.95])  # Adjust layout with a title space
        # # plt.show()
        # plt.savefig("Screenshots/geographical_trends.png", bbox_inches = 'tight',dpi = 300)
   
        # Adjust layout to prevent overlapping
        plt.tight_layout()
        plt.savefig("Screenshots/geographical_trends.png", dpi=300)
    def plot_outliers_boxplot(self, cols):
        """
        Plots box plots to detect outliers in numerical columns.
        """
        # numerical_columns = ['TotalPremium', 'SumInsured', 'CalculatedPremiumPerTerm', 'TotalClaims']
        
        plt.figure(figsize=(12, 4))
        
        # Plotting a box plot for each numerical column
        for i, col in enumerate(cols, 1):
            plt.subplot(1, len(cols), i)
            sns.boxplot(y=self.data[col], color='lightblue')
            plt.title(f'Box Plot of {col}')
            plt.tight_layout()

        # plt.show()
        plt.savefig("Screenshots/outliers_boxplot.png",dpi = 300)
    
    
    def cap_all_outliers(self, numerical_columns):
        """
        Caps the outliers for all numerical columns in the dataframe 
        using the IQR method.
        """
        for column in numerical_columns:
            Q1 = self.data[column].quantile(0.25)
            Q3 = self.data[column].quantile(0.75)
            IQR = Q3 - Q1
            
            lower_bound = Q1 - 1.5 * IQR
            upper_bound = Q3 + 1.5 * IQR
            
            # Cap the outliers
            self.data[column] = self.data[column].apply(lambda x: lower_bound if x < lower_bound else (upper_bound if x > upper_bound else x))
        
        return self.data

    
    def plot_violin_premium_by_cover(self, x_col, y_col):
        """
        Creates a violin plot showing the distribution of TotalPremium by CoverType.
        """
        plt.figure(figsize=(10, 4))
        sns.violinplot(x=x_col, y=y_col, data=self.data, palette='muted', inner='quartile')
        plt.title('Distribution of TotalPremium by CoverType')
        plt.xticks(rotation=45)
        plt.tight_layout()
        # plt.show()
        plt.savefig("Screenshots/premium_by_cover.png")
        plt.close()

    def plot_pairplot(self, cols):
        """
        Creates a pair plot to explore the relationships between numerical features.
        """
        sns.pairplot(self.data[cols], palette='coolwarm')
        plt.title('Pair Plot of Key Numerical Features')
        plt.tight_layout()
        # plt.show()
        
    def plot_correlation_heatmap(self, cols):
        """
        Creates a correlation heatmap for key numerical columns.
        """
        plt.figure(figsize=(8, 4))
        corr_matrix = self.data[cols].corr()
        sns.heatmap(corr_matrix, annot=True, cmap='RdYlGn', linewidths=0.5)
        plt.title('Correlation Heatmap')
        plt.tight_layout()
        #plt.show()
        plt.savefig("Screenshots/correlation_heatmap.png",dpi = 300)


if __name__ == "__main__":
    os.makedirs('Screenshots', exist_ok = True)
    df = pd.read_csv ("data/processeddata/cleaned_data.csv", low_memory = False)
    visualizer = DataVisualizer(df)

    numerical_cols = df.select_dtypes(include=['float64','int64']).columns.to_list()
    visualizer.plot_correlation_heatmap(numerical_cols)
    visualizer.plot_outliers_boxplot(numerical_cols)
    visualizer.plot_violin_premium_by_cover('CoverType','TotalPremium')

    common_cover_types = df['CoverType'].value_counts().nlargest(5).index.to_list()
    visualizer.plot_geographical_trends(common_cover_types)