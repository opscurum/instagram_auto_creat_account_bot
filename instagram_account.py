from selenium import webdriver
import random
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import accountInfoGenerator as account

#import getVerifCode as verifiCode


browser= webdriver.Firefox()
browser.get("http://www.instagram.com/accounts/emailsignup/")
time.sleep(8) 
name = account.username()

#Fill the email value
email_field = browser.find_element(By.NAME,'emailOrPhone')
email_field.send_keys(account.generatingEmail())
print(account.generatingEmail())

#Fill the fullname value
fullname_field = browser.find_element(By.NAME,'fullName')
fullname_field.send_keys(account.generatingName())
print(account.generatingName())

#Fill username value
username_field = browser.find_element(By.NAME,'username')
username_field.send_keys(name)
print(name)

#Fill password value
password_field  = browser.find_element(By.NAME,'password')
password_field.send_keys('123_'+name) #You can determine another password here.

#enter Sign up
WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Sign up']"))).click()  

time.sleep(8)

#Birthday verification
browser.find_element(By.XPATH,("//*[@id='react-root']/section/main/div/article/div/div[1]/div/div[4]/div/div/span/span[1]/select/option[3]")).click()        #XPATH1

WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='react-root']/section/main/div/article/div/div[1]/div/div[4]/div/div/span/span[2]/select"))).click()

browser.find_element(By.XPATH,("//*[@id='react-root']/section/main/div/article/div/div[1]/div/div[4]/div/div/span/span[2]/select/option[12]")).click()       #XPATH2

WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='react-root']/section/main/div/article/div/div[1]/div/div[4]/div/div/span/span[3]/select"))).click()

browser.find_element(By.XPATH,("//*[@id='react-root']/section/main/div/article/div/div[1]/div/div[4]/div/div/span/span[3]/select/option[26]")).click()        #XPATH3

WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='react-root']/section/main/div/article/div/div[1]/div/div[6]"))).click()      #click next



#Enter the confirmation code sent to the e-mail...



browser.find_element(By.XPATH,("/html/body/div[1]/section/main/div/div/div/div/button")).click()

time.sleep(2)


browser.find_element(By.XPATH,("/html/body/div[4]/div/div/div/div[3]/button[2] ")).click() #Notification Place


print('Registering....')


#logout
browser.find_element(By.XPATH, ("//*[@id='react-root']/section/nav/div[2]/div/div/div[3]/div/div[5]/span/img")).click()
browser.find_element(By.XPATH, ( "//*[@id='react-root']/section/nav/div[2]/div/div/div[3]/div/div[5]/div[2]/div[2]/div[2]/div[2]/div")).click()