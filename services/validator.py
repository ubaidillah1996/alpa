def get_valid_number(prompt, minimum=None, maximum=None):

    while True:

        try:

            value = int(input(prompt))


            if minimum is not None and value < minimum:
                print(f"Value must be at least {minimum}")
                continue


            if maximum is not None and value > maximum:
                print(f"Value must not exceed {maximum}")
                continue


            return value


        except ValueError:

            print("Please enter a valid number.")


## Testing validation output : using these code and run : python services/validator.py
# if __name__ == "__main__":

#     number = get_valid_number(
#         "Enter number: "
#     )

#     print(number)

def get_valid_choice(prompt, choices):

    while True:

        value = input(prompt).strip()


        if value in choices:

            return value


        print(
            f"Please choose one of: {', '.join(choices)}"
        )