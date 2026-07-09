from datetime import date


class Activity:

    def __init__(
        self,
        activity,
        category,
        duration,
        notes,
        rating
    ):
        self.date = date.today()
        self.activity = activity
        self.category = category
        self.duration = duration
        self.notes = notes
        self.rating = rating


    def display(self):
        print("====================")
        print(f"Date: {self.date}")
        print(f"Activity: {self.activity}")
        print(f"Category: {self.category}")
        print(f"Duration: {self.duration} minutes")
        print(f"Notes: {self.notes}")
        print(f"Rating: {self.rating}/5")
        print("====================")