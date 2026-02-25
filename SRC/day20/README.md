# Mini Project 1 - Exploratory Data Analysis (EDA)

## Project Overview

This project performs a comprehensive Exploratory Data Analysis (EDA) on a customer analytics dataset. The analysis includes data cleaning, univariate analysis, bivariate analysis, correlation analysis, and data visualization to uncover meaningful patterns and insights from customer behavior data.

## Dataset Information

**Dataset Name:** customer_analytics.csv

**Total Records:** 250 customers (after data cleaning)

**Key Attributes:**
- **CustomerID:** Unique identifier for each customer
- **Age:** Customer age in years
- **Gender:** Male or Female
- **Education:** Educational qualification
- **AnnualIncome:** Annual income in dollars
- **SpendingScore:** Customer spending score (0-100)
- **YearsEmployed:** Years of employment
- **PurchaseFrequency:** Frequency of purchases
- **OnlineVisitsPerMonth:** Number of online visits per month
- **LastPurchaseAmount:** Amount of last purchase in dollars
- **ReturnedItems:** Number of returned items
- **DevicePreference:** Preferred device type

## Project Structure

```
day20/
├── README.md                           # This file
├── customer_analytics.csv              # Input dataset
├── MiniProject1_EDA.ipynb             # Jupyter notebook with interactive analysis
├── generate_eda_pdf_v2.py             # PDF report generation script
├── MiniProject1_EDA_Report.pdf        # Generated comprehensive PDF report
└── output/                            # Output visualizations directory
```

## Prerequisites

- **Python:** 3.7 or higher
- **Package Manager:** pip or conda
- **Virtual Environment:** Recommended but optional

## Installation

### Step 1: Clone or Download the Project
```bash
cd DS_AI_Internship/SRC/day20
```

### Step 2: Create a Virtual Environment (Recommended)
```bash
# Using venv
python -m venv eda_env

# Activate virtual environment
# On Windows:
eda_env\Scripts\activate

# On macOS/Linux:
source eda_env/bin/activate
```

### Step 3: Install Required Packages
```bash
pip install pandas matplotlib seaborn numpy scipy fpdf2 jupyter
```

Or install from requirements:
```bash
pip install -r requirements.txt
```

### Step 4: Verify Installation
```bash
python -c "import pandas, matplotlib, seaborn, numpy; print('All packages installed successfully!')"
```

## How to Run the Project

### Option 1: Run Interactive Jupyter Notebook
```bash
jupyter notebook MiniProject1_EDA.ipynb
```
- Open the notebook in your browser
- Run cells in order from top to bottom
- Visualizations will display inline

### Option 2: Generate PDF Report
```bash
python generate_eda_pdf_v2.py
```
- Generates a comprehensive PDF report with all analyses and visualizations
- Output: `MiniProject1_EDA_Report.pdf`

### Option 3: Run Analysis in Python Script
```bash
python -c "
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load and explore data
df = pd.read_csv('customer_analytics.csv')
print(df.head())
print(df.info())
print(df.describe())
"
```

## Analysis Sections

### 1. **Data Loading & Exploration**
- Load customer analytics dataset
- Display first few rows
- Check data types and shape

### 2. **Data Cleaning**
- Handle missing values in Education and AnnualIncome columns
- Remove duplicate records
- Verify data quality

### 3. **Univariate Analysis**
- **Age Distribution:** Histogram with KDE showing age patterns
- **Gender Distribution:** Bar chart showing gender balance
- **Spending Score:** Histogram of customer spending patterns

### 4. **Bivariate Analysis**
- **Income vs Spending Score:** Scatter plot showing relationship
- **Purchase Amount by Gender:** Box plot comparing across genders

### 5. **Correlation Analysis**
- Heatmap of all numerical variables
- Correlation matrix identification
- Strong relationships highlighted

### 6. **Executive Summary**
- Key dataset characteristics
- Customer profile insights
- Data quality assessment

### 7. **How to Run the Project**
- Installation instructions
- Execution methods
- Troubleshooting guide

## Generated Outputs

### Visualizations Created:
1. **Age Distribution** - Histogram with KDE curve
2. **Gender Distribution** - Bar chart
3. **Spending Score Distribution** - Histogram
4. **Income vs Spending Score** - Scatter plot
5. **Purchase Amount by Gender** - Box plot
6. **Correlation Heatmap** - Full correlation matrix

