num1 = 42    # variable declaration, number initialized
num2 = 2.3   # variable declaration, decimal initialized
boolean = True  # variable declaration, boolean initialized
string = 'Hello World'  #variable declaration, string initialized

#variable declaration, list initialized
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']
#variable declaration, dictionary initialized
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}
#variable declaration, tuple initialized
fruit = ('blueberry', 'strawberry', 'banana')
#
print(type(fruit))
#
print(pizza_toppings[1])

#list add value
pizza_toppings.append('Mushrooms')
#
print(person['name'])
#dictionary change value
person['name'] = 'George'
#dictionary change value
person['eye_color'] = 'blue'
#
print(fruit[2])
#conditional if
if num1 > 45:
    print("It's greater")
#conditional else
else:
    print("It's lower")

if len(string) < 5:
    print("It's a short word!")
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!")
#for loop
for x in range(5):
    print(x)
for x in range(2,5):
    print(x)
for x in range(2,10,3):
    print(x)

#While Loop, variblae declaration
x = 0
while(x < 5):
    print(x)
    x += 1
#list delete value
pizza_toppings.pop()
#list delete value
pizza_toppings.pop(1)

print(person)
#dictionary delete value
person.pop('eye_color')
print(person)

for topping in pizza_toppings:
    if topping == 'Pepperoni':
        continue
    print('After 1st if statement')
    if topping == 'Olives':
        break
#function declaration
def print_hello_ten_times():
    for num in range(10):
        print('Hello')

print_hello_ten_times()
#function declaration with parameter x
def print_hello_x_times(x):
    for num in range(x):
        print('Hello')

print_hello_x_times(4)
#function declaration with parameter x
def print_hello_x_or_ten_times(x = 10):
    for num in range(x):
        print('Hello')

print_hello_x_or_ten_times()
print_hello_x_or_ten_times(4)


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)