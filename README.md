20 July, 2025
# ⚽ FIFA Data Analysis with Python

This project explores player statistics from the FIFA dataset using Python. It focuses on player nationalities, wages, skills like shooting and defending, and includes a closer look at specific clubs like Real Madrid.

## 📁 Files Included

- `fifa.py` — Main Python script that performs the analysis.
- `fifa data.csv` — (Not uploaded here due to size/privacy) The dataset used for analysis.

## 🔍 What the Script Does

- Loads the dataset using Pandas
- Counts players by nationality
- Visualizes top 10 nationalities by player count
- Filters high-earning players (wage > €400,000)
- Displays top 5 earners, tallest and heaviest players by nationality (e.g., Germany)
- Ranks players by shooting and defending skills
- Analyzes Real Madrid players by wage, skills, and nationality
- Uses Matplotlib for bar charts and NumPy for filtering

## 🛠️ Tools Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn (imported but not yet used)

## 📌 How to Run

1. Make sure `fifa data.csv` is in the same folder as `fifa.py`.
2. Run the script using:
   ```bash
   python fifa.py
