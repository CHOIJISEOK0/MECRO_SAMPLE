from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome()

url = 'https://www.google.com'
driver.get(url)

driver.find_element_by_xpath("").send_keys()
driver.find_element_by_xpath("").click()