#!/usr/bin/python3
"""
Script that lists all cities from the database hbtn_0e_4_usa
"""

import MySQLdb


def main(db_user="root", db_passwd="root", db_name="hbtn_0e_4_usa"):
    """
    Function that lists all cities from the database hbtn_0e_4_usa

    Args:
        db_user (str): Database user name
        db_passwd (str): Database user password
        db_name (str): Database user password
    """
    conn = MySQLdb.connect(host="localhost", port=3306, user=db_user,
                           passwd=db_passwd, db=db_name, charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT c.id, c.name, s.name \
                 FROM   states s, cities c \
                 WHERE  s.id = c.state_id \
                 ORDER BY c.id ASC")

    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)

    cur.close()
    conn.close()

if __name__ == "__main__":
    import sys

    if len(sys.argv) < 4:
        print("Usage: {} username password database_name".format(sys.argv[0]))
        exit(1)

    main(sys.argv[1], sys.argv[2], sys.argv[3])
