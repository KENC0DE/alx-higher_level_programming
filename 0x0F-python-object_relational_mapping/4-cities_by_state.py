#!/usr/bin/python3
"""
    Cities by states.
"""


if __name__ == '__main__':
    import sys
    import MySQLdb

    conn = MySQLdb.connect(host='localhost', port=3306,
                           user=sys.argv[1], passwd=sys.argv[2],
                           db=sys.argv[3])
    cursor = conn.cursor()

    query = """SELECT cities.id, cities.name, states.name FROM cities, states
                WHERE cities.state_id = states.id"""
    cursor.execute(query)

    rec = cursor.fetchall()

    for r in rec:
        print(r)

    cursor.close()
    conn.close()
