
from models.project import Project
from database import insert_project, get_projects

def add_project():

    name = input("Project Name: ")
    description = input("Description: ")
    status = input("Status: ")
    progress = int(input("Progress (%): "))
    next_action = input("Next Action: ")


    new_project = Project(
        name,
        description,
        status,
        progress,
        next_action
    )


    insert_project(new_project)

    print("\nProject saved!")


def view_projects():

    projects = get_projects()


    print("\n====== PROJECT TRACKER ======")


    for project in projects:

        print("--------------------")
        print(f"Project: {project[1]}")
        print(f"Description: {project[2]}")
        print(f"Status: {project[3]}")
        print(f"Progress: {project[4]}%")
        print(f"Next Action: {project[5]}")