from models.activity import Activity
from database import (
    insert_activity,
    get_activities
)
from services.validator import get_valid_number

def add_activity():

    activity = input("Activity: ")
    category = input("Category: ")
    duration = get_valid_number(
    "Duration (minutes): ",
    1
)
    notes = input("Notes: ")
    rating = get_valid_number(
    "Rating (1-5): ",
    1,
    5
)


    new_activity = Activity(
        activity,
        category,
        duration,
        notes,
        rating
    )


    insert_activity(new_activity)


    print("\nActivity saved!")

def view_activities():

    activities = get_activities()


    print("\n====== LEARNING HISTORY ======")


    for activity in activities:

        print("--------------------")
        print(f"Date: {activity[1]}")
        print(f"Activity: {activity[2]}")
        print(f"Category: {activity[3]}")
        print(f"Duration: {activity[4]} minutes")
        print(f"Notes: {activity[5]}")
        print(f"Rating: {activity[6]}/5")

def view_activities():

    activities = get_activities()


    print("\n====== LEARNING HISTORY ======")


    for activity in activities:

        print("--------------------")
        print(f"Date: {activity[1]}")
        print(f"Activity: {activity[2]}")
        print(f"Category: {activity[3]}")
        print(f"Duration: {activity[4]} minutes")
        print(f"Notes: {activity[5]}")
        print(f"Rating: {activity[6]}/5")