from models.idea import Idea
from database import (
    insert_idea,
    get_ideas
)
from services.validator import get_valid_choice


def add_idea():

    title = input("Idea Title: ")
    description = input("Description: ")
    priority = get_valid_choice(
    "Priority: ",
    [
        "High",
        "Medium",
        "Low"
    ]
)
    status = get_valid_choice(
    "Status: ",
    [
        "Future",
        "Planning",
        "Active",
        "Completed"
    ]
)


    new_idea = Idea(
        title,
        description,
        priority,
        status
    )


    insert_idea(new_idea)


    print("\nIdea saved!")



def view_ideas():

    ideas = get_ideas()


    print("\n====== IDEA VAULT ======")


    for idea in ideas:

        print("--------------------")
        print(f"Title: {idea[1]}")
        print(f"Description: {idea[2]}")
        print(f"Priority: {idea[3]}")
        print(f"Status: {idea[4]}")