import logging

from second import validate_and_execute, user_input_message
# from second import *
# from second import s
user_input = ""
while user_input != "exit":
    user_input = input(user_input_message)
    days_and_unit = user_input.split(":")
    print(days_and_unit)
    days_and_unit_dictionary = {"days": days_and_unit[0], "unit": days_and_unit[1]}
    print(days_and_unit_dictionary)
    validate_and_execute(days_and_unit_dictionary)

"""my_list = ["January", "February", "March"]
print(my_list[2])
my_list.append("April")
print(my_list)


my_set = {"January", "February", "March"}
for element in my_set:
    print(element)

my_set.add("April")
print(my_set)
my_set.remove("January")
print(my_set)"""


logger = logging.getLogger("MAIN")
logger.error("Error happened in the app")
