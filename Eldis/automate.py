import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


service = Service(executable_path="D:\DEV\Selenium\Drivers\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://google.com")

input_element = driver.find_element(By.CLASS_NAME, "gLFyf") 
input_element.send_keys("Eldis Einsatznachbearbeitung")

time.sleep(3)
driver.quit()