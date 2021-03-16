lst={1,2,3,4,5,6,7,8,9,10}
n=len(lst)
print(len(lst))
sum=n*(n+1)/2
print(sum)

num=int(input("Enter the num :"))
if num<0:
    print("Enter the positive number")

else:
    sum=0
while(num>0):
        sum=sum+num
        num=num-1
print("The sum is",sum)        


