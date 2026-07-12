
from models.project import Project
from database import insert_project, get_projects
from services.validator import get_valid_number

def add_project():

    name = input("Project Name: ")
    description = input("Description: ")
    status = input("Status: ")
    progress = get_valid_number(
    "Progress (%): ",
    0,
    100
)
    next_action = input("Next Action: ")
    priority = input(
    "Priority (High/Medium/Low): "
    )

    new_project = Project(
        name,
        description,
        status,
        progress,
        next_action,
        priority
    )


    insert_project(new_project)

    print("\nProject saved!")


# def view_projects():

#     projects = get_projects()


#     print("\n====== PROJECT TRACKER ======")


#     for project in projects:

#         print("--------------------")
#         print(f"Project: {project[1]}")
#         print(f"Description: {project[2]}")
#         print(f"Status: {project[3]}")
#         print(f"Progress: {project[4]}%")
#         print(f"Next Action: {project[5]}")
    
#         if not projects:

#             print("\nNo projects found.")

#         return

## remark, code diatas menyebabkan fungsi view project terhenti.  masalah, " return" diletakkan dalam loop. apa jadi?
## ambil semua project, print pertama sahaja, dan terus exit.

def view_projects():

    projects = get_projects()


    print("\n====== PROJECT TRACKER ======")


    if not projects:

        print("\nNo projects found.")
        return


    for project in projects:

        print("--------------------")
        print(f"Project: {project[1]}")
        print(f"Description: {project[2]}")
        print(f"Status: {project[3]}")
        print(f"Progress: {project[4]}%")
        print(f"Next Action: {project[5]}")
        print(f"Priority: {project[6]}")