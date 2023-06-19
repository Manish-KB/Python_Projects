import urllib.request
from time import sleep, time
from selenium import webdriver

# driver= webdriver.Chrome('C:/Users/manis/Desktop/Python/chromedriver.exe')
driver=webdriver.Firefox()


driver.get('https://www.cleartrip.com/')


if(input("Permission?")):
  code_box= driver.find_element('xpath','/html/body/div[1]/div/div[2]/div/div[3]/div[2]/aside/div[4]/form/form/div/div/input')
  code_box.send_keys(input("Enter Coupon code"))
  apply_btn=driver.find_element('xpath','/html/body/div[1]/div/div[2]/div/div[3]/div[2]/aside/div[4]/form/form/div/div/input')
  print(driver.find_element('xpath','/html/body/div[1]/div/div[2]/div/div[3]/div[2]/aside/div[4]/div/div[1]/div'))
#   while( ):
#       apply_btn.click()
#       sleep(0.5)
      
      


okbtn=driver.find_element