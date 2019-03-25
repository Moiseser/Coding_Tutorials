#!/bin/bash
###Select the total number of Timeframes & Datapoints from elastic rod model### 
###Declare blank arrays to be filled###
Total_timeframes=0
Discs=10
for ((i=0; i<="$Total_timeframes"; i=i+1))
do
    declare -a Timeframe$i
done


###LOAD TIME FRAME ARRAYS ###
j=0
while [ $j -le $Total_timeframes ] ; do 
# Load file into array.
    let i=0
    while IFS=$'\n' read -r line_data; do
        eval Timeframe$j[i]="${line_data}"
        ((++i))
#Here you specificy the /path/to/array
    done < T$j
    j=$(( $j + 1 ))
done

#This prints the arrays created above. In the next version these will become if statemetns to select approriate charmm inputs
i=0
while [ $i -le $Total_timeframes ]; do
  j=0
  while [ $j -le $Discs ]; do
    eval "printf '%s\n' \"\${Timeframe$i[$j]}\""
    #printf "%s" "$out"
    j=$(( $j + 1 ))
  done
  i=$(( $i + 1 ))
done

i=0
while [ $i -le $Total_timeframes ]; do
  j=0
  while [ $j -le $Discs ]; do
    if [ eval "${Timeframe$i[$j]}" = "con" ]
    then
        echo Fuck u 
    fi    
    j=$(( $j + 1 ))
  done
  i=$(( $i + 1 ))
done
