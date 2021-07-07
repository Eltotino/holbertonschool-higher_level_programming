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

    db = MySQLdb.connect(host="localhost", user=username,
                         passwd=password, db=database)

    cur = db.cursor()
    cur.execute("""SELECT cities.id, cities.name, states.name
    FROM cities
    INNER JOIN states
    ON cities.state_id = states.id;
    """)

    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()


if __name__ == "__main__":
    Find_cities()
