from bs4 import BeautifulSoup
import requests
import os







source = requests.get('https://polycab.com/')
soup = BeautifulSoup(source.content, 'lxml')
for links in soup.find_all('div',class_='wpb_text_column wpb_content_element'): 
    
    
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
        for src in main:
            for img in src.find_all('div',class_='luminate-box wpb_column vc_column_container vc_col-sm-4'): 
                image = img.figure.a.img['nitro-lazy-src']
                name = img.h4.span.text
                link = img.a['href']
                
                
                if "https://polycab.com" not in link:
                    link1 = (f'https://polycab.com{link}')
                
                    print(f'Name - {name}  \nImage Link  - {image}\nLink. - {link1}  ')
                    print('*********************************************************************************************************************************************************')
                    
                    switch_source = requests.get(link1).text
                    soup = BeautifulSoup(switch_source, 'lxml')
                    switch_main = soup.find('div',class_='post_content')
                    for src in switch_main:
                        
                        for img in switch_main.find_all('div',class_='product_data wpb_column vc_column_container vc_col-sm-4'): 
                            image = img.figure.a.img['nitro-lazy-src']
                            name = img.span.text
                            link2 = img.a['href']
                            print(f'Name - {name}  \nImage Link  - {image}\nLink - https://polycab.com{link2} ' ' ')
                            print('--------------------------------------------------------------------------------------------------------------------------------------')
                            
                        for img in switch_main.find_all('div',class_='wpb_column vc_column_container vc_col-sm-4'): 
                            
                            try:
                                image = img.figure.a.img['nitro-lazy-src']
                                name = img.span.text
                                link2 = img.a['href']
                                print(f'Name - {name}  \nImage Link  - {image}\nLink - https://polycab.com{link2} ' ' ')
                                print('--------------------------------------------------------------------------------------------------------------------------------------')
                            except :
                                print('')
                        break
                else:    
                    print(f'Name - {name}  \nImage Link  - {image}\nLink - {link}  ')
                    print('*********************************************************************************************************************************************************')
                    
                    
                    switch_source = requests.get(link)
                    soup = BeautifulSoup(switch_source.content, 'lxml')
                    switch_main = soup.find('div',class_='post_content')
                    for src in switch_main:
                        
                        for img in switch_main.find_all('div',class_='product_data wpb_column vc_column_container vc_col-sm-4'): 
                            image = img.figure.a.img['nitro-lazy-src']
                            name = img.span.text
                            link3 = img.a['href']
                            print(f'Name - {name}  \nImage Link  - {image}\nLink - https://polycab.com{link3} ' ' ')
                            print('--------------------------------------------------------------------------------------------------------------------------------------')
                            
                        for img in switch_main.find_all('div',class_='wpb_column vc_column_container vc_col-sm-4'): 
                            
                            try:
                                image = img.figure.a.img['nitro-lazy-src']
                                name = img.span.text
                                link3 = img.a['href']
                                print(f'Name - {name}  \nImage Link  - {image}\nLink - https://polycab.com{link3} ' ' ')
                                print('--------------------------------------------------------------------------------------------------------------------------------------')
                            except :
                                print('')
                        break

                    #IR Touches
                    from bs4 import BeautifulSoup
                    import requests
                    


                    source = requests.get(link)
                    soup = BeautifulSoup(source.content, 'lxml')
                    main = soup.find('div',class_='post_content')

                    for img in main.find_all('div',class_='product_data wpb_column vc_column_container vc_col-sm-3'): 
                        image = img.figure.a.img['nitro-lazy-src']
                        name = img.span.text
                        link = img.a['href']
                        
                        if "https://polycab.com" not in link:
                            link1 = (f'https://polycab.com{link}')
                            
                            print(f'Name - {name}  \nImage Link  - {image}\nLink. - {link1}  ')
                            print('--------------------------------------------------------------------------------------------------------------------------------------')

                            
                            source = requests.get(link1)
                            soup = BeautifulSoup(source.content, 'lxml')
                            main = soup.find('div',class_='post_content')


                            for img in main.find_all('div',class_='wpb_column vc_column_container vc_col-sm-3'): 
                                try:
                                    image = img.figure.img['nitro-lazy-src']
                                    name = img.span.text
                                    
                                    print(f'Name - {name}  \nImage Link  - {image} ')
                                    print('--------------------------------------------------------------------------------------------------------------------------------------')
                                except:
                                    print('') 
        
        
    
    except :
        print('')


    

