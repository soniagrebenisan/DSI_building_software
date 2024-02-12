import os
import pandas as pd 
import numpy as np 
import math
import matplotlib.pyplot as plt

shelter_occupancy = pd.read_csv('/Users/soniagrebenisan1/Desktop/personal/dsi_course/topic_2_python/data/Daily shelter overnight occupancy.csv')
shelter_occupancy.info()
shelter_occupancy.shape

def lower_names(df):
    return df.lower()
shelter_occupancy = shelter_occupancy.rename(columns=lower_names)
shelter_occupancy[['organization_id', 'shelter_id', 'location_id', 'program_id']] = shelter_occupancy[['organization_id', 'shelter_id', 'location_id', 'program_id']].astype('string')
shelter_occupancy['occupancy_date'] = pd.to_datetime(shelter_occupancy['occupancy_date'])
shelter_occupancy['funding_utilization'] = shelter_occupancy['capacity_actual_bed'] / shelter_occupancy['capacity_funding_bed']

fig, ax = plt.subplots()

occupied_beds = ax.scatter(shelter_occupancy['occupancy_date']
            , shelter_occupancy['occupied_beds']
            , c=['tab:blue']
            , marker=(5,1) # because it's cute and happy
            )
unoccupied_beds = ax.scatter(shelter_occupancy['occupancy_date']
            , shelter_occupancy['unoccupied_beds']
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