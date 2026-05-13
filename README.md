# Singapore Salary Insights Dashboard

A comprehensive data analysis project analyzing 1M+ job postings from Singapore to uncover salary trends, employment patterns, and career growth insights.

![Dashboard Preview](https://img.shields.io/badge/Status-Complete-success?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.13-blue?style=for-the-badge&logo=python)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange?style=for-the-badge&logo=jupyter)
![Streamlit](https://img.shields.io/badge/Streamlit-Interactive-red?style=for-the-badge&logo=streamlit)

## 🔗 Live Demo

**🌐 Interactive Streamlit App:** [https://module1assignment.streamlit.app/](https://module1assignment.streamlit.app/)


## 🎯 Two Ways to Experience the Dashboard

This project delivers insights through two complementary formats:

### 📓 Jupyter Notebook
**File:** `salary_insights_dashboard.ipynb`  
**Best for:** Development, exploration, learning  
**Features:** Interactive code cells, inline visualizations, detailed analysis  
**Requires:** Python + Jupyter

### 🌐 Streamlit Web App
**Live:** [https://module1assignment.streamlit.app/](https://module1assignment.streamlit.app/)  
**Best for:** Live demos, interactive analysis, client presentations  
**Features:** Real-time filtering, 8 interactive Plotly visualizations, sidebar filters

---

## 📑 Table of Contents

- [Quick Start](#-quick-start)
- [Project Overview](#-project-overview)
- [Project Structure](#️-project-structure)
- [Getting Started](#-getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Workflow](#-workflow)
  - [Step 1: Raw Data Collection](#step-1-raw-data-collection)
  - [Step 2: Data Cleaning](#step-2-data-cleaning)
  - [Step 3: Exploratory Analysis (Jupyter)](#step-3-exploratory-data-analysis-jupyter-notebook)
  - [Step 4: Streamlit Dashboard](#step-4-streamlit-interactive-dashboard)
- [Development Journey](#-development-journey)
- [Technical Challenges & Solutions](#-technical-challenges--solutions)
- [Key Findings](#-key-findings)
- [Use Cases](#-use-cases)
- [Technologies Used](#️-technologies-used)
- [Usage Instructions](#-usage-instructions)
- [Project Team](#-project-team)
- [AI-Assisted Development](#-ai-assisted-development)

---

## 🚀 Quick Start

**Choose your preferred way to explore the dashboard:**

| I want to... | Use this | Command |
|--------------|----------|---------|
| 🔍 Explore data interactively | Jupyter Notebook | `jupyter notebook salary_insights_dashboard.ipynb` |
| 🎛️ Filter data in real-time | Streamlit App | Visit [live demo](https://module1assignment.streamlit.app/) |

**First time setup:** See [Installation](#installation) section below.

---

## 📊 Project Overview

This project performs end-to-end data analysis on Singapore job market data, from raw CSV data to interactive visualizations and a full **Streamlit web application**. The analysis provides actionable insights for HR professionals, job seekers, consultants, and policymakers.

### Key Features

- **1M+ job postings** analyzed from Singapore job market
- **53K+ companies** tracked across multiple industries
- **8 interactive visualizations** covering salary distributions, employment types, career progression, and more
- **Multiple delivery formats:**
  - Jupyter Notebook for exploratory analysis
  - **Streamlit web app** with real-time interactive filtering
- **Business insights** tailored for different stakeholders
- **Interactive deployment** optimized for Streamlit Community Cloud

---

## 🗂️ Project Structure

```
Module1-Assignment/
│
├── SGJobData.csv                      # Raw job posting data (~300MB) *
├── SGJobData_cleaned.csv              # Cleaned dataset (272MB, 1,044,583 rows) *
├── SGJobData_cleaned.parquet          # Compressed dataset (49MB, for deployment)
├── convert_to_parquet.py              # CSV to Parquet conversion utility
├── streamlit_dashboard.py             # Streamlit interactive web application
├── salary_insights_dashboard.ipynb    # Jupyter notebook with analysis
├── requirements.txt                   # Streamlit deployment dependencies
├── requirements-dev.txt               # Full dev environment (includes Jupyter)
├── SALARY_INSIGHTS_ANALYSIS.md        # Business insights report
├── VSCode-Copilot-Journey.md          # Development journey documentation
└── README.md                          # This file

* Excluded from git (exceeds 100MB GitHub limit)
```

### 📦 Data Format Strategy

**Challenge:** The cleaned dataset (272MB CSV) exceeds GitHub's 100MB file size limit.

**Solution:** Parquet compression format (for potential cloud deployments)
- ✅ **82% size reduction**: 272MB → 49MB
- ✅ **Faster loading**: Columnar storage optimized for analytics
- ✅ **GitHub compatible**: Well under 100MB limit
- ✅ **Cloud-ready**: Native pandas support with `pyarrow`

**For Development:**
```bash
# Convert CSV to Parquet (one-time setup)
conda activate assignment1
python3 convert_to_parquet.py
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
   
   **For full development environment (includes Jupyter):**
   ```bash
   pip install -r requirements-dev.txt
   ```
   
   **Or install core packages manually:**
   ```bash
   pip install pandas numpy matplotlib seaborn plotly jupyter
   ```

4. **Verify installation:**
   ```bash
   python -c "import pandas, numpy, matplotlib, plotly; print('✓ All required packages installed!')"
   ```

> **Note on Conda Environment:** The file `environment.yml.backup` is available for local conda environments.

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
4. **Remove salary outliers (post-clean filter applied in notebook):**
   - `salary_minimum < 1,200` — blanket floor aligned to Singapore's Progressive Wage Model / Local Qualifying Salary (LQS rising to S$1,800 from Jul 2026); removes placeholders, part-time noise, and sub-subsistence entries
   - `salary_maximum > 30,000` — annual salaries mistakenly entered in monthly fields (99th percentile of salary_max is SGD 20,000)
   - Removed 27,005 rows (2.59%); 1,017,578 rows retained
   - Decision: **Drop** (not impute) — values carry no recoverable information
5. **Add derived columns:**
   - `average_salary = (salary_minimum + salary_maximum) / 2`
   - `salary_spread = salary_maximum - salary_minimum`
5. **Parse JSON categories** to extract primary industry
6. **Save cleaned data** to `SGJobData_cleaned.csv`
7. **Convert to Parquet format** for deployment (`convert_to_parquet.py`)

**Output:** 
- `SGJobData_cleaned.csv` (272MB, 1,044,583 rows) - Local development
- `SGJobData_cleaned.parquet` (49MB, 82% compression) - Git & deployment

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

### Step 4: Streamlit Interactive Dashboard

**File:** `streamlit_dashboard.py`  
**Live:** [https://module1assignment.streamlit.app/](https://module1assignment.streamlit.app/)

Full-featured interactive web application deployed directly from this repository.

#### Features:
- **8 interactive Plotly visualizations** matching the notebook analysis
- **Real-time sidebar filters:** employment type, position level, salary range, years of experience
- **Key metrics row** with live-recalculated totals, median, mean, and std dev
- **Responsive design** working on desktop and mobile browsers

#### Technical Details:
- **Framework:** Streamlit 1.57+
- **Deployment:** Streamlit Community Cloud (deploys from `main` branch)
- **Data:** `SGJobData_cleaned.parquet` — columnar-read (9 columns only) + dtype optimization keeps RAM at ~312 MB
- **Access:** Public web app (no installation required)

---

## � Development Journey

This project was developed with extensive use of **GitHub Copilot in VS Code**, demonstrating effective AI-assisted development practices. For a complete walkthrough of the development process, see [VSCode-Copilot-Journey.md](VSCode-Copilot-Journey.md).

### Project Timeline

**Duration:** February 4 – May 13, 2026

#### Phase 1: Data Analysis & Cleaning (Feb, Day 1-2)
- Analyzed raw dataset (1,048,585 rows)
- Implemented 6-step cleaning process
- Generated business insights report
- Output: Clean dataset ready for visualization

#### Phase 2: Jupyter Dashboard Creation (Feb, Day 2-3)
- Created interactive notebook with 18 cells
- Developed 8 comprehensive visualizations
- Fixed pandas aggregation column naming issue (Chart 4)
- Documented code for reproducibility

#### Phase 3: Streamlit Development (Feb, Day 6-7)
- Created Streamlit dashboard (`streamlit_dashboard.py`) in this repository
- Implemented 8 interactive Plotly charts with real-time sidebar filters
- Deployed to Streamlit Community Cloud

#### Phase 4: OOM Diagnosis & Fix (May 13, 2026)
- Diagnosed silent OOM crash — full parquet load consumed 931 MB RAM
- Fixed with columnar read (9 columns), category dtypes, float32 downcasting
- Memory reduced 931 MB → 312 MB (67%); app now stable on Community Cloud
- Consolidated to this repository; cleaned scratch files and HTML artifacts

### Key Learnings

#### Technical Insights
1. **Pandas Aggregation Pattern:** `.agg(['mean', 'count'])` creates columns named `'mean'`, `'count'`, not the original column name. Always explicitly rename columns after aggregation.

2. **Visualization Library Trade-offs:**
   - **Plotly:** Great for interactive notebooks, but large file sizes and serialization issues for HTML export
   - **Matplotlib:** More reliable for static exports, better browser compatibility
   - **Streamlit:** Best for interactive web apps with real-time filtering

3. **Image Embedding Strategy:** Base64-encoded PNG images create truly standalone HTML files with no external dependencies.

4. **Large Dataset Handling:**
   - Sample data for visualizations (50k rows for histograms)
   - Use `observed=True` in groupby operations
   - Cache expensive computations

5. **Pie Chart Best Practices:**
   - Remove overlapping labels
   - Use comprehensive legends instead
   - Keep percentages on slices for quick reference

#### Effective AI Collaboration
1. **Iterative Problem Solving:** Don't expect perfect solutions on first try - provide feedback and iterate
2. **Specific Prompts Work Better:** "Fix Chart 4's KeyError" > "Fix my chart"
3. **Provide Fallback Options:** "Try X, if that doesn't work, do Y"
4. **Test Incrementally:** Validate each stage before moving forward
5. **Document the Journey:** Capturing failed attempts teaches as much as successful solutions

---

## �🔧 Technical Challenges & Solutions

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

### Challenge 4: Streamlit Community Cloud OOM Crash

**Problem:** Loading all 21 parquet columns consumed 931 MB RAM, silently exceeding Streamlit Community Cloud's ~1 GB free-tier limit. The app started successfully but was OOM-killed at runtime, showing only "Error running app" with no traceback.

**Root cause identified from deployment logs:** Clean startup → runtime crash → no Python exception visible → OOM kill.

**Solution applied to `streamlit_dashboard.py`:**
- `pd.read_parquet(columns=needed_cols)` — load only 9 of 21 columns (−476 MB)
- Cast high-cardinality string columns to `category` dtype (−140 MB)
- Downcast salary float64 → float32 (−12 MB)
- Remove unused `year_month` Period column computation
- **Result: 931 MB → 312 MB (67% reduction)** — stable on Community Cloud

### Challenge 5: Large Dataset Performance

**Problem:** 1M+ rows cause memory issues and slow processing.

**Solution:**
- Sampling for histogram (50k rows)
- Sampling for box plots (2k per category)
- Efficient pandas operations with observed=True
- Chunked data processing where needed

### Challenge 6: Unrealistic Salary Values in Cleaned Dataset

**Problem:** Dashboard showed `salary_minimum = $1` and implausibly large `salary_maximum` values (e.g. $400,000/month), distorting all salary charts and statistics.

**Investigation findings:**
- `salary_minimum == 1`: 2,534 rows — sentinel placeholder left when job posters skipped the field
- `salary_minimum < 100`: 7,420 rows total — systematic scraper/data-entry artifact
- `salary_maximum > 30,000`: 1,375 rows — annual salaries entered in monthly fields (e.g. SGD 267,820 annual ≠ monthly)
- 99th percentile of `salary_maximum` is SGD 20,000; 99.9th is SGD 35,000
- $100–$1,200 band: 18,224 rows — mix of part-time, internship, and suspicious permanent/full-time records

**Decision: Drop with $1,200 blanket floor (not impute)**
- Rationale: Singapore's Progressive Wage Model (PWM) and Local Qualifying Salary (LQS, rising to S$1,800/month from Jul 2026) mean sub-$1,200 full-time salaries are economically implausible for formal employment
- Part-time and internship data below this threshold (1.76% of data) is also dropped — acceptable given dataset size and the distortion these low values cause on salary analysis
- High-end values cannot be reliably converted (annual÷12 would be a guess)
- Impact: 27,005 rows removed (2.59%) from 1,044,583

**Solution applied in `salary_insights_dashboard.ipynb` (Section 2 — Load and Prepare Data):**
```python
df = df[
    (df['salary_minimum'] >= 1200) &
    (df['salary_maximum'] <= 30_000)
].copy()
```

**Result:** 1,017,578 clean rows with salary range SGD 1,200–30,000/month, eliminating chart distortion.

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
| Python | Core programming | 3.13 |
| Pandas | Data manipulation | 3.0.0 |
| NumPy | Numerical computing | 2.4.2 |
| Matplotlib | Static visualizations | 3.10.8 |
| Seaborn | Statistical plots | 0.13.2 |
| Plotly | Interactive charts | 6.5.2 |
| Streamlit | Web application framework | 1.40.2 |
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

### Accessing the Streamlit Dashboard

**Live:** [https://module1assignment.streamlit.app/](https://module1assignment.streamlit.app/)

1. **Access the live app:**
   - Visit the link above — no installation required
   - Works on any device with a web browser

2. **Explore interactive features:**
   - Use sidebar filters (employment type, position level, salary range, experience)
   - Hover over charts for detailed tooltips
   - All 8 visualizations update in real-time based on your selections

3. **Run locally:**
   ```bash
   streamlit run streamlit_dashboard.py
   ```

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

### Choosing the Right Format

| Format | Best For | Pros | Cons |
|--------|----------|------|------|
| **Jupyter Notebook** | Data exploration, development | Interactive code, detailed analysis, reproducible | Requires Python/Jupyter |
| **Streamlit App** | Demos, interactive analysis | No installation, web-based, real-time filtering | Requires internet for live app |

**Recommendation:**
- **Development/Analysis:** Use Jupyter Notebook
- **Interactive Demo:** Use [Streamlit Dashboard](https://module1assignment.streamlit.app/) (web-based, no setup)

---

## 📄 License

This project is for educational purposes as part of the NTU DSAI Module 1 Assignment.

---

## 👥 Project Team

**Group 2 - Module 1 Assignment**  
NTU Data Science and Artificial Intelligence Programme (DS2F)  
February 2026

### Team Members
- **Carol**
- **Fred**
- **Heng CC**
- **Wei Lin**

### Contributions
This project represents a collaborative effort combining data analysis, visualization, web development, and business intelligence to deliver actionable insights from Singapore's job market data.

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

- **v1.0** (Feb 4, 2026) - Initial release
  - Complete data pipeline from raw CSV to HTML dashboard
  - 8 comprehensive visualizations
  - Business insights for 4 stakeholder groups
  - Standalone HTML dashboard (1MB)
  - Full documentation

- **v1.1** (Feb 11, 2026) - Streamlit enhancement
  - Added interactive Streamlit web application
  - Real-time filtering capabilities
  - Dynamic metric calculations
  - Enhanced user experience with modern UI
  - Consolidated documentation

- **v1.2** (Feb 14, 2026) - Streamlit optimization
  - Moved Streamlit demo to separate repository ([sgjobv2](https://github.com/fredchan23/sgjobv2))
  - Simplified implementation for Streamlit Community Cloud
  - Optimized for resource constraints
  - Stable cloud deployment with updated demo link

- **v1.3** (May 13, 2026) - OOM fix & repo consolidation
  - Diagnosed silent OOM crash on Streamlit Community Cloud (931 MB dataset exceeded ~1 GB RAM limit)
  - Fixed: columnar parquet read (9/21 columns) + category/float32 dtype optimization → 312 MB (−67%)
  - Migrated Streamlit app back to this repository; retired separate sgjobv2 repo
  - New canonical URL: [https://module1assignment.streamlit.app/](https://module1assignment.streamlit.app/)
  - Removed HTML dashboard and scratch/temp files; cleaned repository

---

## 🤖 AI-Assisted Development

This project extensively utilized **GitHub Copilot in VS Code** for:
- Data analysis and cleaning automation
- Visualization code generation
- Bug diagnosis and resolution
- Documentation creation
- Code optimization and refactoring

The complete development journey, including prompting strategies, challenges faced, and solutions discovered, is documented in [VSCode-Copilot-Journey.md](VSCode-Copilot-Journey.md) - a comprehensive tutorial for effective AI collaboration in data science projects.

### Key Takeaways
1. **Iterative Development:** AI assistance works best with clear, specific prompts and iterative feedback
2. **Problem Solving:** Multiple solution attempts led to optimal outcomes (HTML export journey)
3. **Documentation:** AI excels at creating comprehensive documentation from project context
4. **Learning Tool:** The journey documentation serves as a reference for future projects

---

**Last Updated:** May 13, 2026  
**Status:** ✅ Complete and Production-Ready

---

<div align="center">

**Built with ❤️ by Group 2**  
*Empowering data-driven decisions in Singapore's job market*

</div>
