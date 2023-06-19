# https://us05web.zoom.us/j/85434812576?pwd=VmpyVTcvbTVDekxXME1aQjZ3NkFaZz09

import urllib.request
from time import sleep, time
from selenium import webdriver

# driver= webdriver.Chrome('C:/Users/manis/Desktop/Python/chromedriver.exe')
driver=webdriver.Firefox()


driver.get('https://us05web.zoom.us/j/85434812576?pwd=VmpyVTcvbTVDekxXME1aQjZ3NkFaZz09')

driver.switch_to.alert.accept()
