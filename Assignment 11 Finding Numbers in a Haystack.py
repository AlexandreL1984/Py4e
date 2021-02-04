#py4e Assignment 11 Findng Numbers in a Haystack

import re

# 1) The basic outline of this problem is to read the file
hand = open("regex_sum_1063222.txt")
a = list()

# 2) look for integers using the re.findall(), looking for a regular expression of '[0-9]+'
for line in hand:
     b = re.findall('[0-9]+',line)
     a = a+b

# 3) And then converting the extracted strings to integers and summing up the integers.
sum = 0
for c in a:
    sum = sum + int(c)

print(sum)
