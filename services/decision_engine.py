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

# 

def generate_project_reason(project):

    progress = project[4]
    priority = project[6]
    next_action = project[5]


    reasons = []


    if priority == "High":

        reasons.append("✓ High priority project")


    elif priority == "Medium":

        reasons.append("✓ Medium priority project")


    if progress >= 80:

        reasons.append("✓ High progress level")


    elif progress >= 50:

        reasons.append("✓ Good progress level")


    else:

        reasons.append("✓ Needs more attention")


    if next_action:

        reasons.append("✓ Has defined next action")


    return "\n".join(reasons)

# def calculate_project_score(project): ## disable this function, sbb upgrade

#     progress = project[4]

#     score = progress


#     if project[5]:
#         score += 10


#     return score

def get_priority_bonus(priority): ## kat sini berlaku konflik pasal score, nk mntk ai bagi recommendation mana yang penting.

    if priority == "High":
        return 80

    elif priority == "Medium":
        return 40

    elif priority == "Low":
        return 0

    return 0 # berakhir dengan none, supaya tak crash

def calculate_project_score(project):

    progress = project[4]

    score = progress


    # has next action
    if project[5]:

        score += 10


    # long next action means clearer action
    if len(project[5]) > 10:

        score += 5


    # priority weight
    priority_bonus = get_priority_bonus(project[6])

    score += priority_bonus


    return score

def explain_project_decision(project):

    explanation = []


    if project[6] == "High":

        explanation.append(
            "✓ High priority project"
        )

    elif project[6] == "Medium":

        explanation.append(
            "✓ Medium priority project"
        )


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

# def explain_project_decision(project):

#     explanation = []


#     if project[4] >= 80:

#         explanation.append(
#             "✓ High progress level"
#         )


#     if project[5]:

#         explanation.append(
#             "✓ Has defined next action"
#         )


#     if project[4] >= 90:

#         explanation.append(
#             "✓ Close to completion"
#         )


#     return explanation