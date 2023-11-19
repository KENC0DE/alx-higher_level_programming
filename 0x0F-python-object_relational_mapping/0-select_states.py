#!/usr/bin/python3
""" Python ORM
"""


if __name__ == '__main__':
    import sys
    import MySQLdb

    args = sys.argv[1:]
    conn = MySQLdb.connect(*args)
    curs = conn.cursor()

    curs.execute('SELECT * FROM states ORDER BY id ASC')
    recs = curs.fetchall()

    for r in recs:
        print(r)
