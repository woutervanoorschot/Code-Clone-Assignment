import os
import json
import glob

# fpaths = glob.glob("/usr/jquery-data/*/jquery.js")
fpaths = glob.glob("/out/jquery-versions/*.js") # these do not really work past version 2.x

def savediff(file1, file2, diff):
    # uses metric from "Analysis of the Linux Kernel Evolution Using Code Clone Coverage"
    metric = (diff/(filelens[file1] + filelens[file2]))
    n = lambda x: x.split('-')[2]
    print(n(file1), n(file2), metric)

# 'global' filelens
filelens = dict()
for file in fpaths: 
    num_lines = sum(1 for line in open(file))
    filelens[file] = num_lines


for fpath1 in fpaths:
    for fpath2 in fpaths:
        if fpath1 == fpath2: 
            savediff(fpath1, fpath2, 0)
            continue

        out = json.load(os.popen('jsinspect -I -L -t 40 {} {} -r json'.format(fpath1, fpath2)))
        # first, count the total amount of code duplication, and keep track of the ranges
        total = 0
        ranges = []
        for copy in out:
            total += abs(copy['instances'][0]['lines'][0] - copy['instances'][0]['lines'][1])
            ranges.append([copy['instances'][0]['lines'][0], copy['instances'][0]['lines'][1]])

        # as certain code duplications overlap, we need to make sure to remove the overlapping lines.
        # to do so, we use a trick where we take the difference in line numbers of the ranges
        overlapcount = 0
        for i in range(len(ranges)):
            for j in range(i+1,len(ranges)):
                a = range(ranges[i][0], ranges[i][1])
                b = range(ranges[j][0], ranges[j][1])
                overlapcount += len([i for i in a if i in b])
        savediff(fpath1, fpath2, total - overlapcount)

