from bs4 import BeautifulSoup
import requests

#Link for f1 officila site 
source = requests.get("https://www.formula1.com/en/results.html/2022/drivers.html").text
soup = BeautifulSoup(source,'lxml')

#Extracted data
try:
    first_names = soup.find_all('span', class_ = 'hide-for-tablet')
    last_names = soup.find_all('span',class_ = 'hide-for-mobile')
    teams = soup.find_all('a',class_ = "grey semi-bold uppercase ArchiveLink")
    points = soup.find_all('td', class_ = "dark bold")

    print("-"*80)
    print("| {:<8}| {:<20}| {:<30}| {:<12}|".format("POS", "DRIVER", "CAR", "PTS"))
    print("-"*80)
    for i in range(len(first_names)):
        print("| {:<8}| {:<20}| {:<30}| {:<12}|".format((i+1),first_names[i].string + " " + last_names[i].string,teams[i].string,points[i].string))
    print("-"*80)
    
except:
    print("Error: NOT FOUND")


