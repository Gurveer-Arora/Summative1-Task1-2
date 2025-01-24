# Overview
This Python program generates a quiz with random simple maths questions based on user-selected options such as which operands they wish to practice. The program asks the user to solve questions in the format a [operand] b = c where one of a, b or c is hidden from the user for them to calculate. The quiz includes a scoring system and a timer which combine to reflect on the user’s ability, accuracy and speed.

# User Documentation
This game allows users to practice and hone their maths skills through a series of basic arithmetic questions. It is a simple and interactive terminal-based game which times users and tracks their current streak, and your goal is the work out the missing number as fast as possible, getting your chosen number of questions right as fast as possible.

## Requirements
-	Python 3.9 or above *(written in Python 3.13.0)*
-	Access to a terminal

## Features
-	User Selected Question Count
-	Support for multiple operations (+, -, x, /)
-	Randomly generated questions
-	Streak tracking to encourage a streak of correct answers
-	A timer for added excitement. Can you beat your personal record?
-	Realtime feedback on answers

## How to Play 
1.	Run the game in a terminal of your choice
2.	Choose which operations you would like to practice
3.	Choose the number of questions you would like to answer
4.	Answer the questions in your terminal
5.	Try and get the questions right as fast as possible!

### Walkthrough
1.	Launch the program in your terminal (The example uses VSCode).
a.	Open the Program in VSCode.
b.	Click the run button on the top right of your screen (circled in red on the picture) 
 
2.	Select the operations you would like to practice
```plaintext
Please write the operations you would like to practice today [+,-,x,/] e.g. type +- for addition and subtraction, type 'all' for all the operations: 
```

**Example responses:**
```plaintext
all
+-
+-x
x
```

3.	Select how many questions you would like to answer 
```plaintext
How many questions you would like to answer?
```

**Example responses:**
```plaintext
5
10
7
```

4.	Answer the questions in your terminal
```plaintext 
8 + ? = 14
What is the missing number?
```

5.	Try and get the questions right as fast as possible!

### Example Gameplay:
```plaintext
Please write the operations you would like to practice today [+,-,x,/] e.g. type +- for addition and subtraction, type 'all' for all the operations: +x
How many questions you would like to answer? 5

? x 5 = 20
What is the missing number? 4
Correct!!!!
Your current streak is 1    

6 + ? = 7
What is the missing number? 1
Correct!!!!
Your current streak is 2
9 + 10 = ?

What is the missing number? 1
Incorrect, the answer was 19
Your current streak is 0

You got 2 questions right out of 3 in 4.32 seconds!!!
```
# Technical Documentation
## Overview
This program is a simple Python-based maths quiz generator. It uses random numbers generated through the random module to select random numbers and a random operator for every question. The program has the ability to time users using the time module, and uses variables to track how many questions the user got correct alongside their current streak.

## Functions
### main()
This is the core function of the game, forming a skeleton of how the game flows and using other functions in main.py to implement the primary logic. 
-	Initialises variables for questions asked, current streak, and correct answers
-	Calls functions to receive user input on which operations to use and how many questions to generate
-	Stores the start time of the game
-	It uses a variety of functions to randomly generate the question, ask the user this question and receive their answer before checking the answer is correct and adjusting variables accordingly.
-	After all questions are asked, it logs the end time and prints out the results.

### ask_num_of_questions()
Asks the user how many questions they would like to answer, if the user gives an invalid response, prompts them again.
-	Uses while True block to ask the user how many questions they would like to answer, breaks out using return statement
-	Uses try except block to ensure input is an integer
-	Checks input is greater than 1
-	Returns input if all checks pass

### ask_for_operations()
Asks the user which operations they would like to practice.
-	Asks user which operations they want to practice, removes all blankspace from their input, makes it all lowercase and converts it to a string
-	Raises valueError if there are issues with the input, potential errors include: submitting an empty string and not submitting and valid operands.
-	If the user submits ‘+-xa’ then the function will filter out the ‘a’ and return ‘+-c’
-	Filters out duplicate operands
-	Returns the final list of operands, filtered and parsed

### rand_operator(operators)
Takes a list as an argument, and randomly selects one of the operators in the list using the randint function from the random module

### operation(operand)
Takes the randomly selected operand as an argument, randomly generates and returns three numbers as a tuple
-	All three numbers initialised to 0
-	Using if/else statement, two of the three numbers are randomly generated
-	Using match block, third number is calculated
-	Returns all three numbers as a tuple

### remove_rand()
Randomly selects one of the three positions in the equation and returns that position.

### ask_the_user(a, b, c, operand, removed)
Takes as argument, the values of all positions, the operand, and the position removed, displays the question and accepts the users answer.
-	Uses match block to check the position removed, then prints the statement replacing that position for a ?.
-	Uses a while true block to allow the user to input their answer, if the input is invalid, will prompt them to answer again, if it is valid, will accept the answer and return it.

### check_answer(answer, their_answer)
Takes as arguments the users answer and the actual answer, compares these, prints the result and returns either true of false

## Error Handling
- **Input Validation:** The program uses try and except blocks to ensure that the user input is valid:
  - For the number of questions, it checks for integers.
  - For the operations, it ensures that the user enters valid operators
- **Exceptions:**
  - ValueError is raised if no valid operations are selected by the user.
## Libraries
- **random:** Used to generate random numbers and select random operations.
- **time:** Used to track the time taken to complete the quiz.


