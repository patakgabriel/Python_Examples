from selenium import webdriver
from getpass import getpass
import time

usr = input("Enter your email: ")
pwd = getpass("Enter your password: ")

chrome_path = r"C:\Users\Gabriel\AppData\Local\Programs\Python\Python36-32\chromedriver.exe"
driver = webdriver.Chrome(chrome_path)
driver.get("https://www.linkedin.com/")

username_box = driver.find_element_by_id("login-email")
username_box.send_keys(usr)

password_box = driver.find_element_by_id("login-password")
password_box.send_keys(pwd)

login_btn = driver.find_element_by_id("login-submit")
login_btn.submit()

network_btn = driver.find_element_by_id("mynetwork-nav-item")
network_btn.click()
navbar= driver.find_element_by_id("extended-nav")

action = webdriver.common.action_chains.ActionChains(driver)
for x in range (0,100):
    time.sleep(1)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    
driver.execute_script("window.scrollTo(0, 0)") 

for x in range(0, 100):
    action.move_to_element_with_offset(navbar, 553, 461)#FIXME can be improve with get resolution and %
   
    action.click()
    action.perform()
    action.move_to_element_with_offset(navbar, 624, 255)#FIXME can be improve with get resolution and %
    
    action.click()
    action.perform()

