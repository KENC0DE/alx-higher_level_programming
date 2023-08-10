#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    argc = len(sys.argv)
    if argc == 1:
        print("0 arguments.")
    elif argc == 2:
        print(f"1 argument:\n{argc - 1}: {sys.argv[1]}")
    else:
        print(f"{argc - 1} arguments:")
        for i in range(1, argc):
            print(f"{i}: {sys.argv[i]}")
