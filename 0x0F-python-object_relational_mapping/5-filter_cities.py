#!/usr/bin/python3
import MySQLdb
import sys
"""lists all states from database"""

if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost', port=3306,
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("""SELECT * cities.name FROM cities INNER JOIN states ON states.id=cities.state_id
                WHERE states.name = s%""".format(sys.argv[4],))

    states = cur.fetchall()
    tmp = list(state[0] for state in states)
    print(*tmp, sep=", ")
    cur.close()
    db.close()
