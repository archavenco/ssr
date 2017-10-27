from math import pi

n = input('')
if n == 'c'.upper() or n == 'c'.lower():
    raduis = input('')
    a = (pi * int(raduis) ** 2)
    print('%.2f' % a)
elif n == 't'.upper() or n == 't'.lower():
    high = input('')
    le = input('')
    print(int(high) * int(le))
else:
    print('error')