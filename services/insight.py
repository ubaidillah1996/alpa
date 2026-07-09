def generate_insight(df):

    print("\n========== AI INSIGHT ==========")


    total_sessions = len(df)


    print(
        f"\nTotal sessions analysed: {total_sessions}"
    )


    category_count = df["category"].value_counts()


    most_active = category_count.idxmax()


    print(
        f"\nMain focus: {most_active}"
    )


    if most_active == "Programming":

        print(
            "\nRecommendation:"
        )

        print(
            "- Continue strengthening programming foundation."
        )

        print(
            "- Consider applying knowledge into projects."
        )


    elif most_active == "Project":

        print(
            "\nRecommendation:"
        )

        print(
            "- Good project focus."
        )

        print(
            "- Remember to document progress."
        )


    print(
        "\n================================"
    )