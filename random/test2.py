from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# connect to google.com
driver = webdriver.Chrome(options=Options())

driver.get("https://the-internet.herokuapp.com/tinymce")

driver.find_element_by_xpath("//span[normalize-space()='Format']").click()

driver.find_element_by_xpath("//div[contains(text(),'Formats')]").click()

driver.find_element_by_xpath("//div[contains(text(),'Headings')]").click()

driver.find_element_by_xpath("//h1[normalize-space()='Heading 1']").click()



# driver.quit()
