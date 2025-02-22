# Distance Classification Script 
# Import necessary libraries
import os
import pandas as pd

# Define dataset path
dataset_path = "dataset/data.csv"  # Change this to your actual dataset file

# Check if dataset exists
if os.path.exists(dataset_path):
    # Load dataset
    df = pd.read_csv(dataset_path)
    
    # Display success message
    print("✅ Dataset loaded successfully!")
    
    # Show first 5 rows
    display(df.head())  
else:
    print("❌ Dataset file not found. Please check the path.")
