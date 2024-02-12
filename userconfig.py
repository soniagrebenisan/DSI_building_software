
import argparse

parser = argparse.ArgumentParser(description='Dataset analysis script')
parser.add_argument('config', type=str, help='Path to the configuration file')
args = parser.parse_args()

# read arguments
print(args.config)