import subprocess 
#subprocess allows you to use bash commands on the shell youre in from python. 
#useful for running software or making/cleaning directories. 
#This is how you run a program using subprocess. 
subprocess.call('charmm <roytate_disc.inp >job.out', shell=True)
#This how you run bash commands or strings
subprocess.call(['mkdir', 'test'])

