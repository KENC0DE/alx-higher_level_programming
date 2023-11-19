#!/usr/bin/python3
""" Python ORM
"""


if __name__ == '__main__':
    import sys
    import MySQLdb

    conn = MySQLdb.connect(host='localhost', port=3306,
                                    user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    curs = conn.cursor()

    curs.execute('SELECT * FROM states ORDER BY id ASC')
    recs = curs.fetchall()

    for r in recs:
        print(r)
