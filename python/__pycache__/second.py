import logging

to_minutes = 24 * 60
#
# def scope_check(num_of_days):
#     print(to_minutes)
#     print(num_of_days)
#
#
# scope_check(20)
# days_to_units(40, "Awesome")
#
#
# print(f'20 days are {20 * to_minutes} minutes')
# print(f'20 days are {35 * to_minutes} minutes')
# print(f'20 days are {35 * to_minutes} minutes')
#


def days_to_units(num_of_days, conversion_unit):
    if conversion_unit == "hours":
        return f'{num_of_days} days are {num_of_days * 24} hours'
    elif conversion_unit == "minutes":
        return f'{num_of_days} days are {num_of_days * 24 * 60} minutes'
    else:
        return "unsupported unit"
# def validate_and_execute():
#     if user_input.isdigit():
#         user_input_number = int(user_input)
#         if user_input_number > 0:
#             calculated_value = days_to_units(user_input_number)
#             print(calculated_value)
#         elif user_input_number == 0:
#             print("you entered a 0, please enter a valid positive number")
#     else:
#         print("your input is not a valid number. Don't ruin my program")
#
#
# user_input = input("Hey user, enter a number of days and I will convert it to minutes!\n")
# validate_and_execute()


def validate_and_execute(days_and_unit_dictionary):
    try:

        user_input_number = int(days_and_unit_dictionary["days"])
        if user_input_number > 0:
            calculated_value = days_to_units(user_input_number, days_and_unit_dictionary["unit"])
            print(calculated_value)
        elif user_input_number == 0:
            print("you entered a 0, please enter a valid positive number")
        else:
            print("you entered a negative number, no conversion for you!")
    except ValueError:
        logger = logging.getLogger("MAIN")
        logger.error("Error happened in the app")


user_input_message = "Hey user, enter a number of days and conversion unit!\n"
