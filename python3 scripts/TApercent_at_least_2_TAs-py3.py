#argv[1] = igv input file from after mapping and normalization of reads

import sys
if sys.version_info[0] < 3:
    raise Exception("Python 3 or a more recent version is required.")

TA = 0; Reads = 0; HitSites = 0
readcounts = []

for line in open(sys.argv[1]):
    split=line.split()
    if split[5].isdigit() == True:
        readcounts.append(int(split[5])+int(split[6])) ## record read counts in list
        TA += 1
        Reads += int(split[5])+int(split[6])
        if (int(split[5])+int(split[6])) > 1: HitSites += 1

#### GETTING QUARTILE NUMBERS
        
##readcounts.sort()
##
##print readcounts[0]
##print readcounts[int(0.25*len(readcounts))]
##print readcounts[int(0.5*len(readcounts))]
##print readcounts[int(0.75*len(readcounts))]
##print readcounts[len(readcounts)-1]

Percent = int(((float(HitSites)/int(TA)) * 100) + 0.5)

print('TA = %d' % (TA))
print('Reads = %d' % (Reads))
print('Sites Hit = %d' % (HitSites))
print('Percent TAs hit = %d' % (Percent))
print('Average Read Count = %d' % (float(sum(readcounts))/float(len(readcounts))))
