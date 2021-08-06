#!/usr/bin/python3
""" script that lists all states
    from the database hbtn_0e_0_usa."""


from sys import argv
import MySQLdb

if __name__ == '__main__':

    my_user = argv[1]
    my_pass = argv[2]
    my_db = argv[3]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=my_user,
        passwd=my_pass,
        db=my_db)

    cur = db.cursor()
    database = cur.execute("SELECT * FROM states ORDER BY id ASC")
    for i in range(database):
        results = cur.fetchone()
        print(results)

    db.close()
