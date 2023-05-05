from bs4 import BeautifulSoup
import requests
import csv


source = requests.get('https://polycab.com/products/switches/accessories').text
soup = BeautifulSoup(source, 'lxml')
main = soup.find('div',class_='post_content')

for src in main:
    for img in main.find_all('div',class_='product_data wpb_column vc_column_container vc_col-sm-4'): 
        image = img.figure.a.img['nitro-lazy-src']
        name = img.span.text
        link = img.a['href']
        print(f'Name - {name}  \nImage Link  - {image}\nLink - https://polycab.com{link} ' ' ')
        print('--------------------------------------------------------------------------------------------------------------------------------------')
        
    for img in main.find_all('div',class_='wpb_column vc_column_container vc_col-sm-4'): 
        
        try:
            image = img.figure.a.img['nitro-lazy-src']
            name = img.span.text
            link = img.a['href']
            print(f'Name - {name}  \nImage Link  - {image}\nLink - https://polycab.com{link} ' ' ')
            print('--------------------------------------------------------------------------------------------------------------------------------------')
        except :
            print('')
    break