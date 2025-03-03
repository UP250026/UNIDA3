print("Hello, World!") # it prints the text value Hello, World!
print(len("Hello, World!")) # it counts the number of characters including space
print(type ("Hello, World")) # it checks the data type
print(str('10'))# it converts number to string
print(int ('10')) # it converts to number
print(float (10)) # it converts integer to decimal
input('Enter name:') #it takes user input

# Variables un python
first_name = 'Mariana'
last_name = 'Pichardo'
country = 'México'
city= 'Aguascalientes'
Age = 25
is_married = False
skills = ['python']
person_info = {
    'first name': ' Mariana ',
    'last name': ' Pichardo ',
    'country' : 'México',
    'city' : 'Aguascalientes'
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
