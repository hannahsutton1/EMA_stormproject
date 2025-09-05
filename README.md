<div align="center">

 # Pennsylvania EMA Project 
 ## Storm Resource Allocation Dashboard and Analysis in Python 

[About This Project](#about-this-project) · [Continuing Analysis](#continuing-analysis) · [Numerical and Categorical Analysis](#numerical-and-categorical-analysis) · [Visualizations](#visualizations)

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

With over 113,000 non-null entries across 53 columns, this dataset is substantial. This makes thorough cleaning essential to ensure it's structured, reliable, and ready for meaningful analysis.


**Initial Data Inspection:**

- Loaded stormevent_details.csv and performed exploratory checks using .head(), .info(), and .describe() to understand structure, data types, and missing values.

  
**Date Formatting:**
- Transformed BEGIN_YEARMONTH and END_YEARMONTH from numeric values into string format with a space inserted after the first four digits.
- Reordered the format from YYYY MM to MM YYYY for improved readability and alignment with conventional date formats.

  
**Date Construction:**
  - Combined BEGIN_DAY with the cleaned BEGIN_YEARMONTH to create a new begin_date column.
  - Similarly, merged END_DAY with END_YEARMONTH to form an end_date column.

    
 **These new columns provide more interpretable date strings for analysis and visualization.**

### Numerical and Categorical Analysis 

### Visualizations


