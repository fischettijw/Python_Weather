# https://www.youtube.com/watch?v=jiPalxUAlUg&list=PL1e1htFlLTtHZI2qQPNLkPo0tLLO46_ym

from custom.func import *
from itertools import zip_longest
import os
os.system('cls')


a = ('a', 'b', 'c', 'd', 'e')
b = (1, 2, 3, 4, 5)
print_ln(a)
d = dict(zip_longest(a, b))
print_ln(d)
print_ln(b)
print_ln()

for _ in range(4):
    print_ln(f'{_} - Hello')
print_ln()

print_ln(a)
for x, y in enumerate(a):
    print_ln(x, y)
print_ln(a)

print_ln(a)
for x, a in enumerate(a):
    print_ln(x, a) if x != 2 else print_ln("x = 2")
print_ln()
