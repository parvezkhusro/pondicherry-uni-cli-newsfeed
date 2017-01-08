#!/usr/bin/python2


import pandas as pd
import urllib2
from bs4 import BeautifulSoup
import datetime

now = datetime.datetime.now()
urlpu = "http://www.pondiuni.edu.in/newsarchive/"+str(now.year)+str(format(now.month, '02d'))
#print urlpu

page = urllib2.urlopen(urlpu)
soup = BeautifulSoup(page, "html.parser")
right_table=soup.find('table', class_='views-table cols-25')

print; print;
print "\tPondicherry University Circulars"+now.strftime(" -- %B %Y")
print "\t------------------------------------------------"

#Generate lists
A=[]
B=[]
C=[]

for row in right_table.findAll("tr"):
    title = row.findAll('a')
    date = row.findAll('td')
    
    if len(title)==1:
        A.append(title[0].find(text=True))
        B.append(date[2].find(text=True).strip())



df=pd.DataFrame(A,columns=['Title'])
df['Date']=B

print df

