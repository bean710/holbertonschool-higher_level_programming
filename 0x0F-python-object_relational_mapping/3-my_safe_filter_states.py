#!/usr/bin/python3
# Lists all states that match the argument given without injection
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT id, name FROM states WHERE BINARY name=%s \
                ORDER BY id", (sys.argv[4],))
    states = cur.fetchall()
    for state in states:
        print((state[0], state[1]))
