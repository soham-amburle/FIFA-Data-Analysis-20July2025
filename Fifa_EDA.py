# 📦 Importing required libraries
import pandas as pd                      # For data manipulation
import numpy as np                       # For numerical operations
from matplotlib import pyplot as plt     # For plotting bar charts
import seaborn as sns                    # For advanced visualization (not used yet)

# 📁 Reading the dataset
fifa = pd.read_csv('fifa data.csv')

# 👀 Previewing the first 5 rows of the dataset
print(fifa.head())

# 🧾 Printing the entire dataset (can be very large — be careful!)
print(fifa)

# 🏷️ Printing all column names
for col in fifa.columns:
    print(col)

# 📐 Checking the shape of the dataset (rows, columns)
print(fifa.shape)

# 📊 Counting players by nationality
print(fifa['nationality'].value_counts())

# 📈 Plotting a bar chart of the top 10 nationalities
plt.figure(figsize=(7, 7))
plt.bar(
    list(fifa['nationality'].value_counts()[0:10].keys()),     # Top 10 countries
    list(fifa['nationality'].value_counts()[0:10]),            # Their player counts
    color=['pink']                                             # All bars are pink
)
plt.show()

# 💸 Creating a DataFrame with player names and wages
player_salary = fifa[['short_name', 'wage_eur']]
print(player_salary.head())

# 💰 Sorting players by wage in descending order
player_salary = player_salary.sort_values(by=['wage_eur'], ascending=False)
print(player_salary.head())

# 🧮 Filtering players who earn more than €400,000
high_earners = player_salary[player_salary['wage_eur'] > 400000]
print(high_earners.head())

# 📊 Bar chart of top 5 highest-paid players
plt.figure(figsize=(8, 5))
plt.bar(
    list(player_salary['short_name'])[0:5],
    list(player_salary['wage_eur'])[0:5],
    color=["magenta", "green", "red", "pink", "orange"]
)
plt.show()

# 🧾 Displaying the top 3 highest-paid players
print(player_salary[0:3])

# 🔤 Printing all player names
print(fifa[['short_name']])

# ✅ Boolean Series: Is nationality Germany?
print(fifa['nationality'] == 'Germany')

# 🇩🇪 Creating a DataFrame of German players
Germany = fifa[fifa['nationality'] == 'Germany']
print(Germany.head(10))

# 📏 Tallest German players
print(Germany.sort_values(by=['height_cm'], ascending=False).head())

# 🔁 Printing all column names again
for col in fifa.columns:
    print(col)

# 🔤 Iterating over characters in a string (not ideal for countries)
for name in 'Germany and Austria':
    print(name)

# 🧍 Looping through a list of footballers
for list_of_names in ['Ronaldo', 'Messi', 'Pele']:
    print(list_of_names)

# 🔁 Looping through dictionary keys
for dict in {'a': 1, 'b': 2}:
    print(dict)

# ⚖️ Heaviest German players
print(Germany.sort_values(by=['weight_kg'], ascending=False).head())

# 🇩🇪 Top 5 richest German players
print(
    Germany[['short_name', 'wage_eur']]
    .sort_values(by=['wage_eur'], ascending=False)
    .head()
)

# 🧮 Checking if Messi exists as Argentine
print(
    np.sum(
        (fifa['nationality'] == 'Argentina') &
        (fifa['short_name'] == 'L. Messi')
    )
)

# 🧮 Argentinian players who are NOT Messi
print(
    np.sum(
        (fifa['nationality'] == 'Argentina') &
        (fifa['short_name'] != 'L. Messi')
    )
)

# 🧮 Messi listed with non-Argentina nationality
print(
    np.sum(
        (fifa['nationality'] != 'Argentina') &
        (fifa['short_name'] == 'L. Messi')
    )
)

# 🌎 Number of unique nationalities
print(len(fifa['nationality'].unique()))

# 💶 Again showing Germany's top earners
print(
    Germany[['short_name', 'wage_eur']]
    .sort_values(by=['wage_eur'], ascending=False)
    .head()
)

# 🔄 Convert top 5 German earners to NumPy array (preferred way)
print(
    Germany[['short_name', 'wage_eur']]
    .sort_values(by=['wage_eur'], ascending=False)
    .head()
    .to_numpy()
)

# 🔄 Same as above but with older `.values` method
print(
    Germany[['short_name', 'wage_eur']]
    .sort_values(by=['wage_eur'], ascending=False)
    .head()
    .values
)

# 📏 Sorting German players by height
print(
    Germany.sort_values(by=['height_cm'], ascending=False).head()
)

# 💶 Again showing Germany’s wage-based top 5
print(
    Germany[['short_name','wage_eur']]
    .sort_values(by=['wage_eur'], ascending=False)
    .head()
)

# 🎯 Creating DataFrame with shooting skill
player_shooting = fifa[['short_name', 'shooting']]
print(player_shooting)

# 🔫 Top 5 players by shooting skill
print(player_shooting.sort_values(by=['shooting'], ascending=False).head())

# 🛡️ Creating DataFrame with defending skill
player_defending = fifa[['short_name', 'defending', 'nationality', 'club']]

# 🛡️ Top 5 defenders
print(player_defending.sort_values(by=['defending'], ascending=False).head())

# ⚪ Creating DataFrame for Real Madrid players
real_madrid = fifa[fifa['club'] == 'Real Madrid']

# 💸 Top 5 Real Madrid players by wage
print(real_madrid.sort_values(by=['wage_eur'], ascending=False).head())

# 🔫 Top 5 Real Madrid players by shooting
print(real_madrid.sort_values(by=['shooting'], ascending=False).head())

# 🛡️ Top 5 Real Madrid players by defending
print(real_madrid.sort_values(by=['defending'], ascending=False).head())

# 🌍 Most common nationalities in Real Madrid (top 2)
print(real_madrid['nationality'].value_counts()[0:2])
