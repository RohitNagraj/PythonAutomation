from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

#chromedriver path
driver = webdriver.Chrome('G:\\Work\\PythonAutomation\\WhatsappMessaging\\chromedriver.exe')

driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver, 600)

#Friend's name
target = '"Vignesh"'

#Message
string = "Messaging with Python"

x_arg = '//span[contains(@title,' + target + ')]'  #XPATH to find the chat window
group_title = wait.until(EC.presence_of_element_located((By.XPATH, x_arg)))
group_title.click()

inp = "//div[@contenteditable='true']" #XPATH to find the message box
box = wait.until(EC.presence_of_element_located((By.XPATH, inp)))

for i in range(5): #Sending same message 5 times
    box.send_keys(string + Keys.ENTER)
    time.sleep(1)