### Report Output:
- **MiniProject1_EDA_Report.pdf** - Comprehensive analysis report with all visualizations and insights

## Key Findings

### Customer Demographics:
- Age range: 20-55 years, concentrated in 25-45 range
- Gender distribution: Nearly balanced (52% Male, 48% Female)
- Most customers in their prime working years

### Spending Patterns:
- Spending not strongly correlated with income
- Mid-income customers ($50k-$150k) are highest spenders
- Complex, multifactorial spending behavior

### Data Quality:
- Successfully handled missing values
- Removed duplicates for accuracy
- Data ready for advanced modeling

### Notable Correlations:
- Age & Years Employed: 0.98 (Very strong)
- Income & Spending Score: -0.38 (Weak negative)

## Usage Examples

### Load and Explore Data
```python
import pandas as pd
df = pd.read_csv('customer_analytics.csv')
print(df.describe())
```

### Generate Visualization
```python
import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(10, 6))
sns.scatterplot(x='AnnualIncome', y='SpendingScore', data=df)
plt.title('Income vs Spending Score')
plt.show()
```

### Create Correlation Heatmap
```python
import seaborn as sns
corr_matrix = df.corr(numeric_only=True)
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.show()
```

## Troubleshooting

### Issue: Module not found error
**Solution:** Ensure all packages are installed
```bash
pip install --upgrade pandas matplotlib seaborn numpy scipy fpdf2 jupyter
```

### Issue: CSV file not found
**Solution:** Verify customer_analytics.csv is in the same directory as scripts

### Issue: Jupyter notebook won't start
**Solution:** Install and launch Jupyter
```bash
pip install jupyter
jupyter notebook
```

### Issue: Plots not displaying in notebook
**Solution:** Add magic command at beginning of notebook
```python
%matplotlib inline
```

## Next Steps & Future Enhancements

1. **Customer Segmentation:** Perform K-means clustering to identify customer groups
2. **RFM Analysis:** Analyze Recency, Frequency, and Monetary values
3. **Predictive Modeling:** Build models to predict customer spending
4. **Seasonal Analysis:** Identify temporal patterns in purchase behavior
5. **Advanced Visualizations:** Create interactive dashboards with Plotly
6. **Statistical Testing:** Conduct hypothesis testing on customer segments

## Libraries Used

| Library | Version | Purpose |
|---------|---------|---------|
| pandas | Latest | Data manipulation and analysis |
| matplotlib | Latest | Static data visualization |
| seaborn | Latest | Statistical visualization |
| numpy | Latest | Numerical computing |
| scipy | Latest | Scientific computing |
| fpdf2 | Latest | PDF report generation |
| jupyter | Latest | Interactive notebooks |

## Dataset Statistics

| Metric | Value |
|--------|-------|
| Total Customers | 250 |
| Total Features | 11 |
| Age Range | 20 - 55 years |
| Income Range | $30,000 - $550,000 |
| Spending Score Range | 10 - 90 |
| Missing Values | Handled |
| Duplicates | Removed |

## License

This project is created as part of the DS & AI Internship Program.

## Author

Created for Mini Project 1 - Exploratory Data Analysis

## Contact & Support

For issues or questions regarding this project:
1. Review the troubleshooting section
2. Check the generated PDF report for detailed analysis
3. Refer to library documentation links below

## Useful Resources

- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Matplotlib Tutorial](https://matplotlib.org/stable/tutorials/index.html)
- [Seaborn Gallery](https://seaborn.pydata.org/examples.html)
- [NumPy Reference](https://numpy.org/doc/stable/reference/)
- [Jupyter Documentation](https://jupyter.org/documentation)

## Changelog

### Version 1.0 (February 2026)
- Initial project setup
- Complete EDA anallysis
- PDF report generation
- Jupyter notebook creation
- README documentation

## Notes

- All analysis is based on the customer_analytics.csv dataset
- Missing values were handled using mode (Education) and median (AnnualIncome)
- Duplicate records were removed for data integrity
- All visualizations are saved with 300 DPI for publication quality
- PDF report includes comprehensive insights and visualizations

---

**Last Updated:** February 2026

**Status:** Complete ✓
