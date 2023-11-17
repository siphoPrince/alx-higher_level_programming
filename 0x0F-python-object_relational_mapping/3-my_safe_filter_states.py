#!/usr/bin/python3
"""
script that takes in arguments and displays
all values in the states table
"""


import MySQLdb
from sys import argv

if __name__ == "__main__":
    conn = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=argv[1],
            password=argv[2],
            db=argv[3]
            )
    cur = conn.cursor()

    cur.execute("SELECT * FROM states WHERE name=%s ORDER BY states.id",
                    (argv[4], ))
    rows = cur.fetchall()

    for row in rows:
        print(row)

    conn.close()
    cur.close()
