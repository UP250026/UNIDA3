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
