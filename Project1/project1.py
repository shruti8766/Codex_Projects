import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Create sample data
data_dict = {
    'column_name': [10, 20, 30, 40, 50],
    'another_column': [5, 4, 3, 2, 1]
}
df = pd.DataFrame(data_dict)
df.to_csv('data.csv', index=False)
print("Sample data.csv file created!")

# Load and analyze
data = pd.read_csv('data.csv')
print("First 5 rows:")
print(data.head())
print("Average of column_name:", data['column_name'].mean())

# Visualizations
plt.hist(data['column_name'])
plt.xlabel('column_name')
plt.ylabel('Frequency')
plt.title('Histogram of column_name')
plt.show()

plt.scatter(data['column_name'], data['another_column'])
plt.xlabel('column_name')
plt.ylabel('another_column')
plt.title('Scatter plot')
plt.show()

corr = data.corr()
sns.heatmap(corr, annot=True)
plt.title('Correlation Heatmap')
plt.show()

# Provide insights (example)
print("Insights: The data shows a negative correlation between columns, as seen in the heatmap and scatter plot.")