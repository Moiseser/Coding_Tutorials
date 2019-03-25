#variable is being set to hold a set of stings
formatter = '%r %r %r %r'

#giving the variable nummberical value
print formatter % (1, 2, 3, 4)
#here we give the variable characters
print formatter % ('one','two','three','four')
#
print formatter % (True, False, False, True)
#here it just printed what the value of the varaible was four times
print formatter % (formatter , formatter , formatter, formatter)
#here the variable is given strings of text mor thqn just a wrd
#and keeping it on the same line with commas
print formatter % (
'I had this thing',
'That you could type up right',
'But it didnt sing',
'so i said goodnight',
)
