import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

chrome_services = Service('C:/Users/HP/Desktop/chromedriver.exe')
driver = webdriver.Chrome(service=chrome_services)

driver.get('https://demoqa.com/')
print(driver.title)

print(driver.current_url)

driver.maximize_window()
time.sleep(5)
driver.minimize_window()


time.sleep(5)
driver.get('https://demoqa.com/elements')

driver.back()

print(driver.current_url)

driver.forward()

print(driver.current_url)

driver.close()