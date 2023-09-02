from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import json

# options1.add_argument('--headless')
# options1.add_argument('--disable-gpu')
def scroll(s):
    for i in range(0, 2):
        s = s + 300
        Driver.execute_script(f"window.scrollTo(0, window.scrollY + {s})")
        time.sleep(1)
def Get_driver():
    service = Service()
    chrome_options = webdriver.ChromeOptions()
    #Normal options
    chrome_options.add_argument("disable-infobars")
    chrome_options.add_argument("start-maximized")
    chrome_options.add_argument("no-sandbox")
    chrome_options.add_argument("disable-blink-features=AutomationControlled")
    chrome_options.add_argument('--blink-settings=imagesEnabled=true')
    #Experimental options:
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    driver = webdriver.Chrome(service=service,options=chrome_options)
    return driver

Driver = Get_driver()

with open("links.txt" , 'r') as file:
    links = file.readlines()
    for link in links:
        #initialize:
        Documents = None
        Color = None
        Brand = None
        Model = None
        Finition = None
        Gearbox = None
        Engine = None
        Year = None
        Mileage = None
        Car_options = None
        Description = None
        User_name = None
        price = None
        location = None
        offered = False
        negotiable = False
        fixed = False
        actual_price = None
        exchange= False
        phone_numbers = []
        image_links = []
        Driver.get(link+'?lang=en')
        time.sleep(2)
        scroll(150)
        title = Driver.find_element(by='xpath',value='//*[@id="sidebar-layout"]/div[1]/header/h1')
        try:
            exchangable = Driver.find_element(by='xpath',value='//*[@id="sidebar-layout"]/div[1]/header/span')
            if 'Accept the exchange' in exchangable.text:
                exchange = True
        except:
            print('')
        try:
            price = Driver.find_element(by='xpath',value='//*[@id="sidebar-layout"]/div[1]/header/div')
            actual_price = price.text
            if 'Offered' in price.text:
                offered = True
            elif 'Negotiable' in price.text:
                negotiable = True
            elif 'Fixed price' in price.text:
                fixed = True
        except:
            print('price not found!')

        description_de_lannonce = Driver.find_element(by='xpath',value='//*[@id="sidebar-layout"]/div[1]/div[4]')
        try:
            Description = Driver.find_element(by='xpath',value='//*[@id="sidebar-layout"]/div[1]/div[4]/div[3]/div/div/div').text
        except:
            print('no description found')
        try:
            User_name = Driver.find_element(by='xpath',value='//*[@id="announcementUserInfo"]/div/a/div[2]').text
        except:
            print('no username')
        try:
            location = Driver.find_element(by='xpath',value='//*[@id="announcementUserInfo"]/div/div[1]/div[2]')
            State = location.text.split('-')[0]
            City = location.text.split('-')[1]
        except:
            print('no location')
        try:
            phone_numbers = Driver.find_element(by='xpath',value='//*[@id="announcementUserInfo"]/div/div[2]/div/div[2]/div').text.split('\n')
        except:
            print('no phone numbers')

        properties_list = description_de_lannonce.text.split('\n')
        for i in range(len(properties_list)):
            if 'Documents' in properties_list[i]:
                Documents = properties_list[i+1]
            elif 'Color' in  properties_list[i]:
                Color = properties_list[i+1]
            elif 'Brand' in  properties_list[i]:
                Brand = properties_list[i+1]
            elif 'Model' in  properties_list[i]:
                Model = properties_list[i+1]
            elif 'Version' in  properties_list[i]:
                Finition = properties_list[i+1]
            elif 'Gearbox' in  properties_list[i]:
                Gearbox = properties_list[i+1]
            elif 'Engine' in  properties_list[i]:
                Engine = properties_list[i+1]
            elif 'Year' in  properties_list[i]:
                Year= properties_list[i+1]
            elif 'mileage' in  properties_list[i]:
                Mileage = properties_list[i+1]
            elif 'Car Options' in  properties_list[i]:
                Car_options = properties_list[i+1: len(properties_list)-2]
        try:
            image_thumbnail = Driver.find_element(by='xpath',value='//*[@id="sidebar-layout"]/div[1]/div[2]/div/div/div/div[1]')
            image_thumbnail.click()
            time.sleep(2)
            number_of_images = Driver.find_element(by=By.CSS_SELECTOR,value='#app > div.v-dialog__content.v-dialog__content--active > div > div.__actions > div > span')

            for i in range(1,int(number_of_images.text.split('/')[1]),1):
                next_image_btn = Driver.find_element(by=By.CSS_SELECTOR,value='#app > div.v-dialog__content.v-dialog__content--active > div > div.__actions > div > button:nth-child(10)')
                img_link = Driver.find_element(by=By.CSS_SELECTOR,value='#app > div.v-dialog__content.v-dialog__content--active > div > div.__wrap > div > div > div > div > div.swiper-slide.swiper-slide-active > div > img')
                link_data = img_link.get_attribute("src")
                image_links.append(link_data)
                next_image_btn.click()
                time.sleep(1)
        except :
            print('No images found')

        properties_dict = {
            'Title': title.text,
            'Documents': Documents,
            'Color': Color,
            'Brand': Brand,
            'Model': Model,
            'Finition': Finition,  # aka version
            'GearBox': Gearbox,
            'Engine': Engine,
            'Year': Year,
            'Mileage': Mileage,
            'Car Options': Car_options,
            'Car Description': Description,
            'User name': User_name,
            'State': State,
            'City': City,
            'Phone numbers': phone_numbers,
            'Price': actual_price,
            'Offered': offered,
            'Exchange': exchange,
            'Negotiable': negotiable,
            'Fixed Price': fixed,
            'images': image_links,
        }
        pretty_json = json.dumps(properties_dict, indent=4,ensure_ascii=False)
        print(pretty_json)

        time.sleep(2)

