import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(r"D:\VSCode\WordPress_Automation\chromedriver.exe")
driver.maximize_window()
driver.get("https://crackplex.com/wp-admin/edit.php")

removeImage="document.getElementsByTagName(\"img\")[0].remove()"
beforeH2 = 'document.getElementsByTagName("h2")[0].previousElementSibling.remove()'


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
driver.execute_script(beforeH2)
time.sleep(10)
mirror = driver.find_elements_by_partial_link_text("Mirror")
#for i in range(0,2):
 #   driver.find_elements_by_partial_link_text("Mirror")[i].clear()

time.sleep(10)    