import urllib.request
from time import sleep, time
from selenium import webdriver

# driver= webdriver.Chrome('C:/Users/manis/Desktop/Python/chromedriver.exe')
driver=webdriver.Firefox()

# print("opening Youtube")
driver.get('https://www.youtube.com')
search=driver.find_element('xpath','/html/body/ytd-app/div[1]/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div[1]/div[1]/input')
search.click()
search.clear()
search.send_keys(input("What do you want to search"))
search_btn=driver.find_element('xpath','/html/body/ytd-app/div[1]/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/button')
search_btn.click()