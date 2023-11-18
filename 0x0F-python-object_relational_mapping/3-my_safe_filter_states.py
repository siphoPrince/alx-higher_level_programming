#!/usr/bin/python3
"""
 write a script that takes in arguments and
 displays all values in the states

"""
import MySQLdb
from sys import argv


def name_state():
    """list states"""
    database = MySQLdb.connect(host="localhost",
                               user=argv[1],
                               passwd=argv[2],
                               db=argv[3],
                               port=3306)
    c = database.cursor()

    name_search = argv[4]
    query = "SELECT * FROM states WHERE name LIKE %s ORDER BY states.id ASC"
    c.execute(query, (f'%{name_search}%',))

    row = c.fetchall()

    for rows in row:
        print(rows)

    c.close()
    database.close()


if __name__ == "__main__":
    name_state()
