import os
import pandas as pd 
import numpy as np 
import math
import matplotlib.pyplot as plt
import argparse
import yaml
import logging


# Define command-line arguments
parser = argparse.ArgumentParser(description='Dataset analysis script')
parser.add_argument('config', type=str, help='Path to the configuration file')

# Set logging level to 'INFO' so that we know that things ran properly
logging.basicConfig(
    level=logging.INFO
    , handlers=[
        logging.StreamHandler() # to console
        , logging.FileHandler('shelter_logging.log') # to file
        ]
    )

# Parse the command-line arguments
args = parser.parse_args()

config_files = ['userconfig.yaml']
# config_files += args.config  # not sure what this does but it was messing up my code

config = {}
for this_config_file in config_files:
    with open(this_config_file, 'r') as yamlfile:
        this_config = yaml.safe_load(yamlfile)
        config.update(this_config)

# Read file from command-line 
config_data = pd.read_csv(args.config)

shelter_occupancy = config_data # this is unnecessary, I know
# '/Users/soniagrebenisan1/Desktop/personal/dsi_course/topic_2_python/data/Daily shelter overnight occupancy.csv'

# Homework 2: log that we have successfully loaded the dataset
logging.info(f"Successfully loaded shelter_occupancy") 

# Homework 2, task 1.1: adding an assertion in case the wrong size dataset is loaded
assert shelter_occupancy.shape == (27079, 32), "Please load dataset again, it is not the right size"
assert 'OCCUPANCY_DATE' in shelter_occupancy.columns, "Error loading shelter_occupancy, occupancy_date is not a column"

def lower_names(df):
    return df.lower()
shelter_occupancy = shelter_occupancy.rename(columns=lower_names)

fig, ax = plt.subplots()

# Homework 2, task 1.2 & 1.3: use try/except to make sure that the columns being used exist in the dataset
try:
    occupied_beds = ax.scatter(shelter_occupancy['occupancy_date']
                , shelter_occupancy[config['columns']['col1']]
                , c=[config['colors']['col1']]
                , marker=(5,1) # because it's cute and happy
                )
    unoccupied_beds = ax.scatter(shelter_occupancy['occupancy_date']
                , shelter_occupancy[config['columns']['col2']]
                , c=[config['colors']['col2']]
                , marker=(5,1) # and shelter data is sad
                )
except NameError as e:
    e.add_note("The column you entered is not a column in this dataset")
    raise e 

ax.set_title(config['labels']['title'])
ax.set_xlabel(config['labels']['x'])
ax.set_ylabel(config['labels']['y']) 
ax.set_axisbelow(True)
ax.grid(alpha=0.3)

plt.savefig('shelter_beds.png')
