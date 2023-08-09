#!/usr/bin/python3
for n in range(ord('Z'), ord('A') - 1, -1):
    if n % 2 == 0:
        ch = chr(n + 32)
    else:
        ch = chr(n)
    print(ch, end='')
