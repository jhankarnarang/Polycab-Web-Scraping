from bs4 import BeautifulSoup
import requests
import csv

csv_file = open('other-accessories.csv','w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Product Name','Image Links'])



switch_source = requests.get('https://polycab.com/products/switches/accessories/other-accessories')
switch_soup = BeautifulSoup(switch_source.content, 'lxml')
switch_main = switch_soup.find('div',class_='post_content')


try:
    for info in switch_main.find_all('div',class_='wpb_column vc_column_container vc_col-sm-4'):
        img = info.figure.div.img['nitro-lazy-src']
        name = info.div.span.text
        print(f'Product_Name - {name}  \nProduct_Img - {img}')
        csv_writer.writerow([name,img])
        
except:
    print('')
try:
    for info in switch_main.find_all('div',class_='luminate-box wpb_column vc_column_container vc_col-sm-4'):
        img1 = info.figure.div.img['nitro-lazy-src']
        name = info.div.span.text
        print(f'Product_Name - {name}  \nProduct_Img - {img}')
        csv_writer.writerow([name,img])
except:
    print('')

    #--SOCKETS
try:
    for info in switch_main.find_all('div',class_='luminate-box wpb_column vc_column_container vc_col-sm-3'):
        img2 = info.figure.div.img['nitro-lazy-src']
        name = info.div.span.text
        print(f'Product_Name - {name}  \nProduct_Img - {img2}')
        csv_writer.writerow([name,img])
except:
    print('')

try:
    for info in switch_main.find_all('div',class_='wpb_column vc_column_container vc_col-sm-3'):
        img3 = info.figure.div.img['nitro-lazy-src']
        name = info.div.span.text
        print(f'Product_Name - {name}  \nProduct_Img - {img3}')
        csv_writer.writerow([name,img])
except:
    print('')

        
    

