#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    # Open database connection
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])

    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    # execute SQL query using execute() method.
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    # Fetch all the rows using fetchall() method.
    data = cursor.fetchall()

    # Print the data
    for row in data:
        print(row)

    # disconnect from server
    db.close()
