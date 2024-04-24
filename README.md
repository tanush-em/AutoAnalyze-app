# AutoAnalyze-app

## Description

AutoAnalyze-app is a user-friendly web application built with Streamlit that automates exploratory data analysis (EDA) tasks, simplifying the process of understanding your datasets. Upload your CSV file, and the app will generate a comprehensive report, saving you valuable time and effort.

## Technology Used

Streamlit: A Python library for creating interactive web applications quickly and efficiently.
Pandas: A powerful Python library for data manipulation and analysis.
ydata-profiling: A Python library for creating detailed profiles of your data, offering a rich set of visualizations beyond basic summary statistics.
streamlit-pandas-profiling: A Streamlit component that integrates ydata-profiling's reports seamlessly into your Streamlit app. 

## Setup Locally

1. Install Dependencies:

Bash
pip install -r requirements.txt
Use code with caution.

2. Run the App:
Bash
streamlit run app.py
This will launch the AutoAnalyze-app in your web browser, typically at http://localhost:8501.

Usage

- Upload your dataset:
Click the "Upload your Dataset" button.
Select a CSV file from your local machine.
- Analyze data:
After successful upload, click the "Analyze Data" button.
- Explore the report:
The app will generate a detailed report, including:
Basic summary statistics
Data type information (if using ydata-profiling)
Missing value counts
Descriptive statistics
Distribution visualizations (if using ydata-profiling)
Correlations (if using ydata-profiling)
Use the scrollbar to navigate through the report.

## Issues and Improvements

If you encounter any issues or have suggestions for improvement, please feel free to create an issue on the GitHub repository: [link to your GitHub repository]

## Contact
Feel free to reach out to me with any questions or feedback: 
Email - tanushtm.work@gmail.com
Instagram ID - _._txnush_._
