from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://www.pythonscraping.com/pages/warandpeace.html')
bs = BeautifulSoup(html.read(), 'html.parser')

# Find all the green text
nameList = bs.find_all('span', {'class':'green'})
for name in nameList:
    print(name.get_text())

# Return a list of header tags in a document
nameList = bs.find_all(['h1','h2','h3','h4','h5','h6'])
for name in nameList:
    print(name.get_text())

# Find all the green and red text
nameList = bs.find_all('span', {'class':{'green','red'}})
for name in nameList:
    print(name.get_text())


# Find the number of times "the prince" is surrounded by tags
nameList = bs.find_all(text='the prince')
print(len(nameList))

#####################################################################

html = urlopen('http://www.pythonscraping.com/pages/page3.html')
bs = BeautifulSoup(html, 'html.parser')

#--------------------------------------------
# Dealing with Children and Other Descendants
#--------------------------------------------
for child in bs.find('table',{'id':'giftList'}).children:
    print(child)

#--------------------------------------------
# Dealing with Siblings
#--------------------------------------------
for sibling in bs.find('table',{'id':'giftList'}).tr.next_siblings:
    print(sibling)

#--------------------------------------------
# Dealing with Parents
#--------------------------------------------
for sibling in bs.find('table',{'id':'giftList'}).tr.next_siblings:
    print(sibling)