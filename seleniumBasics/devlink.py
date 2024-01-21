import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_service = Service("C:/Users/HP/Desktop/chromedriver.exe")

driver = webdriver.Chrome(service=chrome_service)
driver.get("https://dev-link-project.vercel.app/")
print(driver.title)
driver.maximize_window()

username = driver.find_element(By.NAME, "username")
username.send_keys("Akshat")

password = driver.find_element(By.NAME, "password")
password.send_keys("1234rtyu")

login_btn = driver.find_element(By.XPATH, "//button[normalize-space()='Login']")
login_btn.click()

time.sleep(3)

driver.get("https://dev-link-project.vercel.app/myprofile")

time.sleep(3)

driver.back()


driver.get("https://dev-link-project.vercel.app/createpost")

post_title = driver.find_element(By.NAME, "title")
post_title.send_keys("This is a post")

post_body = driver.find_element(By.NAME, "content")
post_body.send_keys("This is the body of the post")

post_btn = driver.find_element(By.ID, "publish")
post_btn.click()

driver.get("https://dev-link-project.vercel.app/myprofile")

edit_btn = driver.find_element(By.XPATH, "//button[normalize-space()='Edit']")
edit_btn.click()

signout_btn = driver.find_element(By.XPATH, "//button[normalize-space()='SIGN OUT']")
signout_btn.click()

click_here = driver.find_element(By.XPATH, "//button[normalize-space()='OK']")
click_here.click()



time.sleep(3)

username2 = driver.find_element(By.NAME, "username")
username2.send_keys("Prachi")

password2 = driver.find_element(By.NAME, "password")
password2.send_keys("1234rtyu")

login_btn2 = driver.find_element(By.XPATH, "//button[normalize-space()='Login']")
login_btn2.click()
time.sleep(3)
