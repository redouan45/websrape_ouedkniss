from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
import json

options1 = Options()
# options1.add_argument('--headless')
# options1.add_argument('--disable-gpu')
options1.add_argument('--blink-settings=imagesEnabled=true')
Driver = webdriver.Chrome(executable_path="./chromedriver.exe",chrome_options=options1)

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
        exchange= False
        image_links = []
        Driver.get(link+'?lang=en')
        time.sleep(2)
        title = Driver.find_element_by_xpath('//*[@id="sidebar-layout"]/div[1]/header/h1')
        try:
            exchangable = Driver.find_element_by_xpath('//*[@id="sidebar-layout"]/div[1]/header/span')
            if 'Accept the exchange' in exchangable.text:
                exchange = True
        except:
            print('')
        try:
            price = Driver.find_element_by_xpath('//*[@id="sidebar-layout"]/div[1]/header/div')
            actual_price = price.text.split(' ')[0]
            if 'Offered' in price.text:
                offered = True
            elif 'Negotiable' in price.text:
                negotiable = True
            elif 'Fixed price' in price.text:
                fixed = True
        except:
            print('price not found!')

        description_de_lannonce = Driver.find_element_by_xpath('//*[@id="sidebar-layout"]/div[1]/div[4]')
        try:
            Description = Driver.find_element_by_xpath('//*[@id="sidebar-layout"]/div[1]/div[4]/div[3]/div/div/div').text
        except:
            print('no description found')
        try:
            User_name = Driver.find_element_by_xpath('//*[@id="announcementUserInfo"]/div/a/div[2]').text
        except:
            print('no username')
        try:
            location = Driver.find_element_by_xpath('//*[@id="announcementUserInfo"]/div/div[1]/div[2]')
            State = location.text.split('-')[0]
            City = location.text.split('-')[1]
        except:
            print('no location')
        try:
            phone_numbers = Driver.find_element_by_xpath('//*[@id="announcementUserInfo"]/div/div[2]/div[2]/div').text.split('\n')
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

        image_thumbnail = Driver.find_element_by_xpath('//*[@id="sidebar-layout"]/div[1]/div[2]/div/div/div/div[1]/div/div[3]')
        image_thumbnail.click()
        time.sleep(2)
        number_of_images = Driver.find_element_by_css_selector('#app > div.v-dialog__content.v-dialog__content--active > div > div > div.__actions > div > span')

        for i in range(1,int(number_of_images.text.split('/')[1]),1):
            next_image_btn = Driver.find_element_by_css_selector('#app > div.v-dialog__content.v-dialog__content--active > div > div > div.__actions > div > button:nth-child(10)')
            img_link = Driver.find_element_by_css_selector('#app > div.v-dialog__content.v-dialog__content--active > div > div > div.__wrap > div > div > div > div > div.swiper-slide.swiper-zoom-container.swiper-slide-active > img')
            link_data = img_link.get_attribute("src")
            image_links.append(link_data)
            next_image_btn.click()
            time.sleep(1)

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
        print(properties_dict)
        pretty_json = json.dumps(properties_dict, indent=4,ensure_ascii=False)
        print(pretty_json)

        time.sleep(2)

