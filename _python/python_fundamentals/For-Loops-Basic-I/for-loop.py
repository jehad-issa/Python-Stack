# 1- Print all integers from 0 to 150
for x in range(0,151,1):
    print(x)

# 2-Print all the multiples of 5 from 5 to 1,000
x=5
y=5
for x in range(5,1001,y):
    print(x)

#3-count-dojo
for i in range(1,101,1):
    if (i%5==0):
        print("coding")
    if(i%10==0):
        print("coding dojo")
else:
    print(i)

#4- Add odd integers from 0 to 500,000, and print the final sum
sum=0
for i in range(1,500000,1):
    if i%2!=0:
        sum=sum+i
print(sum)

#5- Print positive numbers starting at 2018, counting down by fours.
num=2018
while num>0:
    print(num)
    num=num-4

#6-Flexible Counter
low=2
high=9
mult=3
for i in range (low, high+1):
    if i % mult == 0:
        print (i)
            




