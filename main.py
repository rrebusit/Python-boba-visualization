import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

boba = pd.read_csv("bayarea_boba_spots.csv")
#Look at the first 5 rows
boba.head()

#Look at how many rows and how many columns
boba.shape

#Look at variable types
boba.info()

#In this analysis I will be removing the columns *Unnamed: 0*, *id*, *lat*, *long* 
columns_delete = ["Unnamed: 0", "id", "lat", "long"]
boba.drop(columns=columns_delete, inplace=True)
boba.info()

#Looking at the unique cities
cities = boba["city"].unique()
print(cities)
cities_count = boba["city"].nunique()
print(cities_count)

#Looking at the count of unique values of boba shops
unique_count = boba["name"].nunique()
print(unique_count)
unique = boba["name"].unique()
print(unique)

#I can see that shops "T4 Tea" and "T4" are the same so let's make it have a uniform name
boba["name"] = boba["name"].replace("T4", 'T4 Tea')

#Visualize the number of boba shops in each city
#Getting the count of each city
shop_count = boba.groupby("city")["name"].count().reset_index(name="count")
print(shop_count)

#Looking at distribution of shops in each city
plt.figure(figsize=(10, 14))
sns.barplot(x="count", y="city", data=shop_count, orient="h")
plt.title("Number of Boba Shops in Each City")
plt.show()

SF = "San Francisco"
SF_rating = boba[boba['city'] == SF]
SF_rating.head()
SF_rating.shape

# %%
plt.figure(figsize=(8, 10))
rate = sns.barplot(x="rating", y="name", data=SF_rating, orient="h")
for p in rate.patches:
    rating = p.get_width()
    name = p.get_y() + p.get_height() / 2 
    rate.annotate(f'{rating:.2f}', xy=(rating, name), xytext=(5, 0), textcoords='offset points', va='center')
plt.title("Ratings of Boba Shops in San Francisco")
plt.show()
#Puppy Bobar is the best rated in San Francisco with 5 stars