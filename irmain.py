from bs4 import BeautifulSoup
import requests
import csv


source = requests.get('https://polycab.com/products/switches/ir-touch/')
soup = BeautifulSoup(source.content, 'lxml')
main = soup.find('div',class_='post_content')

for img in main.find_all('div',class_='product_data wpb_column vc_column_container vc_col-sm-3'): 
    image = img.figure.a.img['nitro-lazy-src']
    name = img.span.text
    link = img.a['href']
    
    if "https://polycab.com" not in link:
        link1 = (f'https://polycab.com{link}')
        
        print(f'Name - {name}  \nImage Link  - {image}\nLink. - {link1}  ')
        print('--------------------------------------------------------------------------------------------------------------------------------------')


        # source = requests.get(link1)
        # soup = BeautifulSoup(source.content, 'lxml')
        # main = soup.find('div',class_='post_content')


        # for img in main.find_all('div',class_='wpb_column vc_column_container vc_col-sm-3'): 
        #     try:
        #         image = img.figure.img['nitro-lazy-src']
        #         name = img.span.text
                
        #         print(f'Name - {name}  \nImage Link  - {image} ')
        #         print('--------------------------------------------------------------------------------------------------------------------------------------')
        #     except:
        #         print('')    
            


    

