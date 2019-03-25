#\t creastes a tab / shifts the line over when printed
tabby_cat = '\tI am tabbed in.'
# \n again moves what follows it to a new line
persian_cat = '\I am split\non a line.'
# double back slash "\\" makes it just write a single backslash character
backslash_cat = 'I am a \\ a \\ cat.'

#Combining everything we can make a tabbed list each on a new line!
fat_cat = '''
I will do a list :
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
'''

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

#funcode zed said to try

while True :
    for i in ['/','_','|','\\','|']:
            print '%s\r' % i,
