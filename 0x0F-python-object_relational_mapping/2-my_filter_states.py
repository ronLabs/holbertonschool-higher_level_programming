#!/usr/bin/python3
""" script that takes in an argument
    and displays all values in the states table
    of hbtn_0e_0_usa where name matches the argument."""


from sys import argv
import MySQLdb

if __name__ == '__main__':

    my_user = argv[1]
    my_pass = argv[2]
    my_db = argv[3]
    name_s = argv[4]

    db = MySQLdb.connect(
        "localhost",
        my_user,
        my_pass,
        my_db
    )

    cur = db.cursor()
    database = cur.execute("SELECT * FROM states ORDER BY states.id;")
    for i in range(0, database):
        results = cur.fetchone()
        if results[1] == name_s:
            print("{}".format(results))

    cur.close()
    db.close()
