import random

def comp_ch():
    lst = [1,2,3,4,5,6,7,8,9,10]
    choice = random.choice(lst)
    return choice

def intinpt():
    n = input("Enter your No. of Hand Cricket: ")
    try:
        num = int(n)
        # print("try is called")
        return num
    except Exception as e:
        # print(e)
        print("Invalid Input!!! TRY AGAIN")
        num = 0
        # print("except is called")
        return num 


def check_run():
    while(True):
        i = intinpt()
        if i > 0 and i <= 10:
            # print("if is called")
            return i
            break
        else:
            print("Woo It's cheating choose 1 to 10")
            # print("else is called")
            pass

def inpt(play):    
    try:
        p = play[0].upper()
        return p
    except Exception as e:
        p = " "
        # print(e)
        # print("Try again")
        return p

# def p_toss(name):
#     print("Okay", name, "Its time of Toss what's your call Head or Tail: ")
#     while(True):
#         play = input("Waiting...\n")       
#         p_char = inpt(play)
#         print(p_char)
#         if p_char == 'H' or p_char == 'T':
#             return p_char
#             break
#         else:
#             print("INVALID INPUT!!! Please try again") 


def p_batORfield(name):
    print("Okay You won the toss", name, "what you wanna choose B for Bat or F for Field: ")
    while(True):
        play = input("Waiting...\n")       
        p_char = inpt(play)
        print(p_char)
        if p_char == "B" or p_char == "F":
            return p_char
            break
        else:
            print("INVALID INPUT!!! Please try again") 


def f_batORfield(name):
    print("Oops You loose the toss", name, "Its time of Computer to choose")      
    lst = ["Bat","Field"]
    choice = random.choice(lst)
    print("Computer choose to", choice)
    if choice == "Bat":
        p_char = "F"
    else:
        p_char = "B"
    return p_char


# def comp_toss():
#     lst = ["Heads","Tails"]
#     choice = random.choice(lst)
#     c_char = choice[0]
#     return c_char


def enterYN():
    while(True):
        chr = input("Enter Y to Run Again or N to stop: ")
        ch = inpt(chr)
        if ch == "Y" or ch == "N" or ch == "y" or ch == "n":
            return ch
            break
        else:
            print("INVALID INPUT!!! Please try again") 

def pWINtoss():
    print("Okay", name, "Its time of Toss what's your call Odd or Eve(n): ")
    while(True):
        play = input("Waiting...\n")       
        p_char = inpt(play)
        print(p_char)
        if p_char == 'O':
            c = comp_ch()
            p = check_run()
            print("Computer Entered :",c)
            if (c + p) % 2 != 0:
                return True
            else:
                return False
            break
        elif  p_char == 'E':
            c = comp_ch()
            p = check_run()
            print("Computer Entered :",c)
            if (c + p) % 2 == 0:
                return True
            else:
                return False
            break
        else:
            print("INVALID INPUT!!! Please try again")
        



while(True):
    print("\n\n*************   HAND CRICKET    ******************")
    # print("This just like stone paper scissor. Both the players\nshould keep the gestures simultaneously. The snake\ndrinks the water, the gun shoots the snake, and gun\nhas no effect on water.")
    print("*****************************************************")

    name = input("Enter the Your name Player: ")
    # com_ch = comp_ch()
    # player_ch = check_run()
    # sum = com_ch + player_ch
    # working on odd even
    # if comp_toss() == p_toss(name):
    if pWINtoss():
        p_bf = p_batORfield(name)
        print("You Choose to Bat First") if p_bf == 'B' else print("You Choose to Field First")
    else:
        p_bf = f_batORfield(name)
    player_ballPlayed = 0
    computer_ballPlayed = 0
    run_player = 0
    run_computer = 0
    if p_bf == 'B':
        while(True):
            check_ball = comp_ch()
            rp = check_run()
            print("Computer Entered :",check_ball)
            if rp == check_ball:
                print("OOPS OUT")
                run_player += 1
                print(name,"Runs is:",run_player-1,"To Chase: ",run_player)
                while(True):
                    cp = comp_ch()
                    p_check_ball = check_run()
                    print("Computer Entered :",cp)
                    if run_computer > run_player:
                        print("Computer Won by",run_computer - run_player,"RUNS")
                        break 
                    elif cp == p_check_ball:
                        print("Computer OUT")
                        break                       
                    else:
                        run_computer = cp + run_computer
                        computer_ballPlayed += 1
                        print("--------------------------------------------------")
                        print("Computer Runs:",run_computer,"RUNS\nTo Chase:",run_player,"RUNS To make:",run_player-run_computer,"RUNS","\nBall played",computer_ballPlayed)
                        print("--------------------------------------------------")
                        if run_computer > run_player:
                            print("Computer Won by",run_computer - run_player,"RUNS")
                            break 
                break
            else:
                run_player = rp + run_player
                player_ballPlayed += 1
                print("--------------------------------------------------")
                print("Your Runs:",run_player,"RUNS\nBall played",player_ballPlayed)
                print("--------------------------------------------------")
        if run_player>run_computer:print(name, "You won by", run_player-run_computer,"RUNS")
    else:
        while(True):
            cp = comp_ch()
            p_check_ball = check_run()
            print("Computer Entered :",cp)
            if p_check_ball == cp:
                print("Computer OUT")
                run_computer += 1
                print("Computer Runs is:",run_computer-1,"To Chase: ",run_computer)
                while(True):
                    check_ball = comp_ch()
                    rp = check_run()
                    print("Computer Entered :",check_ball)
                    if run_computer < run_player:
                        print(name, "You won by", run_player-run_computer,"RUNS") 
                        break
                    elif rp == check_ball:
                        print("OOPS OUT")
                        break
                    else:
                        run_player = rp + run_player
                        player_ballPlayed += 1
                        print("--------------------------------------------------")
                        print(name,"Runs:",run_player,"RUNS\nTo Chase:",run_computer,"RUNS To make:",run_computer-run_player,"RUNS","\nBall played",player_ballPlayed)
                        print("--------------------------------------------------")
                        if run_computer < run_player:
                            print(name, "You won by", run_player-run_computer,"RUNS") 
                            break
                break
            else:
                run_computer = cp + run_computer
                computer_ballPlayed += 1
                print("--------------------------------------------------")
                print("Computer Runs:",run_computer,"RUNS\nBall played",computer_ballPlayed)
                print("--------------------------------------------------")
        if run_player<run_computer:print("Computer Won by",run_computer - run_player,"RUNS")
    # print("You Won by", run_player-run_computer,"RUNS") if run_player > run_computer else print("You Loose by",run_computer-run_player,"RUNS")
    print("Wanna Play Again Y/N")
    ch = enterYN()
    if ch == "Y" or ch == "y":
        continue
    else:
        break