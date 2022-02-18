from selenium import webdriver
#Creating a Firefox object
driver = webdriver.Firefox()
#driver = webdriver.Chrome()
driver.get('https://cn.bing.com/')
#driver.quit()