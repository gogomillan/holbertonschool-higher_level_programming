#!/usr/bin/python3
"""
Script that lists all states from the database hbtn_0e_0_usa: 
"""

import MySQLdb

def main(db_user="root", db_passwd="root", db_name="hbtn_0e_0_usa"):
    """
    Function lists all states from the database hbtn_0e_0_usa

    Args:
        db_user (str): Database user name
        db_passwd (str): Database user password
        db_name (str): Database user password
    """
    conn = MySQLdb.connect(host="localhost", port=3306, user=db_user,
                           passwd=db_passwd, db=db_name, charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")

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
