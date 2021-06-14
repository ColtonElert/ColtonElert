fname = input("Enter File: ")
if len(fname) < 1 : fname = 'clown.txt'
hand = open(fname)

dictionary = dict()
for lin in hand:
    lin = lin.strip()
    wds = lin.split()
    for w in wds:
        dictionary[w] = dictionary.get(w,0) + 1

largest = -1
theword = None

for k,v in dictionary.items():
    if v > largest :
        largest = v
        theword = k

print('Most Common Word->',theword, largest)


     
        print(w)