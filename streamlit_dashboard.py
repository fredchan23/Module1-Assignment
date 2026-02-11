"""
Singapore Salary Insights Dashboard
Interactive Streamlit application for analyzing 1M+ job postings
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import json
import warnings
warnings.filterwarnings('ignore')

# Page configuration
st.set_page_config(
    page_title="Singapore Salary Insights Dashboard",
    page_icon="💼",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 0.5rem;
    }
    .sub-header {
        font-size: 1.2rem;
        color: #666;
        text-align: center;
        margin-bottom: 2rem;
    }
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1rem;
        border-radius: 10px;
        color: white;
        text-align: center;
    }
    .insight-box {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 5px;
        border-left: 4px solid #1f77b4;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Cache data loading
@st.cache_data
def load_data():
    """Load and prepare the salary data"""
    try:
        df = pd.read_csv('SGJobData_cleaned.csv')
        
        # Prepare additional columns
        df['salary_spread'] = df['salary_maximum'] - df['salary_minimum']
        df['posting_date'] = pd.to_datetime(df['metadata_newPostingDate'], errors='coerce')
        df['year_month'] = df['posting_date'].dt.to_period('M')
        
        # Extract primary industry from categories JSON
        industries_list = []
        for idx, cat_str in enumerate(df['categories'].dropna()):
            try:
                categories = json.loads(cat_str)
                if isinstance(categories, list) and len(categories) > 0:
                    if isinstance(categories[0], dict) and 'category' in categories[0]:
                        industries_list.append({
                            'idx': idx,
                            'industry': categories[0]['category']
                        })
            except:
                pass
        
        if industries_list:
            ind_df = pd.DataFrame(industries_list).set_index('idx')
            df['primary_industry'] = df.index.map(lambda x: ind_df.loc[x, 'industry'] if x in ind_df.index else 'Other')
        else:
            df['primary_industry'] = 'Other'
        
        return df
    except Exception as e:
        st.error(f"Error loading data: {str(e)}")
        return None

# Load data
with st.spinner('Loading data...'):
    df = load_data()

if df is None:
    st.error("Failed to load data. Please ensure 'SGJobData_cleaned.csv' is in the same directory.")
    st.stop()

# Header
st.markdown('<div class="main-header">💼 Singapore Salary Insights Dashboard</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Interactive Analysis of 1M+ Job Postings</div>', unsafe_allow_html=True)

# Sidebar filters
st.sidebar.title("🔍 Filters")
st.sidebar.markdown("---")

# Employment Type filter
employment_types = ['All'] + sorted(df['employmentTypes'].unique().tolist())
selected_employment = st.sidebar.selectbox("Employment Type", employment_types)

# Position Level filter
position_levels = ['All'] + sorted(df['positionLevels'].unique().tolist())
selected_position = st.sidebar.selectbox("Position Level", position_levels)

# Salary range filter
min_salary = int(df['average_salary'].min())
max_salary = int(df['average_salary'].max())
salary_range = st.sidebar.slider(
    "Salary Range (SGD)",
    min_value=min_salary,
    max_value=max_salary,
    value=(min_salary, max_salary)
)

# Experience filter
max_exp = int(df['minimumYearsExperience'].max())
experience_range = st.sidebar.slider(
    "Years of Experience",
    min_value=0,
    max_value=min(max_exp, 20),
    value=(0, min(max_exp, 20))
)

st.sidebar.markdown("---")
st.sidebar.info("**Business Objective:** Provide HR departments, consultancy firms, job seekers, and government agencies with actionable salary insights for benchmarking and planning.")

# Apply filters
filtered_df = df.copy()
if selected_employment != 'All':
    filtered_df = filtered_df[filtered_df['employmentTypes'] == selected_employment]
if selected_position != 'All':
    filtered_df = filtered_df[filtered_df['positionLevels'] == selected_position]
filtered_df = filtered_df[
    (filtered_df['average_salary'] >= salary_range[0]) &
    (filtered_df['average_salary'] <= salary_range[1]) &
    (filtered_df['minimumYearsExperience'] >= experience_range[0]) &
    (filtered_df['minimumYearsExperience'] <= experience_range[1])
]

# Key Metrics Row
st.markdown("### 📊 Key Metrics")
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.metric(
        "Total Job Postings",
        f"{len(filtered_df):,}",
        delta=f"{len(filtered_df)/len(df)*100:.1f}% of total" if len(filtered_df) != len(df) else None
    )

with col2:
    st.metric(
        "Unique Companies",
        f"{filtered_df['postedCompany_name'].nunique():,}"
    )

with col3:
    st.metric(
        "Median Salary",
        f"SGD {filtered_df['average_salary'].median():,.0f}"
    )

with col4:
    st.metric(
        "Mean Salary",
        f"SGD {filtered_df['average_salary'].mean():,.0f}"
    )

with col5:
    st.metric(
        "Salary Std Dev",
        f"SGD {filtered_df['average_salary'].std():,.0f}"
    )

st.markdown("---")

# Visualizations Section
st.markdown("## Interactive Visualizations")

# Chart 1 & 2 in columns
col1, col2 = st.columns(2)

with col1:
    st.markdown("### Salary Distribution")
    sample_size = min(50000, len(filtered_df))
    df_sample = filtered_df.sample(n=sample_size, random_state=42) if len(filtered_df) > sample_size else filtered_df
    
    fig1 = go.Figure()
    fig1.add_trace(go.Histogram(
        x=df_sample['average_salary'],
        nbinsx=50,
        name='Salary Distribution',
        marker_color='rgba(0, 123, 255, 0.7)',
        hovertemplate='<b>Salary Range</b><br>SGD %{x:,.0f}<br><b>Count</b>: %{y}<extra></extra>'
    ))
    
    fig1.add_vline(x=filtered_df['average_salary'].median(), line_dash="dash", line_color="red",
                  annotation_text=f"Median: SGD {filtered_df['average_salary'].median():,.0f}",
                  annotation_position="top right")
    fig1.add_vline(x=filtered_df['average_salary'].mean(), line_dash="dot", line_color="green",
                  annotation_text=f"Mean: SGD {filtered_df['average_salary'].mean():,.0f}",
                  annotation_position="top left")
    
    fig1.update_layout(
        xaxis_title='Average Salary (SGD)',
        yaxis_title='Number of Job Postings',
        hovermode='x unified',
        template='plotly_white',
        height=400
    )
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    st.markdown("### Employment Type Distribution")
    emp_counts = filtered_df['employmentTypes'].value_counts()
    
    fig8 = go.Figure(data=[go.Pie(
        labels=emp_counts.index,
        values=emp_counts.values,
        hovertemplate='<b>%{label}</b><br>Count: %{value:,}<br>Percentage: %{percent}<extra></extra>',
        textinfo='label+percent',
        textposition='inside'
    )])
    
    fig8.update_layout(
        height=400,
        template='plotly_white'
    )
    st.plotly_chart(fig8, use_container_width=True)

# Chart 3: Salary by Position Level
st.markdown("### Salary by Position Level")
pos_level_stats = filtered_df.groupby('positionLevels', observed=True)['average_salary'].agg(['mean', 'median', 'count']).sort_values('mean', ascending=False)

fig3 = go.Figure()
fig3.add_trace(go.Bar(
    x=pos_level_stats.index,
    y=pos_level_stats['mean'],
    name='Mean Salary',
    marker_color='rgba(0, 123, 255, 0.7)',
    text=[f"SGD {val:,.0f}" for val in pos_level_stats['mean']],
    textposition='auto',
    hovertemplate='<b>%{x}</b><br>Mean: SGD %{y:,.0f}<br>Count: %{customdata:,}<extra></extra>',
    customdata=pos_level_stats['count'].values
))

fig3.add_trace(go.Scatter(
    x=pos_level_stats.index,
    y=pos_level_stats['median'],
    name='Median Salary',
    mode='lines+markers',
    line_color='red',
    marker=dict(size=8),
    hovertemplate='<b>%{x}</b><br>Median: SGD %{y:,.0f}<extra></extra>'
))

fig3.update_layout(
    xaxis_title='Position Level',
    yaxis_title='Salary (SGD)',
    hovermode='x unified',
    template='plotly_white',
    height=500,
    xaxis_tickangle=-45
)
st.plotly_chart(fig3, use_container_width=True)

# Chart 4 & 6 in columns
col1, col2 = st.columns(2)

with col1:
    st.markdown("### Salary Growth by Experience")
    df_exp = filtered_df[filtered_df['minimumYearsExperience'] <= 12].copy()
    exp_stats = df_exp.groupby('minimumYearsExperience')['average_salary'].agg(['mean', 'count']).reset_index()
    exp_stats.columns = ['years_experience', 'avg_salary', 'job_count']
    exp_stats = exp_stats[exp_stats['job_count'] > 50].reset_index(drop=True)
    
    fig4 = go.Figure()
    fig4.add_trace(go.Scatter(
        x=exp_stats['years_experience'],
        y=exp_stats['avg_salary'],
        mode='lines+markers',
        name='Average Salary',
        line=dict(color='green', width=3),
        marker=dict(size=8, color='darkgreen'),
        hovertemplate='<b>Experience:</b> %{x} years<br><b>Salary:</b> SGD %{y:,.0f}<br><b>Jobs:</b> %{customdata:,}<extra></extra>',
        customdata=exp_stats['job_count'].values
    ))
    
    fig4.update_layout(
        xaxis_title='Minimum Years of Experience',
        yaxis_title='Average Salary (SGD)',
        hovermode='x unified',
        template='plotly_white',
        height=400,
        xaxis=dict(dtick=1)
    )
    st.plotly_chart(fig4, use_container_width=True)

with col2:
    st.markdown("### Salary Percentiles")
    percentiles = [10, 25, 50, 75, 90]
    percentile_values = [np.percentile(filtered_df['average_salary'], p) for p in percentiles]
    
    fig6 = go.Figure()
    fig6.add_trace(go.Bar(
        x=[f"{p}th" for p in percentiles],
        y=percentile_values,
        marker_color=['#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b'],
        text=[f"SGD {val:,.0f}" for val in percentile_values],
        textposition='auto',
        hovertemplate='<b>%{x} Percentile</b><br>Salary: SGD %{y:,.0f}<extra></extra>'
    ))
    
    fig6.update_layout(
        xaxis_title='Percentile',
        yaxis_title='Salary (SGD)',
        hovermode='x unified',
        template='plotly_white',
        height=400
    )
    st.plotly_chart(fig6, use_container_width=True)

# Chart 2: Salary by Employment Type (Box Plot)
st.markdown("### Salary Distribution by Employment Type")
emp_type_stats = filtered_df.groupby('employmentTypes', observed=True)['average_salary'].agg(['mean', 'median', 'count']).sort_values('mean', ascending=False)

fig2 = go.Figure()
for emp_type in emp_type_stats.index:
    emp_data = filtered_df[filtered_df['employmentTypes'] == emp_type]['average_salary']
    fig2.add_trace(go.Box(
        y=emp_data,
        name=emp_type,
        boxmean=False,
        hovertemplate='<b>%{fullData.name}</b><br>Salary: SGD %{y:,.0f}<extra></extra>'
    ))

fig2.update_layout(
    yaxis_title='Average Salary (SGD)',
    xaxis_title='Employment Type',
    hovermode='closest',
    template='plotly_white',
    height=500,
    showlegend=False
)
st.plotly_chart(fig2, use_container_width=True)

# Chart 5 & 7 in columns
col1, col2 = st.columns(2)

with col1:
    st.markdown("### Top 15 Hiring Companies")
    top_companies = filtered_df['postedCompany_name'].value_counts().head(15).reset_index()
    top_companies.columns = ['Company', 'Postings']
    company_salary = filtered_df.groupby('postedCompany_name')['average_salary'].mean()
    top_companies['Avg_Salary'] = top_companies['Company'].map(company_salary)
    
    fig5 = go.Figure()
    fig5.add_trace(go.Bar(
        x=top_companies['Postings'],
        y=top_companies['Company'],
        orientation='h',
        marker=dict(
            color=top_companies['Avg_Salary'],
            colorscale='Viridis',
            showscale=True,
            colorbar=dict(title='Avg Salary<br>(SGD)')
        ),
        text=[f"SGD {sal:,.0f}" for sal in top_companies['Avg_Salary']],
        textposition='auto',
        hovertemplate='<b>%{y}</b><br>Postings: %{x}<br>Avg Salary: SGD %{marker.color:,.0f}<extra></extra>'
    ))
    
    fig5.update_layout(
        xaxis_title='Number of Job Postings',
        yaxis_title='Company Name',
        hovermode='closest',
        template='plotly_white',
        height=500,
        margin=dict(l=200)
    )
    st.plotly_chart(fig5, use_container_width=True)

with col2:
    st.markdown("### Top Industries by Average Salary")
    if 'primary_industry' in filtered_df.columns and filtered_df['primary_industry'].notna().any():
        top_industries = filtered_df['primary_industry'].value_counts().head(10).index
        industry_stats = filtered_df[filtered_df['primary_industry'].isin(top_industries)].groupby('primary_industry', observed=True)['average_salary'].agg(['mean', 'count']).sort_values('mean', ascending=False)
    else:
        industry_stats = filtered_df.groupby('employmentTypes', observed=True)['average_salary'].agg(['mean', 'count']).sort_values('mean', ascending=False).head(10)
    
    fig7 = go.Figure()
    fig7.add_trace(go.Bar(
        x=industry_stats.index,
        y=industry_stats['mean'],
        marker_color='rgba(0, 123, 255, 0.7)',
        text=[f"SGD {val:,.0f}<br>({int(cnt)} jobs)" for val, cnt in zip(industry_stats['mean'], industry_stats['count'])],
        textposition='auto',
        hovertemplate='<b>%{x}</b><br>Mean: SGD %{y:,.0f}<br>Count: %{customdata:,}<extra></extra>',
        customdata=industry_stats['count'].values
    ))
    
    fig7.update_layout(
        xaxis_title='Industry/Category',
        yaxis_title='Average Salary (SGD)',
        hovermode='x unified',
        template='plotly_white',
        height=500,
        xaxis_tickangle=-45
    )
    st.plotly_chart(fig7, use_container_width=True)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; padding: 2rem 0;">
    <p><b>Singapore Salary Insights Dashboard</b></p>
    <p>Data Source: 1,044,583 job postings from 53,151 companies</p>
    <p>💼 Empowering HR, Job Seekers, Consultants, and Policy Makers with Data-Driven Insights</p>
</div>
""", unsafe_allow_html=True)

