import os
import pandas as pd 
import numpy as np 
import math
import matplotlib.pyplot as plt
import argparse

# Define command-line arguments
parser = argparse.ArgumentParser(description='Dataset analysis script')
parser.add_argument('config', type=str, help='Path to the configuration file')
parser.add_argument('column1', type=str, help='First column you want to plot')
parser.add_argument('column2', type=str, help='Second column you want to plot')

# Parse the command-line arguments
args = parser.parse_args()

# Print the path to the configuration file
print(args.config)

# Read job-specific configuration file 
config_data = pd.read_csv(args.config)

shelter_occupancy = config_data
# shelter_occupancy = pd.read_csv('/Users/soniagrebenisan1/Desktop/personal/dsi_course/topic_2_python/data/Daily shelter overnight occupancy.csv')

def lower_names(df):
    return df.lower()
shelter_occupancy = shelter_occupancy.rename(columns=lower_names)

fig, ax = plt.subplots()

occupied_beds = ax.scatter(shelter_occupancy['occupancy_date']
            # , shelter_occupancy['occupied_beds']  # original
            , shelter_occupancy[args.column1]
            # , c=['tab:blue']  # original
            , c=['tab:blue']
            , marker=(5,1) # because it's cute and happy
            )
unoccupied_beds = ax.scatter(shelter_occupancy['occupancy_date']
            # , shelter_occupancy['unoccupied_beds']  # original
            , shelter_occupancy[args.column2]
            # , c=['tab:orange']  # original
            , c=['tab:orange']  
            , marker=(5,1) # and shelter data is sad
            )

ax.set_title('Shelter Beds - Toronto - By Date')
ax.set_xlabel('Date')
ax.set_ylabel('Beds') 
ax.set_axisbelow(True)
ax.grid(alpha=0.3)
ax.legend([unoccupied_beds, occupied_beds]
          , ['Unoccupied Beds', 'Occupied Beds']
          , bbox_to_anchor=(1, 1)
          , loc='upper left')

plt.savefig('shelter_beds.png')