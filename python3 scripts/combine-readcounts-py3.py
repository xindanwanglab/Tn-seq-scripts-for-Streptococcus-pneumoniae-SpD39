import sys
if sys.version_info[0] < 3:
    raise Exception("Python 3 or a more recent version is required.")

import csv
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('file', nargs='+', help='tabular read counts to combine')
args = parser.parse_args()

lines = []

first = True
i = 0

# open all the files and keep the handles
for fh in args.file:
    file = open(fh, newline='')
    tsvreader = csv.reader(file, delimiter='\t')

    for row in tsvreader:

        row[4] = int(row[4])
        row[5] = int(row[5])

        if first:
            lines.append(row)

        else:
            if ( row[0] != lines[i][0] or row[1] != lines[i][1] or row[2] != lines[i][2]
                 or row[3] != lines[i][3] ):
                raise Exception('row mismatch: row %d' % (i+1))

            lines[i][4] += row[4]
            lines[i][5] += row[5]

        i += 1
        
    first = False
    i = 0

for line in lines:
    line[4] = str(line[4])
    line[5] = str(line[5])
    print('\t'.join(line))
