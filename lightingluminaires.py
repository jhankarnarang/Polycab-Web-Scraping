from bs4 import BeautifulSoup
import requests
import csv

csv_file = open('step-lights.csv','w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Product Name','Image Links','Product Description','Available Wattage'])


led_source = requests.get('https://polycab.com/products/lighting-luminaires/gardenia/step-lights')
led_soup = BeautifulSoup(led_source.content, 'lxml')
led_main = led_soup.find('div',class_='post_content')

try:
    for src in led_main.find_all('div',class_='luminate-box wpb_column vc_column_container vc_col-sm-6'):
        img = src.img['nitro-lazy-src']
        name = src.div.h3.text
        print(f'Name - {name} \nProd_Image - {img}')
        for desc in src.find_all('p'):
            info = desc.text
            print(f'Description - {info}')
        
        csv_writer.writerow([name,img,info])
except:
    print('')
    

try:
    for src in led_main.find_all('div',class_='product_data luminate-box wpb_column vc_column_container vc_col-sm-6'):
        img = src.img['nitro-lazy-src']
        name = src.div.h3.text
        print(f'Name - {name} \nProd_Image - {img}')
        for desc in src.find_all('p'):
            info = desc.text
            print(f'Description - {info}')
        
        csv_writer.writerow([name,img,info])
except:
    print('')

try:
    for src in led_main.find_all('div',class_='product_data img-light wpb_column vc_column_container vc_col-sm-6'):
        img = src.img['nitro-lazy-src']
        name = src.div.h3.text
        print(f'Name - {name} \nProd_Image - {img}')
        for desc in src.find_all('p'):
            info = desc.text
            print(f'Description - {info}')
        
        csv_writer.writerow([name,img,info])
except:
    print('')

try:
    for src in led_main.find_all('div',class_='luminate-box1 img-light wpb_column vc_column_container vc_col-sm-6'):
        img = src.img['nitro-lazy-src']
        name = src.div.h3.text
        print(f'Name - {name} \nProd_Image - {img}')
        for desc in src.find_all('p'):
            info = desc.text
            print(f'Description - {info}')

        csv_writer.writerow([name,img,info])
except:
    print('')

try:
    for src in led_main.find_all('div',class_='wpb_column vc_column_container vc_col-sm-6'):
        img = src.img['nitro-lazy-src']
        name = src.div.h3.text
        print(f'Name - {name} \nProd_Image - {img}')
        for desc in src.find_all('p'):
            info = desc.text
            print(f'Description - {info}')
        
        csv_writer.writerow([name,img,info])
except:
    print('')

try:
    for src in led_main.find_all('div',class_='product_data wpb_column vc_column_container vc_col-sm-6'):
        img = src.img['nitro-lazy-src']
        name = src.div.h3.text
        print(f'Name - {name} \nProd_Image - {img}')
        for desc in src.find_all('p'):
            info = desc.text
            print(f'Description - {info}')
        
        csv_writer.writerow([name,img,info])
except:
    print('')



    
    