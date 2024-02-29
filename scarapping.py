from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd
import json



driver = webdriver.Firefox()
data =[]


for page in range(1,5):
    url = f'https://www.hellowork.com/fr-fr/emploi/recherche.html?k=Software+engineer&k_autocomplete=http%3A%2F%2Fwww.rj.com%2FCommun%2FPost%2FIngenieur_IT&ray=20&cod=all&d=all&p={page}&mode=pagination'
    driver.get(url)

    # Wait for the page to load and for any dynamic content
    sleep(5)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    sleep(5)

    offres = driver.find_elements(By.CSS_SELECTOR, 'li.\!tw-mb-6')

    for offre in offres :
        infos = offre.find_element(By.CLASS_NAME,"offer--maininfo")
        company_name =""
        if(infos.find_element(By.CSS_SELECTOR, '[data-cy="companyName"]')):
            company_name = infos.find_element(By.CSS_SELECTOR, '[data-cy="companyName"]').text.strip()
        job_title, link = "", ""
        if(infos.find_element(By.CSS_SELECTOR, 'h3 a')):
            job_title = infos.find_element(By.CSS_SELECTOR, 'h3 a').text.strip()
            link = infos.find_element(By.CSS_SELECTOR, 'h3 a').get_attribute("href")
        contract_type=""
        if(infos.find_element(By.CSS_SELECTOR, '[data-cy="contract"]')):
            contract_type = infos.find_element(By.CSS_SELECTOR, '[data-cy="contract"]').text.strip()
        location=""
        if(infos.find_element(By.CSS_SELECTOR, '[data-cy="loc"] span')):
            location = infos.find_element(By.CSS_SELECTOR, '[data-cy="loc"] span').text.strip()
        
        row={
        "Company Name": company_name,
        "Job Title": job_title,
        "Contract Type": contract_type,
        "Location": location,
        "Link": link,
        }

        data.append(row)


    sleep(3)
driver.quit()



output_file_path = "data/offres.json"
with open(output_file_path, "w", encoding="utf-8") as output_file:
    json.dump(data, output_file, indent=2, ensure_ascii=False)
