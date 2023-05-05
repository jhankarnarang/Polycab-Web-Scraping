from bs4 import BeautifulSoup
import requests
import csv


source = requests.get('https://polycab.com/products/switches/').text
soup = BeautifulSoup(source, 'lxml')
main = soup.find_all('div',class_='post_content')


for src in main:
    for img in src.find_all('div',class_='luminate-box wpb_column vc_column_container vc_col-sm-4'): 
        image = img.figure.a.img['nitro-lazy-src']
        name = img.h4.span.text
        link = img.a['href']
        
        
        print(f' Link - {link} ' ' ')
       