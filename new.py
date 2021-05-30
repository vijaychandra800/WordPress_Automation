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

def metaDescription():
    default = "Soft Crack, Download Soft Crack For Free. Activate Soft For Free. How to Crack Soft 2021. Soft Free Download."
    new = default.replace("Soft", download.key)
    
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
    align_left = 'document.getElementsByTagName("h4")[0].style.textAlign = "left"'
    driver.switch_to.default_content()
    driver.find_element_by_id('content-html').click()
    download = """<h4>How To Crack Tally</h4>
<ol>
 	<li>Download <a href="https://winfreewares.xyz/full-setup-download/"><strong>Tally Crack</strong></a> from the below links.</li>
 	<li>Uninstall any previous version of Softwares using <a href="https://crackplex.com/revo-uninstaller-pro-crack-latest-version-direct-link/">Revo Uninstaller Pro Crack</a>.</li>
 	<li>Install the software but don't run it.</li>
 	<li>Now Run the Patch file.</li>
 	<li>You've Successfully cracked Tally Pro for Free, Enjoy a Full Version of the software for Free.</li>
</ol>
<h4>Tally Crack Direct Download Links</h4>"""
    new_download = download.replace("Tally", key)

    #Go to new Line and enter Text
    driver.find_element_by_tag_name('h4').send_keys(Keys.ENTER, new_download)

    #Return to Visual
    #driver.switch_to.default_content()
    driver.find_element_by_id('content-tmce').click()


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
download('eTally Pro')
time.sleep(7)
metaDescription()
time.sleep(7)
checkBox()
time.sleep(20)


