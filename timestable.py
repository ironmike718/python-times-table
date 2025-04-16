# imports
import time, sys, os

# variables
c_r = "\033[91m"
c_g = "\033[92m"
c_y = "\033[93m"
c_b = "\033[94m"
c_m = "\033[95m"
c_c = "\033[96m"
c_n = "\033[0m"

banner = f"""\n
{c_m}#########################################################{c_n}
#####                                               #####
#####     {c_b}Welcome to Multiplication Practice!!!{c_n}     #####
#####                                               #####
{c_m}#########################################################{c_n}
"""

# main function
def main():
    os.system("clear")
    print(banner)
    tbl = input("\nWhat times table do you want to practice? ")
    print(f"\nYou have chosen the {c_g}{tbl}{c_n} times table -- Let's Go!!!\n")

    tbl = int(tbl)
    score = 0

    for var in range(1, 13, 1):
        prod = var * tbl
        guess = input(f"What is {tbl} x {var}? ")
        guess = int(guess)

        if guess == prod:
            print(f"{c_g}\tCorrect -- Good Job!!!{c_n}\n")
            score += 1
        else:
            print(f"{c_r}\tIncorrect -- Nice try, but the answer is " + str(prod) + f"{c_n}\n")

    grade = round((score / 12 * 100), 2)

    grade = str(grade)
    score = str(score)

    print(f"{c_c}\nYou got {score} correct answers of 12! Your grade is {grade}%!\n\nGreat Job! Keep Practicing!\n\nLove Always, Dad!!!\n{c_n}")


# primary program control loop
answer = "yes"
while answer == "yes":
    main()
    time.sleep(5)
    answer = input(f"\nDo you want to try again? Type {c_y}yes{c_n} to proceed or any other key(s) to exit: ")

sys.exit()