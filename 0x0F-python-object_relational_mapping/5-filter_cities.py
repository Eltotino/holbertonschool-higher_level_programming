#!/usr/bin/python3
"""
Display cities table rows
"""

import sys
import MySQLdb


def Find_cities():
    """
    cities from the database hbtn_0e_4_usa
    """

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    search = sys.argv[4]

    db = MySQLdb.connect(host="localhost", user=username,
                         passwd=password, db=database)

    cur = db.cursor()
    cur.execute("""SELECT cities.name
    FROM cities
    INNER JOIN states
    ON cities.state_id = states.id
    WHERE states.name = %(state)s
    """, {'state': search})

    rows = cur.fetchall()
    lista = []
    for row in rows:
        for col in row:
            lista.append(col)
    print(', '.join(lista))
    cur.close()
    db.close()


if __name__ == "__main__":
    Find_cities()
