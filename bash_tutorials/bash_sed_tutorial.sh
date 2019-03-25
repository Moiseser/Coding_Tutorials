#!/bin/bash

#In this bash tutorial I will learn how to used the sed command. 
#The sed command allows pieces of text in another file to be deleted or edited!
#For this test I will edit the sedtest file where I will change text in 4th line. 
value=10000
sed -i -e "4 s/.*/set Option $value/" mysed
