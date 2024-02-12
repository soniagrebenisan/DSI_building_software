
import argparse
import yaml
from pprint import pprint

# Define command-line arguments
parser = argparse.ArgumentParser(description='Dataset analysis script')
parser.add_argument('config', type=str, help='Path to the configuration file')
parser.add_argument('column1', type=str, help='First column you want to plot')
parser.add_argument('column2', type=str, help='Second column you want to plot')

# Parse the command-line arguments
args = parser.parse_args()

# Load and parse job-specific and user configuration files
config_paths = ['user_config.yml']
config_paths += args.config

config = {}
for path in config_paths:
    with open(path, 'r') as f:
        this_config = yaml.safe_load(f)
        config.update(this_config)

# Access command-line arguments and configuration settings
column1 = args.column1
column2 = args.column2

# Print configuration settings
print("Configuration settings:")
print(config)
print("Column 1:", column1)
print("Column 2:", column2)