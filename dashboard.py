import pandas as pd
import matplotlib.pyplot as plt

# 1. Load the data using semicolon separator AND converting commas to decimal points
df = pd.read_csv('data/AirQualityUCI.csv', sep=';', decimal=',')

# 2. Clean the data
# Now that 'T' is read as actual numbers, this math comparison will work perfectly!
df = df[df['T'] > -100]  

# Drop any completely blank rows
df = df.dropna(subset=['Date', 'T'])

# 3. Take a small subset so the graph looks clean
df_subset = df.head(100)

# 4. Set up the X and Y axes
x_data = df_subset['Date']
y_data = df_subset['T']      

# 5. Build the graph
plt.figure(figsize=(12, 6))
plt.plot(x_data, y_data, color='darkorange', marker='o', linestyle='-', markersize=4)

# Formatting the look
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.title('Air Quality Dataset: Temperature Trends (First 100 Entries)')
plt.xticks(rotation=45) 
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout() 

# 6. Show it!
plt.show()