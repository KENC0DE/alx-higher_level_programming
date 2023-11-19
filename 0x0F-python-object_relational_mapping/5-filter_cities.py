#!/usr/bin/python3
"""
   All cities by state
"""


if __name__ == '__main__':
    import sys
    import MySQLdb

    conn = MySQLdb.connect(host='localhost', port=3306,
                           user=sys.argv[1], passwd=sys.argv[2],
                           db=sys.argv[3])
    cursor = conn.cursor()

    query = """SELECT cities.name FROM cities
                WHERE cities.state_id = (SELECT id FROM states WHERE name = %s)
                ORDER BY cities.id"""
    cursor.execute(query, (sys.argv[4],))

    rec = cursor.fetchall()

    for i in range(len(rec)):
        if rec[i] != rec[-1]:
            print(rec[i][0], end=', ')
        else:
            print(rec[i][0])

    cursor.close()
    conn.close()
