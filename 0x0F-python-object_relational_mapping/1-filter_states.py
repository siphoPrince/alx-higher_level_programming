#!/usr/bin/python3
"""
geting all states name
"""


import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(
        user=argv[1],
        passwd=argv[2],
        db=argv[3],
        host="localhost",
        port=3306
        )

    cur = db.cursor()

    cur.execute("SELECT * FROM states ORDER BY states.id ASC")

    rows = cur.fetchall()
    for row in rows:
        if row[1].startswith('N'):
            print(row)

    cur.close()
    db.close()
