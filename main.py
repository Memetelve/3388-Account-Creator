from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import os, time, win32clipboard, sys

#variables
i = 0

#Getting driver for Chrome
driver = webdriver.Chrome(ChromeDriverManager().install())

#Opening 10 min mail and copying mail
driver.get("https://10minutemail.net")
driver.implicitly_wait(8)
button = driver.find_element_by_id("copy-button").click()

#Getting clipboard data
win32clipboard.OpenClipboard()
clip_board = win32clipboard.GetClipboardData()
win32clipboard.CloseClipboard()

#Opening 3388 register site
driver.get("https://www.3388.to/register?ref=6gs95b")
driver.implicitly_wait(8)
#Input data to form
form1 = driver.find_element_by_id("name")
form1.send_keys('Memetelve') 

form2 = driver.find_element_by_id("email")
form2.send_keys(clip_board)

form3 = driver.find_element_by_id("password")
form3.send_keys("Patryk to gej")

form4 = driver.find_element_by_id("confirm_password")
form4.send_keys("Patryk to gej")

button = driver.find_element_by_class_name("wibtn-primary").click()
time.sleep(5)

#going back to mail
driver.get("https://10minutemail.net")
while i == 0:
    try:
        #selecting email form 3388
        driver.find_element_by_link_text('3388 Email Verification').click()
        i = i + 1
    except:
        time.sleep(5)

#clicking link
driver.find_element_by_xpath("/html/body/div[1]/div[4]/div/div/div[4]/div/p[4]/a").click()
time.sleep(5)

#creating varaibles from strings
email = "email: " + clip_board + "\n"
password = "passowrd: Patryk to gej \n"

#opening file, writing email and password 
f = open("database.txt", "a")
f.write("_________________\n")
f.write(email)
f.write(password)
f.close()

#ending everything with slight delay
time.sleep(5)
driver.close()
sys.exit(1)
