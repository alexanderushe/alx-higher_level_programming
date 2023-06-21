#!/usr/bin/pyton3
"""script safe from sql injections, display states"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQL.db(host="localhost", user=sys.argv[1],
            password=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE s%", (match, ))
    states = cur.fetchall()
    for state in states:
        print(state)
    cur.close()
    db.close()
