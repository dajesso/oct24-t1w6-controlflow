is_raining = False

# if is_raining == True:
#     print('I need a umbrella felicis')
# else:
#     print("No need for a umbrella felicis")    
    
# print("the end!!")

# Else if

# >=80 -> HD
# 70-79 -> D
# 60-69 -> C
# 50-59 -> p
# <50 -> F

# marks = 44

# if marks >= 80:
#     print("HD")
# elif marks >= 70:
#     print("D")
# elif marks >= 60:
#     print("C")
# elif marks >= 50:
#     print("P")
# else:
#     print("Failed big time")

#  Nested If

# 2 states -> state1 state2
# State1: >=18 can vote
# state2: >=21 can vote

state = 'State2'

# age = 19

# # displays whether they can vote or not

# if state == 'State1':
#     if age >= 18:
#         print("Can vote in state1")
#     else:
#         print("Cannot vote in state 1")
# else:
#     if age >= 21:
#         print("can vote in state 2")
#     else:
#         print("cannot vote in state 2")

day_of_week = 7

# if day_of_week == 1:
#     print('Monday')

# elif day_of_week == 2:

# Ternary

print("I need an umbrella" if is_raining else "You need a umbrella")

match day_of_week:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case _:
        print('That is not a weekday!')

    # 1-5: Weekday
    # 6,7: Weekend
    # Otherwise: Error Message

match day_of_week:
    case 1 | 2 | 3 | 4 | 5:
        print("weekday")
    case 6 | 7:
        print("Weekend")
    case _:
        print("Error not a vaild day")

