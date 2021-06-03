import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(chrome_options=options)
driver.maximize_window()
driver.get("https://site.com/wp-admin/edit.php")

removeImage="document.getElementsByTagName(\"img\")[0].remove()"
beforeH2 = 'document.getElementsByTagName("h2")[0].previousElementSibling.remove()'

def removeLast():
    last = driver.find_elements_by_tag_name("strong")
    for i in range(1,len(last)):
        last[-i].clear()
        

def checkBox():
    driver.switch_to.default_content()
    actions = ActionChains(driver)
    main_box = driver.find_elements_by_id('ez-toc-settings[insert-toc]')[0]
    actions.click(main_box)
    actions.perform()
    for i in range(1,7):
        driver.find_element_by_id('ez-toc-settings[heading-levels]['+str(i)+']').click()

def metaDescription(key):
    default = ""
    new = default.replace("keyword", key)
    
    #Change from Post Iframe to Default
    driver.switch_to.default_content()
    
    #Find Open Editor Button 
    driver.find_element_by_xpath('//*[@id="setting-panel-general"]/div[3]/div/a[1]').click()

    #Update replaced String with KeyWord
    driver.find_element_by_xpath('//*[@id="rank_math_description"]').send_keys(new)  

    #Add Focus Keyword
    driver.find_element_by_xpath('//*[@id="setting-panel-general"]/div[4]/div[2]/tags/span').send_keys(key)

def download(key):
    remove = 'document.getElementsByTagName("h4")[0].nextElementSibling.remove()'
    align_left = 'document.getElementsByTagName(\'h4\')[0].style.textAlign = \'left\';'
    if(bool(driver.find_elements_by_tag_name('h4'))==True):
        driver.execute_script(remove, align_left)
    else:
        find_length = len(driver.find_elements_by_tag_name('h3'))
        remove = 'document.getElementsByTagName("h3")['+str(find_length-1)+'].nextElementSibling.remove()'
        align_left = 'document.getElementsByTagName(\'h3\')['+str(find_length-1)+'].style.textAlign = \'left\';'
        print(remove, align_left)
        driver.execute_script(remove, align_left)    
    driver.switch_to.default_content()
    driver.find_element_by_id('content-html').click()
    time.sleep(7)
    download = ("")
    new_download = download.replace("keyword", key)

    #Sleep
    time.sleep(3)

    #Go to new Line and enter Text
    driver.switch_to.frame('content_ifr')
    a = bool(driver.find_elements_by_tag_name('h4'))
    if(a == True):
        driver.find_elements_by_tag_name('h4')[-1].send_keys(new_download)
    elif(a == False):
        #h3_length = driver.find_elements_by_tag_name('h3')
        #driver.find_elements_by_tag_name('h3')[-1].send_keys(Keys.ENTER)
        driver.find_elements_by_tag_name('h3')[-1].send_keys(new_download)

    #Return to Visual
    #driver.switch_to.default_content()
    time.sleep(7)
    driver.switch_to.default_content()
    driver.find_element_by_id('content-tmce').click()

driver.find_element_by_name("log").send_keys("username")
time.sleep(3)
driver.find_element_by_name("pwd").send_keys("pass")
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
key = 'My Keyword'
download(key)
time.sleep(7)
metaDescription(key)
checkBox()
time.sleep(20)