from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()
#Task_2
#Verify that allows register a User


driver.get('https://demowebshop.tricentis.com/')
register_button = driver.find_element(By.CLASS_NAME, 'ico-register')
register_button.click()
gender_radio_button = driver.find_element(By.ID, 'gender-female')
gender_radio_button.click()
first_name = driver.find_element(By.ID, 'FirstName')
first_name.send_keys('TestFirstName')
last_name = driver.find_element(By.ID, 'LastName')
last_name.send_keys('TestLast')
email = driver.find_element(By.ID, 'Email')
email.send_keys('emai797sdklfjio6hfjksdhk893758@gmail.com')
password = driver.find_element(By.ID, 'Password')
password.send_keys('111111')
confirm_password = driver.find_element(By.ID, 'ConfirmPassword')
confirm_password.send_keys('111111')
register_button = driver.find_element(By.ID, 'register-button')
register_button.click()
success_message_element = driver.find_element(By.CLASS_NAME,'result')
assert success_message_element.is_displayed

#Verify that allows login a User

#driver.get('https://demowebshop.tricentis.com/')
logout_button = driver.find_element(By.CLASS_NAME, 'ico-logout')
logout_button.click()
login_button = driver.find_element(By.CLASS_NAME, 'ico-login')
login_button.click()
email = driver.find_element(By.ID, 'Email')
email.send_keys('email238ewuio6hfjksdhk893758@gmail.com')
password = driver.find_element(By.ID, 'Password')
password.send_keys('111111')
log_in_button = driver.find_element(By.CLASS_NAME, 'login-button')
log_in_button.click()
wait = WebDriverWait(driver, 10)
logout_button = driver.find_element(By.CLASS_NAME, 'ico-logout')
assert logout_button.is_displayed

#Verify that ‘Computers’ group has 3 sub-groups with correct names

computer_tab = driver.find_element(By.XPATH, '//a hrefico-logout')
computer_tab.click()