# Singapore Salary Insights Dashboard

A comprehensive data analysis project analyzing 1M+ job postings from Singapore to uncover salary trends, employment patterns, and career growth insights.

![Dashboard Preview](https://img.shields.io/badge/Status-Complete-success?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge&logo=python)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange?style=for-the-badge&logo=jupyter)

---

## 📊 Project Overview

This project performs end-to-end data analysis on Singapore job market data, from raw CSV data to interactive visualizations and a professional HTML dashboard. The analysis provides actionable insights for HR professionals, job seekers, consultants, and policymakers.

### Key Features

- **1M+ job postings** analyzed from Singapore job market
- **53K+ companies** tracked across multiple industries
- **8 interactive visualizations** covering salary distributions, employment types, career progression, and more
- **Standalone HTML dashboard** for easy sharing and presentation
- **Business insights** tailored for different stakeholders

---

## 🗂️ Project Structure

```
Module1-Assignment/
│
├── SGJobData.csv                      # Raw job posting data (~300MB)
├── SGJobData_cleaned.csv              # Cleaned dataset (1,044,583 rows)
├── salary_insights_dashboard.ipynb    # Jupyter notebook with analysis
├── salary_insights_dashboard.html     # Final HTML dashboard (1MB)
├── chart4_fix.txt                     # Reference code for Chart 4 fix
└── README.md                          # This file
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.12 or higher
- Virtual environment (recommended)
- 2GB+ RAM for processing large dataset

### Installation

1. **Clone or navigate to the project directory:**
   ```bash
   cd /path/to/Module1-Assignment
   ```

2. **Create and activate virtual environment:**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install required packages:**
   ```bash
   pip install pandas numpy matplotlib seaborn plotly jupyter
   ```

4. **Verify installation:**
   ```bash
   python -c "import pandas, numpy, matplotlib, seaborn, plotly; print('All packages installed successfully!')"
   ```

---

## 📈 Workflow

### Step 1: Raw Data Collection

**File:** `SGJobData.csv`

- **Source:** Singapore job posting data
- **Size:** ~300MB
- **Records:** 1,044,583+ job postings
- **Columns:** 21 fields including salary ranges, company info, job requirements

**Key Columns:**
- `salary_minimum`, `salary_maximum` - Salary range
- `postedCompany_name` - Company name
- `title` - Job title
- `minimumYearsExperience` - Required experience
- `employmentTypes` - Employment type (Permanent, Contract, etc.)
- `positionLevels` - Position level (Entry, Mid, Senior, etc.)
- `categories` - Industry categories (JSON format)

### Step 2: Data Cleaning

**Process:**
1. **Load raw data** into pandas DataFrame
2. **Calculate average salary** from min/max ranges
3. **Remove invalid records:**
   - Null values in critical columns
   - Salary outliers (>SGD 500,000)
   - Invalid min>max salary relationships
4. **Add derived columns:**
   - `average_salary = (salary_minimum + salary_maximum) / 2`
   - `salary_spread = salary_maximum - salary_minimum`
5. **Parse JSON categories** to extract primary industry
6. **Save cleaned data** to `SGJobData_cleaned.csv`

**Output:** `SGJobData_cleaned.csv` (284MB, 1,044,583 rows)

### Step 3: Exploratory Data Analysis (Jupyter Notebook)

**File:** `salary_insights_dashboard.ipynb`

The Jupyter notebook contains 18 cells organized into sections:

#### 📚 Import Libraries
- pandas, numpy for data manipulation
- matplotlib, seaborn for static visualizations
- plotly for interactive charts

#### 🔍 Load and Explore Data
- Load cleaned CSV
- Display dataset info, summary statistics
- Check for missing values

#### 📊 Create 8 Visualizations

1. **Chart 1: Salary Distribution**
   - Histogram of average salaries (50k sample)
   - Median and mean lines
   - Insights: Right-skewed distribution, median SGD 3,800

2. **Chart 2: Salary by Employment Type**
   - Box plots for 8 employment types
   - Comparison of salary ranges
   - Insights: Contract roles have 4.3% premium over permanent

3. **Chart 3: Salary by Position Level**
   - Bar chart + line overlay for mean/median
   - 9 position levels analyzed
   - Insights: Senior Management earns 4.0x entry level

4. **Chart 4: Salary Growth by Experience**
   - Line chart showing progression 0-12 years
   - Fixed pandas aggregation column naming issue
   - Insights: 63% salary growth in first 3 years

5. **Chart 5: Top 15 Hiring Companies**
   - Horizontal bar chart with salary color coding
   - Company posting volume + average salary
   - Insights: Top companies offer competitive salaries

6. **Chart 6: Salary Percentiles**
   - Bar chart for 10th, 25th, 50th, 75th, 90th percentiles
   - Benchmarking reference points
   - Insights: Wide salary distribution across market

7. **Chart 7: Top Industries by Salary**
   - Bar chart comparing 10 industries
   - Average salary by category
   - Insights: Industry salary variations significant

8. **Chart 8: Employment Type Distribution**
   - Pie chart with percentages
   - Clean legend-based design (no label overlap)
   - Insights: 43.9% Permanent, 37.7% Full Time, 13.3% Contract

#### 💡 Business Insights Generation
- HR Department strategies
- Job seeker career planning
- Consultancy market analysis
- Government policy recommendations

### Step 4: HTML Dashboard Generation

**File:** `salary_insights_dashboard.html` (1.07MB)

The final HTML dashboard is a **standalone, browser-ready** file with:

#### Features:
- **8 summary metric cards:**
  - Total Jobs, Companies, Median/Mean Salary
  - Entry/Senior Level salary, Growth Factor, Unique Roles

- **8 embedded PNG charts** (matplotlib-generated, base64-encoded)
  - All charts are static images for maximum compatibility
  - No external dependencies required

- **4 business insight sections:**
  - For HR Departments
  - For Job Seekers
  - For Consultancy
  - For Government

- **Professional styling:**
  - Gradient header background
  - Responsive grid layout
  - Hover effects on cards
  - Mobile-friendly design

#### Technical Details:
- All charts embedded as base64 PNG images
- Self-contained HTML (no external CSS/JS files)
- Works in any modern browser
- Optimized file size (1MB) for easy sharing

---

## 🔧 Technical Challenges & Solutions

### Challenge 1: Chart 4 Column Naming Error

**Problem:** Pandas `.agg(['mean', 'count'])` creates columns named `'mean'` and `'count'`, not the original column name.

**Solution:**
```python
exp_stats = df_exp.groupby('minimumYearsExperience')['average_salary'].agg(['mean', 'count']).reset_index()
exp_stats.columns = ['years_exp', 'avg_salary', 'job_count']  # Explicit renaming
```

### Challenge 2: Plotly Chart Export Issues

**Problem:** Kaleido (Plotly image export) requires Chrome/Chromium system dependencies.

**Solution:** Switched to matplotlib/seaborn for generating static PNG images, which don't require browser dependencies.

### Challenge 3: Pie Chart Label Overlap

**Problem:** Employment type labels overlapped in pie chart, making it unreadable.

**Solution:** 
- Removed all category labels from pie slices
- Kept only percentages on slices
- Added comprehensive legend with name, count, and percentage
- Result: Clean, professional appearance

### Challenge 4: Large Dataset Performance

**Problem:** 1M+ rows cause memory issues and slow processing.

**Solution:**
- Sampling for histogram (50k rows)
- Sampling for box plots (2k per category)
- Efficient pandas operations with observed=True
- Chunked data processing where needed

---

## 📊 Key Findings

### Salary Insights
- **Median Salary:** SGD 3,800/month
- **Mean Salary:** SGD 4,712/month (right-skewed distribution)
- **Entry Level:** SGD 2,970/month (0 years experience)
- **Senior Level:** SGD 10,979/month (10+ years experience)
- **Growth Factor:** 3.7x from entry to senior level

### Employment Patterns
- **43.9%** Permanent positions
- **37.7%** Full-time roles
- **13.3%** Contract positions
- **Contract Premium:** 4.3% higher salary than permanent

### Career Growth
- **0-3 years:** +63% salary growth (fastest growth period)
- **3-5 years:** +31% growth (critical retention point)
- **5-10 years:** Steady progression to senior roles
- **10+ years:** 3.7x entry-level compensation

---

## 🎯 Use Cases

### For HR Professionals
- **Salary benchmarking** against market rates
- **Compensation strategy** development
- **Talent retention** insights (3-5 year critical period)
- **Market positioning** using percentile data

### For Job Seekers
- **Realistic salary expectations** by experience level
- **Career progression** timeline planning
- **Industry comparison** for career switches
- **Negotiation leverage** with market data

### For Consultants
- **Market analysis** with 1M+ data points
- **Client advisory** on compensation strategies
- **Industry trends** identification
- **Competitive intelligence** gathering

### For Policymakers
- **Labor market** understanding
- **Skills development** priority setting
- **Employment policy** impact assessment
- **Economic indicators** tracking

---

## 🛠️ Technologies Used

| Technology | Purpose | Version |
|------------|---------|---------|
| Python | Core programming | 3.12.3 |
| Pandas | Data manipulation | 3.0.0 |
| NumPy | Numerical computing | 2.4.2 |
| Matplotlib | Static visualizations | 3.10.8 |
| Seaborn | Statistical plots | 0.13.2 |
| Plotly | Interactive charts (notebook) | 6.5.2 |
| Jupyter | Interactive analysis | Latest |
| HTML5/CSS3 | Dashboard presentation | - |

---

## 📝 Usage Instructions

### Running the Jupyter Notebook

1. **Start Jupyter:**
   ```bash
   jupyter notebook
   ```

2. **Open the notebook:**
   - Navigate to `salary_insights_dashboard.ipynb`
   - Run cells sequentially (Cell → Run All)

3. **View interactive charts:**
   - Plotly charts are interactive in the notebook
   - Hover for tooltips, zoom, pan, etc.

### Viewing the HTML Dashboard

1. **Open in browser:**
   ```bash
   # Option 1: Direct open
   open salary_insights_dashboard.html  # macOS
   xdg-open salary_insights_dashboard.html  # Linux
   start salary_insights_dashboard.html  # Windows
   
   # Option 2: Local server
   python -m http.server 8000
   # Then open: http://localhost:8000/salary_insights_dashboard.html
   ```

2. **Share the dashboard:**
   - Email the HTML file directly
   - Upload to web hosting
   - Share via cloud storage
   - No Python/Jupyter required to view!

### Regenerating the Dashboard

If you modify the data or analysis:

```bash
# Option 1: Run the generation script from notebook
jupyter nbconvert --execute salary_insights_dashboard.ipynb

# Option 2: Use the Python script directly
python << 'EOF'
# [Paste the HTML generation script from the notebook]
EOF
```

---

## 📄 License

This project is for educational purposes as part of the NTU DSAI Module 1 Assignment.

---

## 👤 Author

**Fred C (Group 2)**  
NTU Data Science and Artificial Intelligence Programme (DS2F) 
Module 1 Assignment - February 2026

---

## 🙏 Acknowledgments

- Singapore job market data providers
- NTU DSAI Programme instructors
- Python data science community
- Open-source library maintainers

---

## 📞 Contact & Support

For questions or issues:
- Review the Jupyter notebook for detailed code comments
- Check technical challenges section for common issues
- Verify all prerequisites are installed correctly

---

## 🔄 Version History

- **v1.0** (Feb 2026) - Initial release
  - Complete data pipeline from raw CSV to HTML dashboard
  - 8 comprehensive visualizations
  - Business insights for 4 stakeholder groups
  - Standalone HTML dashboard (1MB)
  - Full documentation

---

**Last Updated:** February 4, 2026  
**Status:** ✅ Complete and Production-Ready
