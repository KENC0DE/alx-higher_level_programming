#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    argc = len(sys.argv)
    if argc == 1:
        print("0 arguments.")
    else:
        for i in range(1, argc):
            print(f"{i}: {sys.argv[i]}")
