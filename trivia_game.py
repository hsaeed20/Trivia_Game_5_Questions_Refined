#Ask the user to answer 5 questions to a trivia game and let them know how many they got right. Allow the user if he/she would like to play again
import requests
import random
from random import choice

right_answers = 0 #used to see how many answers the user got right

while "Y":
    n = 0 #n used as a counter to count the amount of questions needed
    url = 'https://opentdb.com/api.php?amount=10'
    data = requests.get(url).json() 
    for i in range(5): #for loop limits questions to 5
        if n < 5:
            question = data['results'][n] #gains access to the API's questions
            q = question['question'] #variable set to gain access of data in API
            print(q)
            print() #spacing 
            
            correct_answer = question['correct_answer']
    
            incorrect_answer = question['incorrect_answers']            
            incorrect_answer.append(correct_answer)
            
            random.shuffle(incorrect_answer) #shuffles the list
            
            for i in incorrect_answer:
                print(i)
            
            print()
            choice = input("Select your answer: ").strip()
            
            
            if choice == correct_answer:
                print("Correct!")
                print()
                right_answers = right_answers + 1 #acts as a way to track your score at the end of the game
            
            else:
                print("Incorrect, the answer was {}".format(correct_answer))
                print()
             
            n = n + 1 #counter use to count until 5
        
        else:
            break
    
    if right_answers == 5:
        print("NICE WORK!!!")
        print("5/5")
    else:
        print("The amount of correct answers you've recieved:", right_answers, "/5")
    
    option = input("Would you like to play again (Y/N)? ").capitalize().strip()
            
    if option == "Y":
        continue
            
    if option == "N":
        print()
        print("Thanks for playing!")
        break
    