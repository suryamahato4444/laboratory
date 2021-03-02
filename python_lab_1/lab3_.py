'''given the integer N-the number of minutes that is passed mid night
.how many hours and minutes are displayed on the 24 hour digital clock?
The program should print two numbers:the numbers of hour(between 0 and 23)
and the number of minutes (between 0 and 59)'''
#hour=int(input("Enter the hour passed mid night: "))
#minute=int(input("Enter the minute passed :"))

#print("the hour and minutes displayed is",hour,'and',minute)
N=int(input("Enter the min passed mid night:"))
hours=(N//60)
minutes=(N%60)
print(f"The hours is {hours}")
print(f"the minutes is{minutes}")
print(f"its {hours}:{minutes}")