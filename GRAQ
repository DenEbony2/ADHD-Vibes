import random
import time

#File Management

ans_file = open("answers.txt", "r")
quest_file = open("questions.txt", "r")
q_list = quest_file.readlines()
a_list = ans_file.readlines()
        


ans_file.close
quest_file.close

def FileManagement():
    ans_file = open("answers.txt", "r")
    quest_file = open("questions.txt", "r")
    q_list = quest_file.readlines()
    a_list = ans_file.readlines()
        


    ans_file.close
    quest_file.close
    
    


ans_file = open("answers.txt", "a")
quest_file = open("questions.txt", "a")



def CollectQuestions():
    q = ""
    q = input("Enter the question to be answered ")
    quest_file.write(q)
    print("Please wait to answer your question...")
    time.sleep(1)
    CollectAnswers(q)
    

def CollectAnswers(q):
    a = ""
    print("Your question is:", q)
    a = input("\nWhat is the answer to this question? ")
    ans_file.write(a)
    choice = input("Would you like to add another question? ")
    if choice == "Yes".casefold():
        CollectQuestions()
    elif choice == "No".casefold():
        ans_file.close
        quest_file.close
        print ("Have a nice day!!")
        FileManagement()

def AskQuestion():
    print("Time to play!! No difficulty options yet..")
    randomQuestion = random.choice(q_list)
    temp = q_list.index(randomQuestion)
    randomAnswer = a_list[temp]
    print(randomQuestion)
    



def menu():
    
    print("Welcome to the Amazing and Random Question Generator, GRAQ!\n")
    time.sleep(.5)
    mch = input("Admin or Player?\n") ##Menu choice

    #Checks to see if anything other than Admin or Player is entered
    
    #GRAQ talks to the user as if they are a player... gives them the player options
    if mch == "Player".casefold():
        print("Welcome Player! Time to play in\n")
        time.sleep(1)
        print("3\n")
        time.sleep(1)
        print("2\n")
        time.sleep(1)
        print("1\n")
        time.sleep(1)
        AskQuestion()
        exit()
    #GRAQ talks to the user as if they are an... gives them the admin options
    if mch == "Admin".casefold():
       password = input("Welcome, Admin (Suspected), GRAQ requires you to enter your password!\n")
    else:
        print ("Please leave my sight.")
        time.sleep(2)
        exit()

    #Temporary password
    if password == "pAsSwOrD":
        print("Kind of a lame password huh? GRAQ's creator should probably learn how to code those properly. . .")
        time.sleep(2)
        print("Anyways, directing you to the Admin Menu!")
        time.sleep(1)
        CollectQuestions()
    else:
        print("Loser and a Fraud. GRAQ hates frauds")
        exit()
    
    
print(q_list,a_list)

menu()
