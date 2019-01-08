"""
## ==== Never create O(n), if you can O(1) ===== #
“A dispatch table is a table of pointers to functions or methods.”
Link: https://en.wikipedia.org/wiki/Dispatch_table?fbclid=IwAR392A7zZELtQxij7w5iHurjdKJxuYbdyOc6_iVBh7pqvr4oeEUr0xLUNpk
"""

import datetime


def monday_task():
    """
    :return:
    """
    print("Monday task start")


def tuesday_task():
    """
    :return:
    """
    print("Tuesday task start")


def wednesday_task():
    """
    :return:
    """
    print("Wednesday task start")


def thursday_task():
    """
    :return:
    """
    print("Thursday task start")


def friday_task():
    """
    :return:
    """
    print("Friday task start")


def saturday_task():
    """
    :return:
    """
    print("Saturday task start")


def sunday_task():
    """
    :return:
    """
    print("Sunday task start")


date_obj = datetime.datetime(2019, 1, 9)

# Now if we need to find the weekend name and complete the associated task. What should we do ??
# Basically we will use "if elif" statement for get weekend name
start = datetime.datetime.now()
if date_obj.weekday() == 0:
    monday_task()
elif date_obj.weekday() == 1:
    tuesday_task()
elif date_obj.weekday() == 2:
    wednesday_task()
elif date_obj.weekday() == 3:
    thursday_task()
elif date_obj.weekday() == 4:
    friday_task()
elif date_obj.weekday() == 5:
    saturday_task()
elif date_obj.weekday() == 6:
    sunday_task()
end = datetime.datetime.now()
n_diff = end - start
print("O(n) : ", n_diff)

# "if elif" statement means O(n) complexity

# if we make it more readability's and want to remove the O(n) complexity .
# Then we should understand about data structure and should understand about the function purpose. Well will remove the
# O(n) complexity by using "Dispatch table"

# if we create a dictionary for each function , what will look like the function ??

d_start = datetime.datetime.now()

dispatch_table = {
    0: monday_task,
    1: tuesday_task,
    2: wednesday_task,
    3: thursday_task,
    4: friday_task,
    5: saturday_task,
    6: sunday_task,
}
dispatch_table[date_obj.weekday()]()

d_end = datetime.datetime.now()

d_diff = d_end - d_start
print("O(1): ", d_diff)

print("Time different O(n) - O(1)", n_diff - d_diff)
