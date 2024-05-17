#1 Basic
for i in range (1,151):
    print(i)

#2 Multiples of Five
for i in range (5,1005,5):
    print(i)

#3 Counting, the Dojo Way
for i in range(1,101):
    if i%5 == 0 :
        print("Coding")
    elif i%10 == 0 :
        print("Coding Dojo")
    else:
        print(i)

#4 Whoa. That Sucker's Huge 
sum = 0 
for i in range(0,500000):
    if i%2 != 0 :
        sum = sum + i
    #else :
        #continue
print (sum)

#5 Countdown by Fours
for i in range (2018,0,-4):
    print(i)

#6 Flexible Counter 
lowNum=10
highNum=20
mult=2
for i in range(lowNum,highNum):
    if i%mult ==0 :
        print (i)