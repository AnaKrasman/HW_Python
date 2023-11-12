from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.epam.com/about/who-we-are/contact')
submit = driver.find_element(By.CLASS_NAME, "form_row")
actions = ActionChains(driver)
actions.move_to_element(submit).perform()
wait = WebDriverWait(driver, 10)
accept_button = driver.find_element(By.ID, 'onetrust-accept-btn-handler')
accept_button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, 'onetrust-accept-btn-handler')))
accept_button.click()

submit_button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.button-ui[type=submit]')))
required_input_fields = driver.find_elements(By.CLASS_NAME, 'form-component__input[aria-required=true]')

submit_button.click()

for input in required_input_fields:
    assert input.get_attribute('aria-invalid') == 'true'

driver.quit()    