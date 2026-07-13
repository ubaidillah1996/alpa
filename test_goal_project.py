from database import (
    insert_goal_project,
    get_goal_projects
)


# Test link goal dengan project

result = insert_goal_project(1, 11)

print("Insert Result:")
print(result)


# Test ambil project berkaitan goal

projects = get_goal_projects(1)

print("\nLinked Projects:")

for project in projects:

    print(project)