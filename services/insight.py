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

# def generate_project_insight(analytics, current_progress):

#     print("\n========== PROJECT INSIGHT ==========")


#     total_gain = analytics["total_gain"]
#     updates = analytics["updates"]
#     average_gain = analytics["average_gain"]


#     print(
#         f"\nCurrent Progress: {current_progress}%"
#     )

#     print(
#         f"Total Progress Gain: +{total_gain}%"
#     )

#     print(
#         f"Total Updates: {updates}"
#     )

#     print(
#         f"Average Growth: {average_gain:.2f}%"
#     )


#     print("\nInsight:")


#     if current_progress >= 90:

#         print(
#             "- Project is close to completion."
#         )


#         print(
#             "- Focus on final delivery steps."
#         )


#     elif average_gain >= 10:

#         print(
#             "- Project is progressing consistently."
#         )


#         print(
#             "- Continue current momentum."
#         )


#     else:

#         print(
#             "- Project progress is slow."
#         )


#         print(
#             "- Review next action and restart momentum."
#         )


#     print(
#         "\n================================"
#     )

def generate_project_insight(analytics, current_progress):

    print("\n========== PROJECT INSIGHT ==========")


    total_gain = analytics["total_gain"]
    updates = analytics["updates"]
    average_gain = analytics["average_gain"]


    print(f"\nCurrent Progress: {current_progress}%")
    print(f"Total Progress Gain: +{total_gain}%")
    print(f"Total Updates: {updates}")
    print(f"Average Growth: {average_gain:.2f}%")


    status = ""
    insight = ""
    recommendation = ""


    if current_progress >= 90:

        status = "🟢 Almost Complete"

        insight = (
            "Project is close to completion."
        )

        recommendation = (
            "Prepare final delivery steps."
        )


    elif average_gain >= 10:

        status = "🟢 Healthy Progress"

        insight = (
            "Project is progressing consistently."
        )

        recommendation = (
            "Continue current momentum."
        )


    else:

        status = "🟡 Needs Attention"

        insight = (
            "Project progress is slowing down."
        )

        recommendation = (
            "Review next action and restart progress."
        )


    print("\nStatus:")
    print(status)


    print("\nInsight:")
    print(insight)


    print("\nRecommendation:")
    print(recommendation)


    print("\n================================")