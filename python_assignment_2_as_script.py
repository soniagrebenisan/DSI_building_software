import os
import pandas as pd 
import numpy as np 
import math
import matplotlib.pyplot as plt
import argparse
import yaml


# Define command-line arguments
parser = argparse.ArgumentParser(description='Dataset analysis script')
parser.add_argument('config', type=str, help='Path to the configuration file')
# parser.add_argument('--title', '-t', type=str, help='Plot title')
# parser.add_argument('--output_file', '-o', type=str, help='Output plot filename')
########## parser.add_argument('column1', type=str, help='First column you want to plot')
########## parser.add_argument('column2', type=str, help='Second column you want to plot')

# Parse the command-line arguments
args = parser.parse_args()

# Print the path to the configuration file
# print(args.config)

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

def lower_names(df):
    return df.lower()
shelter_occupancy = shelter_occupancy.rename(columns=lower_names)

fig, ax = plt.subplots()

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

ax.set_title(config['labels']['title'])
ax.set_xlabel(config['labels']['x'])
ax.set_ylabel(config['labels']['y']) 
ax.set_axisbelow(True)
ax.grid(alpha=0.3)
# ax.legend([unoccupied_beds, occupied_beds]
#           , ['Unoccupied Beds', 'Occupied Beds']
#           , bbox_to_anchor=(1, 1)
#           , loc='upper left')

plt.savefig('shelter_beds.png')