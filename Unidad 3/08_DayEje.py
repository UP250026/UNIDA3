#1. Create  an empty dictionary called dog
dog={}

#2. Add name, color, breed, legs, age to the dog dictionary
dog['Name']= 'Inshiwe'
dog['color']= 'Black'
dog['breed']= 'Pastor Belga'
dog['legs']= '4'
dog['age']= '3'

#3. Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student = {
    'first_name': 'Celeste',
    'last_name': 'Puga', 
    'gender': 'Femenine', 
    'age': '23', 
    'marital_status': 'Married',  
    'skills': ['Music, Art'],  
    'country': 'Guanajuato',  
    'city': 'Guanajuato',  
    'address': 'Pastita 53'  
}

#4. Get the length of the student dictionary
student_length = len(student)
print("Longitud del diccionario de estudiante:", student_length)

#5. Get the value of skills and check the data type, it should be a list
skills = student['skills']
print("Habilidades:", skills)
print("Tipo de habilidades:", type(skills))

#6. Modify the skills values by adding one or two skills
student['skills'].extend(['C++', 'JavaScript'])
print("Habilidades actualizadas:", student['skills'])

#7. Get the dictionary keys as a list
keys_list = list(student.keys())
print("Claves del diccionario:", keys_list)

#8. Get the dictionary values as a list
values_list = list(student.values())
print("Valores del diccionario:", values_list)

#9. Change the dictionary to a list of tuples using _items()_ method
student_tuples = list(student.items())
print("Diccionario como lista de tuplas:", student_tuples)

#10. Delete one of the items in the dictionary
del student['marital_status']
print("Diccionario después de eliminar marital_status:", student)

#11. Delete one of the dictionaries
del dog