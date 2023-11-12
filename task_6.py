from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

 

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.epam.com/')
search_button = driver.find_element(By.CLASS_NAME, 'header-search__button').click()
search_input = driver.find_element(By.ID, 'new_form_search')
search_input.send_keys('AI')
find_button = driver.find_element(By.CLASS_NAME, 'custom-search-button').click()
search_results = driver.find_element(By.XPATH, "//h2[contains(text(), '481 results for')]")
assert search_results.is_displayed
driver.quit()