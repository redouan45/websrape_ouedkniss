from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from datetime import datetime
def scroll(s):
    for i in range(0, 6):
        s = s + 250
        Driver.execute_script(f"window.scrollTo(0, window.scrollY + {s})")
        time.sleep(1)
print(datetime.now())
options1 = Options()
options1.add_argument('--headless')
options1.add_argument('--disable-gpu')
options1.add_argument('--blink-settings=imagesEnabled=false')
Driver = webdriver.Chrome(executable_path="C:/Users/HP/Desktop/chromedriver.exe",chrome_options=options1)
total = 0
keywords= ["208 2020",'dacia logan' ]
for keyword in keywords:
    keyword.replace(" ", "-")
#Can add &hasPictures=true in link
#Can add hasPrice=true in link

def keyword_search(pages):
    global total
    for keyword in keywords:
        Driver.get(f'https://www.ouedkniss.com/automobiles/{1}?keywords={keyword}&lang=en')
        time.sleep(3)
        scroll(400)
        pages_nav = Driver.find_element_by_xpath('//*[@id="search-content"]/div/div[4]/div/nav/ul')
        if int(pages_nav.text.split('\n')[-1]) < pages :
            pages = int(pages_nav.text.split('\n')[-1])
            print(f'Only found {pages} Pages')
        for i in range(1, pages, 1):
            links = []
            Driver.get(f'https://www.ouedkniss.com/automobiles/{i}?keywords={keyword}&lang=en')
            time.sleep(3)
            scroll(400)
            elems = Driver.find_elements_by_xpath("//a[@href]")
            for elem in elems:
                if not ("/store/" in elem.get_attribute("href") or "/Ooredoo" in elem.get_attribute("href") ):
                    links.append(elem.get_attribute("href"))
            total += len(links) - 14
            print(total)
            with open("links.txt", "a+") as file:
                for link in links[12:len(links) - 2]:
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
            for link in links[12:len(links)-2]:
                file.write(link+'\n')
        time.sleep(1)

keyword_search(50)