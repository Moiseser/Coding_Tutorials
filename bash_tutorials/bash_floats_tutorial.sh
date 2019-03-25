#!/bin/sh
#Bash can deal with floating point numbers the way most languages do it will treat them as integers
#therefore we must use the "bc" command to treat them as float numbers
 val1=1.5E-1
 val2=1
 echo $r_exti
 if [ 1 -eq "$(echo "${val1} < ${val2}" | bc)" ]
 then 
    echo hello 
fi 
