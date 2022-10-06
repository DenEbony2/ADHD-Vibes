from cmath import pi
import itertools
import os
import random
import time

#Defining the price numbers + case numbers in lists called cases and case_number respectively
global cases, case_number
global pChoice, rnd

cases = [.01, 1, 5, 10, 25, 50, 75, 100, 200, 300, 400, 500, 750, 1000, 5000, 10000, 25000, 50000, 75000, 100000, 200000, 300000, 400000, 500000, 750000, 1000000]
case_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]


#uses the case list and creates a separate list called r_cases to make a completely random case
def randomizeCases():
    global case_dict, r_cases
    r_cases = random.sample(cases, len(cases)) #propogates r_cases with the values of cases in random indexes
    case_dict = dict(zip(r_cases, case_numbers)) #(zips all into a dictionary for switch case use)
    return

#Self Explainable really, takes in r_cases and case number (previously cases by accident). Assigns both to a dictionary, this way we can use
#switch cases to find out the randomized case number
def playerChoice(name):
    i = 0
    randomizeCases()
    time.sleep(1)
    print("\nOk {}, there are 26 cases being shuffled by my lovely models, the invisibitties as we speak".format(name))
    time.sleep(1)
    print("\nBefore we begin, we're going to have you choose a case.")
    time.sleep(1)
    print("\nThis case will be safe from being taken out, BUT, you do not know the value of the case, it can be the big million, or one cent!")
    time.sleep(1)

    while i == 0:
        time.sleep(1)
        p_case = int(input("Tough decisions come quick, choose a case to be your forvever partner: "))
        if p_case > 27 - 1:
            print("\nWe only have a million to give, {}!".format(name))
        elif p_case <= 0:
            print("\nYou think you're funny eh?")
            time.sleep(10)
            print("I just wasted 10 seconds of your life, THAT's funny!")
        elif p_case < 26 - 1 or p_case == 26:
            i = 1    
            print("\nOkay! Now that you have selected your case (Case {}), Its time to play the GAME!".format(p_case))
    storePCase(p_case)

#Also self explainable, stores the player's chosen case in user_case to use to check if the player decides to select their own case
def storePCase(p_case):
    global user_caseam
    global user_case
    user_caseam = r_cases[p_case - 1] #since the user is asked to take in a number from 1 - 26 and lists count from 0, p_case - 1 is used
    user_case = case_numbers[p_case - 1] #same explanation
    case_numbers.remove(user_case)
    r_cases.remove(user_caseam)
    firstChoices(user_case)
    
#GRAQ gives the user the choice to pick 3 cases as the first round of the game
def firstChoices(user_case):
    i = 0
    x = 0
    rnd = 0
    uc = []
    count = 0
    

    print("Now, you have 25 cases remaining. To start us off, I'll give you the opportunity to choose between 6 cases!")
    time.sleep(1)
    x = int(input("Choose the cases you wish to eliminate first: "))
    if x == user_case:
        print("\nHey, {}, you CHOSE Case {} as your FUCKING FOREVER PARTNER!".format(name, user_case))
        time.sleep(1)
        print("\nChoose a different case. GRAQ doesn't have time for this shit, he has a SHOW to run: ")
    elif x == 0:
        print("\nListen {}, you keep thinking you're funny, choosing the number 0 but...".format(name))
        time.sleep(10)
        print("\33[91m\nYou're not, get kicked off the show bitch.\33[0m")
        time.sleep(2)
    else:
        uc.append(x)
        i += 1

    #Choose your six cases, this will be used again in the upcoming rounds
    while i < 6:
        x = int(input("\nChoose the cases you wish to eliminate next: "))
        if x == user_case:
            print("\nHey, {}, you CHOSE Case {} as your FUCKING FOREVER PARTNER!".format(name, user_case))
            time.sleep(1)
            print("\nChoose a different case. GRAQ doesn't have time for this shit, he has a SHOW to run: ")
        if x > 27 - 1:
            print("\nWe only have a million to give, {}!".format(name))
        elif x == 0:
            print("Getting real tired of your shit.")
            time.sleep(3)
        #Checking for a dupe in the while loop    
        count = uc.count(x)
        if count > 0:
            print("Dupe Detected!")
            time.sleep(1)
            print("Removing. . .")
        else:
            uc.append(x)
            i+= 1          
    compareCases(uc)
        
#Compare the Cases from r_case to the ones chosen and remove them from r_case
def compareCases(uc): 
    global picks
    moneyValue = []
    rnd = 0
    picks = []
    
    for i in uc:
        x = r_cases[i - 1]
        moneyValue.append(x)
        x = case_numbers[i - 1]
        picks.append(x)
    

    for i in range(len(moneyValue)):
        temp = moneyValue[i]
        if temp <= 100000:
            print("${} gone! Amazing job!".format(temp))
            r_cases.remove(temp)
            
            
        elif temp > 100000:
            print("${} gone! WHAT A LOSER!".format(temp))
            r_cases.remove(temp)
            
    rnd += 1
    bankerWager(rnd)    

