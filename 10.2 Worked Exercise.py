# 10.2 Write a program to read through the mbox-short.txt
# and figure out the distribution by hour of the day for
# each of the messages.

name = input("Enter file:")
open_file=open(name)
file_dict={}

# Pull the hour out from the 'From ' line
# by finding the time and then splitting the string
# a second time using a colon.

for line in open_file :
    line=line.rstrip()
    if line.startswith("From ") :
            words=line.split()
            time=words[5]
            hours=time[:2]
            file_dict[hours]=file_dict.get(hours,0)+1

# Once you have accumulated the counts for each hour,
# print out the counts, sorted by hour as shown below.

for k,v in sorted (file_dict.items()) :
    print(k,v)
