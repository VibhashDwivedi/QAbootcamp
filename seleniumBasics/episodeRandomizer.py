import time

from selenium import webdriver

from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By

chrome_service = Service("C:/Users/HP/Desktop/chromedriver.exe")

driver = webdriver.Chrome(service=chrome_service)

driver.get("https://episode-randomizer-vibhashdwivedi.vercel.app/")
print(driver.title)

driver.maximize_window()

time.sleep(3)

friends = driver.find_element(By.XPATH, "//div[@class='row']//div[1]//div[1]//div[1]")

friends.click()

time.sleep(3)

driver.back()

time.sleep(3)

himym = driver.find_element(By.XPATH, "//div[@class='container']//div[2]//div[1]//div[1]")
himym.click()

time.sleep(3)

driver.back()

time.sleep(3)

bigbang = driver.find_element(By.XPATH, "//div[@class='container']//div[3]//div[1]//div[1]")

bigbang.click()

time.sleep(3)

driver.back()

time.sleep(3)

