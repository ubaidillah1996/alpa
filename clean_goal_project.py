import sqlite3


connection = sqlite3.connect("learning.db")

cursor = connection.cursor()


cursor.execute("""
DELETE FROM goal_projects
""")


connection.commit()

connection.close()


print("Goal project links cleaned.")