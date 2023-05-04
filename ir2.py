from bs4 import BeautifulSoup
import requests
import csv


source = requests.get('https://polycab.com/products/switches/ir-touch-switches/ir-touch-feel')
soup = BeautifulSoup(source.content, 'lxml')
main = soup.find('div',class_='post_content')


for img in main.find_all('div',class_='wpb_column vc_column_container vc_col-sm-3'): 
    try:
        image = img.figure.img['nitro-lazy-src']
        name = img.span.text
        
        print(f'Name - {name}  \nImage Link  - {image} ')
        print('--------------------------------------------------------------------------------------------------------------------------------------')
    except:
        print('')    
    
