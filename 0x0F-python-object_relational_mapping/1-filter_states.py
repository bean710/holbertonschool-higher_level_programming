#!/usr/bin/python3
# This file is a script to list all states in a table that start with N
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT id, name FROM states ORDER BY id")
    states = cur.fetchall()
    for state in states:
        if (state[1][0] == "N"):
            print((state[0], state[1]))
