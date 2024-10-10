#Write a Python program to calculate the area of a circle given its radius using the formula ``` area=π×r^2``` ( Take pie as 3.14)
import math

radius = float(input("enter the radius"))
print(radius)
print(math.pi)
area = math.pi * math.pow(radius, 3)
print("Area of the circle is :", area)

print(f"Area of the circle is : {area: .3f}")