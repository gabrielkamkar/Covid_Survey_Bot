
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os

website = 'https://studenthealthoc.sa.ucsb.edu/login_dualauthentication.aspx'
chromedriver_path = 'C:\\Program Files (x86)\\chromedriver.exe'
user = 'username'
secret = 'password'

driver = webdriver.Chrome(chromedriver_path)
driver.get(website)

# driver.close() , close window
# driver.quit(), close entire browser

# have driver wait a bit just in case
# simplest way to do this
driver.implicitly_wait(2)

# clicking first link to get to login page
link_1 = driver.find_element_by_id("cmdStudentDualAuthentication")
link_1.click()

# input username and password and click login
driver.implicitly_wait(2)
username = driver.find_element_by_id('txtUsername')
password = driver.find_element_by_id('txtPassWord')

username.send_keys(user)
password.send_keys(secret)

submit = driver.find_element_by_id('cmdStandardProceed')
submit.click()

# get to covid survey page
driver.implicitly_wait(2)
link_2 = driver.find_element_by_link_text('Complete Survey')
link_2.click()

# click continue and finish the survey!
driver.implicitly_wait(2)
link_3 = driver.find_element_by_link_text('Continue')
link_3.click()

buttons = driver.find_elements_by_class_name('required')

for i in range(1,10,2):
    buttons[i].click()

finish = driver.find_elements_by_class_name('btn.btn-lg.btn-success')
finish[1].click()

# quit driver

driver.quit()


# YOU'RE DONE!!

