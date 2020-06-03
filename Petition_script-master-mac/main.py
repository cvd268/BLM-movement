from selenium import webdriver
import time
import random
from random import randrange
import os

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")

driver = webdriver.Chrome((os.getcwd() + "/Petition_script-master-mac/chromedriver"))
#add info
first_name = ''
last_name = ''
email = '@gmail.com'

# might need to change directory path
file1 = open((os.getcwd() + "/Petition_script-master-mac/change_urls.txt"), 'r')
urls = file1.readlines()
first_time = True

for url in urls:
    try:
        time.sleep(10)
        driver.get(url)

        if first_time:
            # login
            inputElement = driver.find_element_by_id("firstName")
            inputElement.send_keys(first_name)

            inputElement = driver.find_element_by_id("lastName")
            inputElement.send_keys(last_name)

            inputElement = driver.find_element_by_id("email")
            inputElement.send_keys(email)

            first_time = False

        driver.find_element_by_xpath('//button[normalize-space()="Sign this petition"]').click()
        # wait 5 seconds for web page to load
        time.sleep(5)
        driver.find_element_by_xpath("//button[normalize-space()='No, I'll share instead']").click()

        time.sleep(5)
        driver.find_element_by_xpath("//button[normalize-space()='Send an email']").click()

    except Exception as e:
        print(url, e)
    
    break

time.sleep(5)
driver.quit()
