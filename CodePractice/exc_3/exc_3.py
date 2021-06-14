fh = open('mbox-short.txt')
for line in fh:
    lineslice = line.rstrip()
    print(lineslice.upper())