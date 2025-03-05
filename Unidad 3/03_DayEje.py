#Boolean
print(True)
print(False)

#Exercises1 Day3

#Number1
#Declare your age as integer variable
print ('Age: 24')

#Number2
#Declare you heigth as float variable
print ('Heigth: 1.52')

#Number3
#Declare a variable that store a complex number
print('Complex number:',1 + 1j) 

#Number4
#Write a script that prompts the user to enter base he
base=int (input('Enter base:  '))
Heigth=int (input('Enter heigth  '))
area= int (0.5*base*Heigth)
print ('THE AREA OF THE TRIANGLE IS:  ', area)

#Number5
#Write a script thet prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter= a + b + c)
SideA=int (input('Enter A:  '))
SideB=int (input('Enter B:  '))
SideC=int (input('Enter C:  '))
perimeter= int (SideA+SideB+SideC)
print ('THE PERIMETER OF THE TRIANGLE IS:  ', perimeter)

#Number6
#Get length and width of a rectangle using prompt. Calculate its area (area= length x width) and perimeter (perimeter 2 x (length + width))
Length=int (input('Enter Length:  '))
Width=int (input('Enter Width:  '))
area=int (Length*Width)
print ('The area is:  ', area)
perimeter=int (2*(Length+Width))
print ('The perimeter is:  ', perimeter)

#Number7
#Get radius of a circle using prompt. Calculate the area(area=pi x r x r) and circumference =(c 2 x pi x r) where pi = 3.14
r=int (input('Enter r:  '))
area=int (3.14*r*r)
print ('The area is:  ',area)
circumference=int (2*3.14*r)
print ('The circumference ir:  ',circumference)

#Number8
#Calculate the slope, x-intercept and y-intercept of y = 2x -2
x1 = int(input('x1: '))
y1 = int(input('y1: '))
x2 = int(input('x2: '))
y2 = int(input('y2: '))
slope= int(y2-y1) / int(x2-x1)
print('slope:', slope)

#Number9
#Slope is (m = y2-y1/x2-x1). Find the slope and [Euclidean distance](https://en.wikipedia.org/wiki/Euclidean_distance#:~:text=In%20mathematics%2C%20the%20Euclidean%20distance,being%20called%20the%20Pythagorean%20distance.) between point (2, 2) and point (6,10) 
Y1= int(input('y1: '))
Y2= int(input('y2: '))
X1= int(input('x1: '))
X2= int(input('x2: '))
Slope= int((Y2 - Y1) / int(X2 - X1))
print('slope:', Slope)

x1= int(X1)
y1= int(Y1)
x2= int(X2)
y2= int(Y2)
distance= int((X2 - X1) * 2 + (Y2 - Y1) * 2)
print('distance:', distance)


#Number10
#Compare the slopes in tasks 8 and 9.
#Boolean
#True, False

print(Slope >= slope)
print(Slope <= slope)
print(Slope == slope)
print(Slope != slope)
print(Slope > slope)
print(Slope < slope)

#Number11
#Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
x= int(input('x: '))
X= int(input('X: '))
y= int(x**2 + 6*X + 9)
print('y:', y)

#Number12
#Find the length of 'python' and 'dragon' and make a falsy comparison statement.
print(len('python') == len('dragon'))
print(len('python') != len('dragon'))
print(len('python') < len('dragon'))
print(len('python') > len('dragon'))
print(len('python') >= len('dragon'))
print(len('python') <= len('dragon'))

#Number13
#Use _and_ operator to check if 'on' is found in both 'python' and 'dragon'
#boolean
#True, False

python = 'python'
dragon = 'dragon'
print("on" in python and "on" in dragon)

#Number14
#_I hope this course is not full of jargon_. Use _in_ operator to check if _jargon_ is in the sentence.
Frase= 'I hope this course is not full of jargon'
print(Frase)
print("jargon" in Frase)

#Number15
#There is no 'on' in both dragon and python
print("no" in python and "no" in dragon)

#Number16
#Find the length of the text _python_ and convert the value to float and convert it to string
len('python')
print(float(len('python')))
print(str(len('python')))

#Number17
#Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
#Boolean

Valor_1 = (input('Enter a number: ')) 
Remainder = float(Valor_1) % 2
if Remainder == 0:
    print('el valor es par:', Remainder)
else:
    print('el valor es impar:', Remainder)

#Number18
#Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
Valor1 = (7)
Divisor = float(Valor1) / 3
if Divisor == int(2.7):
    print('True')
else:
    print('False')

#Number19
#Check if type of '10' is equal to type of 10
if type(10) == '10':
    print('True')
else:
    print('False')

#Number20
#Check if int('9.8') is equal to 10
if int('9.8') == 10:
    print('True')
else:
    print('False')

#Number21
#Writ a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
Horaschambeadas= int(input('Horas trabajadas: '))
Pago= int(input('Pago por hora: '))
Salario= int(Horaschambeadas * Pago)
print('Salario:', Salario)

#Number22
#Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
Years= int(input('Enter a number: '))
Valor_1= str(Years*365*24*60*60)
print('los segundos que has vivido son: ', Valor_1)

#Number23
#Write a Python script that displays the following table
for i in range(1, 6):
   print (i, 1, i*2, i*3)
