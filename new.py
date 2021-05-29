import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(r"I:\Code\WordPress_Automation\chromedriver.exe")
driver.maximize_window()
driver.get("https://crackplex.com/wp-admin/edit.php")

removeImage="document.querySelector(\"#tinymce > div:nth-child(2) > div > p:nth-child(1)\").remove()"
youAlso="document.querySelector(\"#tinymce > div > div > p:nth-child(2)\").remove()"

def returnTitle():
    pass

driver.find_element_by_name("log").send_keys("CrackPlex")
time.sleep(3)
driver.find_element_by_name("pwd").send_keys("5sUnf8pq$YAryr$1oc")
time.sleep(3)
driver.find_element_by_name("wp-submit").send_keys(Keys.ENTER)
time.sleep(5)
driver.find_element_by_class_name('row-title').click()
time.sleep(7)
driver.switch_to.frame('content_ifr')
driver.execute_script(removeImage)
driver.execute_script(youAlso)
time.sleep(10)

#driver.find_elements_by_partial_link_text("Mirror")