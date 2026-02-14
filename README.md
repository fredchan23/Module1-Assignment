# Singapore Salary Insights Dashboard

A comprehensive data analysis project analyzing 1M+ job postings from Singapore to uncover salary trends, employment patterns, and career growth insights.

![Dashboard Preview](https://img.shields.io/badge/Status-Complete-success?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.13-blue?style=for-the-badge&logo=python)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange?style=for-the-badge&logo=jupyter)
![Streamlit](https://img.shields.io/badge/Streamlit-Interactive-red?style=for-the-badge&logo=streamlit)

## 🔗 Live Demos

**📄 HTML Dashboard:** [https://fredchan23.github.io/Module1-Assignment/](https://fredchan23.github.io/Module1-Assignment/)

Note: Streamlit Cloud will crash on this dashboard after few minutes, still investigating the cause if it's due to community version.

**🌐 Interactive Streamlit App:** [https://sdnibvcppey2eeglnevtec.streamlit.app/](https://sdnibvcppey2eeglnevtec.streamlit.app/)


## 🎯 Three Ways to Experience the Dashboard

This project delivers insights through three complementary formats:

### 📓 Jupyter Notebook
**File:** `salary_insights_dashboard.ipynb`  
**Best for:** Development, exploration, learning  
**Features:** Interactive code cells, inline visualizations, detailed analysis  
**Requires:** Python + Jupyter

### 📄 HTML Dashboard  
**File:** `salary_insights_dashboard.html` (1.07 MB)  
**Live:** [https://fredchan23.github.io/Module1-Assignment/](https://fredchan23.github.io/Module1-Assignment/)  
**Best for:** Sharing, presentations, offline viewing  
**Features:** Self-contained, no dependencies, email-friendly  
**Requires:** Any web browser

### 🌐 Streamlit Web App
**File:** `streamlit_dashboard.py`  
**Live:** [https://module1-assignment-wzahr5d7eaerkjxqtqtjdf.streamlit.app/](https://module1-assignment-wzahr5d7eaerkjxqtqtjdf.streamlit.app/)  
**Best for:** Live demos, interactive analysis, client presentations  
**Features:** Real-time filters, dynamic updates, professional UI  
**Requires:** Python + Streamlit

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
  - [Step 4: HTML Dashboard](#step-4-html-dashboard-generation)
  - [Step 5: Streamlit Dashboard](#step-5-streamlit-interactive-dashboard)
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
| 📊 View dashboard offline | HTML File | Open `salary_insights_dashboard.html` in browser |
| 🎛️ Filter data in real-time | Streamlit App | `streamlit run streamlit_dashboard.py` |

**First time setup:** See [Installation](#installation) section below.

---

## 📊 Project Overview

This project performs end-to-end data analysis on Singapore job market data, from raw CSV data to interactive visualizations, professional HTML dashboard, and **interactive Streamlit web application**. The analysis provides actionable insights for HR professionals, job seekers, consultants, and policymakers.

### Key Features

- **1M+ job postings** analyzed from Singapore job market
- **53K+ companies** tracked across multiple industries
- **8 interactive visualizations** covering salary distributions, employment types, career progression, and more
- **Multiple delivery formats:**
  - Jupyter Notebook for exploratory analysis
  - Standalone HTML dashboard for easy sharing
  - **Streamlit web app** with real-time filtering
- **Business insights** tailored for different stakeholders
- **Interactive filters** for dynamic data exploration

---

## 🗂️ Project Structure

```
Module1-Assignment/
│
├── SGJobData.csv                      # Raw job posting data (~300MB)
├── SGJobData_cleaned.csv              # Cleaned dataset (272MB, 1,044,583 rows) *
├── SGJobData_cleaned.parquet          # Compressed dataset (49MB, for deployment)
├── convert_to_parquet.py              # CSV to Parquet conversion utility
├── salary_insights_dashboard.ipynb    # Jupyter notebook with analysis
├── salary_insights_dashboard.html     # Standalone HTML dashboard (1MB)
├── streamlit_dashboard.py             # Interactive Streamlit web app
├── requirements.txt                   # Core dependencies for Streamlit Cloud
├── requirements-dev.txt               # Full dev environment (includes Jupyter)
├── environment.yml.backup             # Conda environment (for local use only)
├── chart4_fix.txt                     # Reference code for Chart 4 fix
├── SALARY_INSIGHTS_ANALYSIS.md        # Business insights report
├── VSCode-Copilot-Journey.md          # Development journey documentation
└── README.md                          # This file

* SGJobData_cleaned.csv is excluded from git (exceeds 100MB GitHub limit)
```

### 📦 Data Format Strategy

**Challenge:** The cleaned dataset (272MB CSV) exceeds GitHub's 100MB file size limit.

**Solution:** Parquet compression format
- ✅ **82% size reduction**: 272MB → 49MB
- ✅ **Faster loading**: Columnar storage optimized for analytics
- ✅ **GitHub compatible**: Well under 100MB limit
- ✅ **Streamlit Cloud ready**: Native pandas support with `pyarrow`

**For Development:**
```bash
# Convert CSV to Parquet (one-time setup)
conda activate assignment1
python3 convert_to_parquet.py
```

The `streamlit_dashboard.py` automatically loads from `SGJobData_cleaned.parquet`.

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
   
   **For Streamlit Dashboard only:**
   ```bash
   pip install -r requirements.txt
   ```
   
   **For full development environment (includes Jupyter):**
   ```bash
   pip install -r requirements-dev.txt
   ```
   
   **Or install manually:**
   ```bash
   pip install streamlit pandas numpy plotly
   ```

4. **Verify installation:**
   ```bash
   python -c "import streamlit, pandas, numpy, plotly; print('✓ All required packages installed!')"
   ```

> **Note on Conda Environment:** The file `environment.yml.backup` is available for local conda environments but is **not used for Streamlit Cloud deployment** to avoid dependency conflicts. Streamlit Cloud uses `requirements.txt` only.

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

### Step 5: Streamlit Interactive Dashboard

**File:** `streamlit_dashboard.py`

An interactive web application built with Streamlit for real-time data exploration.

#### Features:
- **Real-time Interactive Filters** (Sidebar):
  - Employment Type selector
  - Position Level filter
  - Salary range slider
  - Years of experience slider

- **5 Key Metric Cards:**
  - Total Job Postings (with percentage of filtered data)
  - Unique Companies
  - Median Salary
  - Mean Salary
  - Salary Standard Deviation

- **8 Interactive Visualizations:**
  - All charts update dynamically based on filter selections
  - Plotly interactive charts (hover, zoom, pan)
  - Professional layout with responsive design

#### Technical Details:
- **Framework:** Streamlit 1.40.2
- **Data Caching:** `@st.cache_data` for optimal performance
- **Layout:** Wide mode with sidebar controls
- **Responsive:** Works on desktop and mobile browsers
- **No tabs:** Clean single-page layout focusing on visualizations

#### Running the Dashboard:
```bash
# Install Streamlit
pip install streamlit

# Run the app
streamlit run streamlit_dashboard.py
```

The dashboard will automatically open at `http://localhost:8501`

---

## � Development Journey

This project was developed with extensive use of **GitHub Copilot in VS Code**, demonstrating effective AI-assisted development practices. For a complete walkthrough of the development process, see [VSCode-Copilot-Journey.md](VSCode-Copilot-Journey.md).

### Project Timeline

**Duration:** February 4-11, 2026 (7 days)

#### Phase 1: Data Analysis & Cleaning (Day 1-2)
- Analyzed raw dataset (1,048,585 rows)
- Implemented 6-step cleaning process
- Generated business insights report
- Output: Clean dataset ready for visualization

#### Phase 2: Jupyter Dashboard Creation (Day 2-3)
- Created interactive notebook with 18 cells
- Developed 8 comprehensive visualizations
- Fixed pandas aggregation column naming issue (Chart 4)
- Documented code for reproducibility

#### Phase 3: HTML Dashboard Generation (Day 3-4)
- **Attempt 1:** Plotly `.to_html()` - empty charts
- **Attempt 2:** Optimized Plotly - large file size (15+ MB)
- **Attempt 3:** Kaleido image export - dependency issues
- **Breakthrough:** Matplotlib PNG + base64 embedding
- Result: Standalone 1.07 MB HTML file

#### Phase 4: Visual Refinement (Day 4-5)
- Fixed pie chart label overlaps
- Optimized chart layouts
- Enhanced professional appearance
- Final HTML dashboard completed

#### Phase 5: Streamlit Development (Day 6-7)
- Converted Jupyter notebook to Streamlit app
- Implemented interactive filters
- Added real-time metric calculations
- Optimized for performance with data caching

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

### Challenge 4: Streamlit Cloud Deployment Dependencies

**Problem:** Streamlit Cloud deployment failed with "ModuleNotFoundError: No module named 'plotly'" despite plotly being in requirements.txt with many other packages.

**Solution:** 
- Created minimal `requirements.txt` with only essential packages for Streamlit dashboard
- Created separate `requirements-dev.txt` for full development environment
- Reduced dependencies from 59 packages to 9 core packages
- Result: Faster deployment and cleaner dependency management

**Files:**
- `requirements.txt` - Streamlit Cloud deployment (streamlit, pandas, numpy, plotly)
- `requirements-dev.txt` - Local development (includes Jupyter, matplotlib, testing tools)

### Challenge 5: Large Dataset Performance

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

### Running the Streamlit Dashboard

1. **Start the Streamlit app:**
   ```bash
   streamlit run streamlit_dashboard.py
   ```

2. **Access the dashboard:**
   - Automatically opens at `http://localhost:8501`
   - Or manually navigate to that URL in your browser

3. **Use interactive filters:**
   - **Employment Type:** Select specific employment categories
   - **Position Level:** Filter by career level
   - **Salary Range:** Adjust min/max salary with sliders
   - **Experience:** Filter by years of experience required
   - All 8 charts update in real-time based on your selections

4. **Explore the visualizations:**
   - Hover over charts for detailed information
   - Use Plotly's built-in tools (zoom, pan, export)
   - View dynamically calculated metrics at the top
   - Charts include interactive legends (click to show/hide)

5. **Share the dashboard:**
   - Run on a local network for team access
   - Deploy to Streamlit Cloud for public sharing
   - Keep the app running for live demonstrations

6. **Deploy to Streamlit Cloud (Optional):**
   
   **Prerequisites:**
   - GitHub account
   - Project pushed to GitHub repository
   - `requirements.txt` in project root (already included)
   
   **Steps:**
   1. Go to [share.streamlit.io](https://share.streamlit.io)
   2. Sign in with GitHub
   3. Click "New app"
   4. Select your repository and branch
   5. Set main file path: `streamlit_dashboard.py`
   6. Click "Deploy"
   
   **Important:** The project uses a minimal `requirements.txt` optimized for Streamlit Cloud deployment. For local development with Jupyter, use `requirements-dev.txt`.

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
| **HTML Dashboard** | Sharing, presentations, archival | No dependencies, email-friendly, works offline | Static, no filtering |
| **Streamlit App** | Live demos, interactive analysis | Real-time filtering, dynamic updates, professional UI | Requires Python runtime |

**Recommendation:**
- **Development/Analysis:** Use Jupyter Notebook
- **Quick Sharing:** Use HTML Dashboard (1MB, self-contained)
- **Client Presentations:** Use Streamlit Dashboard (interactive, professional)

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

**Last Updated:** February 11, 2026  
**Status:** ✅ Complete and Production-Ready

---

<div align="center">

**Built with ❤️ by Group 2**  
*Empowering data-driven decisions in Singapore's job market*

</div>
