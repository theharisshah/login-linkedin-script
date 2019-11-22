from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('/Users/harisshah/Downloads/chromedriver')

driver.get('https://www.linkedin.com')
driver.fullscreen_window()
driver.implicitly_wait(30)
email = driver.find_element_by_name('session_key')
driver.implicitly_wait(30)
email.send_keys('example@email.com')
driver.implicitly_wait(30)
password = driver.find_element_by_name('session_password')
driver.implicitly_wait(30)
password.send_keys('Password')
driver.implicitly_wait(30)
driver.find_elements_by_class_name('sign-in-form__submit-btn')[0].click()