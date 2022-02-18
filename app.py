from selenium import webdriver
from selenium.webdriver.common.by import By

#creating a firefox object
driver = webdriver.Firefox()

#user credentials
username = "afilipem@gmail.com"
password = "y4KDvEfW5%s7"

driver.get('https://www.hudl.com')
print("Browser Opened and Page Loaded")

driver.implicitly_wait(5) # seconds
driver.find_element(By.XPATH,'//a[@href="'+"/login"+'"]').click()
print("Clicked on Log in button and loaded log in page")
#driver.quit()
