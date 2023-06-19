import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

while True:
    email_id=input("Enter Your Email ID: ")
    print(email_id)
    if (int(input("Is the entered email correct? Press 1 to proceed. Else press 0: ")))==1:
        break
    
x=0
p=[]
i=[]

print("To stop giving the input give page number and item number as 0")
while True:
    y=int(input("Page Number: "))
    z=int(input("Item Number: "))
    if( y>0 and y<57 and z>0 and z<9):
       p.append(y)
       i.append(z)
       x+=1
    elif y==0 and z==0 :
        print("Input Stopped")
        break
    else:
        print("Invalid Input")
   
print("Pg Item") 
for n in range(0,x) :
    print(str(p[n])+"  "+str(i[n]))


r=int(input("press 1 to proceed else 0: "))

if r==1:    
  
    #uncomment the following and comment driver= webdriver.Chrome('C:/Users/manis/Desktop/Python/chromedriver.exe') below to run this prog without opening the browser(headless mode)
    # options = webdriver.ChromeOptions()
    # options.headless = True
    # driver = webdriver.Chrome('C:/Users/manis/Desktop/Python/chromedriver.exe', options=options)
    directory = os.getcwd()
    # driver= webdriver.Chrome('C:/Users/manis/Desktop/Python/chromedriver.exe')
    driver= webdriver.Chrome(directory+'/chromedriver.exe')
    print(directory)

    driver.get('https://docs.google.com/forms/d/e/1FAIpQLSfAVItAwmhqxVFxPZ4tNC1pr0_3O_sjKChvepanipegNeLVAg/viewform')

    email=driver.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div[1]/div[2]/div[1]/div/div[1]/input')
    page_base_1="/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div/span/div/div["
    page_base_2="]/label/div/div[1]/div/div[3]/div"
    item_base_1="/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div/span/div/div["
    item_base_2="]/label/div/div[1]/div/div[3]/div"




        
    for n in range(0,x) :
        
        email=driver.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div[1]/div[2]/div[1]/div/div[1]/input')
        email.click()
        email.send_keys(email_id)
        page=page_base_1+str(p[n])+page_base_2
        item=item_base_1+str(i[n])+item_base_2
        
        # Select Page Number
        (driver.find_element("xpath",page)).click()

        #  Select Item Number
        (driver.find_element("xpath",item)).click()

        
        
   
        #Click on Submit    
        
        (driver.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div/span')).click()
        
        # click on Submit new form
        (driver.find_element("xpath",'/html/body/div[1]/div[2]/div[1]/div/div[4]/a')).click() 
    if x==1:
        print("Form Submitted Succesfully ("+(str(x)+" item)")) 
    elif x>1:
        print("Form Submitted Succesfully ("+(str(x)+" item(s))"))    
        
        
print("Operation Terminated")     
       
driver.close()