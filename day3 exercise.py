print('mahadev')

#Exercises - Day 3

#Declare your age as integer variable

year=int(input('enyer the your birth year'))

age=2024-year

print('your current age is= ' , age )


#Declare your height as a float variable

X=float(input('Enter your height in ft'))

height=X*30.48

print('the height is=', height , 'cm')


#Declare a variable that store a complex number

## Complex numbers

print('Complex numbers', 3+10j)

a=int(input('enter the number'))
b=3j

print('complex number is = ' , a+b)

import cmath

q=3
e=6
z=(complex(q,e))

print('real part of complex number= ', z.real)
print('imaginary part of complex number =' , z.imag)


#Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).


base=int(input('enter the base of triangle'))
height=int(input('enter the height of triangle'))

area=0.5*base*height

print('the area of triangle is = ' , area)



#Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).

a=(int(input('enter the side1 of triange = ')))
b=(int(input('enter the side2 of trinagle = ')))
c=(int(input('enter the side3 of triangle = ')))


perimeter=a*b*c
print('the perimeter of the triangle is = ', perimeter)