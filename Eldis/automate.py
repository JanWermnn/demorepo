import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from getpass import getpass

username = input("Benutzer: ")
password = getpass("Passwort: ")

BetSys = os.name  
print("Betriebssystem:", BetSys)

service = Service(executable_path=r"D:\DEV\Selenium\Drivers\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://einsatznachbearbeitung.bayern.de/login")

time.sleep(1)

driver.find_element("id", "username").send_keys(username)
driver.find_element("id", "password").send_keys(password)
driver.find_element(By.XPATH, "/html/body/div/div[1]/section/main/div[1]/div[2]/form/div[3]/button").click()

time.sleep(10)
driver.quit()