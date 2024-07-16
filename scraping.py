#Importation des biblio

import requests
from bs4 import BeautifulSoup

url = 'https://www.emploi.ci/recherche-jobs-cote-ivoire'
page = 'https://www.emploi.ci/recherche-jobs-cote-ivoire?page='
r = requests.get(url)

def ToutePages():
    Lien = []
    NbrPage = 1
    for i in range(6):
        i = f"{page}{NbrPage}"
        NbrPage += 1
        Lien.append(i)
    return Lien

def Emploi(url):
    url = requests.get(url)
    soup = BeautifulSoup(url.content, 'html.parser')
    Posts = soup.find_all('div', class_='job-description-wrapper')
    anoucements = []
    for Post in Posts:
        try:
            Lien = Post['data-href']
        except AttributeError as e:
            Lien = ""
        try:
            titre = Post.find('h5').find('a').get_text()
        except AttributeError as e:
            titre = ""
        try:
            date = Post.find('p', class_='job-recruiter').get_text()
        except AttributeError as e:
            date = ""
        try:
            Structure = Post.find('a', class_= 'company-name').get_text()
        except AttributeError as e:
            Structure = ""
        try:
            description = Post.find('div', class_='search-description').get_text()
        except AttributeError as e:
            description = ""
        try:
            region = Post.find('p').get_text()
        except AttributeError as e:
            region = ""

        anoucements.append((Lien,titre, date, Structure, description, region))	
            
    chemin = r"C:\Users\LENOVO\Documents\scraping\emplois1.csv"
    with open(chemin, "a") as f:
        for announcement in anoucements:
            f.write(','.join(announcement) + '\n')
        
    return anoucements
    
def TEmploi():
    pages = ToutePages()
    for page in pages:
        Emploi(url=page)
        print(f"on scrape {page}")
TEmploi()