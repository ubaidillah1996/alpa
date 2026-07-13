import sqlite3
import os

DATABASE_NAME = "learning.db"


# 

# def create_connection():

#     connection = sqlite3.connect("learning.db")

#     print(connection)

#     return connection

def create_connection():

    print(
        "DATABASE:",
        os.path.abspath("learning.db")
    )

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
        next_action TEXT,
        priority TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS project_history (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        project_id INTEGER,
        old_progress INTEGER,
        new_progress INTEGER,
        changed_at TEXT
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

        print("DEBUG TYPES") ## tujuan trace bug, mana yang problem
        print(type(project.name))
        print(type(project.description))
        print(type(project.status))
        print(type(project.progress))
        print(type(project.next_action))
        print(type(project.priority))


        cursor.execute("""
        INSERT INTO projects
        (
        name,
        description,
        status,
        progress,
        next_action,
        priority
        )

        VALUES (?, ?, ?, ?, ?,?)

        """,
        (
            project.name,
            project.description,
            project.status,
            project.progress,
            project.next_action,
            project.priority
        ))

        print("DEBUG INSERT:") ## print bahagian ni ibarat error logging = keluarkan maklumat untuk cari punca, akan keluarkan error output untuk detect problem ada kat mana.
        print(project.name)
        print(project.priority)


        connection.commit()


    except Exception as e:

        print("Unable to save project.")
        print(f"Error: {e}")


    finally:

        connection.close()

# def get_projects():

#     connection = create_connection()

#     cursor = connection.cursor()


#     cursor.execute("""
#     SELECT * FROM projects
#     """)

def get_projects():

    connection = create_connection()

    try:

        cursor = connection.cursor()


        cursor.execute("""
        SELECT * FROM projects
        """)


        projects = cursor.fetchall()


        return projects


    except Exception as e:

        print("Unable to get projects.")
        print(f"Error: {e}")

        return []


    finally:

        connection.close()

def get_project_history(project_id):

    connection = create_connection()

    try:

        cursor = connection.cursor()


        cursor.execute("""
        SELECT *
        FROM project_history
        WHERE project_id = ?
        ORDER BY id DESC
        """,
        (project_id,)
        )


        history = cursor.fetchall()


        return history


    except Exception as e:

        print("Unable to get project history.")
        print(f"Error: {e}")

        return []


    finally:

        connection.close()

def analyze_project_progress(project_id):

    history = get_project_history(project_id)


    if not history:

        return None


    total_gain = 0


    for record in history:

        old_progress = record[2]
        new_progress = record[3]

        gain = new_progress - old_progress

        total_gain += gain


    update_count = len(history)


    average_gain = total_gain / update_count


    return {
        "total_gain": total_gain,
        "updates": update_count,
        "average_gain": average_gain
    }

def update_project_progress(project_id, progress):

    connection = create_connection()

    try:

        cursor = connection.cursor()


        # 1. Get current progress
        cursor.execute("""
        SELECT progress
        FROM projects
        WHERE id = ?
        """,
        (project_id,)
        )


        old_progress = cursor.fetchone()[0]


        # 2. Save history
        cursor.execute("""
        INSERT INTO project_history
        (
        project_id,
        old_progress,
        new_progress,
        changed_at
        )

        VALUES (?, ?, ?, datetime('now'))

        """,
        (
            project_id,
            old_progress,
            progress
        ))


        # 3. Update project
        cursor.execute("""
        UPDATE projects
        SET progress = ?
        WHERE id = ?
        """,
        (
            progress,
            project_id
        ))


        connection.commit()


        print("Project progress updated successfully!")


    except Exception as e:

        print("Unable to update project.")
        print(f"Error: {e}")


    finally:

        connection.close()

# def update_project_progress(project_id, progress): ## old version disposs.

#     connection = create_connection()

#     try:

#         cursor = connection.cursor()

#         cursor.execute("""
#         UPDATE projects
#         SET progress = ?
#         WHERE id = ?
#         """,
#         (
#             progress,
#             project_id
#         ))

#         connection.commit()


#     except Exception as e:

#         print("Unable to update project.")
#         print(f"Error: {e}")


#     finally:

#         projects = cursor.fetchall()


#     connection.close()


#     return projects

def get_ideas():

    connection = create_connection()

    cursor = connection.cursor()


    cursor.execute("""
    SELECT * FROM ideas
    """)


    ideas = cursor.fetchall()


    connection.close()


    return ideas

def get_project_progress(project_id):

    connection = create_connection()

    cursor = connection.cursor()


    cursor.execute("""
    SELECT progress
    FROM projects
    WHERE id = ?
    """,
    (project_id,)
    )


    result = cursor.fetchone()


    connection.close()


    return result[0]