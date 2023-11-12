from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait



driver = webdriver.Chrome()
driver.maximize_window()
expected_title = 'EPAM Ukraine - найбільша ІТ-компанія в Україні | Вакансії'
driver.get('https://www.epam.com/')
accept_button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, 'onetrust-accept-btn-handler')))
accept_button.click()
language_toggle = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CLASS_NAME, 'location-selector__button')))
language_toggle.click()
ua_language = driver.find_element(By.PARTIAL_LINK_TEXT,'Україна')
ua_language.click()
wait = WebDriverWait(driver, 20)
actual_title = driver.title
if actual_title == expected_title:
      print(f'{driver.name} - Title is correct: {actual_title}')
else:
      print(f'{driver.name} - Title is incorrect. Expected: {expected_title}, Actual: {actual_title}')

driver.quit()