#1
x = [ [5,2,3], [10,8,9] ] 
x[1][0]=15
print(x)

students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
students[0]["last_name"] = "Bryant"
print(students)

sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
sports_directory['soccer'][0] = "Andres"
print(sports_directory)

z = [ {'x': 10, 'y': 20} ]

z[0]['y'] = 30
print(z)


#2
students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
def iterateDictionary(list):
    for i in range (0, len(list)-1):
        output = ""
        for key, val in list[i].items():
            output+= f"{key} - {val},"
        print(output)

iterateDictionary(students) 

#3
students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
def  iterateDictionary2(key_name, some_list):
    for i in range (0,len(some_list)-1): 
        for key,value in some_list[i].items():
            if key == key_name:
                print(value)

iterateDictionary2('last_name', students)
iterateDictionary2('first_name', students)

#4
dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(some_dict):
    for key,val in some_dict.items() :
        print(f"{len(val)} {key.upper()}")
        for i in range (0, len(val)):
            print(val[i])
printInfo(dojo)