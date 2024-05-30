import pandas as pd
import ipdb

# Sample data for the DataFrame
data = {
    'A': [1, 2, 3, 4],
    'B': [5, 6, 7, 8],
    'C': [9, 10, 11, 12]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Set a breakpoint using ipdb
ipdb.set_trace()

# Perform some operations on the DataFrame
df['D'] = df['A'] + df['B']
mean_a = df['A'].mean()
sum_c = df['C'].sum()

# Print the DataFrame and results
print(df)
print(f"Mean of column 'A': {mean_a}")
print(f"Sum of column 'C': {sum_c}")
