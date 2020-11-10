from random import randint


def get_number():
    """Ask user for number.

    Get an answer only as an int.

    :rtype int
    :return user choice = number as int
    :raise ValueError if not int
    """
    while True:
        try:
            user_choice = int(input("Guess the number: "))
            break
        except ValueError:
            print("It's not a number!")
    return user_choice


def guess_the_number():
    """Compare results

    Try compare user's and computer's choices.
    Return information whether the user's choice is greater,
    less or equal to the computer's choice.
    Stop running when both are equal.

    :return result of comparison as string
    :rtype str
    """
    comp_choice = randint(1, 100)
    user_answer = get_number()
    while user_answer != comp_choice:
        if user_answer < comp_choice:
            print("To small!")
        else:
            print("To big!")
        user_answer = get_number()
    print("You win!")


if __name__ == '__main__':
    guess_the_number()
