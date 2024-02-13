from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd

# On crée une instance du web-driver Firefox et on va sur la page de eBay.fr
driver = webdriver.Firefox()
driver.get("https://www.hellowork.com/fr-fr/")

# En fonction de notre connexion et des performances de notre machine, il faudra attendre que la page charge avant de passer à la suite
sleep(2)

# Trouver l'élément de la barre de recherche par son ID
search_bar = driver.find_element(By.CSS_SELECTOR, 'input[name="k"]')
search_bar.send_keys("Software Engineer")
search_bar.send_keys(Keys.ENTER)



sleep(5)
# Fermer le navigateur une fois que la boucle est terminée
driver.quit()