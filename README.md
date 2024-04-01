# Job Offers Scraper for Software Engineers in France

This project is designed to scrape job offers for Software Engineers or other Computer Science related jobs in France from the HelloWork platform in order to analyze various data about the state of the SWE French job market such as the **average salary**, the **number of offers by regions** and the **most asked hard skills**. We will analyze the data using R for insights into the current job market trends for Software Engineers.

## Overview

The project is structured into several scripts and notebooks, each handling a distinct part of the data collection, preprocessing, and analysis process:

- `scrapHardSkills.py`: Scrapes hard skills from an exhaustive GitHub repository and put them in `hardskills.csv`.
- `scrapOffersLink.py`: Uses Selenium to navigate HelloWork and collect links to individual job offers and add them to the `offresLink.json` file.
- `scrapOfferInfo.py`: Extracts detailed information from each job offer link collected by `scrapOffersLink.py` and put them in the `output_file.csv`.
- `preprocessing.ipynb`: Jupyter notebook for preprocessing the raw data scraped from HelloWork and avoid NaN or other values that could compromise the analysis. The processed values are stored in the `finalData.csv` file, that we will use for future analysis.
- `cs_job_dash.Rmd`: R Markdown document for analyzing the preprocessed data and showcasing insights.
- `hardskills.csv`, `offresLink.json`, `output_file.csv`, `finalData.csv`: Data files generated at various stages of the pipeline.

## Content of the Dashboard

The dashboard is built using `flexdashboard` with a `shiny` runtime to enable interactivity.

### Main Features

- **Interactive Map of Job Offers**: Distribution of job offers across French departments, with the ability to filter based on specific criteria.
- **Salary Insights**: Average SWE salary ranges segmented by region, sector, and experience level.
- **Skill Analysis**: Most sought-after hard skills in the market.
- **Sector and Region Comparison**: Compare the number of job offers and average salaries across different sectors and regions to pinpoint where the most lucrative opportunities lie.

### How to Navigate

Upon loading the dashboard, users are greeted with a comprehensive analysis of the subject matter, presented across various sections:
- **Presentation**: Introduces the dashboard's purpose and provides an overview of the French SWE job market.
- **Offers by Counties**: Visualizes the number of job offers available across French departments.
- **Skills Required**: Breaks down the most demanded skills in the job market, offering insights for job seekers.
- **Salaries by Region & Sector**: Showcases salary trends, allowing for a comparison across different areas and industries.

### Additional Features

- **Downloadable Scripts and Report**: Users can download the Python scripts used for data scraping and preprocessing, along with a detailed PDF report of the findings (in French).
- **Contributors**: Credits to the team behind the dashboard: EL-OTHMANI Youssef, FLANDRE Noe, MICHELIN Marc-Alexandre, RUBIO Arthur and TERRASSON Ludovic.

## Compatibility

This project has been tested on R versions 4.3.2 and 4.3.3, as well as Python version 3.8. Please ensure that you have one of these specified versions installed before running the application to ensure proper functioning of the packages.
The IDE used was RStudio version 2023.12.1+402.

## Installation

To run this project, you'll need Python, Jupyter Notebook, and R. Specific Python package dependencies.
Python dependencies include `requests`, `beautifulsoup4`, `selenium`, `pandas`, and `csv`. The project also requires a Selenium WebDriver compatible (we used Firefox in our case) with your browser for script automation.
R packages include `flexdashboard`, `leaflet`, `ggplot2`, `maps`, `readr`, `dplyr`, `ggmap`, `tmaptools`, `sf`, `tidyr`, `shiny`, `plotly`, `stringr`, `corrplot`, `randomForest`, `formattable`, and `caret`.

Please ensure to have all the Python librairies and R packages installed before running the code.

### Clone the repository on your device
    ```bash
    git clone https://github.com/arthur-ru/CS-Job-Offers-Fr.git
    ```

### Setting up a Python Environment

1. Install Python 3.8 or higher.
2. Create a virtual environment: `python -m venv venv`
3. Activate the virtual environment:
- On Windows: 
```python
venv\Scripts\activate
```
- On macOS and Linux: 
```python
source venv/bin/activate
```
4. Install the required Python packages: 
```python
pip install requests beautifulsoup4 selenium pandas
```

### Setting up R

Ensure you have R and RStudio installed. Dependencies required for the R Markdown analysis can be installed using:
```r
install.packages(c("flexdashboard", "leaflet", "ggplot2", ...))
```

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements (such as scrapping and processing data for another Computer Science job like Data Scientist), please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.