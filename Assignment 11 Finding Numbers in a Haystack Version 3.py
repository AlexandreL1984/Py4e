#py4e Assignment 11 Findng Numbers in a Haystack

import re

# 1) The basic outline of this problem is to read the file:
hand = open('regex_sum_textfilenumber.txt')
lst = []

# 2) look for integers using the re.findall(), looking for a regular expression of '[0-9]+'
for line in hand:
line = line.rstrip()
numbers = re.findall('[0-9]+', line)

# 3) And then converting the extracted strings to integers and summing up the integers.
for number in numbers:
if number != '':
lst.append(int(number))
print(sum(lst))``
