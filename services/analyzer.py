import pandas as pd
from database import create_connection
from services.insight import generate_insight

def get_activity_dataframe():

    connection = create_connection()


    query = """
    SELECT *
    FROM activities
    """


    df = pd.read_sql_query(
        query,
        connection
    )


    connection.close()


    return df



def generate_learning_report():

    df = get_activity_dataframe()


    if df.empty:

        print("""
            ========== LEARNING REPORT ==========

                No learning activity found.

                Start adding activities to generate insights.

            =====================================
        """)

        return ## debugging, return kena masuk under print, baru tak bugging.



    print("\n========== LEARNING REPORT ==========")


    print(
        f"\nTotal Learning Sessions: {len(df)}"
    )


    total_time = df["duration"].sum()


    print(
        f"Total Learning Time: {total_time} minutes"
    )


    most_active = (
        df["category"]
        .value_counts()
        .idxmax()
    )


    print(
        f"Most Active Category: {most_active}"
    )


    print("\nActivity Breakdown:")

    category_count = df["category"].value_counts()


    for category, count in category_count.items():

        print(f"{category}: {count} sessions")


    print("\n====================================")

    generate_insight(df)