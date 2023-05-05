from bs4 import BeautifulSoup
import requests
import csv


source = requests.get('https://polycab.com/products/wires/').text
soup = BeautifulSoup(source, 'lxml')
main = soup.find_all('div',class_='post_content')
#print(main)


for img in soup.find_all('div',class_='https://polycab.com/products/wires/'):

    for link in img.find_all('figure',class_='wpb_wrapper vc_figure'):
        f_link = link.a['href']
        if "https://polycab.com" not in f_link:
            fanlink = (f'https://polycab.com{f_link}')
            print(f'Link - https://polycab.com{f_link} ' ' ')
        else:
            
            print(f'Link - https://polycab.com{f_link} ' ' ')
           
