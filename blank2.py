from bs4 import BeautifulSoup
import requests
import csv

csv_file = open('pumps.csv','w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Product name','Image Links','Product Description'])

source = requests.get('https://polycab.com/products/pumps/')
soup = BeautifulSoup(source.content, 'lxml')


for links in soup.find_all('div',class_='wpb_column vc_column_container vc_col-sm-12'): 
    
    try:

        prod = links.find('div',class_='luminate-box wpb_column vc_column_container vc_col-sm-4')
        prod_img = prod.figure.img['nitro-lazy-src']
        print(prod_img)
        prod_name = prod.figcaption.text
        print(prod_name)
        prod_des = links.find('div',class_='luminate-box wpb_column vc_column_container vc_col-sm-6 vc_col-has-fill')
        prod_desc = prod_des.ul.text
        print(prod_desc)
        csv_writer.writerow([prod_name,prod_img,prod_desc])
    except:
        print('')
  