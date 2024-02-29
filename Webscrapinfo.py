from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv
from bs4 import BeautifulSoup

def extract_data_from_page():
    driver = webdriver.Firefox()
    url = 'https://www.hellowork.com/fr-fr/emplois/45661282.html'
    driver.get(url)
    data = []
    # Wait for the page to load and for any dynamic content
    time.sleep(5)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    region_element = soup.find('script', string=lambda text: text and 'Region' in text)
    departement_element = soup.find('script', string=lambda text: text and 'Departement' in text)

    # Extract the content of the elements if they exist
    region = region_element.string.split("'Region': '")[1].split("'")[0] if region_element else None
    departement = departement_element.string.split("'Departement': '")[1].split("'")[0] if departement_element else None
    ville_element = soup.find('script', string=lambda text: text and 'Ville' in text)
    ville = region_element.string.split("'Ville': '")[1].split("'")[0] if ville_element else None
    metier_element = soup.find('script', string=lambda text: text and 'Metier' in text)
    metier = metier_element.string.split("'Metier': '")[1].split("'")[0] if metier_element else None
    domaine_element = soup.find('script', string=lambda text: text and 'Domaine' in text)
    domaine = domaine_element.string.split("'Domaine': '")[1].split("'")[0] if domaine_element else None
    fonction_element = soup.find('script', string=lambda text: text and 'Fonction' in text)
    fonction = fonction_element.string.split("'Fonction': '")[1].split("'")[0] if fonction_element else None
    entreprise_element = soup.find('script', string=lambda text: text and 'Nom-Entreprise' in text)
    entreprise = entreprise_element.string.split("'Fonction': '")[1].split("'")[0] if entreprise_element else None
    print("Entreprise:", entreprise)
    print("Region:", region)
    print("Departement:", departement)
    print("Ville:", ville)
    print("Metier:", metier)
    print("Domaine:", domaine)
    print("Fonction:", fonction)
    trucx = driver.find_elements(By.CSS_SELECTOR, 'li.\!tw-block')
    print(len(trucx))

data = extract_data_from_page()
#
# # Save the data to a CSV file
# csv_file_path = 'data/extracted_data.csv'
# with open(csv_file_path, 'w', newline='', encoding='utf-8') as file:
#     writer = csv.writer(file)
#     writer.writerow(['Text Content'])
#     for item in data:
#         writer.writerow([item])
#
# print(f"Data extracted and saved to '{csv_file_path}'.")
