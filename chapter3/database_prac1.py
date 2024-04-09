import mysql.connector

mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="11071399",
    database="information_people"
)

mycursor = mydb.cursor()
sql = "INSERT INTO informations (Name, Weight, Height) VALUES (%s, %s, %s)"
val = [('milad', 120, 185), ('amir', 90, 180), ('fatemeh', 63, 175),
       ('mahboobeh', 60, 162), ('khosro', 83, 175), ('mahshid', 62, 172), ('shahin', 82, 175)]
mycursor.executemany(sql, val)
mycursor.execute("SELECT * FROM informations")

my_result = mycursor.fetchall()
mydb.commit()
# sort my_result based last item decreasing and second item increasing
sort_my_result = sorted(my_result, key=lambda x: (-x[-1], x[1]))
print(sort_my_result)
for i in sort_my_result:
    # print('%s %s %s' % (x[0], x[2], x[1]))
    print(f'{i[0]} {i[2]} {i[1]}')

mydb.close()
