# Import pandas library and alias it as 'pd' for data manipulation
import pandas as pd

# Import sys module (commonly used for command-line arguments or system interaction)
import sys

# Import yaml module to read configuration files written in YAML format
import yaml

# Import os module to interact with the operating system (paths, directories, etc.)
import os


# ------------------------------------------------------------
# Load parameters from params.yaml file
# ------------------------------------------------------------

# Open 'params.yaml', safely load its contents as a Python dictionary,
# and extract the 'preprocess' section from it
params = yaml.safe_load(open("params.yaml"))['preprocess']


# ------------------------------------------------------------
# Preprocessing function definition
# ------------------------------------------------------------

def preprocess(input_path, output_path):
    # Read the input CSV file from the given input path into a pandas DataFrame
    data = pd.read_csv(input_path)
    
    # Create the output directory if it does not already exist
    # os.path.dirname extracts the directory part of the output path
    # exist_ok=True prevents errors if the directory already exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    # Save the processed data to the output path as a CSV file
    # header=None removes column headers
    # index=False prevents writing row indices to the file
    data.to_csv(output_path, header=None, index=False)
    
    # Print a confirmation message indicating where the processed data was saved
    print(f"Preprocessed data saved to {output_path}")


# ------------------------------------------------------------
# Script entry point
# ------------------------------------------------------------

# This condition ensures the preprocess function runs only
# when this script is executed directly (not imported as a module)
if __name__ == "__main__":
    
    # Call the preprocess function using input and output paths
    # defined in the params.yaml file
    preprocess(params["input"], params["output"])