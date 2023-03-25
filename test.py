from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from datetime import datetime

print(datetime.now())
options = Options
options.headless = True
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--blink-settings=imagesEnabled=false')
Driver = webdriver.Chrome(executable_path="C:/Users/HP/Desktop/chromedriver.exe",options=options,chrome_options=chrome_options)
total = 0
pages = 50
keywords= ["208 noire",'dacia logan' ]
for keyword in keywords:
    keyword.replace(" ", "-")
#TODO:Rework keyword_search() such that number of results is considered
def keyword_search():
    global total
    for keyword in keywords:
        for i in range(1, pages, 1):
            links = []
            Driver.get(f'https://www.ouedkniss.com/automobiles/{i}?keywords={keyword}&lang=en')
            time.sleep(2)
            s = 100
            for i in range(0, 3):
                s = s * 4
                Driver.execute_script(f"window.scrollTo(0, window.scrollY + {s})")
                time.sleep(1)
            elems = Driver.find_elements_by_xpath("//a[@href]")
            for elem in elems:
                if not ("/store/" in elem.get_attribute("href") or "/Ooredoo" in elem.get_attribute("href")):
                    links.append(elem.get_attribute("href"))
            total += len(links) - 14
            print(total)
            with open("links.txt", "a+") as file:
                for link in links[3:len(links) - 11]:
                    file.write(link + '\n')
            time.sleep(1)


def normal_search():
    global total
    for i in range(1,pages,1):
        links = []
        Driver.get(f"https://www.ouedkniss.com/automobiles/{i}")

        time.sleep(2)
        s = 100
        for i in range(0,3):
            s = s *4
            Driver.execute_script(f"window.scrollTo(0, window.scrollY + {s})")
            time.sleep(1)
        elems = Driver.find_elements_by_xpath("//a[@href]")
        for elem in elems:
            if not ("/store/" in elem.get_attribute("href") or "/Ooredoo"in elem.get_attribute("href")):
                links.append(elem.get_attribute("href"))
        total += len(links)-14
        print(total)
        with open("links.txt","a+") as file:
            for link in links[3:len(links)-11]:
                file.write(link+'\n')
        time.sleep(1)

normal_search()