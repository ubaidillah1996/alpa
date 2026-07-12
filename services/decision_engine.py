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

    priority_project = None
    highest_score = -1


    for project in projects:

        score = calculate_project_score(project)


        print(
            f"{project[1]} = {score}"
        )


        if score > highest_score:

            highest_score = score
            priority_project = project


        elif score == highest_score:

            current_progress = project[4]
            selected_progress = priority_project[4]


            if current_progress > selected_progress:

                priority_project = project


    return priority_project


# def select_priority_project(projects):

#     # if not projects:

#     #     return None


#     priority_project = None

#     highest_score = -1


#     for project in projects:

#         progress = project[4]

#         score = calculate_project_score(project)

#         print(
#         f"{project[1]} = {score}"
#         )

#         if score > highest_score:

#             highest_score = score
#             priority_project = project

#         elif score == highest_score:

#             current_progress = project[4]
#             selected_progress = priority_project[4]

#             if current_progress > selected_progress:

#                 priority_project = project

#     return priority_project

def generate_project_reason(project):

    progress = project[4]


    if progress >= 80:

        return "Project is close to completion."


    elif progress >= 50:

        return "Project has good progress and should continue."


    else:

        return "Project needs more attention."

# def calculate_project_score(project): ## disable this function, sbb upgrade

#     progress = project[4]

#     score = progress


#     if project[5]:
#         score += 10


#     return score

def calculate_project_score(project):

    progress = project[4]

    score = progress


    # has next action
    if project[5]:

        score += 10


    # long next action means clearer action
    if len(project[5]) > 10:

        score += 5


    return score

def explain_project_decision(project):

    explanation = []


    if project[4] >= 80:

        explanation.append(
            "✓ High progress level"
        )


    if project[5]:

        explanation.append(
            "✓ Has defined next action"
        )


    if project[4] >= 90:

        explanation.append(
            "✓ Close to completion"
        )


    return explanation