#!/bin/sh

#This script sorts the hh.csv file from the ex01 according to the 2nd and then by 1st column in ascending order
INFILE=../ex01/hh.csv
OUTFILE=hh_sorted.csv

head -n 1 $INFILE > $OUTFILE; # This command prints 1 line from the top of a INFILE to OUTFILE
tail -n +2 $INFILE | sort -t, -k2 -k1 >> $OUTFILE; 
# Takes everything from line 2 and sorts first by 2nd and then by 1st column in ascending order
#sort -t defines separator 

# Run with bash sorter.sh