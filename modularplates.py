from bs4 import BeautifulSoup
import requests
import csv

csv_file = open('modularplatescurlcaprina.csv','w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Product Name','Image Links'])

md_source = requests.get('https://polycab.com/products/switches/modular-plates/caprina/')
md_soup = BeautifulSoup(md_source.content, 'lxml')
md_main = md_soup.find('div',class_='post_content')

# for src in md_main.find_all('div',class_='vc_row wpb_row vc_inner vc_row-fluid product_slider'):
#     try:
for info in md_main.find_all('div',class_='ms-slide'):
    #print(info)
    img = info.img['nitro-lazy-src']
    name = info.div.h3.text
    print(f'Product_Name - {name}  \nProduct_Img - {img}')
    csv_writer.writerow([name,img])

    
    # except:
    #     print('')
    

        
    

