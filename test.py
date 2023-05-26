from bs4 import BeautifulSoup
import requests
import pandas as pd
import csv


source = requests.get('https://swadeshplywoods.com/swadesh-flush-doors/')
soup = BeautifulSoup(source.content, 'lxml')

img = soup.find('div',class_='wpb_column vc_column_container vc_col-sm-4 mpc-column')
prod_img = img.figure.div.img['src']
print(prod_img)

p_info = soup.find('div',class_='wpb_column vc_column_container vc_col-sm-8 mpc-column')
prod_name = p_info.h2.text
print(prod_name)
p_feature = p_info.ul.text.replace('\n\n\n\n','')
print(p_feature)
p_table = p_info.table.text.replace('\n\n','')
print(p_table)

 