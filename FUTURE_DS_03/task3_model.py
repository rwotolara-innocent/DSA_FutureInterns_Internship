# Import necessary libraries
import pandas as pd  # Import pandas for data manipulation
import seaborn as sns  # Import seaborn for advanced visualizations
import matplotlib.pyplot as plt  # Import matplotlib for plotting
import numpy as np  # Import numpy for numerical operations

# Mount Google Drive to access files
from google.colab import drive
drive.mount('/content/drive')  # Connects Colab to your Google Drive

# Define the file path for the dataset
file_path = 'student_feedback.csv'  # Path to the dataset in Google Drive

# Load the dataset into a pandas DataFrame
df = pd.read_csv(file_path)  # Reads the CSV file into a DataFrame

# Data cleaning
# Get all columns except 'Student ID' for rating analysis
rating_columns = df.columns[1:]
for col in rating_columns:  # Loop through each rating column
    df[col] = pd.to_numeric(df[col], errors='coerce')  # Convert to numeric, handle errors
    df[col] = df[col].fillna(df[col].mean())  # Fill missing values with column mean

# Calculate average ratings for each aspect
# Select all aspect columns except 'Course recommendation'
aspect_columns = df.columns[1:-1]
avg_ratings = df[aspect_columns].mean()  # Compute mean rating for each aspect

# Calculate overall rating per course and identify top/bottom performers
df['Overall Rating'] = df[aspect_columns].mean(axis=1)  # Average across rows for overall rating
top_courses = df.nlargest(3, 'Overall Rating')['Student ID']  # Get top 3 Student IDs
bottom_courses = df.nsmallest(3, 'Overall Rating')['Student ID']  # Get bottom 3 Student IDs

# Find correlations between aspects
correlation_matrix = df[aspect_columns].corr()  # Compute correlation matrix

# Print insights
print("College Course Feedback Insights:")  # Header for output
print(f"Average Ratings per Aspect:{avg_ratings}")  # Display average ratings
print(f"Top 3 Courses by Overall Rating (Student IDs): {', '.join(map(str, top_courses))}")  # Show top courses
print(f"Bottom 3 Courses by Overall Rating (Student IDs): {', '.join(map(str, bottom_courses))}")  # Show bottom courses
print(f"Correlation Matrix:{correlation_matrix}")  # Display correlation matrix

# Save processed data
df.to_csv('/content/drive/MyDrive/processed_course_feedback.csv', index=False)  # Save DataFrame to CSV

# Visualizations
# Bar Chart: Average Ratings per Aspect
plt.figure(figsize=(12, 6))  # Set figure size
avg_ratings.plot(kind='bar', color='skyblue')  # Create bar plot
plt.title('Average Ratings per Course Aspect')  # Set title
plt.xlabel('Aspect')  # Label x-axis
plt.ylabel('Average Rating (1-10)')  # Label y-axis
plt.xticks(rotation=45, ha='right')  # Rotate x-labels for readability
plt.tight_layout()  # Adjust layout
plt.savefig('/content/drive/MyDrive/avg_ratings_bar.png')  # Save plot
plt.close()  # Close figure

# Heatmap: Correlations between Aspects
plt.figure(figsize=(10, 8))  # Set figure size
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1)  # Create heatmap
plt.title('Correlation Between Course Aspects')  # Set title
plt.tight_layout()  # Adjust layout
plt.savefig('/content/drive/MyDrive/correlation_heatmap.png')  # Save plot
plt.close()  # Close figure

# Scatter Plot: Subject Knowledge vs. Explanation Clarity
plt.figure(figsize=(8, 6))  # Set figure size
sns.scatterplot(x='Well versed with the subject', y='Explains concepts in an understandable way', data=df, hue='Overall Rating', palette='viridis')  # Create scatter plot
plt.title('Subject Knowledge vs. Explanation Clarity')  # Set title
plt.xlabel('Well versed with the subject (1-10)')  # Label x-axis
plt.ylabel('Explains concepts in an understandable way (1-10)')  # Label y-axis
plt.tight_layout()  # Adjust layout
plt.savefig('/content/drive/MyDrive/scatter_subject_explanation.png')  # Save plot
plt.close()  # Close figure

print("Files saved: processed_course_feedback.csv, avg_ratings_bar.png, correlation_heatmap.png, scatter_subject_explanation.png")  # Confirm saved files
