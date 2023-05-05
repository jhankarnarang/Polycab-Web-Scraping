from bs4 import BeautifulSoup
import requests
import csv

def scrape(url):
    source = requests.get(url).text
    soup = BeautifulSoup(source, 'lxml')
    #print(soup.prettify())


    for links in soup.find_all('div',class_='wpb_text_column wpb_content_element'): 
        #print(links)
        
        try:  #cables & Wires
            link = links.a['href']
            print("****************************************************************************************************************************************************")
            print(link)   
            print('')
            
     
            
            p_source = requests.get(link)
            p_page = BeautifulSoup(p_source.content, 'lxml')
            
            main = p_page.find_all('div',class_='post_content')
            #print(main)

            for src in main:
                for img in src.find_all('div',class_='wire-box wpb_column vc_column_container vc_col-sm-6'):
                    
                    image = img.figure.div.img['nitro-lazy-src']
                    name = img.h4.span.text
                    desc = img.p.text
                    print(f' Name - {name}  \nImage Link  - {image}\nDesc. - {desc} ' ' ')
                    print('--------------------------------------------------------------------------------------------------------------------------------------')
                for img in src.find_all('div',class_='wpb_column vc_column_container vc_col-sm-6'):
                    image = img.figure.div.img['nitro-lazy-src']
                    name = img.h4.span.text
                    desc = img.p.text
                    print(f'Name - {name}  \nImage Link  - {image}\nDesc. - {desc}  ')
                    print('--------------------------------------------------------------------------------------------------------------------------------------')

            
            #SWITHCES
            
        
        except :
            print('')
    
    
    
if __name__ == '__main__':

    '''
    usage:
    -> check if url is correct
    -> run
    '''

    url = 'https://polycab.com/'
    scrape(url)


