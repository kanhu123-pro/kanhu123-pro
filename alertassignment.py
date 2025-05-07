from selenium import webdriver
import time
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.get(r"https://the-internet.herokuapp.com/javascript_alerts")
driver.maximize_window()
time.sleep(4)
#to click ok or click yes
driver.find_element(By.XPATH,"//button[text()='Click for JS Alert']").click()
time.sleep(3)
driver.switch_to.alert.accept()
time.sleep(3)
#to click ok or cancel      
driver.find_element(By.XPATH,"//button[text()='Click for JS Confirm']").click()
time.sleep(3)
driver.switch_to.alert.accept()
time.sleep(3)
#to click send key
driver.find_element(By.XPATH,"//button[text()='Click for JS Prompt']").click()
driver.switch_to.alert.send_keys("hello")
time.sleep(3)