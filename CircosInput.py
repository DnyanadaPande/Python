#!/usr/bin/python3

# Script to read the alignment files and extract the
# chromosome number, vector integration position and strand.
# The extracted chr no., position and strand will further be used to create the circos plot input file.

import sys
import numpy
import math
import re
import collections
import os
import csv
from numpy import array
from decimal import *
from cmath import *

path = '/home/dnyanada/Circos_input/'
files = [f for f in os.listdir(path) if f.endswith('.tsv')]
print(files)

for x in range(0,len(files)):
    print(files[x])

    # Make a number range to name the files.
    with open("File%i.csv" % x, "w") as ft:
        ft = csv.writer(ft, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
        ft.writerow(["Chr","start","strand"])

        with open(files[x], 'r') as fh:
            lines = fh.readlines()
            lines = lines[1:]

            for l in lines:
                val    = l.split("\t")
                align  = val[9]
                data   = align.split("_")

                if len(data) == 3:
                  chrs = data[0]
                  start = data[1]
                  strand = data[2]
                elif len(data) == 5:
                    if data[1] != "chrUn":          # Filter the entries that do not align to a specific chromosome.
                        chrs = data[0]
                        start = data[3]
                        strand = data[4]
                    else:
                        print("Data has chrUn")
                        continue
                elif len(data) == 4:
                    if data[0] != "chrUn":          # Filter the entries that do not align to a specific chromosome.
                       chrs = data[1]
                       start = data[2]
                       strand = data[3]
                    else:
                       print("Data has chrUn")
                       continue
                else:
                  continue

                ft.writerow([chrs,start,strand])


        fh.close()
