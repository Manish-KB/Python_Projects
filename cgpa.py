print("Welcome to CGPA calculator")
# s1=float(input("Enter Sem 1 SGPA: "))*21
# s2=float(input("Enter Sem 2 SGPA: "))*21
# s3=float(input("Enter Sem 3 SGPA: "))*24
# s4=float(input("Enter Sem 4 SGPA: "))*24
# s5=float(input("Enter Sem 5 SGPA: "))*24
# print("CGPA: "+str( (s1+s2+s3+s4+s5)/ 114))
nSum=0;
dSum=0;
n=int(input("Enter number of semesters: "))
for i in range(n):
    x=float(input("Enter Sem "+str(i+1)+ " SGPA: "))
    y=int(input("Enter Sem "+str(i+1)+ " Total Credits: "))
    nSum+=(x*y)
    dSum+=y
print("CGPA: "+str( (nSum/dSum)))
k=input("Enter 1 to exit ")

# <iframe src="https://trinket.io/embed/python/8e1adac210" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
