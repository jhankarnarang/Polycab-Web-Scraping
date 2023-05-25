from bs4 import BeautifulSoup
import requests
import pandas as pd
import csv


source = requests.get('https://swadeshplywoods.com/')
soup = BeautifulSoup(source.content, 'lxml')
links = soup.find('nav',class_='menu-main-menu-container')
for p_links in links.find('li',class_='menu-item menu-item-type-custom menu-item-object-custom menu-item-has-children menu-item-6945'):
    try:
        prod_links = p_links.li
        print(prod_links)

    except:
        print('')
