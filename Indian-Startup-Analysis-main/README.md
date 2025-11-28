# Indian Startup Analysis

## Overview

This application provides an interactive analysis of Indian startups using Streamlit and Pandas. It is designed to give insights from two primary perspectives: Company and Investor. It offers detailed visualizations and data analyses, including funding details, industry sectors, and investor activities.

## Features

### Company POV

1. **Name**: Displays the startup's name.
2. **Founders**: Lists the names of the founders.
3. **Industry**: Shows the primary industry of the startup.
4. **Subindustry**: Displays the subindustry the startup operates in.
5. **Location**: Provides the geographical location of the startup.
6. **Funding Rounds**: Lists the various funding rounds the startup has gone through.
7. **Stage**: Indicates the current stage of the startup (e.g., Seed, Series A).
8. **Investors**: Lists the investors involved in the startup.
9. **Date**: Shows the date of the latest funding round or relevant date.
10. **Similar Companies**: Suggests companies similar to the one being analyzed.

### Investor POV

1. **Name**: Displays the investor's name.
2. **Recent Investments**: Lists the latest investments made by the investor.
3. **Biggest Investments**: Highlights the largest investments made by the investor.
4. **Generally Invests In**:
   - **Sector (Pie Chart)**: Visualizes the distribution of investments by sector.
   - **Stage (Pie Chart)**: Shows the distribution of investments by startup stage.
   - **City (Pie Chart)**: Represents the distribution of investments by city.
5. **YoY Investment Graph**: Graphs the year-over-year investment trends of the investor.
6. **Similar Investors**: Recommends investors with similar investment patterns.

### General Analysis

1. **MoM Chart**:
   - **Total Investments**: Displays the total investment amount month-over-month.
   - **Count**: Shows the count of investments month-over-month.
2. **Cards**:
   - **Total**: Displays the total funding amount across all startups.
   - **Max**: Shows the maximum funding amount for a single startup.
   - **Avg**: Provides the average funding amount per startup.
   - **Total Funded Startups**: Displays the total number of startups funded.
3. **Sector Analysis (Pie Chart)**:
   - **Top Sectors**: Visualizes the top sectors by count and sum of investments.
4. **Type of Funding**: Analyzes the distribution of different types of funding received by startups.
5. **City Wise Funding**: Shows the distribution of funding across different cities.
6. **Top Startups**:
   - **Year-Wise**: Lists the top startups for each year.
   - **Overall**: Provides an overall ranking of top startups.
7. **Top Investors**: Lists the top investors based on various criteria.

## Installation

To run this application locally, you need to have Python and the necessary libraries installed. Follow these steps to set up:

1. **Clone the Repository**:

    ```bash
    git clone https://github.com/Panchalparth471/Indian-Startup-Analysis.git
    cd Indian-Startup-Analysis
    ```

2. **Create a Virtual Environment (Optional but recommended)**:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install Required Libraries**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Run the Streamlit Application**:

    ```bash
    streamlit run app.py
    ```

## Data Sources

This application uses publicly available data sources and APIs to gather information about Indian startups and investors. Ensure that you have access to the data sources mentioned in the application configuration.

## Configuration

Configure the application by editing the `config.py` file to include your data sources and API keys if required.

## Usage

After running the application, navigate to the provided URL (usually `http://localhost:8501`) in your web browser. Use the sidebar to select different analysis perspectives and explore the data.

## Contributing

If you would like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For any questions or support, please contact [panchalparth471@gmail.com](mailto:panchalparth471@example.com).
