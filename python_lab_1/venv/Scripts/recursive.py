def factorial(num):
    print("factorial call with num"+str(num))
    if num<0:
        return "number cannot be negative"
    elif num==1 or num==0:
        return 1
    else:
        result=num*factorial(num-1)
        print("intermediate result for:num",'*factorial(num-1):',result)
        return result
print(factorial(4))