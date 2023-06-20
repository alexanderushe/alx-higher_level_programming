#!/usr/bin/python3
"""listing all states from database"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
            pass=sys.argv[2], db=sys.argv[3], port =3306)
    cur = db.cursor()
    cur.execute("SELECT * FROM states")
    rows = cur.fetchall()
    for r in rows:
        print(r)
    cur.close()
    db.close()

