from math import pi

n = input('')
if n == 'c':
    raduis = input('')
    a = (pi * int(raduis) ** 2)
    print('%.2f' % a)
elif n == 't':
    high = input('')
    le = input('')
    print(int(high) * int(le))
else:
    print('error')