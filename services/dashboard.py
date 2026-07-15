
from database import (
    get_projects,
    get_active_projects,
    get_goals
)

from services.analyzer import (
    get_activity_dataframe
)

from services.decision_engine import (
    select_priority_project
)

def generate_dashboard():

    projects = get_projects()

    active_projects = get_active_projects()

    goals = get_goals()

    df = get_activity_dataframe()


    print("\n========== ALPA DASHBOARD ==========\n")


    print(
        f"Goals: {len(goals)}"
    )

    print(
        f"Projects: {len(projects)}"
    )

    print(
        f"Active Projects: {len(active_projects)}"
    )

    print(
        f"Learning Sessions: {len(df)}"
    )

    total_time = df["duration"].sum()


    print(
    f"Learning Time: {total_time} minutes"
    )

    if not df.empty:

        main_focus = (
        df["category"]
        .value_counts()
        .idxmax()
        )


        print(
        f"Main Focus: {main_focus}"
        )

    if active_projects:

        recommended = select_priority_project(
        active_projects
    )


    print(
        f"Recommended Project: {recommended[1]}"
    )

    print(
        "\n===================================="
    )

if __name__ == "__main__": ## testing output

    generate_dashboard()