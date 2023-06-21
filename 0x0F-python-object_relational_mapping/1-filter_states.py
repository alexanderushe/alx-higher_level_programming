#!/usr/bin/python3
"""lists all states from db with N"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
            password=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
    cur.execute("""SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY states.id""")
    states = cur.fetchall()
    for state in states:
        print(state)
    cur.close()
    db.close()
