#!/usr/bin/python3
""" script that lists all states
    with a name starting with N(upper N)
    from the database hbtn_0e_0_usa."""


from sys import argv
import MySQLdb

if __name__ == '__main__':

    my_user = argv[1]
    my_pass = argv[2]
    my_db = argv[3]

    db = MySQLdb.connect(
        "localhost",
        my_user,
        my_pass,
        my_db
    )

    cur = db.cursor()
    database = cur.execute("SELECT id, name FROM states ORDER BY states.id;")
    for i in range(0, database):
        results = cur.fetchone()
        if results[1][0] == 'N':
            print(results)

    cur.close()
    db.close()
