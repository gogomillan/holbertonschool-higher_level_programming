#!/usr/bin/python3
"""
Script that takes in arguments and displays all values in the states table of
hbtn_0e_0_usa where name matches the argument. But safe from MySQL injections!
"""
import MySQLdb


def main(db_user="root", db_passwd="root", db_name="hbtn_0e_0_usa",
         fltr_name="--"):
    """
    Function lists states from the database hbtn_0e_0_usa filtered but safe
    from SQL injections!

    Args:
        db_user (str): Database user name
        db_passwd (str): Database user password
        db_name (str): Database user password
        fltr_name (str): State name to find (filter)
    """
    conn = MySQLdb.connect(host="localhost", port=3306, user=db_user,
                           passwd=db_passwd, db=db_name, charset="utf8")
    cur = conn.cursor()
    stmt = "SELECT c.name \
            FROM   states s, cities c \
            WHERE  s.name = %(par_name)s \
              AND  c.state_id = s.id \
            ORDER BY c.name DESC"
    cur.execute(stmt, {'par_name': fltr_name})

    query_rows = cur.fetchall()
    print(", ".join([row[0] for row in query_rows]))

    cur.close()
    conn.close()

if __name__ == "__main__":
    import sys

    if len(sys.argv) < 5:
        print("Usage: {} usrname passwd dbName stateName".format(sys.argv[0]))
        exit(1)

    main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
