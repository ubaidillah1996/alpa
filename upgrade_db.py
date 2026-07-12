from database import create_connection

connection = create_connection()

cursor = connection.cursor()

cursor.execute("""
ALTER TABLE projects
ADD COLUMN priority TEXT
""")

connection.commit()

connection.close()

print("Priority column added successfully!")

## reason file ni wujud, untuk update row or table pada db, which is learning.db
## kerana sqlite viewer biasa tak boleh edit database