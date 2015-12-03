"""mysql connection poc

    Simple poc using mysql in python.
    MySQL runs on localhost, it seems on OSX by default on port 3307, not 3306

    TODO:   Check advantage of autocommit=False
            (It might make sense to set autocommit to false and then use
            conn.commit() if one has multiple entries.)

"""
import pymysql


def run():
    conn = pymysql.connect(host='localhost', port=3307, user='root',
                           passwd='gr82cu', db='poc_python', autocommit=True)
    cur = conn.cursor()
    # explain table
    print("Explain Table:\t {0}".format(cur.description))
    # insert
    cur.execute("insert into poc_simple (name, surname) values \
                ('John', 'Doe');")
    # select
    cur.execute("select * from poc_simple")
    print ("select * from poc_simple;")
    for row in cur:
        print(row)
    cur.close()
    conn.close()

if __name__ == "__main__":
    run()
