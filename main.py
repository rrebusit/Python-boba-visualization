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

#Remove the column *Unnamed: 0*
del boba['Unnamed: 0']
boba.info()

#Renaming *id* column to *shop* to make it clear it is the shop name
boba.rename(columns={"id": "shop"}, inplace=True)
boba.info()

#Looking at the count of unique values of boba shops
unique_count = boba["shop"].nunique()
print(unique_count)
unique = boba["shop"].unique()
print(unique)


#Looking at distribution of *rating* on *shop*
sns.barplot(x="shop", y="rating", data=boba)
plt.title("Bar Plot")
plt.show()