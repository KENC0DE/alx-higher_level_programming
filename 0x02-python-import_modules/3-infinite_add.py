#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    argc = len(sys.argv)
    sum = 0
    if argc == 1:
        sum = 0
    else:
        for n in range(1, argc):
            sum += int(sys.argv[n])
    print(sum)
