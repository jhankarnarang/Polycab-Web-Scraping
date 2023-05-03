from bs4 import BeautifulSoup
import requests
import csv


source = requests.get('https://polycab.com/products/fans/ceiling').text
soup = BeautifulSoup(source, 'lxml')
main = soup.find_all('div',class_='post_content')
#print(main)


for img in soup.find_all('div',class_='wpb_column vc_column_container vc_col-sm-12'):

    for link in img.find_all('figure',class_='wpb_wrapper vc_figure'):
        f_link = link.a['href']
        f_img = link.a.img['nitro-lazy-src']
        
    for fanname in img.find_all('div',class_='product_data wpb_column vc_column_container vc_col-sm-4'):
        f_name = fanname.text
        print(f_name)
        
        
        if "https://polycab.com" not in f_link:
            fanlink = (f'https://polycab.com{f_link}')
            print(f'Name - {f_name}  \nImage Link  - {f_img}\nLink - https://polycab.com{f_link} ' ' ')
            print('--------------------------------------------------------------------------------------------------------------------------------------')
            
        else:
            
            print(f'Name - {f_name}  \nImage Link  - {f_img}\nLink - https://polycab.com{f_link} ' ' ')
            print('--------------------------------------------------------------------------------------------------------------------------------------')
            

    for fanname in img.find_all('div',class_='product_data wpb_column vc_column_container vc_col-sm-3'):
        f_name = fanname.text
        print(f_name)
        
        
        if "https://polycab.com" not in f_link:
            fanlink = (f'https://polycab.com{f_link}')
            print(f'Name - {f_name}  \nImage Link  - {f_img}\nLink - https://polycab.com{f_link} ' ' ')
            print('--------------------------------------------------------------------------------------------------------------------------------------')
            
        else:
            
            print(f'Name - {f_name}  \nImage Link  - {f_img}\nLink - https://polycab.com{f_link} ' ' ')
            print('--------------------------------------------------------------------------------------------------------------------------------------')
            
            
