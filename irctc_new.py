
import urllib.request
from time import sleep, time
from selenium import webdriver

# driver= webdriver.Chrome('C:/Users/manis/Desktop/Python/chromedriver.exe')
driver=webdriver.Firefox()


driver.get('https://www.irctc.co.in/nget/train-search')
sleep(2)

loginbtn=driver.find_element("xpath",'/html/body/app-root/app-home/div[1]/app-header/div[2]/div[2]/div[1]/a[1]')
loginbtn.click()
sleep(1)
logininput=driver.find_element("xpath",'//*[@id="8204514"]')
logininput.send_keys('sumithtrip')
passwordinput=driver.find_element("xpath",'//*[@id="1252662"]')
passwordinput.send_keys('svc413')
sok=driver.find_element("xpath",'/html/body/app-root/app-home/div[3]/app-login/p-dialog[1]/div/div/div[2]/div[2]/div/div[2]/div[2]/div[2]/form/span/button')
sleep(10)
#open file in write and binary mode
# with open('Logo.png', 'wb') as file:
# #identify image to be captured
#    l = driver.find_element('xpath','/html/body/app-root/app-home/div[3]/app-login/p-dialog[1]/div/div/div[2]/div[2]/div/div[2]/div[2]/div[2]/form/div[4]/div/app-nlp-captcha/div/div[2]/div/div[1]/div[8]/div/div/div/img')
# #write file
#    file.write("Logo.png")
# # if(input("Enter 5 when clicked")==5):

captcha=driver.find_element("xpath",'//*[@id="captcha"]')
# cin=input("Enter captcha: ")
# captcha.click()
# captcha.send_keys("cin")                            
sleep(5)
sok.click()
sleep(15)
source=driver.find_element("xpath",'/html/body/app-root/app-home/div[3]/div/app-main-page/div/div/div[1]/div[2]/div[1]/app-jp-input/div/form/div[2]/div[1]/div[1]/p-autocomplete/span/input')
dest=driver.find_element("xpath",'/html/body/app-root/app-home/div[3]/div/app-main-page/div/div/div[1]/div[2]/div[1]/app-jp-input/div/form/div[2]/div[1]/div[2]/p-autocomplete/span/input')
source.send_keys(input("Enter From station"))
dest.send_keys(input("Enter To station"))
date=driver.find_element("xpath",'/html/body/app-root/app-home/div[3]/div/app-main-page/div/div/div[1]/div[2]/div[1]/app-jp-input/div/form/div[2]/div[2]/div[1]/p-calendar/span/input')
date.send_keys(input("Enter date us dd/mm/yyyy format"))
search=driver.find_element("xpath",'/html/body/ap0p-root/app-home/div[3]/div/app-main-page/div/div/div[1]/div[2]/div[1]/app-jp-input/div/form/div[5]/div/button')