#Each round, the expected value is calculated using the formula in the function and returned, this is the last thing to be done every time.
def expectedValue(rnd):
    global percentage, x
    exp_value = 0.00
    percentage = 0.00
    x = 0.0
    if rnd == 1:
        percentage = 0.15
    elif rnd == 2:
        percentage = 0.24
    elif rnd == 3:
        percentage = 0.34
    elif rnd == 4:
        percentage = 0.44
    elif rnd == 5:
        percentage = 0.54
    elif rnd == 6:
        percentage = 0.64
    elif rnd == 7:
        percentage = 0.74
    elif rnd == 8:
        percentage = 0.84
    elif rnd == 9:
        percentage = 0.94
    elif rnd == 10:
        percentage = 1

    for i in range(len(r_cases)):
        x += 1
        exp_value += r_cases[i]
      
    return (exp_value)

#This is it, the banker is taking in the expected value that was given to him and makes his offer.
def bankerWager(rnd):
    
    print("\33[31mRING...\33[0m")
    time.sleep(1)
    print("\33[31mRING...\33[0m")
    time.sleep(1)
    print("\33[31mRING...\33[0m")
    time.sleep(1)
    print("\nOh..? Looks like the Banker is calling us! Let's see what he has to offer for you..")
    exp_value = expectedValue(rnd)
    wager = (exp_value * percentage) / x
    wager = round(wager,2)
    time.sleep(5)
    print("BANKER OFFER: \33[33m{}\33[0m".format(wager))
    dond(rnd,wager)
    
#If the user chooses deal, the user wins the money given by the banker and the game ends, if not, its off to the next rounds
def dond(rnd,wager):
    if rnd != 10:
        print("Its time to make the choice, {}".format(name))
        time.sleep(2)
        print("Dael or No Dael?")
        time.sleep(2)
        ans = input("Your choice is: ").casefold()
        if ans == "Dael".casefold():
            dael(wager)
        elif ans == "No Dael".casefold():
            rnd += 1
            nextRound(user_case,rnd)
    else:
        print("uh whoops")
    
def main_menu():
    global name
    print("Welcome to this computer's best and worst only gameshow, Dael or no Dael!\n")
    time.sleep(1)
    print("I am your one and only host living inside your walls, GRAQ!\n")
    time.sleep(1)
    print("What's your name?\n")
    time.sleep(.5)
    name = input("Enter name here: ")
    print("Alright {}, its time to play Dael or no Dael!".format(name))
    time.sleep(1)
    playerChoice(name)

def dael(wager):
    print("Its a deal! You, {} are the proud winner of ${}!".format(name,wager))
    time.sleep(1)
    print("\nI've been your host, GRAQ and I will see you all next time on DAEL OR NO DAEL! Goodnight!")
    
def nextRound(user_case,rnd):
    i = 0
    x = 0
    uc = []
    count = 0
    
    #Goes thru an if statement check to see which round the game is currently at, then lets the user choose those cases
    if rnd == 2:
        case_ch = 5
    elif rnd == 3:
        case_ch = 4
    elif rnd == 4:
        case_ch = 3
    elif rnd == 5:
        case_ch = 2
    elif rnd >= 6 and rnd != 11:
        case_ch = 1

    print("ROUND", rnd)
    time.sleep(1)
    print(case_numbers)
    print("You have the opportunity to eliminate {} cases, now...".format(case_ch))
    time.sleep(3)
    while i < case_ch:
        x = int(input("\nChoose the cases you wish to eliminate next: "))
        if x == user_case:
            print("\nHey, {}, you CHOSE Case {} as your FUCKING FOREVER PARTNER!".format(name, user_case))
            time.sleep(1)
            print("\nChoose a different case. GRAQ doesn't have time for this shit, he has a SHOW to run: ")
            time.sleep(2)
            if chosenCaseCheck(x) == True:
                print("You've already chosen that case buckaroo!")
            else:
                print("Go ahead buckaroo")
        else:               
            if x == 0:
                print("Getting real tired of your shit.")
                time.sleep(3)
            elif x > case_ch:
                print("We dont have that many cases you dumbass.")
                time.sleep(3)        
        #Checking for a dupe in the while loop 
            else:   
                count = uc.count(x)
                if count > 0:
                    print("Dupe Detected!")
                    time.sleep(1)
                    print("Removing. . .")
                else:
                    uc.append(x)
                    i+= 1          
                    compareCases(uc)

def chosenCaseCheck(x):
    p = 0
    for i in range(len(picks)):
        while p < 0:
                if x - 1 == i:
                    p += 1
                    return True
                else:
                    p = 0
                    return False
main_menu()


