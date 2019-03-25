#create a mapping of state to abbreviation
#we define our dictionary here for setting state names to abbreviations
states = {
    'Oregon':'OR',
    'Florida': 'FL' ,
    'California' : 'CA',
    'New York' : 'NY',
    'Michigan':'MI'
    }

#create a basic set of states an some cities in them
#we define a new dict of cities using some of the abbreviations made above
#and this time define cities
cities = {
    'CA':'San Franciso',
    'MI':'Detroid',
    'FL':'Jacksonville'
}

#add some more cities
#this is another way to define more terms for our dict similar to above
#its almost like a function within a function
cities ['NY'] = 'New York'
cities ['OR'] = 'Portland'

#print some cities
#Here we see when we print cities[NY] we got the defiition we gave NY which is New York
#same goes for FL
print '_'* 10
print 'NY state has :', cities['NY']
print 'FL State has:' , cities['FL']

#print some states
#This then prints the defintion given to the full state names
print '_' * 10
print 'Michigans abbreviation is : ' , states['Michigan']
print 'Floridas abbreviation is:', states['Florida']

#do it by using the state then cities dict
#coding is read inside out so whats really being inputed is:
#cities[MI] etc , which will read out a city  as defined by our abbrviation
print '_'*10
print 'Michigan has:' , cities[states['Michigan']]
print 'Florida has :', cities[states['Florida']]

#print every state abbreviation
#we are allocting the defined abbreviations in our dict to
#the variable 'abbrev here and then printing using formatters as we know'
print '_'*10
for state , abbrev in states.items():
    print '%s is abbreviated %s' %(state,abbrev)
#print ever city in state
#we then take out newly created list of abbrev and define city:
#as the list of items associated to the abbrev which are our cities!
#so from our dicts we have created two lists!and print to see
print '_'
for abbrev, city in cities.items():
    print '%s has the city %s' %(abbrev,city)

#now do both at the same time
#we assign our dict abbrev to a list again as abbrev but this time to print
#we use what we already know of cities[abbrev] which is just cities[CA] for example
#and we print to make sure
print '_'*10
for state , abbrev in states.items():
    print '%s state is abbrevited %s and has city %s' %(
    state,abbrev,cities[abbrev])
#im not sure what we did here?
print '_'*10
#safely get an abbreviation by state that might not be there
state = states.get('Texas', None)

if not state:
    print 'Sorry, no Texas'
#get a city with a default value
city = cities.get('TX','Does not exist')
print 'The city for the state TX is %s' %city
