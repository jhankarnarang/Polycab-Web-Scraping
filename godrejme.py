
from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('https://www.godrej.com/godrej-locks-and-security-solutions/Locks').text
soup = BeautifulSoup(source, 'lxml')


csv_file = open('scrape.csv','w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Links','Image Links'])


for links in soup.find_all('div',class_='temp32-item'): 

    link = links.a['href']
    print(link)
    csv_writer.writerow([link])
    


print("IMAGE LINKS")
for img in soup.find_all('div',class_='temp32-img focuspoint'): 
    
    image = img.img['src']
    print(image)
    csv_writer.writerow([image])
csv_file.close()