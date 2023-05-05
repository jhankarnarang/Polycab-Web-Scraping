import requests
from bs4 import BeautifulSoup

fan_source = requests.get('https://polycab.com/products/fans/exhaust/domestic/revivo/')
fan_soup = BeautifulSoup(fan_source.content, 'lxml')



for fan_main in fan_soup.find('div',class_='wpb_column vc_column_container vc_col-sm-12'):
    try:
            prod_im = fan_main.find('div',class_='wpb_text_column wpb_content_element ')
            prod_img = fan_main.img['nitro-lazy-src']
            prod_name = fan_main.h2.text
            print(prod_name)
        
            print(prod_img)
            
            
    except:
        print('')