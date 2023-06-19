


from datetime import datetime
from multiprocessing.sharedctypes import Value

now = datetime.now()

current_time = now.strftime("%H:%M")
print("Current Time =", current_time)
val = input('Input value: ')
print(val)
reason=input("Reason: ")
print(reason)