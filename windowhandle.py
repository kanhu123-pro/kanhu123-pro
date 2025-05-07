from selenium import webdriver
import time

from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get(r"https://demowebshop.tricentis.com/login")
driver.maximize_window()
time.sleep(2)

driver.find_element(By.LINK_TEXT,"YouTube").click()
time.sleep(3)
handles=driver.window_handles
driver.switch_to.window(handles[1])
time.sleep(2)
driver.find_element(By.XPATH,'//input[@placeholder="Search"]').send_keys("selenium class")
time.sleep(3)
driver.find_element(By.XPATH,'//button[@title="Search"][1]').click()
time.sleep(3)
driver.switch_to.window(handles[0])
driver.find_element(By.ID,"small-searchterms").send_keys("computer")
time.sleep(3)
driver.find_element(By.XPATH,'//input[@type="submit"][1]').click()
time.sleep(5)