# Top 10 Restaurants Analysis

This Python script provides an analysis of restaurant data, focusing on identifying and visualizing the top 10 rated restaurants based on customer ratings. It utilizes Pandas for data manipulation, Matplotlib, and Seaborn for data visualization.

## Features

- **Data Import**: Imports data from three CSV files: `cuisines.csv`, `locations.csv`, and `ratings.csv`.

- **Data Filtering**: Filters out restaurants with fewer than 10 ratings to focus on more reliably rated establishments.

- **Average Rating Calculation**: Calculates the average rating for each restaurant and identifies the top-rated ones.

- **Data Merging**: Merges the top-rated restaurants' data with their respective location and cuisine information.

- **Popular Cuisine Identification**: Determines the most popular cuisine type among the top 10 rated restaurants.

- **Data Visualization**:
  - **Average Ratings Plot**: Creates a bar plot showing the average ratings of the top 10 restaurants, labeled with their names.
  - **Cuisine Count Plot**: Generates a count plot depicting the distribution of cuisine types among these top restaurants.

## Usage

To run this script, ensure you have the required libraries installed:

```bash
pip install pandas matplotlib seaborn
```

Run the script in a Python environment. The script will read the data, perform analysis, and display the plots automatically.

## Data Files

- `cuisines.csv`: Contains cuisine types associated with each restaurant.
- `locations.csv`: Holds location information for each restaurant.
- `ratings.csv`: Includes customer ratings for restaurants.

## Output

The script outputs the following:

- A list of valid restaurants (based on the rating count filter).
- A DataFrame showing the top-rated restaurants with their names and average ratings.
- The most popular cuisine type in the top 10 rated restaurants.
- Visual plots for a clear and intuitive understanding of the data.
