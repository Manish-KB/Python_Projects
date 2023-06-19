
from time import sleep, time
from selenium import webdriver

driver= webdriver.Chrome('C:/Users/manis/Desktop/Python/chromedriver.exe')


driver.get('https://www.youtube.com/')

searchBox = driver.find_element("xpath",'/html/body/ytd-app/div[1]/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div[1]/div[1]/input') 
searchBox.send_keys('mark rober')
searchButton=driver.find_element("xpath",'/html/body/ytd-app/div[1]/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/button')
searchButton.click()

searchButton=driver.find_element("xpath",'//*[@id="guide-button"]')
searchButton.click()