import selenium.common.exceptions
from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from datetime import datetime
def scroll(s):
    for i in range(0, 6):
        s = s + 300
        Driver.execute_script(f"window.scrollTo(0, window.scrollY + {s})")
        time.sleep(1)
print(datetime.now())
options1 = Options()
# options1.add_argument('--headless')
# options1.add_argument('--disable-gpu')

def Get_driver():
    service = Service()
    chrome_options = webdriver.ChromeOptions()
    #Normal options
    chrome_options.add_argument("disable-infobars")
    chrome_options.add_argument("start-maximized")
    chrome_options.add_argument("no-sandbox")
    chrome_options.add_argument('--blink-settings=imagesEnabled=false')
    chrome_options.add_argument("disable-blink-features=AutomationControlled")
    #Experimental options:
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    driver = webdriver.Chrome(service=service,options=chrome_options)
    return driver

Driver = Get_driver()
total = 0
keywords= ["fiat",'dacia logan' ]
for keyword in keywords:
    keyword.replace(" ", "-")
#Can add &hasPictures=true in link
#Can add hasPrice=true in link

def keyword_search(pages):
    global total
    for keyword in keywords:
        pages1 = pages
        Driver.get(f'https://www.ouedkniss.com/automobiles/{1}?keywords={keyword}&lang=en')
        time.sleep(3)
        scroll(450)
        try:
            pages_nav = Driver.find_element(by='xpath',value='//*[@id="search-content"]/div/div[3]/div/nav/ul')
            if int(pages_nav.text.split('\n')[-1]) < pages :
                pages = int(pages_nav.text.split('\n')[-1])
                print(f'Only found {pages} Pages')
        except selenium.common.exceptions.NoSuchElementException :
            print('no results found')
            pages1 = 1
        for i in range(1, pages1, 1):
            links = []
            Driver.get(f'https://www.ouedkniss.com/automobiles/{i}?keywords={keyword}&lang=en')
            time.sleep(3)
            scroll(400)
            elems = Driver.find_elements(by='xpath',value="//a[@href]")
            for elem in elems:
                if not ("/store/" in elem.get_attribute("href") or "/Ooredoo" in elem.get_attribute("href") ):
                    links.append(elem.get_attribute("href"))
            total += len(links) - 14
            print(total)
            with open("links.txt", "a+") as file:
                for link in links[12:len(links) - 11]:
                    file.write(link + '\n')
            time.sleep(1)

def normal_search(pages):
    global total
    for i in range(1,pages,1):
        links = []
        Driver.get(f"https://www.ouedkniss.com/automobiles/{i}")
        time.sleep(2)
        scroll(400)
        elems = Driver.find_elements_by_xpath("//a[@href]")
        for elem in elems:
            if not ("/store/" in elem.get_attribute("href") or "/Ooredoo"in elem.get_attribute("href")):
                links.append(elem.get_attribute("href"))
        total += len(links)-14
        print(total)
        with open("links.txt","a+") as file:
            for link in links[12:len(links)-11]:
                file.write(link+'\n')
        time.sleep(1)

keyword_search(3)