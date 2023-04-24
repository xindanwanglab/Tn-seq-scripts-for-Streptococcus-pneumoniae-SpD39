#argv[1] is S. pneumo TA list (generated from TAfinder.py)
#argv[2] is mapped reads file (bowtie)
#argv[3] is S. pneumo gene list

import sys
if sys.version_info[0] < 3:
    raise Exception("Python 3 or a more recent version is required.")

#create dictionary of chrI TA sites

chrITA={}

for line in open(sys.argv[1]):  # opens files line by line
    split= line.split()         #splits string into columns--treates consecutive spaces as 1 single tab
    TAsite=int(split[0])
    chrITA[TAsite]=[0,0]

#counts reads at each TA site
for line in open(sys.argv[2]):
    split = line.split('\t')  #splits string into 'columns'
    strand = split[1]       #designate a marker for column 1 info
    if strand == '+':
        site = int(split[3]) + 15  #if on + strand, take column 3 position and add 1bp)
        if site in chrITA: chrITA[site][0] += 1  #if read has been found before, tally 1 more in F reads
    if strand == '-':
        site = int(split[3]) + 1 #if on - strand, add col 3 position to length of read in position 4 and add 1
        if site in chrITA: chrITA[site][1] += 1  #if read has been found before, tally 1 more in R reads

# assign gene names

gene_dict = {}; prev_end = 0; IG = 'IG_1';

for line in open(sys.argv[3]):
    split = line.split('\t')
    gene = split[0]; start = int(split[4]); end = int(split[5])
    gene_dict[gene]=[start, end]
    IG = 'IG_' + gene
    if start > prev_end+1:
        gene_dict[IG]=[prev_end+1,start-1]
    prev_end = end
gene_dict['IG_chrmEnd'] = [2045905, 2046116] #must adjust last intergenic region for organism of interest (in this case pneumo)

## Example EHEC EDL933 [5528421,5528445]
##         pESBL [88545,88546] *although the end is 88545, add 1 to make it work (so there's a difference between start and end)

# store gene names into TA site dictionary
for k,v in gene_dict.items():
    start = v[0]; end = v[1];
    for i in range(start,end+1):
        if i in chrITA: chrITA[i].append(k)
    
            
#print
# change to sorted for python3
CI_sites = sorted(chrITA)
#CI_sites = chrITA.keys()
#CI_sites.sort()

##readcounttotal = 0
##TAs = 0
##hitsites = 0

for i in CI_sites:
#    print('B sub', '\t',  i, '\t',  i+1, '\t', chrITA[i][2], '\t', chrITA[i][0], '\t', chrITA[i][1])
    print(f'B sub\t{i}\t{i+1}\t{chrITA[i][2]}\t{chrITA[i][0]}\t{chrITA[i][1]}')
##    readcounttotal += chrITA[i][0]
##    readcounttotal += chrITA[i][1]
##    TAs += 1
##    if chrITA[i][0] +  chrITA[i][1] > 0: hitsites += 1
        
##print readcounttotal
##print TAs
##print hitsites

#un comment the above (from readcounttotal=0 down to print hitsites to get a table of how many TA sites are hit by the transposon

#To append on new lists to an existing dictionary
#>>> for i in range(0,100): #where 0,100 will be the stard and end columns of the  gene list
        # if i in a: a[i].append('gene') #this adds the word 'gene', but you want the annotation of the column 1 in the gene list

#append on info dep on chromosome (2 separate chrI and chrII gene list files):
