from bs4 import BeautifulSoup
import requests
import csv


csv_file = open('Wires&Cables.csv','w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Product Name','Image Links','Product Description'])

source = requests.get('https://polycab.com/')
soup = BeautifulSoup(source.content, 'lxml')
for links in soup.find_all('div',class_='wpb_text_column wpb_content_element'): 
    
    
    try:  
        link = links.a['href']
        print(link)   
        print('')
    except:
        print('')
        
    #--Wires & Cables
    wires_source = requests.get(link)
    wires_soup = BeautifulSoup(wires_source.content, 'lxml')
    for img in wires_soup.find_all('div',class_='wire-box wpb_column vc_column_container vc_col-sm-6'):
        
        image = img.figure.div.img['nitro-lazy-src']
        name = img.h4.span.text
        desc = img.p.text
        print(f' Name - {name}  \nImage Link  - {image}\nDesc. - {desc} ' ' ')
        csv_writer.writerow([name,image,desc])

    for img in wires_soup.find_all('div',class_='wpb_column vc_column_container vc_col-sm-6'):
        image = img.figure.div.img['nitro-lazy-src']
        name = img.h4.span.text
        desc = img.p.text
        print(f'Name - {name}  \nImage Link  - {image}\nDesc. - {desc}  ')
        csv_writer.writerow([name,image,desc])


    #----SWITCHES----
    switch_source = requests.get(link)
    switch_soup = BeautifulSoup(switch_source.content, 'lxml')
    for img in switch_soup.find_all('div',class_='luminate-box wpb_column vc_column_container vc_col-sm-4'): 
        link = img.a['href']
        if "https://polycab.com" not in link:
            link1 = (f'https://polycab.com{link}')
            
            switch_source1 = requests.get(link1).text
            switch_soup1 = BeautifulSoup(switch_source1, 'lxml')
            switch_main1 = switch_soup1.find('div',class_='post_content')
            
                
            for img in switch_main1.find_all('div',class_='product_data wpb_column vc_column_container vc_col-sm-4'): 
                link2 = img.a['href']
                link3 = (f'https://polycab.com{link2}')
                print(link3)
                switch_source2 = requests.get(link3)
                switch_soup2 = BeautifulSoup(switch_source2.content, 'lxml')
                switch_main2 = switch_soup2.find('div',class_='post_content')

                for src in switch_main2.find('div',class_='wpb_column vc_column_container vc_col-sm-12'):
                    try:
                        for info in switch_main2.find_all('div',class_='wpb_column vc_column_container vc_col-sm-4'):
                            img = info.figure.div.img['nitro-lazy-src']
                            name = info.div.span.text
                            print(f'Product_Name - {name}  \nProduct_Img - {img}')
                            
                    except:
                        print('')
                    try:
                        for info in switch_main2.find_all('div',class_='luminate-box wpb_column vc_column_container vc_col-sm-4'):
                            img1 = info.figure.div.img['nitro-lazy-src']
                            name = info.div.span.text
                            print(f'Product_Name - {name}  \nProduct_Img - {img}')
                    except:
                        print('')

                        #--SOCKETS
                    try:
                        for info in switch_main2.find_all('div',class_='luminate-box wpb_column vc_column_container vc_col-sm-3'):
                            img2 = info.figure.div.img['nitro-lazy-src']
                            name = info.div.span.text
                            print(f'Product_Name - {name}  \nProduct_Img - {img}')
                    except:
                        print('')

                    try:
                        for info in switch_main2.find_all('div',class_='wpb_column vc_column_container vc_col-sm-3'):
                            img3 = info.figure.div.img['nitro-lazy-src']
                            name = info.div.span.text
                            print(f'Product_Name - {name}  \nProduct_Img - {img}')
                    except:
                        print('')


            for img in switch_main1.find_all('div',class_='wpb_column vc_column_container vc_col-sm-4'): 
                
                try:
                    link5 = img.a['href']
                    link4 = (f'https://polycab.com{link5}')
                    print(link3)
                    print('--------------------------------------------------------------------------------------------------------------------------------------')
                
                
                    switch_source3 = requests.get(link4)
                    switch_soup3 = BeautifulSoup(switch_source3.content, 'lxml')
                    switch_main3 = switch_soup3.find('div',class_='post_content')

                    for src in switch_main3.find('div',class_='wpb_column vc_column_container vc_col-sm-12'):
                        try:
                            for info in switch_main2.find_all('div',class_='wpb_column vc_column_container vc_col-sm-4'):
                                img = info.figure.div.img['nitro-lazy-src']
                                name = info.div.span.text
                                print(f'Product_Name - {name}  \nProduct_Img - {img}')
                                
                        except:
                            print('')
                        try:
                            for info in switch_main3.find_all('div',class_='luminate-box wpb_column vc_column_container vc_col-sm-4'):
                                img1 = info.figure.div.img['nitro-lazy-src']
                                name = info.div.span.text
                                print(f'Product_Name - {name}  \nProduct_Img - {img}')
                        except:
                            print('')

                            #--SOCKETS
                        try:
                            for info in switch_main3.find_all('div',class_='luminate-box wpb_column vc_column_container vc_col-sm-3'):
                                img2 = info.figure.div.img['nitro-lazy-src']
                                name = info.div.span.text
                                print(f'Product_Name - {name}  \nProduct_Img - {img}')
                        except:
                            print('')

                        try:
                            for info in switch_main3.find_all('div',class_='wpb_column vc_column_container vc_col-sm-3'):
                                img3 = info.figure.div.img['nitro-lazy-src']
                                name = info.div.span.text
                                print(f'Product_Name - {name}  \nProduct_Img - {img}')
                        except:
                            print('')
                except:
                    print('')
            

        else:    
            print(f'Switch Link - {link}  ')
        



        
                
           

    
    
        

        