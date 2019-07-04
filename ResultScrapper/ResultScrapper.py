from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time

chrome = webdriver.Chrome('./chromedriver')

wait = WebDriverWait(chrome, 600)

chrome.get('http://exam.msrit.edu')

x_usn = '//input[@id="usn"]'
x_captcha = '//input[@id="osolCatchaTxt0"]'
x_go = '//input[@class="buttongo"]'
x_name = '//td[@class="headingdateWhite"]'
x_USN = '//td[@style=" text-transform:uppercase;"]'
x_sgpa = '//*[@id="main"]/div/table/tbody/tr[11]/td/table/tbody/tr/td[2]/table/tbody/tr/td[4]/div/span[2]'
x_cgpa = '//*[@id="main"]/div/table/tbody/tr[11]/td/table/tbody/tr/td[2]/table/tbody/tr/td[5]/div/span[2]'

f = open("Results.txt", "a")
for i in range(1, 150):

    usn = wait.until(ec.presence_of_element_located((By.XPATH, x_usn)))
    if (i < 10):
        usn.send_keys("1MS17IS00" + str(i))
    elif i < 100:
        usn.send_keys("1MS17IS0" + str(i))
    else:
        usn.send_keys("1MS17IS" + str(i))

    captcha = wait.until(ec.presence_of_element_located((By.XPATH, x_captcha)))
    if i == 1:
        temp = input()
    captcha.send_keys(temp)

    go = wait.until(ec.presence_of_element_located((By.XPATH, x_go)))
    go.click()

    USN = wait.until(ec.presence_of_element_located((By.XPATH, x_USN)))
    name = wait.until(ec.presence_of_element_located((By.XPATH, x_name)))
    sgpa = wait.until(ec.presence_of_element_located((By.XPATH, x_sgpa)))
    cgpa = wait.until(ec.presence_of_element_located((By.XPATH, x_cgpa)))

    f.write(USN.text[6:] + "        ")
    f.write(name.text)
    for i in range(30-len(name.text)):
        f.write(" ")
    f.write(sgpa.text)
    for i in range(10-len(sgpa.text)):
        f.write(" ")
    f.write(cgpa.text + "\n")

    chrome.back()
f.close()
