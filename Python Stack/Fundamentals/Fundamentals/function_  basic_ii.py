#1
def countdown(num):
    my_list=[]
    for i in range(num, -1, -1):
        my_list.append(i)
    return my_list
print(countdown(5))

#2
def print_return(list):
    print(list[0])
    return list[1]
print(print_return([1,2]))

#3
def first_plus_length(list):
    sum = list[0] + len(list)
    return(sum)
print(first_plus_length([5,7,6,4,9,1]))

#4
def values_Greater_than_Second(list):
    if len(list)<2: 
        return False
    list1=[]
    for i in range(0, len(list)):
        if list[i]> list[1]:
            list1.append(list[i])
    print (len(list1))
    return list1
print(values_Greater_than_Second([5,3,7,9,1,2,0]))


#5
def This_Length_That_Value(a,b):
    list = []
    for i in range(0,a):
        list.append(b)
    return list
print(This_Length_That_Value(4,2))