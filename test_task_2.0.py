from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()

#Task_2

#Verify that allows register a User
#Change email.send_keys('emai79jio6hfjksdhk893758@gmail.com') before run

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
email.send_keys('emai09009hf53875837584iu34893758@gmail.com')
password = driver.find_element(By.ID, 'Password')
password.send_keys('111111')
confirm_password = driver.find_element(By.ID, 'ConfirmPassword')
confirm_password.send_keys('111111')
register_button = driver.find_element(By.ID, 'register-button')
register_button.click()
success_message_element = driver.find_element(By.CLASS_NAME,'result')
assert success_message_element.is_displayed

#Verify that allows login a User

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

computers_menu = driver.find_element(By.CSS_SELECTOR, "ul[class='list']>li>a[href='/computers']")
computers_menu.click()
wait = WebDriverWait(driver, 10)
submenu_computers = driver.find_element(By.CSS_SELECTOR, "ul[class='list']")
expected_submenu_items = ["Desktops", "Notebooks", "Accessories"]
for item in expected_submenu_items:
    assert item in submenu_computers.text, f"expected item '{item}' not found"

#Verify that allows sorting items (different options)

desktops_menu = driver.find_element(By.CSS_SELECTOR, "ul[class='sublist']>li>a[href='/desktops']")
desktops_menu.click()
wait = WebDriverWait(driver, 10)
sorting_dropdown = Select(driver.find_element(By.CSS_SELECTOR, "select#products-orderby"))
sorting_options = ["Position", "Name: A to Z", "Name: Z to A", "Price: Low to High", "Price: High to Low", "Created on"]
for option in sorting_options:
    sorting_dropdown = Select(driver.find_element(By.CSS_SELECTOR, "select#products-orderby"))
    sorting_dropdown.select_by_visible_text(option)

sorting_dropdown = Select(driver.find_element(By.CSS_SELECTOR, "select#products-orderby"))
sorting_dropdown.select_by_visible_text(sorting_options[4])
all_products = driver.find_elements(By.CLASS_NAME, 'actual-price');
assert all_products[0].text == '1800.00'


#Verify that allows changing number of items on page

total_items = 4
items_per_page_dropdown = Select(driver.find_element(By.CSS_SELECTOR, "select#products-pagesize"))
items_per_page_options = [4, 8, 12]
for option in items_per_page_options:
    items_per_page_dropdown = Select(driver.find_element(By.CSS_SELECTOR, "select#products-pagesize"))
    items_per_page_dropdown.select_by_visible_text("4")
    displayed_items = driver.find_elements(By.CSS_SELECTOR, "div.product-item")
    assert len(displayed_items) == min(total_items, option), f"Expected {min(total_items, option)} items per page, but found {len(displayed_items)}"

