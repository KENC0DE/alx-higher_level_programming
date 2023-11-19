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
                INNER JOIN states ON cities.state_id = states.id
                WHERE states.name = %s
                ORDER BY cities.id ASC"""
    cursor.execute(query, (sys.argv[4],))

    rec = cursor.fetchall()

    ls = list(r[0] for r in rec)
    print(", ".join(ls))

    cursor.close()
    conn.close()
