s=int(input("Enter the second: "))
day=s//(24*60*60)
rem1=s%(24*60*60)
hour=rem1/(60*60)
rem2=rem1%(60*60)
minute=rem2/60



# hour=s//(60*60)
# minute=s//60
print(f"The total time is {day} days : {hour} hour : {minute} mins")

