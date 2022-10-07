#!/bin/sh

head -n 1 ../ex02/hh_sorted.csv > hh_positions.csv
tail -n +2 ../ex02/hh_sorted.csv | \
awk 'BEGIN { FS = OFS = "," } 
    {
        STR = ""
        if (index(tolower($3), "junior"))
            STR = STR"Junior/"
        if (index(tolower($3), "middle"))
            STR = STR"Middle/"
        if (index(tolower($3), "senior"))
            STR = STR"Senior"
        if (STR == "")
            STR = "-"
        gsub(/[\/ ]*$/, "", STR)
        
        $3 = "\""STR"\""
        print
    }' \
    >> hh_positions.csv
    # FS: field separator for file reading
    # OFS: Output Filed Separator
    # gsub - substitutes 
    # run bash cleaner.sh