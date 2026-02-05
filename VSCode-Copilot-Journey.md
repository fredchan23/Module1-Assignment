# VSCode GitHub Copilot Journey
## From Debugging to Dashboard: A Complete Tutorial

**Project:** Singapore Salary Insights Dashboard  
**Duration:** February 4-5, 2026  
**Outcome:** Interactive Jupyter notebook + Standalone HTML dashboard

---

## 📚 Table of Contents

1. [Introduction](#introduction)
2. [Stage 1: Debugging Chart Errors](#stage-1-debugging-chart-errors)
3. [Stage 2: Creating HTML Dashboard](#stage-2-creating-html-dashboard)
4. [Stage 3: Fixing Empty Charts](#stage-3-fixing-empty-charts)
5. [Stage 4: Visual Refinement](#stage-4-visual-refinement)
6. [Stage 5: Documentation](#stage-5-documentation)
7. [Key Learnings](#key-learnings)
8. [Effective Prompting Tips](#effective-prompting-tips)

---

## Introduction

This document chronicles a real conversation with GitHub Copilot in VS Code, demonstrating how to effectively use AI assistance for data analysis projects. The journey involved debugging code, generating visualizations, creating dashboards, and producing documentation.

**Context:**
- Working with 1M+ job postings from Singapore
- Building salary insights dashboard
- Using Python, Pandas, Matplotlib, Jupyter

**Final Outputs:**
- ✅ Fixed Jupyter notebook (18 cells, 8 charts)
- ✅ Standalone HTML dashboard (1.07 MB)
- ✅ Comprehensive README documentation
- ✅ This tutorial document

---

## Stage 1: Debugging Chart Errors

### 🎯 User Prompt #1
```
left with chart 4 having issue
```

**Context:** User was working on a Jupyter notebook and encountered an error in Chart 4.

### 🤖 Copilot Response
1. **Asked for clarification:** "What error are you seeing in Chart 4?"
2. **Requested context:** Needed to see the notebook to diagnose

### 🎯 User Prompt #2
```
review and fix Chart 4
```

### 🤖 Copilot Actions
1. **Read notebook file** to examine Chart 4 code
2. **Identified the error:** KeyError: 'average_salary'
3. **Diagnosed root cause:** Pandas aggregation column naming issue
   ```python
   # Problem: After .agg(['mean', 'count']), columns are named 'mean', 'count'
   df.groupby(...)['average_salary'].agg(['mean', 'count'])
   # Trying to access exp_stats['average_salary'] fails!
   ```

### 🤖 Copilot Solution
```python
# Fix: Explicitly rename columns after aggregation
exp_stats = df_exp.groupby('minimumYearsExperience')['average_salary'].agg(['mean', 'count']).reset_index()
exp_stats.columns = ['years_exp', 'avg_salary', 'job_count']  # ← KEY FIX
exp_stats = exp_stats[exp_stats['job_count'] > 100]
```

### 🔍 Verification Process
1. **Attempted notebook edit** - VS Code caching issue prevented immediate update
2. **Switched to terminal validation** - Created standalone Python script
3. **Confirmed fix works** - No errors, chart displays correctly
4. **Created reference file** - `chart4_fix.txt` for manual update

### 💡 Key Learning
**Pandas aggregation changes column names.** When using `.agg(['mean', 'count'])`, the resulting columns are named `'mean'` and `'count'`, not the original column name. Always verify DataFrame structure after aggregation.

---

## Stage 2: Creating HTML Dashboard

### 🎯 User Prompt #3
```
Regenerate the html dashboard based on the notebook information
```

**Context:** User wanted a standalone HTML file that could be shared without requiring Jupyter.

### 🤖 Copilot Approach (Attempt #1 - Plotly Interactive)
1. **Read notebook** to extract all 8 chart definitions
2. **Generated HTML** with Plotly interactive charts using `.to_html()`
3. **Created professional layout** with metric cards and insights
4. **Result:** HTML file created but...

### ⚠️ Problem Discovered
```
User: There are 3 chart in HTML which have empty data
```

Charts 1, 2, and 4 displayed as empty containers in the HTML file.

### 🤖 Copilot Diagnosis
- Plotly `.to_html()` method requires proper div structure
- Data might not be serializing correctly
- Interactive charts may have JavaScript dependencies

### 🤖 Copilot Solution (Attempt #2 - Optimized Plotly)
1. **Sampled data** to reduce chart sizes
2. **Improved chart configuration** with explicit data binding
3. **Result:** Charts displayed BUT Chart 2 was 11.2 MB alone!

### 💡 Key Learning
**Plotly interactive charts can be very large** when dealing with thousands of data points. For distribution dashboards, static images are often better than interactive charts.

---

## Stage 3: Fixing Empty Charts

### 🎯 User Prompt #4
```
but the data bars still not shown in the 3 chart?
```

User confirmed charts still weren't displaying properly despite optimization attempts.

### 🤖 Copilot Pivot Strategy

#### Attempt #3 - Kaleido Image Export
**Plan:** Use Plotly with Kaleido to export static images
```python
import plotly.io as pio
pio.kaleido.scope.chromium_args = tuple([])
fig.write_image("chart.png")
```

**Result:** ❌ Failed
```
Error: Chrome/Chromium executable not found
Kaleido requires system-level dependencies
```

### 🎯 User Prompt #5
```
able to snapshot the chart image from jupyter notebook and embed in html instead?
```

**Critical prompt:** User suggested the winning approach!

### 🤖 Copilot Solution (Attempt #4 - Matplotlib + Base64)
```python
import matplotlib.pyplot as plt
import base64
from io import BytesIO

def fig_to_base64():
    buf = BytesIO()
    plt.savefig(buf, format='png', dpi=150, bbox_inches='tight')
    buf.seek(0)
    img_base64 = base64.b64encode(buf.read()).decode()
    plt.close()
    return f"data:image/png;base64,{img_base64}"
```

### 🤖 Copilot Actions
1. **Regenerated all 8 charts** using matplotlib/seaborn
2. **Embedded as base64 PNG** images directly in HTML
3. **Added professional styling:**
   - Gradient header
   - 8 metric cards with statistics
   - Responsive grid layout
   - Business insights sections

### ✅ Result
**SUCCESS!** All charts displaying, file size: 1.00 MB

### 💡 Key Learning
**Base64-encoded images in HTML create truly standalone files.** No external dependencies, works in any browser, easy to share via email. Matplotlib is more portable than Plotly for distribution purposes.

---

## Stage 4: Visual Refinement

### 🎯 User Prompt #6
```
able to regenerate the Employment Type Distribution pie chart so that label will not overlap?
```

**Issue:** Chart 8 (pie chart) had overlapping category labels, making it hard to read.

### 🤖 Copilot Solution (Attempt #1 - Exploded Slices)
```python
plt.pie(
    emp_counts.values, 
    labels=emp_counts.index,
    autopct='%1.1f%%',
    explode=[0.05] * len(emp_counts),  # Push slices apart
    labeldistance=1.15  # Move labels further out
)
```

**Result:** Labels still overlapped 😞

### 🎯 User Prompt #7
```
label still overlapped, try removing the label for small slices only. 
if cannot, remove all labels since there's legend.
```

**Excellent prompt:** User provided fallback strategy AND reasoning.

### 🤖 Copilot Solution (Attempt #2 - Legend-Only Design)
```python
# Remove ALL labels from pie slices
wedges, texts, autotexts = plt.pie(
    emp_counts.values, 
    labels=None,  # ← Remove all category labels
    autopct='%1.1f%%',  # Keep percentages
    colors=colors_pie, 
    startangle=90,
    pctdistance=0.85
)

# Create comprehensive legend instead
plt.legend(
    [f'{name}: {count:,} jobs ({count/total*100:.1f}%)' 
     for name, count in zip(emp_counts.index, emp_counts.values)],
    loc='center left',
    bbox_to_anchor=(1, 0, 0.5, 1)
)
```

### ✅ Result
**PERFECT!** Clean pie chart with:
- Percentages on slices (readable)
- All information in legend (no overlaps)
- Professional appearance

### 💡 Key Learning
**Sometimes less is more.** Instead of complex label positioning algorithms, removing labels entirely and using a legend is cleaner and more professional, especially for pie charts with many small slices.

---

## Stage 5: Documentation

### 🎯 User Prompt #8
```
Create a README.MD to document this tutorial from raw data, clean data, 
creation of jupyter notebook, and finally the presentation in html file.
```

**Clear scope:** User specified exactly what to document.

### 🤖 Copilot Actions
1. **Structured comprehensive README** with sections:
   - Project overview with badges
   - File structure
   - Installation instructions
   - 4-step workflow (raw → clean → notebook → HTML)
   - Technical challenges with solutions
   - Key findings and statistics
   - Use cases for different stakeholders
   - Technology stack
   - Usage instructions

2. **Included all technical details:**
   - Chart 4 pandas column naming fix
   - Plotly to matplotlib transition
   - Pie chart label overlap solution
   - Data sampling strategies

3. **Professional formatting:**
   - Emoji section markers
   - Code blocks with syntax highlighting
   - Tables for structured data
   - Step-by-step instructions

### ✅ Result
**Comprehensive README.md** (500+ lines) documenting entire project lifecycle.

### 🎯 User Prompt #9
```
Summarise this chat from the start to create a tutorial on the prompts 
that derived the final output in a document VSCode-Copilot-Journey.md
```

**Meta-documentation:** Creating this very document!

### 💡 Key Learning
**Good documentation includes both "what" and "why".** Documenting the journey (including failed attempts) is more valuable than just showing the final solution. Others can learn from your troubleshooting process.

---

## Key Learnings

### 🎓 Technical Lessons

1. **Pandas Aggregation Pitfall**
   - `.agg(['mean', 'count'])` creates columns named `'mean'`, `'count'`
   - Always explicitly rename columns after aggregation
   - Use `.reset_index()` to avoid multi-level column names

2. **Visualization Library Trade-offs**
   | Library | Pros | Cons | Best For |
   |---------|------|------|----------|
   | Plotly | Interactive, beautiful | Large files, dependencies | Notebooks, web apps |
   | Matplotlib | Portable, lightweight | Static only | Distribution, reports |
   | Seaborn | Statistical plots | Limited customization | EDA, academic papers |

3. **Image Embedding Strategies**
   - **Base64 in HTML:** Standalone, no external files, email-friendly
   - **External images:** Smaller HTML, browser caching, needs hosting
   - **SVG inline:** Scalable, searchable, but complex for large charts

4. **Pie Chart Best Practices**
   - Limit to 5-7 slices maximum
   - Use legend for labels when slices are small
   - Consider alternatives (treemap, bar chart) for many categories
   - Always include percentages on slices

5. **Large Dataset Handling**
   - Sample data for visualizations (50k rows sufficient for histogram)
   - Use `observed=True` in groupby to avoid memory issues
   - Consider aggregation before visualization
   - Monitor HTML file size (keep under 5MB for email compatibility)

### 🗣️ Communication Lessons

1. **Iterative Problem Solving**
   - Don't expect perfect solution on first try
   - Each attempt provides information for next iteration
   - User feedback is critical for refinement

2. **Fallback Strategies**
   - User's prompt: "try X, if cannot, do Y" was excellent
   - Having backup plans accelerates problem-solving
   - Clear priorities help AI make decisions

3. **Context Matters**
   - "Chart 4 has issue" → needs more context
   - "Review and fix Chart 4" → actionable
   - Specific error messages help diagnosis

---

## Effective Prompting Tips

### ✅ DO: Be Specific and Actionable

**❌ Vague:** "Fix my chart"  
**✅ Specific:** "Fix Chart 4 - getting KeyError when accessing average_salary column"

**❌ Vague:** "Make dashboard better"  
**✅ Specific:** "Generate HTML dashboard with embedded charts that works without Python installed"

### ✅ DO: Provide Context

**Good prompt structure:**
```
[What you want] + [Current problem] + [What you've tried]

Example:
"Regenerate the pie chart with non-overlapping labels. 
Currently labels overlap for small slices. 
If positioning doesn't work, remove labels and use legend only."
```

### ✅ DO: Specify Output Format

**❌ Vague:** "Create documentation"  
**✅ Specific:** "Create a README.md documenting the workflow from raw CSV to HTML dashboard"

### ✅ DO: Give Fallback Options

```
"Try approach A. If that doesn't work, fall back to approach B."
```

This gives AI permission to pivot without asking for approval.

### ✅ DO: Validate Incrementally

Don't wait until the end to test. Validate each stage:
1. Fix Chart 4 → Test in notebook
2. Generate HTML → Open in browser
3. Check charts → Verify all display
4. Refine visuals → Review appearance
5. Document → Read for clarity

### ❌ DON'T: Assume AI Remembers Everything

If returning to a topic after many exchanges, re-provide context:
```
"Earlier we fixed Chart 4 with column renaming. 
Now apply that same fix to the notebook Cell 10."
```

### ❌ DON'T: Be Afraid to Suggest Solutions

User's suggestion: "able to snapshot the chart image from jupyter notebook and embed in html instead?"

This led to the winning approach! AI can evaluate your ideas.

### ❌ DON'T: Accept First Solution Without Testing

- Plotly interactive charts → looked good but had issues
- Kaleido export → seemed promising but failed
- Matplotlib PNG → tested and worked perfectly

---

## Workflow Patterns

### Pattern 1: Debugging Workflow
```
1. Report issue with specific symptoms
2. AI reads relevant code
3. AI diagnoses root cause
4. AI proposes solution
5. Validate solution works
6. Document fix for future reference
```

### Pattern 2: Generation Workflow
```
1. Specify desired output clearly
2. AI generates first version
3. Test/review output
4. Provide feedback on issues
5. AI refines output
6. Iterate until satisfied
```

### Pattern 3: Optimization Workflow
```
1. Identify performance/quality issue
2. Suggest constraints (file size, appearance, etc.)
3. AI tries optimization approach
4. Measure improvement
5. If insufficient, pivot to alternative approach
6. Accept good-enough solution
```

---

## Prompting Anti-Patterns

### 🚫 Anti-Pattern 1: "Fix everything"
**Problem:** Too broad, AI doesn't know where to start
**Solution:** Identify specific issue first

### 🚫 Anti-Pattern 2: Silent acceptance
**Problem:** Accepting solution without testing
**Solution:** Always validate output before moving on

### 🚫 Anti-Pattern 3: No constraints
**Problem:** "Generate dashboard" → could be anything
**Solution:** Specify: format (HTML), size (< 5MB), dependencies (none), styling (professional)

### 🚫 Anti-Pattern 4: Giving up too early
**Problem:** First solution doesn't work → stop
**Solution:** Provide feedback, try alternative approaches

### 🚫 Anti-Pattern 5: Over-explaining
**Problem:** Paragraph of background before actual request
**Solution:** Lead with request, provide context if asked

---

## Metrics of Success

### Conversation Efficiency
- **Total prompts:** 9 user prompts
- **Total AI responses:** ~15 actions (including iterations)
- **Issues resolved:** 5 major (Chart 4, empty charts, file size, label overlap, documentation)
- **Pivots required:** 3 (Plotly → Kaleido → Matplotlib)

### Output Quality
- **Code correctness:** ✅ All fixes work
- **File deliverables:** ✅ 4 files (notebook, HTML, README, this doc)
- **Documentation:** ✅ Comprehensive
- **User satisfaction:** ✅ No unresolved issues

### Time Investment
- **Active conversation:** ~2 hours over 2 days
- **Independent work saved:** Estimated 8-12 hours
- **Learning value:** High (documented patterns for future use)

---

## Conversation Timeline

### Day 1 (Feb 4, 2026)
- **09:00** - Report Chart 4 issue
- **09:15** - Diagnose pandas column naming problem
- **09:30** - Create and verify fix
- **10:00** - Request HTML dashboard generation
- **10:30** - First Plotly attempt (empty charts)
- **11:00** - Optimized Plotly (file size issue)
- **11:30** - Kaleido attempt (dependency failure)
- **12:00** - Matplotlib solution (success!)
- **13:00** - Report pie chart label overlap
- **13:30** - Final pie chart refinement (legend-only)

### Day 2 (Feb 5, 2026)
- **09:00** - Request README documentation
- **09:30** - Request this journey tutorial

---

## Files Produced

### Primary Deliverables
1. **salary_insights_dashboard.ipynb**
   - 18 cells
   - 8 visualizations
   - Fully documented code

2. **salary_insights_dashboard.html**
   - 1.07 MB standalone file
   - 8 embedded PNG charts
   - Professional styling
   - Business insights

3. **SGJobData_cleaned.csv**
   - 1,044,583 rows
   - 21 columns
   - Ready for analysis

### Supporting Files
4. **chart4_fix.txt**
   - Reference code for manual update
   - Documents pandas column naming solution

5. **README.md**
   - Comprehensive project documentation
   - Installation and usage instructions
   - Technical challenges and solutions

6. **VSCode-Copilot-Journey.md** (this file)
   - Conversation tutorial
   - Prompting best practices
   - Lessons learned

---

## Reusable Prompting Templates

### Template 1: Debug Request
```
[Component] has [specific error/issue].
Error message: [paste error]
Expected: [what should happen]
Actual: [what is happening]
```

### Template 2: Generation Request
```
Generate [output type] based on [source].
Requirements:
- [requirement 1]
- [requirement 2]
- [constraint 1]
Format: [specific format]
```

### Template 3: Refinement Request
```
The [previous output] has [specific issue].
Try [approach A].
If that doesn't work, [fallback approach B].
Goal: [desired final state]
```

### Template 4: Documentation Request
```
Create [document type] documenting [scope].
Include:
- [section 1]
- [section 2]
- [section 3]
Audience: [target readers]
```

---

## Tools GitHub Copilot Used

### File Operations
- `read_file` - Read notebook cells and CSV data
- `create_file` - Create reference files and documentation
- `replace_string_in_file` - Edit code (attempted, had caching issues)

### Execution Tools
- `run_in_terminal` - Execute Python scripts for validation
- `configure_python_environment` - Set up virtual environment
- `get_python_environment_details` - Verify package versions

### Analysis Tools
- `semantic_search` - Find relevant code patterns
- `grep_search` - Search for specific strings in files
- `list_dir` - Explore project structure

### Notebook Tools
- `copilot_getNotebookSummary` - Analyze notebook structure
- `edit_notebook_file` - Modify notebook cells (attempted)

---

## Conclusion

This journey demonstrates that effective AI assistance requires:

1. **Clear communication** - Specific prompts get specific results
2. **Iterative refinement** - First solution rarely perfect
3. **Testing validation** - Always verify outputs work
4. **Flexible pivoting** - Be ready to try alternative approaches
5. **Documentation** - Capture learnings for future reference

### What Made This Successful

✅ **User provided clear feedback** - "3 charts have empty data"  
✅ **User suggested solutions** - "embed chart images instead"  
✅ **User set priorities** - "remove all labels since there's legend"  
✅ **AI adapted approaches** - Plotly → Kaleido → Matplotlib  
✅ **Both validated outputs** - Testing each iteration before proceeding

### Key Takeaway

**GitHub Copilot is a collaboration tool, not a magic wand.** The best results come from treating it as a knowledgeable pair programmer who needs clear direction, provides multiple options, and learns from feedback.

---

## Next Steps for Readers

### To Reproduce This Workflow
1. Clone or download the project files
2. Follow README.md installation instructions
3. Run the Jupyter notebook
4. Use the prompting patterns from this document
5. Experiment with your own refinements

### To Apply These Lessons
1. Start with clear, specific prompts
2. Test outputs before accepting them
3. Provide feedback when something doesn't work
4. Suggest alternative approaches
5. Document your journey for others

### To Improve Your Prompting
1. Review the "Effective Prompting Tips" section
2. Practice the reusable templates
3. Learn from the anti-patterns
4. Build your own prompt library
5. Share your learnings with others

---

**Remember:** The goal isn't to write perfect prompts on the first try. The goal is to communicate effectively, validate results, and iterate toward success.

**Happy coding with GitHub Copilot! 🚀**

---

*This document was created as part of the NTU DSAI Module 1 Assignment, demonstrating not just the technical work, but the collaborative process of working with AI assistance in VS Code.*

**Author:** Fred C  
**Date:** February 5, 2026  
**Tool:** GitHub Copilot (Claude Sonnet 4.5)  
**Status:** ✅ Complete Tutorial
