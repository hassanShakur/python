from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver = 'C:\Users\Hassan\Development\chromedriver'
driver = webdriver.Chrome(chrome_driver)

driver.get('https://www.google.com')

some_link = driver.find_element_by_link_text('Go to google')
some_link.click()

# Type & submit
search = webdriver.find_element_by_name('search')
search.send_keys('Dragon')
search.send_keys(Keys.ENTER)
