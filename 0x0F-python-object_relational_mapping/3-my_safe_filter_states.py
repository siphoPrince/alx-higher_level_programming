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

    query = "SELECT cities.id, cities.name, states.name FROM cities JOIN " \
            "states ON cities.state_id = states.id"

    if cur.execute(query):
        rows = cur.fetchall()

    for row in rows:
        print(row)

    conn.close()
    cur.close()
