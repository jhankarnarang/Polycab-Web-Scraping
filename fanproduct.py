from bs4 import BeautifulSoup
import requests
import csv

# csv_file = open('superia-lite-sp01.csv','w')
# csv_writer = csv.writer(csv_file)
# csv_writer.writerow(['Product Name','Image Links','Product Description'])


fan_source = requests.get('https://polycab.com/products/fans/wall/thunderstorm/')
fan_soup = BeautifulSoup(fan_source.content, 'lxml')
fan_main = fan_soup.find('div',class_='wpb_column vc_column_container vc_col-sm-12')
for prod_info in fan_soup.find_all('div',class_='vc_row wpb_row vc_inner vc_row-fluid product_slider'):
    
    try:
        prod_img = prod_info.img['nitro-lazy-src']
        prod_name = fan_main.h2.text
        print(prod_img)
        print(prod_name)
        
        
    except:
        print('')

# for prod_info1 in fan_main.find_all('div',class_='wpb_text_column wpb_content_element'):
#     try:
#         prod_img1 = prod_info1.img['nitro-lazy-src']
#         print(prod_img1)
#         prod_desc1 = prod_info1.h3.text
#         print(prod_desc1)
#         prod_spe1 = prod_info1.find('div',class_='wpb_single_image wpb_content_element vc_align_left')
#         prod_spec1 = prod_spe1.figure.img['nitro-lazy-src']
#         print(prod_spe1)
#     except:
#         print('')
    

    

    
    


        