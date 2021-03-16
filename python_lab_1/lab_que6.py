#you live 4 miles from university.The bus drives 25 mph but

d=4
velocity=25
time_taken=((d/velocity)*60)
#2 mins in each stop
time_spend=20
total_time=time_taken+time_spend
print(f"total time taken by bus is {total_time}")

j1=((1/7)*60)
j2=((2/15)*60)
j3=((1/7)*60)
total_walk_time=j1+j2+j3
print(f"Time taken by running is {total_walk_time}")
if (total_time>total_walk_time):
    print("Taking bus is slower than running")

else:
    print("Taking bus is faster than running")



