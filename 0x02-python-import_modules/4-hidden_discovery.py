#!/usr/bin/python3.8
if __name__ == '__main__':
    import hidden_4
    deffnames = dir(hidden_4)
    for name in deffnames:
        if not name.startswith("__"):
            print(name)
