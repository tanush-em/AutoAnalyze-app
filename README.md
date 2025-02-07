# AutoAnalyze-app

AutoAnalyze-app is a user-friendly web application built with Streamlit that automates exploratory data analysis (EDA) tasks, simplifying the process of understanding your datasets. Upload your CSV file, and the app will generate a comprehensive report, saving you valuable time and effort.

## Technology Used

- Streamlit: A Python library for creating interactive web applications quickly and efficiently.
- Pandas: A powerful Python library for data manipulation and analysis.
- ydata-profiling: A Python library for creating detailed profiles of your data, offering a rich set of visualizations beyond basic summary statistics.
- streamlit-pandas-profiling: A Streamlit component that integrates ydata-profiling's reports seamlessly into your Streamlit app. 

## Setup Locally

1. Install Dependencies:

<code>pip install -r requirements.txt</code>
Use code with caution.

2. Run the App:

<code>streamlit run app.py</code>
This will launch the AutoAnalyze-app in your web browser, typically at http://localhost:8501.

## Usage

- Upload your dataset: Click the "Upload your Dataset" button. Select a CSV file from your local machine.
- Analyze data: After successful upload, click the "Analyze Data" button.
- Explore the report: The app will generate a detailed report, including:
    - Basic summary statistics
    - Data type information 
    - Missing value counts
    - Descriptive statistics
    - Distribution visualizations 
    - Correlations
Use the scrollbar to navigate through the report.

## Issues and Improvements
1. Extending support for other dataset formats such as excel, json etc.
2. Dowloading the final EDA Report

## Contact
Any contributions are highly appreciable.
Feel free to reach out to me with any questions or feedback: 
- Email - [Gmail](tanushtm.work@gmail.com)
