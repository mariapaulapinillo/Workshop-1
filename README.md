# Workshop-1
This project implements a full ETL pipeline for candidate evaluation data.
The pipeline follows a Data Warehouse star schema and includes:

Extraction from CSV files.

Transformation into dimension and fact tables.

Loading into a SQLite database.

KPI calculation through SQL queries.

Visualization dashboard built with Plotly Dash.

The goal is to provide actionable insights about candidate hiring trends, experience, and performance.
------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Architecture
🔹 ETL Process

Extraction: Reads candidate data from CSV.

Transformation: Builds dimension tables (dim_candidates, dim_country, dim_tech, dim_seniority, dim_date) and a fact table (fact_candidates).

Loading: Stores data in a SQLite database.

🔹 Star Schema
<img width="1176" height="745" alt="image" src="https://github.com/user-attachments/assets/a86398ac-ed27-44da-8ed6-a96953b308db" />

----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# KPIs

The following KPIs were defined to analyze hiring trends:

Hires by Technology – Which technologies have the highest hiring rates.

Hires by Year – Yearly hiring trends.

Hires by Seniority – Distribution of hires across seniority levels.

Hires by Country Over Time – Country-specific hiring evolution.

Hires by Experience Range – Hiring distribution by years of experience.

Average Scores – Mean values for code challenge and technical interview performance.
---------------------------------------------------------------------------------------------------------------------------------------------------------------------
 # Dashboard

The interactive dashboard was built with Plotly Dash.
<img width="1848" height="592" alt="image" src="https://github.com/user-attachments/assets/3fab12de-cae6-49c6-9e3b-0fffe00f35d1" />
<img width="1845" height="603" alt="image" src="https://github.com/user-attachments/assets/4949c55e-6feb-48b8-b115-b86e9632e53c" />
---------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Installation & Usage
1. Clone the repository
2. Install dependencies
3. Run the ETL process
4. Start the dashboard
5. Open the app in your browser
-------------------------------------------------------------------------------------------------------------------------------------------------------------------
Documentation
Justification of Star Schema Design: https://docs.google.com/document/d/1Qle8R9y_bgkX_HvUfK1RUfNsUwhouF2ceCpxCcmFdKk/edit?usp=sharing
