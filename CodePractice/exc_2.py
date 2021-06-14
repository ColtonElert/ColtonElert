#print("Excercise 2 from FreeCodeCamp")
str = 'X-DSPAM-Confidence: 0.8475'
ipos = str.find(':')
#print(ipos)
piece = str[ipos + 1:]
#print(piece)
value = float(piece)
#print(value)
#print(value + 42)