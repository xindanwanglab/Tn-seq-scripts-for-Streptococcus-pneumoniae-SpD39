import csv
import argparse

import sys
if sys.version_info[0] < 3:
    raise Exception("Python 3 or a more recent version is required.")

parser = argparse.ArgumentParser()
parser.add_argument('file', help='tabular file to parse')
parser.add_argument('multiplier', type=float, help='number use to scale columns 5 and 6')
args = parser.parse_args()

with open(args.file, newline='') as file:
    tsvreader = csv.reader(file, delimiter='\t')
    for row in tsvreader:
        # multiply by our multiplier and then round to zero decimal places
        row[4] = str(round(float(row[4]) * args.multiplier))
        row[5] = str(round(float(row[5]) * args.multiplier))
        print('\t'.join(row))
