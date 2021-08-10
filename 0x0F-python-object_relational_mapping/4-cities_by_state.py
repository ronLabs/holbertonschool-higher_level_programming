#!/usr/bin/python3
""" script that lists all cities
    from the database hbtn_0e_4_usa """


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
    database = cur.execute("SELECT cities.id, cities.name, states.name \
                         FROM cities JOIN states ON cities.state_id = \
                         states.id ORDER BY cities.id;")
    for i in range(0, database):
        results = cur.fetchone()
        print("{}".format(results))

    cur.close()
    db.close()
