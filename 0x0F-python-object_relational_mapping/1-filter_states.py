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

    conn = MySQLdb.connect(
        "localhost",
        my_user,
        my_pass,
        my_db
    )

    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id;")
    query_rows = cur.fetchall()
    for row in query_rows:
        if row[1].startswith('N'):
            print(row)
    cur.close()
    conn.close()
