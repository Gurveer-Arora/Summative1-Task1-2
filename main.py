from random import randint # importing random integer generator from module random
import time # Importing the time module to track the duration of the quiz


def main():
    # initialise variables to track the num of questions asked, correct answers and current streak
    questions_asked = 0
    current_streak = 0
    correct_answers = 0

    # ask the users which operations they want to do and how many questions they want to answer
    operations = ask_for_operations()
    questions = ask_num_of_questions()

    print("")

    # records the start time of the quiz
    start_time = time.time()

    # Asks the user the questions
    while questions_asked < questions:
        # randomly generates an opperator to use in the question
        opperator = rand_opperator(operations)

        # generates the 3 numbers used in the equation
        a, b, c = operation(opperator)

        # randomly selects which position in the equation is hidden from the user
        removed_pos = remove_rand()

        # Asks the user the question and recieves their answer
        answer = ask_the_user(a, b, c, opperator, removed_pos)

        # checks their answer, updates the correct_answers and current_streak variables
        positions = {"a": a, "b": b, "c": c}
        if check_answer(positions.get(removed_pos), answer):
            correct_answers += 1
            current_streak += 1
        else:
            current_streak = 0

        # prints out the current streak
        print(f"Your current streak is {current_streak}\n")

        # increments the questions_asked counter
        questions_asked += 1

    # records the end time of the quiz
    end_time = time.time()

    # prints out the users score and the time taken to answer the questions, rounded to 2 dp
    print(f"You got {correct_answers} questions right out of {questions_asked} "
          f"in {round((end_time - start_time), 2)} seconds!!!")


def ask_num_of_questions():
    """
    Asks the user how many questions they would like to answer and returns their answer

    Returns
    -------
    int: The number of questions the user wants to answer
    """
    while True:
        # confirms the user input an int, otherwise prints an error message and asks them again
        try:
            questions = int(input("How many questions you would like to answer? "))
        except:
            print("Sorry, that is not a valid number of questions")
            continue

        # if input less than 1, prints an error message and asks them again
        if questions <= 0:
            print("You must input a value greater than 0")
            continue

        return questions



def ask_for_operations():
    """
    Asks the user which operations they want to practice from the options [+, -, x, /]

    Returns
    -------
    list: A list of operations the user wants to practice e.g. ["+", "x"]

    Raises
    ------
    ValueError: If no valid operation is selected by the user
    """

    # Asks the user to input all the operations they want to do, removes all the spaces
    # and ensures it is all lowercase
    user_choice = str("".join(input("Please write the operations you would like to practice "
                                    "today [+,-,x,/] e.g. type +- for addition and subtraction, "
                                    "type 'all' for all the operations: ").split())).lower()

    # ensures the user provided an input, otherwise raises ValueError
    if user_choice == "":
        raise ValueError("You must select atleast one operand")

    if user_choice == "all":
        return ["+", "-", "x", "/"]

    # loops through all characters in user_choice, appends valid operands to allowed_operations,
    # skips invalid operands
    allowed_operations = []
    for operand in user_choice:
        if operand in ("+", "-", "/", "x"):
            allowed_operations.append(operand)
        else:
            print(f"Sorry, {operand} is not currently supported, skipping operand")

    # if the user didn't input any valid operands, raises a ValueError
    if not allowed_operations:
        raise ValueError("No valid operands selected")

    # returns list of operations chosen by the user, ensuring the list contains unique values
    return list(set(allowed_operations))


def rand_opperator(opperators):
    """
    Picks a random opporator from addition, multiplication, subtraction and division and returns it

    Returns
    -------
    String: Returns the random opperator as a string
    """
    # returns a random opperator from the list using random module
    return opperators[randint(0, len(opperators) - 1)]



def operation(operand):
    """
    Returns 3 numbers to be used in the question in the format a [+,-,x,/] b = c

    Args
    ----
    operand (str): The operand which is used in the question asked to the user, can take values 
    ["+", "-", "x", "/"]

    Returns
    -------
    tup of int: contains the values of a, b and c
    """

    # initialised variables a, b and c
    a = b = c = 0

    # if statement to determine which two values of the three to randomly generate
    if operand == "/":
        b, c = randint(1, 10), randint(1, 10)
    else:
        a, b = randint(1, 10), randint(1, 10)

    # determines what the final value should be
    match operand:
        case "/":
            a = c * b
        case "+":
            c = a + b
        case "-":
            c = a - b
        case "x":
            c = a * b

    # returns a tupple containing the values for a, b and c
    return a, b, c


def remove_rand():
    """
    Randomly selects a position in the equation to remove, this is the position of the equation
    where the user has to deduce what the value is

    Returns
    -------
    String: random letter a, b or c which correlates to a position in the equation a [+,-,x,/] b = c
    """
    # defines a list of the available options to be removed
    options = ["a", "b", "c"]

    # returns a random letter from the options list
    return options[randint(0, 2)]



def ask_the_user(a, b, c, operand, removed):
    """
    Asks the user the question and returns their answer

    Args
    ----
    a, b, c (int): The numbers used in the equation that the user will be asked
    operand (str): The operand used in the equation, one of ["+", "-", "x", "/"]
    removed (str): The postion of the number that won't be shown to the user and they
    have to work out

    Returns
    -------
    int: The users answer is returned
    """
    # prints the question for the user, removing a randomly generated position
    match removed:
        case "a":
            print(f"? {operand} {b} = {c}")
        case "b":
            print(f"{a} {operand} ? = {c}")
        case "c":
            print(f"{a} {operand} {b} = ?")

    # asks the user to input their answer and if it is valid, it returns this
    # otherwise it asks them again
    while True:
        try:
            # returns the users answer
            return int(input("What is the missing number? "))
        except ValueError:
            print("Your answer must be an number")




def check_answer(answer, their_answer):
    """
    Checks the users answer, prints a message for the user and returns True or False based on 
    if their answer is correct

    Args
    ----
    answer (int): The correct answer
    their_answer (int) :The answer the user gave to the question

    Returns
    -------
    bool: True if their answer was correct (answer == their_answer) else False
    """
    # checks if the user's answer and actual answer are the same
    if answer == their_answer:
        print("Correct!!!!")
        return True
    else:
        print(f"Incorrect, the answer was {answer}")
        return False


main()
