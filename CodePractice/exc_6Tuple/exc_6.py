fname = input("Enter File: ")
if len(fname) < 1 : fname = 'mbox-short.txt'
hand = open(fname)

dictionary = dict()
for lin in hand:
    lin = lin.strip()
    wds = lin.split()
    for w in wds:
        dictionary[w] = dictionary.get(w,0) + 1

tmp = list()
for k,v in dictionary.items() :
    newtuple = (v,k)
    tmp.append(newtuple)
    tmp = sorted(tmp, reverse=True)
#prints tuple of descending order word count
print('Sorted Flipped Tuple', tmp[:5])
#shows which words appeared most first
for v,k in tmp[:5]:
    print(k,v)
