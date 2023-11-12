from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


driver = webdriver.Chrome()
driver.get('https://www.epam.com/')
wait = WebDriverWait(driver, 10)
accept_button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, 'onetrust-accept-btn-handler')))
accept_button.click()
menu_button = driver.find_element(By.CLASS_NAME, 'hamburger-menu__button')
menu_button.click()
theme_toggle = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'theme-switcher')))
theme_toggle.click()
theme_changed = 5
theme_label = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CLASS_NAME, 'theme-switcher-label')))
assert theme_label.text == 'Light Mode'

driver.quit()