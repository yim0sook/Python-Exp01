import sqlite3

db = sqlite3.connect("contacts.sqlite")
db.execute("CREATE TABLE IF NOT EXISTS contacts (name TEXT, phone INTEGER, email TEXT)")
db.execute("INSERT into contacts(name, phone, email) VALUES('Tim', 235488, 'asd@email.com')")
db.execute("INSERT INTO contacts VALUES('Brian', 56456, 'brain@email.com')")

cursor = db.cursor()
cursor.execute("SELECT * from contacts")

#print(cursor.fetchall())
# for row in cursor => print date as tuple, unpack tuple like (Tim, 234588, asd@email.com) do like below

print(cursor.fetchone())
print(cursor.fetchone())
print(cursor.fetchone())

for name, phone, email in cursor:
    print(name)
    print(phone)
    print(email)
    print("-" * 20)

cursor.close()
db.commit()  # if without commit, Inserted data is deleted when this session is over, so next pgm will not see the data
db.close()