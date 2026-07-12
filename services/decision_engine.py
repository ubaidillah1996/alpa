def calculate_project_priority(project):

    progress = project[4]


    if progress >= 80:

        priority = "HIGH"

    elif progress >= 50:

        priority = "MEDIUM"

    else:

        priority = "LOW"


    return priority

if __name__ == "__main__": ## testing output

    project = (
        1,
        "Dota Analyzer",
        "Analyze match",
        "Active",
        80,
        "Complete CRUD"
    )


    result = calculate_project_priority(project)


    print(result)

def select_priority_project(projects):

    if not projects:

        return None


    priority_project = None

    highest_score = -1


    for project in projects:

        progress = project[4]


        if progress > highest_score:

            score = 3

            highest_score = progress
            priority_project = project

    return priority_project

def generate_project_reason(project):

    progress = project[4]


    if progress >= 80:

        return "Project is close to completion."


    elif progress >= 50:

        return "Project has good progress and should continue."


    else:

        return "Project needs more attention."