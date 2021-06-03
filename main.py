import time,sys

# typing effect adapted from https://www.101computing.net/python-typing-text-effect/
def typing_print(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.01)

def typing_input(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.01)
    value = input()  
    return value

# error handling adapted from https://stackoverflow.com/questions/23294658/asking-the-user-for-input-until-they-give-a-valid-response
def get_valid_value(prompt):
    while True:
        try:
            value = float(typing_input(prompt))
        except ValueError:
            typing_print("That's not a number!\n")
            continue
        if value < 0:
            typing_print("Positive numbers only!\n")
        elif value == 0:
            typing_print("Too boring!\n")
        else:
            break
    return value
        
typing_print("Welcome to the thinkmoney tribute!\n")
time.sleep(1)
dd1 = get_valid_value("How much is your monthly subsciption to My Little Pony?: £")
dd2 = get_valid_value("How much is your daily donation to the Mosquito Preservation Society?: £")
dd3 = get_valid_value("How much is your weekly payment to HerbalLife Totally Not a Scam Product?: £")
dd_total = dd1 + (dd2 * 28) + (dd3 * 4)
typing_print("It's February 2022! How convenient for you - there's only 28 days this month! I wonder how much your bills will add up to?\n")

while True:
    math_question = typing_input("Do you want to do some math? Answer yes or no: ").lower()
    if math_question == "no":
        typing_print("You and me neither! Check this out...\n")
        break
    elif math_question == "yes":
        user_answer = get_valid_value("How much do those bills add up to this month?: £")
        if user_answer == dd_total:
            typing_print("Well done! *Pat on the back*. I bet this could save you time though...\n")
        else:
            typing_print("Close, but no cigar! Mistakes are normally expensive with banks - let me help you out...\n")
        break
    else:
        typing_print("That's not a valid answer...\n")
        continue

format_dd_total = "{:.2f}".format(dd_total)

time.sleep(1)
typing_print("thinkmoney uses jamjar accounts, saving you time by doing the maths for you!\n")
time.sleep(1)
typing_print("My Little Pony (monthly) + Mosquito Preservation Society (daily) + HerbalLife Totally Not a Scam Product (weekly):\n")
time.sleep(1)
typing_print(f"Your bills add up to £{format_dd_total} this month.\n")
time.sleep(1)
typing_print("thinkmoney - banking made easy.\n")
time.sleep(1)
typing_print("Find out more at https://www.thinkmoney.co.uk/.\n")
time.sleep(1)
typing_input("Press enter to exit")