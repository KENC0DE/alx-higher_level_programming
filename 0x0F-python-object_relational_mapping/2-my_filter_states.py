#!/usr/bin/python3
"""
    Filter states by user input
"""


if __name__ == '__main__':
    import sys
    import MySQLdb

    conn = MySQLdb.connect(host='localhost', port=3306,
                           user=sys.argv[1], passwd=sys.argv[2],
                           db=sys.argv[3])
    cursor = conn.cursor()

    cursor.execute("""SELECT * FROM states
                   WHERE name = '{}'""".format(sys.argv[4]))

    rec = cursor.fetchall()

    for r in rec:
        print(r)