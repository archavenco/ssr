from math import pi

n = input('')

if n.upper() == 'C':
    raduis = input('')
    a = (pi * int(raduis) ** 2)
    print('%.2f' % a)
elif n.upper() == 'T':
    high = input('')
    le = input('')
    print(int(high) * int(le))
else:
    print('error')