import numpy as np
import sys
import os
import subprocess
#load the csv data
datafile_name = sys.argv[1]
filenames = []
ch_drive = []
with open(datafile_name, 'r') as f:
    for line in f:
        if ("CHF" in line) or ("CHA" in line):
            parts = line.split(' ')
            #remove empty splits
            parts = [p for p in parts if p]
            #remove the \n at on the last part
            parts[-1] = parts[-1].strip()
            #the filename is the 2nd part, the ch drive is the last part
            filenames.append(parts[2])
            ch_drive.append(parts[-1])

#for each of the filenames, create the command and run it
for filename, ch in zip(filenames, ch_drive):
    command = f"rsync -rv --stats --progress -t /drives/{ch}/replace/{filename} adamdong@fir.computecanada.ca:/home/adamdong/projects/rrg-istairs-ad/adamdong/bass_vdiff/"
    #replace replace with {0,1,2,3,4,5,6,7}
    command = command.replace("replace", "{0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15}")
    subprocess.run(command, shell=True)
    #run the command
    # os.system(command)
    print(command)
