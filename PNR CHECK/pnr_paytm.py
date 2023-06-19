import urllib
import urllib.request
from time import sleep, time
from selenium import webdriver
from PIL import ImageTk, Image 
from selenium.common.exceptions import NoSuchElementException  

# driver=webdriver.Firefox()

from selenium.webdriver.firefox.options import Options

options = Options()
options.add_argument("--headless")
driver = webdriver.Firefox(options=options)

print("Checking PNR status...")
driver.get('https://paytm.com/train-tickets/pnr-status')


f = open("pnr_number.txt", "r")


# pnr=4238058443
pnr=int(f.read())
pnr_input=driver.find_element("xpath",'//*[@id="text-box"]')
pnr_input.click()
sleep(2)
pnr_input.send_keys(pnr)
submit_btn=driver.find_element("xpath",'/html/body/div/div/div[2]/div/div[2]/div[1]/div/div[2]/div[2]/div/div[6]/div/a/button')
submit_btn.click()
driver.save_screenshot("image.png")




with Image.open('image.png') as img:
    img.show()