import sqlite3


DATABASE_NAME = "learning.db"


def create_connection():

    connection = sqlite3.connect("learning.db")

    return connection

def get_active_projects():

    connection = create_connection()

    cursor = connection.cursor()


    cursor.execute("""
    SELECT *
    FROM projects
    WHERE status = ?
    """,
    ("Active",))


    projects = cursor.fetchall()


    connection.close()


    return projects

def create_tables():

    connection = create_connection()

    cursor = connection.cursor()


    cursor.execute("""
    CREATE TABLE IF NOT EXISTS activities (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT,
        activity TEXT,
        category TEXT,
        duration INTEGER,
        notes TEXT,
        rating INTEGER
    )
    """)


    cursor.execute("""
    CREATE TABLE IF NOT EXISTS ideas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        description TEXT,
        priority TEXT,
        status TEXT
    )
    """)


    cursor.execute("""
    CREATE TABLE IF NOT EXISTS projects (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        description TEXT,
        status TEXT,
        progress INTEGER,
        next_action TEXT
    )
    """)


    connection.commit()
    connection.close()


if __name__ == "__main__":
    create_tables()
    print("Database created successfully!")


def insert_activity(activity):

    connection = create_connection()

    try:

        cursor = connection.cursor()

        cursor.execute("""
        INSERT INTO activities
        (date, activity, category, duration, notes, rating)
        VALUES (?, ?, ?, ?, ?, ?)
        """,
        (
            activity.date,
            activity.activity,
            activity.category,
            activity.duration,
            activity.notes,
            activity.rating
        ))

        connection.commit()


    except Exception as e:

        print("Unable to save activity.")
        print(f"Error: {e}")


    finally:

        connection.close()

def get_activities():

    connection = create_connection()

    cursor = connection.cursor()

    cursor.execute("""
    SELECT * FROM activities
    """)

    activities = cursor.fetchall()

    connection.close()

    return activities

def insert_idea(idea):

    connection = create_connection()

    try:

        cursor = connection.cursor()


        cursor.execute("""
        INSERT INTO ideas
        (title, description, priority, status)

        VALUES (?, ?, ?, ?)

        """,
        (
            idea.title,
            idea.description,
            idea.priority,
            idea.status
        ))


        connection.commit()


    except Exception as e:

        print("Unable to save idea.")
        print(f"Error: {e}")


    finally:

        connection.close()


def insert_project(project):

    connection = create_connection()

    try:

        cursor = connection.cursor()


        cursor.execute("""
        INSERT INTO projects
        (
        name,
        description,
        status,
        progress,
        next_action
        )

        VALUES (?, ?, ?, ?, ?)

        """,
        (
            project.name,
            project.description,
            project.status,
            project.progress,
            project.next_action
        ))


        connection.commit()


    except Exception as e:

        print("Unable to save project.")
        print(f"Error: {e}")


    finally:

        connection.close()

def get_projects():

    connection = create_connection()

    cursor = connection.cursor()


    cursor.execute("""
    SELECT * FROM projects
    """)


    projects = cursor.fetchall()


    connection.close()


    return projects

def get_ideas():

    connection = create_connection()

    cursor = connection.cursor()


    cursor.execute("""
    SELECT * FROM ideas
    """)


    ideas = cursor.fetchall()


    connection.close()


    return ideas

