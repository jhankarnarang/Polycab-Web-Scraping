from bs4 import BeautifulSoup
import requests
import pandas as pd
import csv

csv_file = open('scrape.csv','w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Prod_img','Prod_name','Prod_feature','Prod_specification'])

url = 'https://swadeshplywoods.com/swadesh-flush-doors/'
source = requests.get(url)
soup = BeautifulSoup(source.content, 'lxml')

img = soup.find('div',class_='wpb_column vc_column_container vc_col-sm-4 mpc-column')
prod_img = img.figure.div.img['src']
print(prod_img)

p_info = soup.find('div',class_='wpb_column vc_column_container vc_col-sm-8 mpc-column')
prod_name = p_info.h2.text
print(prod_name)
p_feature = p_info.ul.text.replace('\n\n\n\n','')
print(p_feature)
dfs = pd.read_html(url)                                                                                                         
df = dfs[0]
print(df)
df.to_csv('table.csv')
csv_writer.writerow([prod_img,prod_name,p_feature])

 