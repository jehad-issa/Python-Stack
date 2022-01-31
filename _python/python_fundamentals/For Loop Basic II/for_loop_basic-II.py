# 1- Biggie Size
arr=[-1,3,5,-5]
def big_size(arr):
    for i in range(0,4,1):
        if arr[i]>0:
            arr[i]="big"
    return arr 
print(big_size([-1,3,5,-5])) 


# 2-Count Positives
arr=[2,5,6,-1,-7,-3,0,10]
def count_positives(arr):
    count=0
    for val in arr:
        if val>0:
            count+=1
            arr[len(arr)-1]=count
    return arr 
print(count_positives([2,5,6,-1,-7,-3,0,10]))         

# 3-Sum Total
arr=[1,5,7,2]
def sum(arr):
    sum=0
    for val in arr:
        sum+= val
    return sum

print(sum([1,5,7,2]))   

# 4-Average
arr=[2,6,8,10]
def average(arr):
    sum=0
    for val in arr:
        sum+= val
    return (sum/len(arr)) 
print(average([2,6,8,10]))       

# -5 Length 
arr=[1,2,3,4]
def length (arr):
    len=0
    for val in arr:
        len+=1
    return len
print(length([1,2,3,4]))        


# -6 minimum
arr=[1,5,-2,-7,3]
def minimum(arr):
    if len(arr)<0:
        return False
    minInt = arr[0]
    for val in arr:
        if val<minInt:
            minInt = val
    return minInt
print(minimum([1,5,-2,-7,3])) 

# 7- Maximum
arr=[1,5,-2,-7,3]
def maximum(arr):
    if len(arr)<0:
        return False
    maxInt = arr[0]
    for val in arr:
        if val>maxInt:
            maxInt = val
    return maxInt
print(maximum([1,5,-2,-7,3])) 

# 8- Ultimate Analysis 
arr=[5,8,9,7,-4,3,-6]
def ultimate_analysis(array):
    myDictonary = {'sumTotal': 0, 'average': 0, 'minimum': array[0], 'maximun': array[0], 'length': len(array)}
    for val in array:
        if myDictonary['minimum']>val:
            myDictonary['minimum'] = val
        if myDictonary['maximun']<val:
            myDictonary['maximun'] = val
        myDictonary['sumTotal']+= val
        myDictonary['average']=myDictonary['sumTotal']/len(array)
    return myDictonary
print(ultimate_analysis([5,8,9,7,-4,3,-6]))

# 9-Reverse List
def reverse_list(arr):
    for i in range(0, (len(arr)-1),1):
        temp = arr[i]
        arr[i] = arr[len(arr)-1-i]
        arr[len(arr)-1-i] = temp
    return arr
print(reverse_list([2,4,6,8]))


