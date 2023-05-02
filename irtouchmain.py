from bs4 import BeautifulSoup
import requests
import csv

csv_file = open('ir-touch-feel.csv','w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Product Name','Image Links',])

source = requests.get('https://polycab.com/products/switches/ir-touch-switches/ir-touch-feel')
soup = BeautifulSoup(source.content, 'lxml')
main = soup.find('div',class_='post_content')


for img in main.find_all('div',class_='wpb_column vc_column_container vc_col-sm-3'): 
    try:
        image = img.figure.img['nitro-lazy-src']
        name = img.span.text
        
        print(f'Name - {name}  \nImage Link  - {image} ')
        csv_writer.writerow([name,image])
    except:
        print('') 

for img in main.find_all('div',class_='vc_row wpb_row vc_inner vc_row-fluid lumi-list luminate-pimg'): 
    try:
        image = img.figure.div.img['nitro-lazy-src']
        print(f'Image Link  - {image} ')
        print("DESCRIPTION")
        for nm in img.find_all('li'):
            name = nm.text
            print(name)
            csv_writer.writerow([name,image])
    except:
        print('') 