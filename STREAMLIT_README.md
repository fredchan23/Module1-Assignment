# Singapore Salary Insights - Streamlit Dashboard

## 🚀 Quick Start

### Prerequisites
Make sure you have Python 3.7+ installed and the required packages.

### Installation

1. **Install required packages:**
```bash
pip install streamlit pandas numpy plotly
```

Or if you have the requirements.txt:
```bash
pip install -r requirements.txt
```

2. **Ensure data file is present:**
Make sure `SGJobData_cleaned.csv` is in the same directory as `streamlit_dashboard.py`

### Running the Dashboard

```bash
streamlit run streamlit_dashboard.py
```

The dashboard will automatically open in your default web browser at `http://localhost:8501`

## 📊 Features

### Interactive Filters
- **Employment Type:** Filter by Permanent, Contract, Internship, etc.
- **Position Level:** Filter by entry-level, mid-senior, senior management, etc.
- **Salary Range:** Interactive slider to focus on specific salary bands
- **Years of Experience:** Filter by experience requirements

### Four Main Sections

#### 1. 📈 Visualizations
- **Salary Distribution:** Histogram showing overall salary patterns
- **Employment Type Distribution:** Pie chart of market composition
- **Salary by Position Level:** Bar chart comparing different career levels
- **Salary Growth by Experience:** Line chart showing career progression
- **Salary Percentiles:** Quick reference for salary benchmarking
- **Salary Distribution by Employment Type:** Box plots for detailed comparison
- **Top 15 Hiring Companies:** See who's hiring the most
- **Top Industries by Salary:** Compare industries by compensation

#### 2. 💡 Insights
Business intelligence for:
- **HR Departments:** Compensation strategy and benchmarking
- **Job Seekers:** Career planning and salary expectations
- **Consultancy Firms:** Market positioning and advisory
- **Government Agencies:** Policy planning and labor market analysis

#### 3. 📊 Statistics
Detailed statistical analysis including:
- Comprehensive salary metrics
- Employment type breakdown
- Position level statistics
- Market overview

#### 4. 🔍 Deep Dive
Interactive data explorer:
- Customizable data views
- Column selection
- Sorting options
- Statistical summaries

## 🎨 Dashboard Layout

The dashboard uses a wide layout with:
- **Sidebar:** All filter controls
- **Main Area:** Key metrics and tabbed content
- **Responsive Design:** Works on different screen sizes

## 📁 File Structure

```
Module1-Assignment/
├── streamlit_dashboard.py      # Main Streamlit application
├── SGJobData_cleaned.csv       # Data file (required)
├── STREAMLIT_README.md         # This file
└── requirements.txt            # Python dependencies
```

## 💡 Tips

1. **Filtering:** Use the sidebar filters to focus on specific segments of the job market
2. **Reset Filters:** Refresh the page to reset all filters
3. **Export Visualizations:** Hover over any chart to see Plotly's interactive toolbar
4. **Performance:** Large datasets are automatically sampled for histogram performance

## 🐛 Troubleshooting

**Dashboard won't start:**
- Ensure all required packages are installed: `pip install streamlit pandas numpy plotly`
- Check that Python version is 3.7 or higher: `python --version`

**Data file not found:**
- Make sure `SGJobData_cleaned.csv` is in the same directory as the script
- Check the file name matches exactly (case-sensitive)

**Visualizations not loading:**
- Check internet connection (Plotly may load resources online)
- Try refreshing the page with Ctrl+R (Cmd+R on Mac)

**Slow performance:**
- The dashboard automatically samples large datasets
- Close other browser tabs to free up memory
- Adjust the experience filter to reduce data size

## 🔧 Customization

You can customize the dashboard by editing `streamlit_dashboard.py`:
- Modify color schemes in the chart definitions
- Add new visualizations
- Change filter default values
- Adjust layout and styling

## 📝 Notes

- All salary values are in SGD (Singapore Dollars)
- Data is cached for better performance
- Charts are interactive - click, hover, zoom, and pan
- Use the full-screen button in charts for detailed exploration

## 🤝 Support

For issues or questions:
1. Check this README
2. Review the Streamlit documentation: https://docs.streamlit.io
3. Check Plotly documentation: https://plotly.com/python/

---

**Built with:** Streamlit, Plotly, Pandas, NumPy
