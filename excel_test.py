# import xlwt
  
# import xlrd as xl                             #Import xlrd package
# loc = ("C:/Users/manis/Desktop/Python/test.xlsx")          #Giving the location of the file 
  



# wb = xl.open_workbook(loc)                    #opening & reading the excel file
# s1 = wb.sheet_by_index(0)                     #extracting the worksheet
# s1.cell_value(0,0)                            #initializing cell from the excel file mentioned through the cell position
  

# print("No. of rows:", s1.nrows)               #Counting & Printing thenumber of rows & columns respectively
# print("No. of columns:", s1.ncols) 

# workbook = xlwt.Workbook() 
  
# sheet = workbook.add_sheet("Sheet1")
  
# # Specifying style
# style = xlwt.easyxf('font: bold 1')
  
# # Specifying column
# sheet.write(0, 0, 'SAMPLE', style)


#import xlwt module 
import xlwt  
 #import xlrd module 
import xlrd  #from xlutils module I'll call copy class
from xlutils.copy import copy 
    #open the excel file
rb = xlrd.open_workbook ('test.xlsx') 
       #make a writable copy of the opened excel file
wb = copy (rb)  
       # #read the first sheet to write to within the writable copy
w_sheet = wb.get_sheet(0) 
       #  #write or modify the value at first row
w_sheet.write(0, 1, 'Modified!')
wb.save('test.xlsx')