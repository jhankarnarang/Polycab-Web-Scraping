from bs4 import BeautifulSoup
import requests
import csv


csv_file = open('super-premium-ceiling-fan.csv','w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Product Link','Product Name','Image Links'])


source = requests.get('https://polycab.com/products/fans/ceiling/super-premium-fans/')
soup = BeautifulSoup(source.content, 'lxml')
main = soup.find('div',class_='ceiling_fan wpb_column vc_column_container vc_col-sm-12')


for links in main.find_all('div',class_='wpb_column vc_column_container vc_col-sm-3'):
    try:
        f_link = links.figure.a['href']
        fan_img = links.figure.a.img['nitro-lazy-src']
        fan_name = links.h4.span.text
        if "https://polycab.com" not in f_link:
            fan_link = (f'https://polycab.com{f_link}')
        else:
            fan_link = f_link
            
    except:
        print('')
    
           
    
    
    fan_source = requests.get(fan_link)
    fan_soup = BeautifulSoup(fan_source.content, 'lxml')
    


    for fan_main in fan_soup.find_all('div',class_='wpb_column vc_column_container vc_col-sm-12'):
        try:
            prod_im = fan_main.find('div',class_='wpb_text_column wpb_content_element')
            prod_img = prod_im.img['nitro-lazy-src']
            prod_name = fan_main.h3.text
            print(fan_link)
            print(prod_img)
            print(prod_name) 
            csv_writer.writerow([fan_link,prod_name,prod_img])
        except:
            print('')


        
