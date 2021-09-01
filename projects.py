# guessing number game

# winning_number=59
# import random     ##these two lines are used when we want a random  winning number
# winning_number =random.randint(1,100)
# guess=0
# number=int(input("guess any random number between 0-100 and u win:::"))
# while True: ### or ## while not game_over:
#     if number==winning_number:
#         print(f"you won!!,and you guessed this number in {guess} times")
#         game_over=True
#         break
#     else:
#         if number < winning_number:
#                 print("too low")
#         else:
#             if number>winning_number:
#                 print("too high")

#     guess+=1
#     number=int(input("guess again:"))


# rock paper scissor game

# import random, sys
# print("n tttt ****** Rock Paper Scissors *****")

# win = 0
# loss = 0
# tie = 0
# # Loop 
# while True:
#     print(f"Win: {win}nLoss: {loss}nTie: {tie}")
#     print("""Enter Your Move: 
#             r - rock 
#             p - paper 
#             s - scissors 
#             q - quit""")
#     UserMove = input(" Type one of rock, paper, scissor or quit : ")
#     if UserMove == 'q':
#         sys.exit()   #Quit 
#     #  computer choice: 
#     randomNumber = random.randint(1, 3)
#     # Computer Choose it move. 
#     if randomNumber == 1:
#         computerMove = 'r'
#         print("Rock")
#     elif randomNumber == 2:
#         computerMove = 'p'
#         print("Paper")
#     elif randomNumber == 3:
#         computerMove = 's'
#         print("Scissors")
#     #Check Win
#     if UserMove == computerMove:
#         print("It is tie:!")
#         tie += 1
#     elif UserMove == 'r' and computerMove == 's':
#         print("You win!")
#         win += 1
#     elif UserMove == "p" and computerMove == 'r':
#         win += 1
#         print("You win!")
#     elif UserMove == "s" and computerMove == 'p':
#         win += 1
#         print("You win!")
#     elif UserMove == "r" and computerMove == 'p':
#         loss += 1
#         print("You Lose!")
#     elif UserMove == "p" and computerMove == 's':
#         loss += 1
#         print("You Lose!")
#     elif UserMove == "s" and computerMove == 'r':
#         loss += 1
#         print("You Lose!")



# calculator


""" Calculator
----------------------------------------
"""
def addition ():
    print("Addition")
    n = float(input("Enter the number: "))
    t = 0 
    ans = 0
    while n != 0:
        ans = ans + n
        t+=1
        n = float(input("Enter another number (0 to calculate): "))
    return [ans,t]
def subtraction ():
    print("Subtraction")
    n = float(input("Enter the number: "))
    t = 0 
    sum = 0
    while n != 0:
        ans = ans - n
        t+=1
        n = float(input("Enter another number (0 to calculate): "))
    return [ans,t]
def multiplication ():
    print("Multiplication")
    n = float(input("Enter the number: "))
    t = 0
    ans = 1
    while n != 0:
        ans = ans * n
        t+=1
        n = float(input("Enter another number (0 to calculate): "))
    return [ans,t]
def average():
    an = []
    an = addition()
    t = an[1]
    a = an[0]
    ans = a / t
    return [ans,t]
while True:
    list = []
    print(" My first python program!")
    print(" Simple Calculator in python by Malik Umer Farooq")
    print(" Enter 'a' for addition")
    print(" Enter 's' for substraction")
    print(" Enter 'm' for multiplication")
    print(" Enter 'v' for average")
    print(" Enter 'q' for quit")
    c = input(" ")
    if c != 'q':
        if c == 'a':
            list = addition()
            print("Ans = ", list[0], " total inputs ",list[1])
        elif c == 's':
            list = subtraction()
            print("Ans = ", list[0], " total inputs ",list[1])
        elif c == 'm':
            list = multiplication()
            print("Ans = ", list[0], " total inputs ",list[1])
        elif c == 'v':
            list = average()
            print("Ans = ", list[0], " total inputs ",list[1])
        else:
            print ("Sorry, invilid character")
    else:
        break