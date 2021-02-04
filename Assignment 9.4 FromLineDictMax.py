fname = input('Enter File:')
if len(fname) < 1: fname = mbox-short.txt
hand = open(fname)

lst = list()

for line in hand:
    if not line.startswith("From:"): continue
    line = line.split()
    lst.append(line[1])

counts = dict()
for word in lst:
    counts[word] = counts.get(word,0) + 1

bc = None
bg = None
for word,count in counts.items():
    if bc is None or count > bc:
        bc = count
        bg = word

print (bg, bc)
