# this program converts an IGV file to a mapped Artemis plot for visualization
#argv[1] = the TAmap input file from after mapping and normalization of reads

import sys
if sys.version_info[0] < 3:
    raise Exception("Python 3 or a more recent version is required.")

TA={}

for line in open(sys.argv[1]):
    split=line.split()
    TAsite=int(split[3])
    F = int(split[5])
    R = int(split[6])/-1
    TA[TAsite]=[F,R]

# converted to python3 sort
TA_keys = sorted(TA)
#TA_keys =TA.keys()
#TA_keys.sort()

print("%s\t%s\t%s" % ("#BASE","Finsert","Rinsert"))
print("%s\t%s\t%s" % ("colour","5:150:55","225:0:0"))
for i in TA_keys:
    print("%d\t%d\t%d" % (i,TA[i][0],TA[i][1]))
