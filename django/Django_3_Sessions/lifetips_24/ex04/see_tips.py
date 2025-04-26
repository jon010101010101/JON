import sqlite3

con = sqlite3.connect('db.sqlite3')
cur = con.cursor()
cur.execute("SELECT * FROM tips_tip")
for row in cur.fetchall():
    print(row)
con.close()
