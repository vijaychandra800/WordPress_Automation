import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(chrome_options=options, executable_path=r'I:\chromedriver.exe')
driver.maximize_window()
driver.get("https://crackplex.com/wp-admin/edit.php")

removeImage="document.getElementsByTagName(\"img\")[0].remove()"
beforeH2 = 'document.getElementsByTagName("h2")[0].previousElementSibling.remove()'


def removeLast():
    last = driver.find_elements_by_tag_name("strong")
    for i in range(1,5):
        last[-i].clear()

def checkBox():
    driver.switch_to.default_content()
    actions = ActionChains(driver)
    main_box = driver.find_elements_by_id('ez-toc-settings[insert-toc]')[0]
    actions.click(main_box)
    actions.perform()
    for i in range(1,7):
        driver.find_element_by_id('ez-toc-settings[heading-levels]['+str(i)+']').click()


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
time.sleep(5)
removeLast()
time.sleep(7)
checkBox()
time.sleep(10)    

