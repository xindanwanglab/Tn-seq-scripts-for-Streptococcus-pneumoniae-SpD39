Mariner Tn-Seq analysis scripts for Streptococcus pneumoniae SpD39

Updated 2021-07-17
 
Software needed: Python3, bowtie-1.1.1, Artemis

Explanation of scripts:

a. map the reads using bowtie-1.1.1 with these parameters: -v 3 -a --best --strata -m 1 -q
b. the number of reads at each TA sites can be counted using these scripts: ReadCounter_15-py3.py and ReadCounter_16-py3.py 
c. combine the data by using this script: combine-readcounts-py3.py
d. nomalize the reads by running this command: normalize-counts-py3.py
e. to understand the coverage of your Tn library, you can count the number of TA sites that were hit by 2 or 10 reads using these scripts: TApercent_at_least_2_TAs-py3.py and TApercent_at_least_10_TAs-py3.py
f. generate files that can be viewed using Artemis: Artemize-py3.py 
g. to compare different libraries, run this script: mannwhitneyu_pneumo-py3.py
