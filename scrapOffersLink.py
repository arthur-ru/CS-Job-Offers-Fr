from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd
import json



driver = webdriver.Firefox()
data =[]
page =1
url = f'https://www.hellowork.com/fr-fr/emploi/recherche.html?k=Software+engineer&k_autocomplete=Software+engineer&l=france&l_autocomplete=france&ray=all&cod=all&d=all&p={page}&mode=pagination'
driver.get(url)
sleep(5)
pagination = driver.find_element(By.ID,"pagin")
lastPage=int(pagination.find_elements(By.CSS_SELECTOR, 'ul li')[-2].text)
sleep(5)

for page in range(1,lastPage):
    url = f'https://www.hellowork.com/fr-fr/emploi/recherche.html?k=Software+engineer&k_autocomplete=Software+engineer&l=france&l_autocomplete=france&ray=all&cod=all&d=all&p={page}&mode=pagination'
    driver.get(url)

    # Wait for the page to load and for any dynamic content
    sleep(5)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    sleep(5)

    offres = driver.find_elements(By.CSS_SELECTOR, 'li.\!tw-mb-6')

    for offre in offres :
        infos = offre.find_element(By.CLASS_NAME,"offer--maininfo")
        link =""
        if(infos.find_element(By.CSS_SELECTOR, 'h3 a')):
            link = infos.find_element(By.CSS_SELECTOR, 'h3 a').get_attribute("href")
        row = {
            "link":link
        }

        data.append(row)


    sleep(3)
driver.quit()



output_file_path = "data/offresLink.json"
with open(output_file_path, "w", encoding="utf-8") as output_file:
    json.dump(data, output_file, indent=2, ensure_ascii=False)
