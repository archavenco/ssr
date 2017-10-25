"""
This is a
multi-line
comment!
"""
from math import pi
from time import sleep
from datetime import datetime
now = datetime.now()
print('Starting the calculator')
print('Current time: %s/%s/%s %s:%s' % (now.month, now.day, now.year, now.hour, now.minute))
sleep(1)
hint = "Don't forget to include the correct units! Exiting..."
op = input('Enter C for Circle or T for Triangle: ')
op = op.upper()
if op == 'C':
  radius = float(input("Enter radius: "))
  area = pi * radius ** 2
  print('The pie is baking...')
  sleep(1)
  print('Area: %.2f. \n %s' % (area, hint))
elif op == 'T':
  base = float(input("Enter area of a triangle: "))
  height = float(input("Enter height: "))
  area = 0.5 * base * height
  print('Uni Bi Tri...')
  sleep(1)
else:
  print('Error! Invalid shape selector specified. Exiting.')