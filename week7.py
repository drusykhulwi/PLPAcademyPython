import pandas as pd
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
import seaborn as sns

# Load the Iris dataset
iris = load_iris()
iris_df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
iris_df['species'] = iris.target

# Map species numbers to names
species_map = {i: species for i, species in enumerate(iris.target_names)}
iris_df['species'] = iris_df['species'].map(species_map)

# Check the data types and any missing values
print(iris_df.info())
print(iris_df.isnull().sum())

df = iris_df.dropna()  # Example of dropping missing values

# Compute basic statistics of numerical columns
print(iris_df.describe())
# Compute the mean of each numerical column grouped by species
grouped_means = iris_df.groupby('species').mean()
print(grouped_means)

# Line chart for Sepal Length
plt.figure(figsize=(10, 6))
sns.lineplot(data=iris_df, x=iris_df.index, y='sepal length (cm)', hue='species')
plt.title('Sepal Length Over Index')
plt.xlabel('Index')
plt.ylabel('Sepal Length (cm)')
plt.legend(title='Species')
plt.show()

# Bar chart showing the average petal length per species
plt.figure(figsize=(10, 6))
sns.barplot(x='species', y='petal length (cm)', data=iris_df)
plt.title('Average Petal Length per Species')
plt.xlabel('Species')
plt.ylabel('Petal Length (cm)')
plt.show()

# Histogram of Sepal Length
plt.figure(figsize=(10, 6))
sns.histplot(iris_df['sepal length (cm)'], kde=True)
plt.title('Distribution of Sepal Length')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Frequency')
plt.show()

# Scatter plot to visualize the relationship between Sepal Length and Petal Length
plt.figure(figsize=(10, 6))
sns.scatterplot(x='sepal length (cm)', y='petal length (cm)', hue='species', data=iris_df)
plt.title('Sepal Length vs. Petal Length')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Petal Length (cm)')
plt.legend(title='Species')
plt.show()
