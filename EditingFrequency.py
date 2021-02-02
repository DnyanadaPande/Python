#!/usr/bin/python3
# Dnyanada Pande, May 2019
# Read the input file with aligned sequence, frequency and CIGAR and calculate the editing frequency.

# Import the required modules.
import sys
import math
import re
import collections
import os
from sys import argv
from numpy import array
from decimal import *
from cmath import *

# User input for alignment file and output file.
samFiles = argv[1]
outFile  = argv[2]

with open(samFiles, 'r') as fh:
    with open(outFile, 'w') as ft:

        # Making a list of all the filenames.
        file_list = [line.rstrip('\n') for line in fh]
        for i in file_list:
            print(i)

            with open(i, 'r') as f:
                hdr_ct = 0
                total_ct = 0
                lines = f.readlines()
                print(lines[0])
                print(lines[1])
                lines = lines[2:]

                # Search for a specific CIGAR pattern in each entry.
                for l in lines:
                    val = l.split("\t")

                    ct = val[0]
                    num = ct.split("_")
                    cig = val[5]
                    seq = val[9]
                    hdr = cig.find("1I6M3I")
                    total_ct += int(num[2])

                    if hdr > -1:
                        hdr_ct = hdr_ct + int(num[2])

                freq = hdr_ct/total_ct
                ft.write(i + "\t" + str(hdr_ct) + "\t" + "%.2f" % round(freq,2) + "\n")

            f.close()
    ft.close()
fh.close()
