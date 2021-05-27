import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

post1="//*[@id=\"post-530\"]/td[1]/strong/a"
del_img="//*[@id=\"tinymce\"]/div/div/p[1]"

driver = webdriver.Chrome(r"C:\Users\vijay\Downloads\selenium\chromedriver.exe")
driver.maximize_window()
driver.get("https://crackplex.com/wp-admin/edit.php")
driver.find_element_by_name("log").send_keys("CrackPlex")
time.sleep(3)
driver.find_element_by_name("pwd").send_keys("5sUnf8pq$YAryr$1oc")
time.sleep(3)
driver.find_element_by_name("wp-submit").send_keys(Keys.ENTER)
time.sleep(5)
driver.find_element_by_xpath(post1).click()
#driver.find_element_by_name("post_title").send_keys(Keys.BACKSPACE)
time.sleep(7)
driver.find_element_by_xpath(del_img).send_keys(Keys.DELETE)
time.sleep(10)

#driver.close()  
