import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

boba = pd.read_csv("bayarea_boba_spots.csv")

'''
Look at the first 5 rows
'''
boba.head()

'''
Look at how many rows and how many columns
'''
boba.shape

'''
Look at variable types
'''
boba.info()

'''
In this analysis I will be removing the columns *Unnamed: 0*, *id*, *lat*, *long* 
'''
columns_delete = ["Unnamed: 0", "id", "lat", "long"]
boba.drop(columns=columns_delete, inplace=True)
boba.info()

'''
Looking at the unique cities
'''
cities = boba["city"].unique()
print(cities)
cities_count = boba["city"].nunique()
print(cities_count)

'''
Looking at the count of unique values of boba shops
'''
unique_count = boba["name"].nunique()
print(unique_count)
unique = boba["name"].unique()
print(unique)

'''
I can see that shops "T4 Tea" and "T4" are the same so let's make it have a uniform name
'''
boba["name"] = boba["name"].replace("T4", 'T4 Tea')

'''
Visualize the number of boba shops in each city
'''
'''
Getting the count of shops in each city
'''
shop_count = boba.groupby("city")["name"].count().reset_index(name="count")
print(shop_count)

'''
Looking at distribution of shops in each city (San Francisco has the most)
'''
plt.figure(figsize=(10, 14))
sns.barplot(x="count", y="city", data=shop_count, orient="h")
plt.title("Number of Boba Shops in Each City")
plt.show()

'''
Looking at San Francisco
'''
SF = "San Francisco"
SF_rating = boba[boba["city"] == SF]
SF_rating.head()
SF_rating.info()
SF_rating.shape

'''
Creating barplot to visualize the ratings of boba shops in San Francisco
'''
plt.figure(figsize=(8, 10))
rate = sns.barplot(x="rating", y="name", data=SF_rating, orient="h")
for p in rate.patches:
    rating = p.get_width()
    name = p.get_y() + p.get_height() / 2 
    rate.annotate(f'{rating:.2f}', xy=(rating, name), xytext=(5, 0), textcoords='offset points', va='center')
plt.title("Ratings of Boba Shops in San Francisco")
plt.show()
'''
Puppy Bobar is the best rated in San Francisco with 5 stars)
'''

'''
Next let's visualize which boba shop in the bay has the max ratings
'''
max_ratings = boba.groupby('name')[['rating', 'city']].max().reset_index()
top_ten = max_ratings.nlargest(10, 'rating')

plt.figure(figsize=(8, 10))
ten = sns.barplot(x="rating", y="name", hue="city", data=top_ten, orient="h")
for p in ten.patches:
    rating = p.get_width()
    name = p.get_y() + p.get_height() / 2 
    city_match = top_ten.loc[top_ten['name'] == p.get_y(), 'city'].values
if city_match:
    city = city_match[0]
    ten.annotate(f'{city} - {rating:.2f}', xy=(rating, name), xytext=(5, 0), textcoords='offset points', va='center')

plt.title("Top 10 Boba Shops in the Bay Area")
plt.show()

'''
Now let's visualize which boba shops have the minimum ratings
'''
min = boba.groupby('name')[['rating', 'city']].max().reset_index()
min_ten = min.sort_values(by='rating', ascending=True)
bottom = min_ten.head(10)

plt.figure(figsize=(8, 10))
ten = sns.barplot(x="rating", y="name", hue="city", data=bottom, orient="h") 
for p in ten.patches:
    rating = p.get_width()
    name = p.get_y() + p.get_height() / 2 
    city_matches = bottom.loc[bottom['name'] == p.get_y()]
    if not city_matches.empty: 
        city = city_matches['city'].values[0]
        ten.annotate(f'{city} - {rating:.2f}', xy=(rating, name), xytext=(5, 0), textcoords='offset points', va='center')
        
plt.title("Bottom 10 Boba Shops in the Bay Area")
plt.show()

'''
This ends the data visulization of boba shops in the Bay Area
'''

