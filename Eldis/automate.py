import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from getpass import getpass
from bs4 import BeautifulSoup

username = input("Benutzer: ")
password = getpass("Passwort: ")



BetSys = os.name  
print("Betriebssystem:", BetSys)
if BetSys == "nt":  # Windows
    service = Service(executable_path=r"D:\DEV\Selenium\Drivers\chromedriver-win64\chromedriver.exe")
else:  # macOS
    service = Service(executable_path=r"/Users/janw/dev/chromedriver-mac-arm64/chromedriver")

driver = webdriver.Chrome(service=service)
driver.maximize_window()

driver.get("https://einsatznachbearbeitung.bayern.de/login")
time.sleep(1)

driver.find_element("id", "username").send_keys(username)
driver.find_element("id", "password").send_keys(password)
driver.find_element(By.XPATH, "/html/body/div/div[1]/section/main/div[1]/div[2]/form/div[3]/button").click()
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div/div/div/div/main/div/div/nav/ul/li/ul/li[1]/ul/li[1]/a/span").click() #Klicken auf Einsatzdaten
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div/div/div/div/main/div[3]/div/div/div[2]/div[1]/div[1]/button[2]").click()  #Klicken auf Anzahl Datensätze
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="page-length-100"]').click() #Klicken auf Radio Button 100 Einsätze
time.sleep(3)
schlagwort_zellen = driver.find_elements(By.CSS_SELECTOR, '[data-cell-field="schlagwort"]')


html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

table1 = soup.find("table",{"class":"data-table"})
table2 = soup.find('tbody')
table3 = soup.find_all('tr')
t = 1
Einsatz = []
Einsatzliste = []
for tr in table3:
    table4 = tr.find_all('td')
    if len(Einsatz) != 0:
        toprint = Einsatz[7],Einsatz[5],Einsatz[3],Einsatz[2]
        print(toprint)
    Einsatz = []
    for td in table4:
        Einsatz.append(td.get_text())
    
"""
for item in Einsatzliste:
    print(t, item)
    t += 1

# Die Texte extrahieren und in eine Liste schreiben
schlagwort_liste = [zelle.text for zelle in schlagwort_zellen]

print("Gefundene Schlagworte:")
for eintrag in schlagwort_liste:
    print(eintrag)
    
"""
time.sleep(1)

driver.find_element(By.XPATH, '/html/body/div[1]/header/div/ul/li[2]/a').click() #Ausloggen
driver.quit()