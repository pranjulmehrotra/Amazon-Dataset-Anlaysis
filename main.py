import pandas as pd
import os

# Set the path to the folder containing the data sets
data_folder = 'C:\Users\DELL\Desktop\AMAZON DATA SET'

# Initialize an empty list to store the data frames
data_frames = []

# Iterate through each file in the folder
for filename in os.listdir(data_folder):
    if filename.endswith('.csv'):  # Adjust the file extension if necessary
        file_path = os.path.join(data_folder, filename)
        
        # Read the data set into a pandas DataFrame
        df = pd.read_csv(file_path)
        
        # Perform your analysis on the individual data set here
        # ...
        
        # Add the DataFrame to the list
        data_frames.append(df)

# Combine all data frames into a single DataFrame
combined_df = pd.concat(data_frames)

# Generate the final report
# ...

# Save the combined DataFrame and the report
combined_df.to_csv('/path/to/save/combined_data.csv', index=False)
# save the report using appropriate method

print("Analysis and report generation completed.")
