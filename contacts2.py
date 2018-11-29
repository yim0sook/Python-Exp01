import sqlite3

db = sqlite3.connect("contacts.sqlite")

new_email = 'new@email.com'
#phone = 56456
phone =input("Please enter the phone number")

#update_sql = "UPDATE contacts SET email = 'anotherupdate@email.com' WHERE contacts.phone = 56456"
# sql1: update_sql = "UPDATE contacts SET email = '{}' WHERE phone = {}".format(new_email, phone)
update_sql = "UPDATE contacts SET email = ? WHERE phone = ?"
print(update_sql)

update_cursor = db.cursor()
#sql1:update_cursor.execute(update_sql)
#update_cursor.executescript(update_sql)   - this can execute multiple scripts like inputted '56456;drop table contacts'
update_cursor.execute(update_sql,(new_email,phone))
print("{} rows updated".format(update_cursor.rowcount))

print()
print("Are connections the same{}".format(update_cursor.connection == db))
print()

update_cursor.connection.commit()  # especially update your cursor, it is recommended to commit by cursor
update_cursor.close()

for name, phone, email in db.execute("SELECT  * FROM contacts"):
    print(name)
    print(phone)
    print(email)
    print("-" * 20)
# for row in db.execute("SELECT  * FROM contacts"):
#     print(row)

db.close()