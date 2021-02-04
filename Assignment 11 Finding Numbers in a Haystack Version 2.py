#py4e Assignment 11 Findng Numbers in a Haystack

import re

# 1) The basic outline of this problem is to read the file:

handle=open('regex_sum_1063222.txt')
my_list=list()

# 2) look for integers using the re.findall(), looking for a regular expression of '[0-9]+'
for line in handle:
y=re.findall('[0-9]+',line)

# 3) And then converting the extracted strings to integers and summing up the integers.
my_list=my_list.append(int(y))
print(sum(my_list))
