### Exercises: Level 1
#1. Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output:

#    ```sh
 #   Enter your age: 30
  #  You are old enough to learn to drive.
   # Output:
    #Enter your age: 15
    #You need 3 more years to learn to drive.
    #```

edad = int(input("Introduzca su edad: "))
if edad >= 18:
    print("Tiene la edad suficiente para conducir.")
else:
    print(f"Necesita esperar {18 - edad} años para poder conducir.")


#2. Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age. Output:

 #   ```sh
  #  Enter your age: 30
   # You are 5 years older than me.
    #```

mi_edad = 25  # Puedes modificar esta edad
edad_usuario = int(input("Ingrese su edad: "))
diferencia = abs(mi_edad - edad_usuario)
if edad_usuario > mi_edad:
    print(f"Eres {diferencia} años mayor que yo.")
elif edad_usuario < mi_edad:
    print(f"Soy {diferencia} años mayor que tú.")
else:
    print("Tenemos la misma edad.")

#3. Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b. Output:

#```sh
#Enter number one: 4
#Enter number two: 3
#4 is greater than 3
#```

a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))
if a > b:
    print(f"{a} es mayor que {b}")
elif a < b:
    print(f"{a} es menor que {b}")
else:
    print(f"{a} es igual a {b}")


### Exercises: Level 2

   #1. Write a code which gives grade to students according to theirs scores:

    #    ```sh
     #   80-100, A
      #  70-89, B
       # 60-69, C
        #50-59, D
        #0-49, F
        #```

puntaje = int(input("Ingrese la puntuación del estudiante: "))
if 80 <= puntaje <= 100:
    print("Calificación: A")
elif 70 <= puntaje < 80:
    print("Calificación: B")
elif 60 <= puntaje < 70:
    print("Calificación: C")
elif 50 <= puntaje < 60:
    print("Calificación: D")
else:
    print("Calificación: F")


   #1. Check if the season is Autumn, Winter, Spring or Summer. If the user input is:
    #September, October or November, the season is Autumn.
    #December, January or February, the season is Winter.
    #March, April or May, the season is Spring
    #June, July or August, the season is Summer

mes = input("Ingrese un mes: ").lower()
if mes in ["septiembre", "octubre", "noviembre"]:
    print("La estación es Otoño.")
elif mes in ["diciembre", "enero", "febrero"]:
    print("La estación es Invierno.")
elif mes in ["marzo", "abril", "mayo"]:
    print("La estación es Primavera.")
elif mes in ["junio", "julio", "agosto"]:
    print("La estación es Verano.")
else:
    print("Mes no válido.")


  # 2. The following list contains some fruits:

   # ```sh
    #fruits = ['banana', 'orange', 'mango', 'lemon']
    #```
    #If a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit exists print('That fruit already exist in the list')
 
fruits = ['banana', 'orange', 'mango', 'lemon']
fruit = input("Ingrese una fruta: ").lower()
if fruit in fruits:
    print("Esa fruta ya existe en la lista.")
else:
    fruits.append(fruit)
    print("Lista actualizada de frutas:", fruits)

### Exercises: Level 3

   #1. Here we have a person dictionary. Feel free to modify it!

#```py
 #       person={
  #  'first_name': 'Asabeneh',
   # 'last_name': 'Yetayeh',
    #'age': 250,
    #'country': 'Finland',
    #'is_marred': True,
    #'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    #'address': {
     #   'street': 'Space street',
      #  'zipcode': '02210'
    #}
    #}
#```

 #    * Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
  #   * Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
   #  * If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!
   #  * If the person is married and if he lives in Finland, print the information in the following format:

#```py
#    Asabeneh Yetayeh lives in Finland. He is married.
#```

person = {
}

# Verificar si la clave 'skills' existe y mostrar la habilidad central
if 'skills' in person:
    middle_index = len(person['skills']) // 2
    print("Habilidad central:", person['skills'][middle_index])

# Verificar si la persona tiene la habilidad 'Python'
if 'skills' in person and 'Python' in person['skills']:
    print("La persona tiene la habilidad Python.")

# Determinar el tipo de desarrollador según las habilidades
skills_set = set(person['skills'])
if {'JavaScript', 'React'} == skills_set:
    print("Es un desarrollador Frontend.")
elif {'Node', 'Python', 'MongoDB'}.issubset(skills_set):
    print("Es un desarrollador Backend.")
elif {'React', 'Node', 'MongoDB'}.issubset(skills_set):
    print("Es un desarrollador Fullstack.")
else:
    print("Título desconocido.")

# Verificar si la persona está casada y vive en Finlandia
if person['is_married'] and person['country'] == 'Finland':
    print(f"{person['first_name']} {person['last_name']} vive en Finlandia. Está casado.")