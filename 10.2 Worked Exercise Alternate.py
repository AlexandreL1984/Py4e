# 10.2 Write a program to read through the mbox-short.txt
# and figure out the distribution by hour of the day for
# each of the messages.

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
counts = dict()

# Pull the hour out from the 'From ' line
# by finding the time and then splitting the string
# a second time using a colon.

for line in handle:
    if not line.startswith("From "): continue
    time = line.split()
    time = time[5]
    hour = time.split(':')
    counts[hour[0]] = counts.get(hour[0],0) + 1

# Once you have accumulated the counts for each hour,
# print out the counts, sorted by hour as shown below.

lst = list()
for k, v in counts.items():
    newtup = (k, v)
    lst.append(newtup)
lst = sorted(lst)
for k, v in lst:
    print(k, v)
