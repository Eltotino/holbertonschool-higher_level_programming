#!/usr/bin/python3
"""My filter module"""
import sys
import MySQLdb


def find():
    """Find state with a given name"""

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    search = sys.argv[4]

    db = MySQLdb.connect(host='localhost',
                         port=3306,
                         user=username,
                         passwd=password,
                         db=database
                         )

    cur = db.cursor()
    cur.execute("""SELECT *\
                FROM states\
                WHERE name LIKE BINARY '{}'\
                ORDER BY id ASC""".format(search)
                )
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()

if __name__ == "__main__":
    find()
