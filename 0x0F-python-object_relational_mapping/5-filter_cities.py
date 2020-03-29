#!/usr/bin/python3
# This script lists all cities, filtered by input
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT cities.name \
                FROM cities LEFT JOIN states ON \
                cities.state_id=states.id \
                WHERE states.name=%s \
                ORDER BY cities.id",
                (sys.argv[4],))
    cities = cur.fetchall()
    cities = [x[0] for x in cities]
    print(", ".join(cities))
