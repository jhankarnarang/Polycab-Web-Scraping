from bs4 import BeautifulSoup
import requests
import csv


# csv_file = open('air-circulator-fans.csv','w')
# csv_writer = csv.writer(csv_file)
# csv_writer.writerow(['Product Link','Product Name','Image Links'])


source = requests.get('https://rajelectricals.co.in/')
soup = BeautifulSoup(source.content, 'lxml')
main = soup.find('div',class_='elementor-column-wrap elementor-element-populated')
print(main)

# for links in soup.find_all('div',class_='wpb_column vc_column_container vc_col-sm-6'):
#     try:
#         f_link = links.figure.a['href']
        
#         if "https://polycab.com" not in f_link:
#             fan_link = (f'https://polycab.com{f_link}')
            
#         else:
#             fan_link = f_link
        
            
#     except:
#         print('')
#     print(fan_link)
    
    
           
    
    
#     fan_source = requests.get(fan_link)
#     fan_soup = BeautifulSoup(fan_source.content, 'lxml')
#     fan_main = fan_soup.find('div',class_='wpb_column vc_column_container vc_col-sm-12')
#     for prod_info in fan_soup.find_all('div',class_='vc_row wpb_row vc_inner vc_row-fluid product_slider'):
        
#         try:
#             prod_img = prod_info.img['nitro-lazy-src']
#             prod_name = fan_main.h2.text
#             print(prod_img)
#             print(prod_name)
#             csv_writer.writerow([fan_link,prod_name,prod_img])
            
            
#         except:
#             print('')

#         # try:
#         #     prod_im = fan_main.find('div',class_='wpb_text_column wpb_content_element ')
#         #     prod_img = fan_main.img['nitro-lazy-src']
#         #     prod_name = fan_main.h2.text
#         #     print(prod_name)
        
#         #     print(prod_img)
#         #     csv_writer.writerow([fan_link,prod_name,prod_img])
            
            
#         # except:
#         #     print('')

        

        
