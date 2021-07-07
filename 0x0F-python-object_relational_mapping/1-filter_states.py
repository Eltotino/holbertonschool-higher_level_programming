#!/usr/bin/python3
"""Filtering states Module"""
import MySQLdb
import sys


def select_states():
    """Filters states from the database"""

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(host='localhost',
                         port=3306,
                         user=username,
                         passwd=password,
                         db=database
                         )

    cur = db.cursor()
    cur.execute("SELECT *\
                FROM states\
                WHERE name LIKE BINARY 'N%'\
                ORDER BY id ASC"
                )
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()

if __name__ == "__main__":
    select_states()
