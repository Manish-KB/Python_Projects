import urllib
import urllib.request
from time import sleep, time
from selenium import webdriver
from PIL import ImageTk, Image 
from selenium.common.exceptions import NoSuchElementException  


# creating a simple tkinter window
# if you are using python2
# use import Tkinter as tk
# Import required libraries
from tkinter import *
from PIL import ImageTk, Image
from PIL import Image
import climage
  
# converts the image to print in terminal
# inform of ANSI Escape codes



# driver= webdriver.Chrome('C:/Users/manis/Desktop/Python/chromedriver.exe')
driver=webdriver.Firefox()


driver.get('https://www.indianrail.gov.in/enquiry/PNR/PnrEnquiry.html?locale=en')





print("Opening the Website...")
pnr=4238058443
pnr_input=driver.find_element("xpath",'//*[@id="inputPnrNo"]')
pnr_input.click()
pnr_input.send_keys(pnr)
submit_btn=driver.find_element("xpath",'//*[@id="modal1"]')
submit_btn.click()
sleep(2)
print("Saving Captch Image...")
# img = driver.find_element("xpath",'//*[@id="CaptchaImgID"]')
# src = img.get_attribute('src')
# urllib.request.urlretrieve(src, "captcha.png")





driver.save_screenshot("image.png")



captcha=int(eval(input("Enter the captcha problem (Enter 0 if the captcha does not appear): ")))
while(captcha==0):
    driver.save_screenshot("image.png")
    captcha=int(eval(input("Enter the captcha problem: ")))
    
 
captcha_input=driver.find_element("xpath",'//*[@id="inputCaptcha"]')
captcha_input.click()
captcha_input.clear()
captcha_input.send_keys(captcha)
sbmt=driver.find_element("xpath",'//*[@id="submitPnrNo"]')
sbmt.click()   

# try:
#     driver.find_element("xpath",'//*[@id="errorResultmodal"]')
# except NoSuchElementException:
#         driver.save_screenshot("image.png")
#         captcha=int(eval(input("Enter the captcha problem: ")))                     
sleep(2)
driver.find_element("xpath",'//*[@id="disha-banner-close"]').click()
driver.find_element("xpath",'/html/body/div[5]/div[3]/img').click()
driver.save_screenshot("image.png")
# with Image.open('image.png') as img:
#     img.show()

