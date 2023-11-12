from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
 

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.epam.com/about')
company_logo = driver.find_element(By.CLASS_NAME, 'header__logo-container')
company_logo.click()
wait = WebDriverWait(driver, 20)
expected_main_page_url = 'https://www.epam.com/'
#assert driver.current_url == expected_main_page_url

if driver.current_url == expected_main_page_url:
      print(f'{driver.current_url} - URL is corect')
else:
      print(f'{driver.current_url} - Title is incorrect. Expected: {expected_main_page_url}, Actual: {driver.current_url}')

driver.quit()      