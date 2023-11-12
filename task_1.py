from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
import os
import os.path

driver = webdriver.Chrome()
driver.maximize_window()

#Task_1

expected_title = 'EPAM | Software Engineering & Product Development Services'

driver.get('https://www.epam.com/')
actual_title = driver.title
if actual_title == expected_title:
      print(f'{driver.name} - Title is correct: {actual_title}')
else:
      print(f'{driver.name} - Title is incorrect. Expected: {expected_title}, Actual: {actual_title}')

driver.quit()