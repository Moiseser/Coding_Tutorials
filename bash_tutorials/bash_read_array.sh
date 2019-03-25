#!/bin/bash
######READING IN AN ARRAY################## 

##THIS DECLARES AN ARRAY#
declare -a myarray

# Load file into array.
let i=0
while IFS=$'\n' read -r line_data; do
    myarray[i]="${line_data}"
    ((++i))
#Here you specificy the /path/to/array     
done < anarray

# Explicitly report array content.
#let i=0
#while (( ${#myarray[@]} > i )); do
#    printf "${myarray[i++]}\n"
#done

#Arrays begin at 0 in BASH
###If check###
Timeframes=5 
for  ((i=0; i<="$Timeframes" ; i=i+1))
do
    #echo $i
    echo ${myarray[$i]}
    if [ "${myarray[$i]}" = "con" ]
    then 
        echo found value do stuff!  
    fi
done
