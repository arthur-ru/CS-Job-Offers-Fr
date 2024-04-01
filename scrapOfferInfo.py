from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd
import json
import csv


# Initialize driver
driver = webdriver.Firefox()

# Specify path to your JSON file
json_file_path = "/data/offres.json"

# Read data from the JSON file
with open(json_file_path, 'r') as file:
    offreLinks = json.load(file)

skills = pd.read_csv('/data/hardskills.csv')


dataOffre =[]

# Access link attributes
for item in offreLinks:
    link_value = item['link']

    driver.get(link_value)
    sleep(5)
    try:
        pageContent = driver.find_element(By.CLASS_NAME,"tw-layout-inner-grid")
        secondPart = pageContent.find_element(By.CSS_SELECTOR,"section.tw-flex")
        otherInfo = secondPart.find_elements(By.CSS_SELECTOR,"ul li")
    except:
        continue
    # # Extract job title
    try:
        job_title_element = driver.find_element(By.CSS_SELECTOR, '[data-cy="jobTitle"]')
        job_title = job_title_element.text
    except:
        job_title = ""

    # # Extract company name
    try:
        company_name_element = driver.find_element(By.CLASS_NAME, "tw-text-base")
        company_name = company_name_element.text
    except:
        company_name = ""

    try:
    # Extract location
        location_elements = driver.find_elements(By.CLASS_NAME, "tw-tag-contract-s")
        location = location_elements[0].text  # Assuming the first element is the location

    # Extract the text from the element
        contract_type = location_elements[1].text 
    except:
        location=""
        contract_type=""

    try:
        salaire = driver.find_element(By.CLASS_NAME,"tw-tag-attractive-s").text
    except:
        salaire=""

    
    try:
        paragraph = pageContent.find_element(By.CLASS_NAME,"tw-typo-long-m").text
    except:
        paragraph = ""
    found_hardskills = []




    for index, row in skills.iterrows():
        if not pd.isna(row['hardskills']):
            hardSkill =  row['hardskills'].strip().lower()
            if hardSkill in paragraph.lower():
                found_hardskills.append(hardSkill)

# Print the found elements
    niveau_etude = ""
    secteur = ""
    teletravail = False
    experience =""

    try:
        teletravailElement =  secondPart.find_element(By.CLASS_NAME,"tw-tag-primary-s")
        if(teletravailElement.get_attribute("innerHTML").strip().lower().find("télétravail") != - 1):
            teletravail =True  
    except:
        teletravail = False

    for i in otherInfo:
        if(i.get_attribute("innerHTML").strip().lower().startswith("bac")):
            niveau_etude = i.get_attribute("innerHTML").strip()
        if(i.get_attribute("innerHTML").strip().lower().startswith("secteur") or i.get_attribute("innerHTML").strip().lower().startswith("service")):
            secteur = i.get_attribute("innerHTML").strip()
        if(i.get_attribute("innerHTML").strip().lower().startswith("exp.")):
            experience = i.get_attribute("innerHTML").strip()

    dataOffre.append({
            'Job Title': job_title,
            'Company Name': company_name,
            'Location': location,
            'Contract Type': contract_type,
            'Niveau Etude': niveau_etude,
            'Secteur': secteur,
            'Teletravail': teletravail,
            'Experience': experience,
            'Salaire': salaire.encode('utf-8').decode('utf-8'),
            'skills':found_hardskills
        })
    print({
            'Job Title': job_title,
            'Company Name': company_name,
            'Location': location,
            'Contract Type': contract_type,
            'Niveau Etude': niveau_etude,
            'Secteur': secteur,
            'Teletravail': teletravail,
            'Experience': experience,
            'Salaire': salaire.encode('utf-8').decode('utf-8'),
            'skills':found_hardskills
        })

    
columns = ['Job Title', 'Company Name', 'Location', 'Contract Type', 'Niveau Etude', 'Secteur', 'Teletravail', 'Experience', 'Salaire', 'skills']

df = pd.DataFrame(dataOffre,columns=columns)
df.to_csv('/data/output_file.csv', index=False)
driver.quit()