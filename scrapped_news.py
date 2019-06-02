import requests
import pandas
from bs4 import BeautifulSoup
#import numpy as np
r=requests.get("https://www.thehindu.com/news/national/?utm_source=google&utm_medium=cpc&utm_campaign=national-th&gclid=EAIaIQobChMIns3mlf3O4AIVRI6PCh1wvgIREAAYASAAEgJe4fD_BwE")
c=r.content
soup=BeautifulSoup(c,"html.parser")
#print(soup.prettify())
#list(soup.children)
all=soup.find_all("div",{"class":"story-card-news"})
print(all[2].find("h3").text.replace("\n",""))
#print(all.find("a",href=True))
print(all[3].find("h3").text.replace("\n",""))
print(all[4].find("h3").text.replace("\n",""))
print(all[5].find("h3").text.replace("\n",""))
l=[]
for item in all[2:len(all)]:
	d={}
	d["info"]=item.find("h3").text.replace("\n","")
	l.append(d)
#print(l)
df=pandas.DataFrame(l)
print(df)
df["info"].tolist()
