import datetime

user_input = input("Enter your goal with a deadline separated with a colon\n")
input_list = user_input.split(":")

goal = input_list[0]
deadline = input_list[1]

deadline_date = datetime.datetime.strptime(deadline, "%d/%m/%Y")
# calculate how many days from now till deadline

today_date = datetime.datetime.today()
time_till = deadline_date - today_date
print(f'Dear user! You have {time_till.days} remaining until your goal to {goal} becomes void')
