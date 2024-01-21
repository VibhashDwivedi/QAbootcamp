import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_service = Service("C:/Users/HP/Desktop/chromedriver.exe")

driver = webdriver.Chrome(service=chrome_service)
driver.get("https://www.saucedemo.com/v1/")
print(driver.title)

username = driver.find_element(By.ID, "user-name")
username.send_keys("standard_user")

password = driver.find_element(By.NAME, "password")
password.send_keys("secret_sauce")

login_btn = driver.find_element(By.XPATH, "//input[@id='login-button']")
login_btn.click()

cart = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
if cart.is_displayed():
    print('user logged in')
else:
    print('user not logged in')


add_to_cart = driver.find_element(By.XPATH, "//body[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[3]/div[3]/button[1]")
add_to_cart.click()

cart = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
cart.click()

checkout = driver.find_element(By.XPATH, "//a[normalize-space()='CHECKOUT']")
checkout.click()

first_name = driver.find_element(By.ID, "first-name")
first_name.send_keys("John")

last_name = driver.find_element(By.ID, "last-name")
last_name.send_keys("Doe")

postal_code = driver.find_element(By.ID, "postal-code")
postal_code.send_keys("12345")

continue_btn = driver.find_element(By.XPATH, "//input[@value='CONTINUE']")
continue_btn.click()

finish = driver.find_element(By.XPATH, "//a[normalize-space()='FINISH']")
finish.click()

image = driver.find_element(By.CLASS_NAME, "pony_express")
if image.is_displayed():
    print('Order placed successfully')
else:
    print('Order not placed')
        

time.sleep(3)

driver.close()

