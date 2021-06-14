import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
    print(line.decode().strip())
#Extra code that starts a word count dictionary
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
print(counts)

# This code does the same thing as the exc_7 with fewer lines 
# it automatically encodes your data for you
# however it does not print the headers of the page only the body
