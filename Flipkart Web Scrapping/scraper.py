from bs4 import BeautifulSoup 
import requests 
import csv
import pandas as pd

#Flipkart url from which we extract our mobiles list/data
#In this we extract price, name, rating of all mobiles in first page of that website.
url="https://www.flipkart.com/search?q=mobiles&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_7_na_na_ps&otracker1=AS_QueryStore_OrganicAutoSuggest_1_7_na_na_ps&as-pos=1&as-type=RECENT&suggestionId=mobiles%7CMobiles&requestId=1b4f2aba-c559-4f6d-bd01-7a82ccceb8df&as-searchtext=mobiles"

response = requests.get(url)
htmlcontent = response.content

#using beautiful soup for parsing HTML content
soup = BeautifulSoup(htmlcontent,"html.parser")
print(soup.prettify)

products=[]
prices=[]
ratings=[]
product=soup.find('div',attrs={'class':'_4rR01T'})

print(product.text)

#Extracting all the data from above given.
for a in soup.findAll('a',href=True, attrs={'class':'_1fQZEK'}):

  name=a.find('div',attrs={'class':'_4rR01T'})

  price=a.find('div',attrs={'class':'_30jeq3 _1_WHN1'})

  rating=a.find('div',attrs={'class':'_3LWZlK'})

  products.append(name.text)

  prices.append(price.text)

  ratings.append(rating.text)

# Storing data in CSV format
import pandas as pd

df = pd.DataFrame({'Product Name':products,'Prices':prices,'Ratings':ratings})

df.head()
df.to_csv('products.csv')