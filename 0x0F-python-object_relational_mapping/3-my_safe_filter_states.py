#!/usr/bin/python3
"""
    SQL Injection...
"""


if __name__ == '__main__':
    import sys
    import MySQLdb

    conn = MySQLdb.connect(host='localhost', port=3306,
                           user=sys.argv[1], passwd=sys.argv[2],
                           db=sys.argv[3])
    cursor = conn.cursor()

    query = "SELECT * FROM states WHERE name LIKE BINARY %s"
    cursor.execute(query, (sys.argv[4],))

    rec = cursor.fetchall()

    for r in rec:
        print(r)
