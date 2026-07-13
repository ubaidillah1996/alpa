

from services.intelligence import generate_daily_summary
from database import (
    create_tables,
)
from services.analyzer import generate_learning_report
from menus.activity_menu import (
    add_activity,
    view_activities
)
from menus.idea_menu import (
    add_idea,
    view_ideas
)
from menus.project_menu import (
    add_project,
    view_projects
)
from services.intelligence import generate_recommendation
from database import update_project_progress

# def add_activity():

#     activity = input("Activity: ")
#     category = input("Category: ")
#     duration = int(input("Duration (minutes): "))
#     notes = input("Notes: ")
#     rating = int(input("Rating (1-5): "))


#     new_activity = Activity(
#         activity,
#         category,
#         duration,
#         notes,
#         rating
#     )


#     insert_activity(new_activity)

#     print("\nActivity saved!")


# def view_activities():

#     activities = get_activities()


#     print("\n====== LEARNING HISTORY ======")


#     for activity in activities:

#         print("--------------------")
#         print(f"Date: {activity[1]}")
#         print(f"Activity: {activity[2]}")
#         print(f"Category: {activity[3]}")
#         print(f"Duration: {activity[4]} minutes")
#         print(f"Notes: {activity[5]}")
#         print(f"Rating: {activity[6]}/5")

# def add_project():

#     name = input("Project Name: ")
#     description = input("Description: ")
#     status = input("Status: ")
#     progress = int(input("Progress (%): "))
#     next_action = input("Next Action: ")


#     new_project = Project(
#         name,
#         description,
#         status,
#         progress,
#         next_action
#     )


#     insert_project(new_project)

#     print("\nProject saved!")

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

def update_project():

    print("\n====== UPDATE PROJECT PROGRESS ======")


    project_id = int(
        input("Project ID: ")
    )


    new_progress = int(
        input("New Progress (%): ")
    )


    update_project_progress(
        project_id,
        new_progress
    )


    print("\nProject updated successfully!")

def menu():

    create_tables()


    while True:

        print("""
==============================
 AI PERSONAL LEARNING ASSISTANT
==============================

1. Add Activity
2. View Activities
3. Add Idea
4. View Ideas
5. Add Project
6. View Projects
7. Generate Report
8. Smart Project Recommendation
9. Update Project
10. Exit

        """)


        choice = input("Choose: ")


        if choice == "1":

            add_activity()


        elif choice == "2":

            view_activities()


        elif choice == "3":

            add_idea()


        elif choice == "4":

            view_ideas()


        elif choice == "5":

            add_project()
        

        elif choice == "6":

            view_projects()


        # elif choice == "7":

        #     generate_learning_report()
        
        # 
        
        elif choice == "7": # keputusan akhir, dua function dipisahkan unutk mudah debug dan kerja lebih kemas

            generate_learning_report()

        elif choice == "8":

            recommendation = generate_recommendation()

            print(recommendation)


        elif choice == "9":

            update_project()


        elif choice == "10":

            print("Exit")
            break

menu()
