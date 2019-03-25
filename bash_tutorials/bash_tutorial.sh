#Comments are made with hashtags. 
#The next line should be at the top of every bashscript it is called 
#the "shebang" line. It tells the shell it is a bashscript. 
#!/bin/sh

#To make a bashscript useable you must use "chmod +x mybash.sh" on the shell 

#echo is used to print text to screen
echo Hello World!

#This is how you call a variable 
#Bash is case sensitive and no spaces should be inbetween variable definitons  

myfavGundam="Rx-78-2"
echo The value of this variable is, $myfavGundam


#This is how you read a variable 

echo What is your favorite mobile suit? 
read mobile_suit
echo It is, $mobile_suit

######IF STATEMENTS#######
echo How old are you?
read age
if [ "$age" -gt 20 ]
then
    echo You can drink 
else 
    echo You are too young too drink 
fi
####OPERATORS IN BASH #########
# ==, !=, >, >=, vice versa 

for file in $FILES 
do 
    echo $(basename $file)
done
