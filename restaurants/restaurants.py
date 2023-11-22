# Importing necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Reading the data from csv files
cuisines = pd.read_csv("cuisines.csv")
locations = pd.read_csv("locations.csv")
ratings = pd.read_csv("ratings.csv")

# Filtering restaurants with at least 10 ratings
ratings_count = ratings.groupby('placeID').size()
valid_restaurants = ratings_count[ratings_count >= 10].index
print(valid_restaurants)

# Calculating average ratings
average_ratings = ratings[ratings['placeID'].isin(valid_restaurants)].groupby('placeID').mean()

# Sorting by rating to get the top-rated restaurant
top_rated = average_ratings.nlargest(10, 'rating').reset_index()
print(top_rated)

# Merging with locations and cuisines to get names and cuisine types
#top_rated = top_rated.merge(locations, on='placeID').merge(cuisines, on='placeID')[['placeID', 'name', 'cuisine', 'rating']]
top_rated = top_rated.merge(locations, on='placeID')
top_rated = top_rated.merge(cuisines.groupby('placeID').agg(lambda x: ', '.join(x)), on='placeID', how='left')

# Displaying the top-rated restaurant
print("Top Rated Restaurant:")
print(top_rated)

# Task: Identify the most popular cuisine type in the Top 10 best rated restaurants

# Sorting by rating to get the top 10
top_10 = average_ratings.nlargest(10, 'rating').reset_index()

# Merging with cuisines to get cuisine types
top_10_cuisines = top_10.merge(cuisines, on='placeID')

# Getting the most common cuisine in the top 10 list
popular_cuisine = top_10_cuisines['cuisine'].value_counts().idxmax()

# Displaying the most popular cuisine type
print("\nMost Popular Cuisine Type in the Top 10 List:")
print(popular_cuisine)


# Merge top_10 with locations and cuisines
top_10_with_details = top_10.merge(locations, on='placeID').merge(cuisines, on='placeID')

# Plotting the average ratings of the top 10 restaurants
plt.figure(figsize=(10, 6))
sns.barplot(data=top_10_with_details, x='name', y='rating')
plt.xticks(rotation=45)
plt.title('Average Ratings of Top 10 Restaurants')
plt.ylabel('Average Rating')
plt.xlabel('Restaurant Name')
plt.show()

# Plotting the count of each cuisine type in the top 10 list
plt.figure(figsize=(10, 6))
sns.countplot(data=top_10_with_details, x='cuisine')
plt.title('Count of Each Cuisine Type in Top 10 Restaurants')
plt.xticks(rotation=45)  # Rotate the x labels for better readability
plt.ylabel('Count')
plt.xlabel('Cuisine Type')
plt.show()
