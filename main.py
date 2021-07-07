from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException
import time
import os
email = os.environ.get("EMAIL")
password = os.environ.get("PASSWORD")
target_user = "dualipa" #the instagram accpunt whose following you want to follow
driver_path = "D:/chromedriver.exe"
driver = webdriver.Chrome(executable_path = driver_path)
driver.get("https://www.instagram.com/")

time.sleep(3)
email_entry = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
email_entry.send_keys(email)
time.sleep(2)
password_entry = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
password_entry.send_keys(password)
time.sleep(2)
log_in = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button')
log_in.click()

time.sleep(5)
close = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button')
close.click()
time.sleep(2)
close = driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')
close.click()

driver.get(f'https://www.instagram.com/{target_user}/')
time.sleep(3)
followers = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a')
followers.click()

time.sleep(3)
followers_slide = driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]')
# following_slide = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a')
for _ in range(0,10):
    driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", followers_slide)
    time.sleep(1)

follow = driver.find_elements_by_css_selector('.PZuss li button')
for n in follow:
    try:
        n.click()
        time.sleep(1)
    except ElementClickInterceptedException:
        cancel_button = driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div[3]/button[2]')
        cancel_button.click()