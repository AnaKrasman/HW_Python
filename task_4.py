from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.epam.com/')
accept_button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, 'onetrust-accept-btn-handler')))
accept_button.click()
footer = driver.find_element(By.CLASS_NAME, 'footer-container')
actions = ActionChains(driver)
actions.move_to_element(footer).perform()

policies_list = driver.find_element(By.CLASS_NAME, 'policies')
expected_policies = ['INVESTORS', 'COOKIE POLICY', 'OPEN SOURCE', 'APPLICANT PRIVACY NOTICE', 'PRIVACY POLICY', 'WEB ACCESSIBILITY']
for policy in expected_policies:
    assert policy in policies_list.text, f"expected policy '{policy}' not found"

driver.quit()    