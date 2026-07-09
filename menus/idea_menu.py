from models.idea import Idea
from database import (
    insert_idea,
    get_ideas
)

def add_idea():

    title = input("Idea Title: ")
    description = input("Description: ")
    priority = input("Priority: ")
    status = input("Status: ")


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