# Data Science PPTS - Bike Race Analysis Project

This repository contains course materials for Data Science (PowerPoint presentations converted to markdown) and a complete bike race data analysis project.

## Course Materials

The `docs/slides_as_text/` directory contains markdown versions of the course PowerPoint presentations covering topics such as:
- Introduction to Data Science
- Setting up your working environment
- Advanced Python programming
- Regular expressions and web scraping
- NumPy, Matplotlib, and Pandas

## Bike Race Analysis Project

The `bike_race_analysis/` directory contains a complete data science project analyzing multi-stage bicycle races, including the Tour de France.

### Project Structure

```
bike_race_analysis/
├── 01_web_scraping.ipynb      # Web scraping notebook
├── 02_data_cleaning.ipynb     # Data cleaning notebook
├── 03_data_analysis.ipynb     # Data analysis and visualization notebook
└── data/
    ├── raw/                   # Raw scraped data (CSV/JSON)
    └── cleaned/               # Cleaned processed data
```

### Notebooks

1. **01_web_scraping.ipynb**
   - Scrapes data from the Tour de France GitHub dataset
   - Collects complementary data from Wikipedia on bicycle races
   - Outputs raw data to CSV/JSON files
   - Uses `requests` and `BeautifulSoup`

2. **02_data_cleaning.ipynb**
   - Standardizes names, dates, and times
   - Handles missing data through imputation or dropping records
   - Converts relative times (e.g., "+05:30") to absolute timestamps
   - Outputs cleaned data ready for analysis

3. **03_data_analysis.ipynb**
   - Analyzes distance and stage statistics
   - Examines team dynamics over seasons
   - Compares stage distances across tours
   - Visualizes trends and patterns using Matplotlib
   - Uses NumPy for data manipulation

### Requirements

Install the required dependencies:

```bash
pip install -r requirements.txt
```

### Running the Project

1. Start with `01_web_scraping.ipynb` to collect the data
2. Run `02_data_cleaning.ipynb` to clean and prepare the data
3. Finally, execute `03_data_analysis.ipynb` to analyze and visualize results

All notebooks are designed to run cleanly from top to bottom in JupyterLab.

## License

This project is for educational purposes as part of a Data Science course.
