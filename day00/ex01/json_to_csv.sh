#!/bin/sh

# converts file (first argument) from .json to .csv using filter filter.jq

INFILE=../ex00/hh.json
JQ="/Users/rdanyell/.brew/Cellar/jq/1.6/bin/jq" #where jq is

$JQ -rf filter.jq $INFILE > hh.csv #outfile name

# run with bash json_to_csv.sh