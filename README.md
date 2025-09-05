<div align="center">

 # Pennsylvania EMA Project 
 ## Storm Resource Allocation Dashboard and Analysis in Python 

[About This Project](#about-this-project) · [Continuing Analysis](#continuing-analysis) · [Cleaning the Data](#cleaning-the-data) · [Numerical and Categorical Analysis](#numerical-and-categorical-analysis) · [Visualizations](#visualizations)

</div>

### About this Project 

Developed as part of the graduate course DAT 530: Present and Visualize Data at Southern New Hampshire University, this project focused on designing data visualizations tailored to diverse audiences within a state government context. Using Tableau, I created an interactive dashboard alongside two additional deliverables: a PowerPoint presentation and a public-facing pamphlet.

Project Scenario:
As a "contracted data analyst", I was tasked with developing three data visualization solutions for a state government (selected Pennsylvania from available source data):
- Storm Activity Presentation: Created a PowerPoint for the state budget office to support the establishment of a monetary reserve and guide the allocation of emergency resources to high-risk areas.
- Interactive Dashboard: Designed a dynamic dashboard for the Emergency Management Agency (EMA) to assess storm damage, allocate emergency equipment, and respond to media inquiries. 
- Public Safety Pamphlet: Developed a visually engaging pamphlet to educate the public on storm preparedness, featuring key statistics and safety recommendations.

This project emphasized effective communication through data visualization, adapting technical insights for decision-makers, operational teams, and the general public.

**Preview: Tableau Dashboard (Click to go to TableauPublic):**

[![Dashboard Preview](https://public.tableau.com/static/images/St/StormDashboard_17559311714590/Dashboard1/1.png)](https://public.tableau.com/views/StormDashboard_17559311714590/Dashboard1?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)

## Continuing Analysis

### Cleaning the Data 


**This dataset contains over 113,000 storm event records with detailed temporal fields spread across multiple columns. To prepare the data for analysis and visualization, the following cleaning steps were performed:**


**Initial Inspection**
- Loaded the dataset and reviewed structure, data types, and completeness using .head(), .info(), and .describe().


**Date Construction**
- Reformatted BEGIN_YEARMONTH and END_YEARMONTH by removing inserted spaces and converting them to strings.
- Padded BEGIN_DAY and END_DAY to ensure two-digit consistency.
- Combined year-month and day fields into a single string and converted to datetime objects using pd.to_datetime() with format %Y%m%d.
- Reformatted resulting dates into MM/DD/YYYY for readability and consistency.


**Datetime Enhancement**
- Cleaned BEGIN_TIME and END_TIME by zero-padding to four digits (HHMM format).
- Converted time strings into timedelta objects and added them to the corresponding begin_date and end_date columns.
- Final begin_date_time and end_date_time columns were formatted as MM/DD/YYYY HH:MM for timestamp-level granularity.

**Column Consolidation**
- With full datetime columns constructed, redundant fields such as BEGIN_YEARMONTH, BEGIN_DAY, and BEGIN_TIME can be safely removed to streamline the dataset.

### Numerical and Categorical Analysis 

### Visualizations


