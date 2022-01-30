# 1-Countdown
def count_down (num):
    arr=[]
    for i in range(num,-1,-1):
        arr.append(i)
    return arr
print (count_down(10))
        
# 2-Print and Return
def print_and_return(list):
    print(list[0])
    return list[1]
print (print_and_return([1,5]))

# 3-First Plus Length
#  Example: first_plus_length([1,2,3,4,5])
def first_plus_length(list):
    print(list[0])
    return len(list)
print(first_plus_length([1+5]))

# 4-Values Greater than Second 
def values_greater_than_second(list):
    if len(list)<2:
        return False
    newList = []
    for val in list:
        if val>list[1]:
            newList.append(val)
    print(len(newList))    
    return newList
print(values_greater_than_second([1,4,6,8,20]))


