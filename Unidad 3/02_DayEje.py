print("Hello, World!") # it prints the text value Hello, World!
print(len("Hello, World!")) # it counts the number of characters including space
print(type ("Hello, World")) # it checks the data type
print(str('10'))# it converts number to string
print(int ('10')) # it converts to number
print(float (10)) # it converts integer to decimal
input('Enter name:') #it takes user input

# Variables un python
first_name = 'Odeth'
last_name = 'Espinoza'
country = 'México'
city= 'San Juan de los Lagos, Jal'
Age = 23
is_married = False
skills = ['python']
person_info = {
    'first name': ' Odeth',
    'last name': ' Espinoza ',
    'country' : 'México',
    'city' : 'San Juan de los Lagos, Jal'
    }
print('first name:',first_name)
print('First name length: ', len(first_name))
print('last name:', last_name)
print('last name length: ', len(last_name))
print('country:' , country)
print('city:', city)
print('Age: ', Age)
print('Married: ', is_married)
print('Person information:', person_info)



first_name = input('What is your name: ')
age = input('How old are you? ')


print(first_name)
print(age)

#Day 2
#Excersise 1

print('Hello World')
print(len('Hello , World'))
print(type('Hello , World'))
print(str('10')) 
print(int('10'))
print(float('10'))

first_name = (input('Enter your name:' ))
last_name = (input('Enter your last name: '))
country = input('Enter your country: ')
city = input('Enter your city: ')
age = (input('Enter your age: '))
is_married = (input('Are you married? True or False: '))
skills = ['HTML', 'CSS', 'JS', 'React', 'Python']
person_info = {
    'firstname': first_name,   
    'lastname': last_name,
    'country': country,
    'city': city,
}

print('Hello', first_name)
print('First name:', first_name)
print('First name length:', len(first_name))
print('Last name: ', last_name)
print('Last name length: ', len(last_name))
print('Country: ', country)
print('City: ', city)
print('Age: ', age)
print('Married: ', is_married)
print('Skills: ', skills)
print('Person information: ', person_info)

print(first_name, last_name, country, age, is_married)
print('first_name:', first_name)
print('last_name: ', last_name)
print('country: ', country)
print('age: ', age)
print('is_married: ', is_married)

print(first_name)   
print(age)

#Excersise 2

#2.1

print(type(first_name))
print(type(last_name))
print(type(country))
print(type(city))
print(type(age))
print(type(is_married))
print(type(skills))
print(type(person_info))

#2.2 - 2.3

print(len(first_name))
print(len(last_name))

#Excersise 2.4

print(len(first_name) > len(last_name))
print(len(first_name) < len(last_name))
print(len(first_name) == len(last_name))
print(len(first_name) != len(last_name))
print(len(first_name) >= len(last_name))
print(len(first_name) <= len(last_name))

#Excersise 2.5

num_one = 5
num_two = 4

#Excersise 2.6 - 2.11

Total= int(num_one + num_two)
Difference= int(num_one - num_two)
Product= int(num_one * num_two)
Division= int(num_one / num_two)
Remainder= int(num_one % num_two)
Exp= int(num_one ** num_two)
Floor_division= int(num_one // num_two)

print('Total:', Total)
print('Difference:', Difference)
print('Product:', Product)
print('Division:', Division)
print('Remainder:', Remainder)
print('Exp:', Exp)
print('Floor division:', Floor_division)

#Excersise 2.12

Radius= int(30)
Area_of_circule= int(3.14 * Radius ** 2)  
Circum_of_circule= int(2 * 3.14 * Radius)
print('Area of a circle:', Area_of_circule)
print('Circumference of a circle:', Circum_of_circule)

#Excersise 2.13

print("\nUser Information:")
print(f"First Name: {first_name}")
print(f"Last Name: {last_name}")
print(f"Country: {country}")
print(f"Age: {age}")

#Excersise 2.14

help('keywords')
