from services.analyzer import get_activity_dataframe
from datetime import datetime
from datetime import timedelta
from database import get_active_projects
from services.decision_engine import (
    select_priority_project,
    generate_project_reason,
    calculate_project_score
)
# from services.analyzer import generate_recommendation

def generate_daily_summary():

    df = get_activity_dataframe()

    print(df["date"].head())

    if df.empty:

        print("No learning data available.")

        return


    today_df = analyze_today(df)


    if today_df.empty:

        print("No activity today.")

        return


    print("\n========== ALPA DAILY SUMMARY ==========")


    print("\n📚 Learning Activity")

    print(
    f"Sessions: {len(today_df)}"
    )


    total_time = today_df["duration"].sum()


    print(
    f"Total Time: {total_time} minutes"
    )


    week_df = analyze_last_7_days(df)


    today_time, weekly_average, status = compare_progress(
    today_df,
    week_df
    )

    insight = generate_insight(status)

    recommendation = generate_recommendation()

    print("\n📊 Performance Analysis")


    print(
    f"7-Day Sessions: {len(week_df)}"
    )


    print(
    f"Weekly Average: {weekly_average:.1f} minutes"
    )


    print(
    f"Status: {status}"
    )



    print("\n🧠 Insight")

    print(insight)



    print("\n🎯 Recommendation")

    print(recommendation)
    

    print("========================================")


# def analyze_today():
#     pass

def analyze_today(df):

    today = datetime.now().strftime("%Y-%m-%d")


    today_df = df[
        df["date"] == today
    ]


    return today_df


# def analyze_week():
#     pass

def analyze_last_7_days(df):

    today = datetime.now()

    seven_days_ago = (
        today - timedelta(days=7)
    ).strftime("%Y-%m-%d")


    week_df = df[
        df["date"] >= seven_days_ago
    ]


    return week_df

# def compare_progress():
#     pass

def compare_progress(today_df, week_df):

    today_time = today_df["duration"].sum()


    weekly_average = (
        week_df["duration"].sum()
        / 7
    )


    if today_time > weekly_average:

        status = "Above Average 🚀"

    elif today_time < weekly_average:

        status = "Below Average"

    else:

        status = "Average"


    return (
        today_time,
        weekly_average,
        status
    )

# def generate_insight():
#     pass

def generate_insight(status):

    if status == "Above Average 🚀":

        return (
            "Strong learning momentum today."
        )


    elif status == "Below Average":

        return (
            "Learning activity is below your weekly pattern."
        )


    else:

        return (
            "Learning activity is consistent."
        )
    
# def generate_recommendation():

#     projects = get_active_projects()


#     if not projects:

#         return "No active project found."


#     project = select_priority_project(projects)


#     return (
#         f"Focus on: {project[1]}\n"
#         f"Next Action: {project[5]}"
#     )


# def generate_recommendation():

#     projects = get_active_projects()

#     print("\nDEBUG PROJECTS:")
#     print(projects)

#     if not projects:

#         return "No active project found."

#     ...

def generate_recommendation():

    # score = calculate_project_score(project) ## salah susunan, output tak keluar
    
    print("🔥 NEW SMART RECOMMENDATION RUNNING")

    projects = get_active_projects()

    print("\nDEBUG PROJECTS:")
    print(projects)


    if not projects:

        return "No active project found."


    project = select_priority_project(projects)

    score = calculate_project_score(project)

    reason = generate_project_reason(project)


    return (
        "\n========== SMART RECOMMENDATION ==========\n\n"
        f"Project: {project[1]}\n"
        f"Decision Score: {score}\n\n"
        f"Progress: {project[4]}%\n\n"
        f"Reason:\n{reason}\n\n"
        f"Next Action:\n{project[5]}\n\n"
        "=========================================="
    )

## database.py → ambil data
## intelligence.py → buat keputusan daripada data
## main.py → panggil dan tunjuk kepada user