from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
import time
import csv

def extract_data_from_all_pages():
    s = Service('/Users/noeflandre/Downloads/geckodriver')
    driver = webdriver.Firefox(service=s)
    
    page = 1
    data = []

    while True:
        url = f'https://www.hellowork.com/fr-fr/emploi/recherche.html?k=Software+engineer&k_autocomplete=http%3A%2F%2Fwww.rj.com%2FCommun%2FPost%2FIngenieur_IT&ray=20&cod=all&d=all&p={page}&mode=pagination'
        driver.get(url)

        # Wait for the page to load and for any dynamic content
        time.sleep(5)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)

        parent_elements = driver.find_elements(By.XPATH, "//li[contains(@class, '!tw-mb-6')]")
        if not parent_elements:  # If no elements are found, assume we're at the last page
            break
        print(f"Processing page {page} - found {len(parent_elements)} parent elements.")

        for element in parent_elements:
            nested_elements = element.find_elements(By.XPATH, ".//*[contains(@class, 'tw-text-ellipsis') and contains(@class, 'tw-whitespace-nowrap') and contains(@class, 'tw-block') and contains(@class, 'tw-overflow-hidden') and contains(@class, '2xsOld:tw-max-w-[20ch]')]")
            for nested_element in nested_elements:
                text_content = nested_element.text.strip()
                if text_content:
                    data.append(text_content)
        
        # Attempt to find a link to the next page or increment page number
        page += 1

    driver.quit()
    return data

data = extract_data_from_all_pages()

# Save the data to a CSV file
csv_file_path = 'extracted_data.csv'
with open(csv_file_path, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Text Content'])
    for item in data:
        writer.writerow([item])

print(f"Data extracted and saved to '{csv_file_path}'.")
