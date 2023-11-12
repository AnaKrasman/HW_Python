from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.epam.com/about')

download_link = driver.find_element(By.CSS_SELECTOR, '.button-ui-23.btn-focusable[download]')
actions = ActionChains(driver)
actions.move_to_element(download_link).perform()
accept_button = driver.find_element(By.ID, 'onetrust-accept-btn-handler')
accept_button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, 'onetrust-accept-btn-handler')))
accept_button.click()
driver.get("chrome://downloads");
wait = WebDriverWait(driver, 10).until(EC.title_is('Downloads'))
wrapper = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'downloads-manager')))
wrapper1 = driver.execute_script(
                "return arguments[0].shadowRoot", wrapper)
wrapper2 = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#downloadsList downloads-item')))

fileName = driver.execute_script(
                "return arguments[0].shadowRoot.querySelector('#downloadsList downloads-item')", wrapper2)
                
print(fileName)
expected_filename = 'EPAM_Corporate_Overview_Q3_october'
expected_extension = '.pdf' 



driver.quit()