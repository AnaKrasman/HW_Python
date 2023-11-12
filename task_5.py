from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.epam.com/')
location_section = driver.find_element(By.ID, 'id-890298b8-f4a7-3f75-8a76-be36dc4490fd')
actions = ActionChains(driver)
actions.move_to_element(location_section).perform()
regions = driver.find_element(By.CLASS_NAME, 'js-tabs-links-list')
expected_region = ['AMERICAS', 'EMEA', 'APAC']
for region in expected_region:
    assert region in regions.text, f"expected region '{region}' not found"

region_to_switch = driver.find_element(By.LINK_TEXT, 'APAC')
assert region_to_switch.get_attribute('aria-selected') == 'false'
region_to_switch.click()
assert region_to_switch.get_attribute('aria-selected') == 'true'
driver.quit()