#Py4E Chapter 12
#Scraping Numbers from HTML using BeautifulSoup
#Actual data: http://py4e-data.dr-chuck.net/comments_1063224.html (Sum ends with 67)

#Import BeautifulSoup
from urllib import request
from bs4 import BeautifulSoup

#Open and Read the URL
html=request.urlopen('http://python-data.dr-chuck.net/comments_1063224.html').read()
soup = BeautifulSoup(html)
tags=soup('span')
#Count the Sum
sum=0
for tag in tags:
    sum=sum+int(tag.contents[0])
#Print the Sum
print(sum)
