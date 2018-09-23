import random
import time

#
# This python scripts simulates playing the Mega Millions game a bunch of times a second until the Jackpot is won.
# After running this, you may never want to spend money on a lottery ticket again.  It just took me 16,723,798 games
# to hit the jackpot by buying two tickets a game.  I spent $66,895,192 and around 174,206 years of playing two games a
# a week and buying two tikets per game.  The simulation ran roughly 24,904 games a second on my processor.  
# The good news is I grossed $105,487,574.
#
# See: https://valottery.com/GamesAndMore/Megamillions/
#
# Author: J Caple
# Date: 9/23/2018
#

# 100 milly
JACKPOT = 100000000

# Purchase 2 tickets at a time
num_tickets = 2

# Mega Millions Random Draw ((5) 1-70, (1) 1-25)
def drawMegaMillionNumbersAtRandom():

    # Keep track of numbers drawn this iteration so numbers cannot repeat
    picked_balls = [0] * 70
    drawing = []

    ball_one = random.randint(1,70)
    picked_balls[ ball_one-1 ] = 1

    ball_two = random.randint(1,70)
    while(picked_balls[ ball_two-1 ] == 1):
        ball_two = random.randint(1,70)
    
    picked_balls[ ball_two-1 ] = 1

    ball_three = random.randint(1,70)
    while(picked_balls[ ball_three-1 ] == 1):
        ball_three = random.randint(1,70)
    
    picked_balls[ ball_three-1 ] = 1

    ball_four = random.randint(1,70)
    while(picked_balls[ ball_four-1 ] == 1):
        ball_four = random.randint(1,70)
    
    picked_balls[ ball_four-1 ] = 1

    ball_five = random.randint(1,70)
    while(picked_balls[ ball_five-1 ] == 1):
        ball_five = random.randint(1,70)
    
    picked_balls[ ball_five-1 ] = 1

    # Mega Ball is independent of the other 5 numbers
    mega_ball = random.randint(1,25)

    drawing.append(ball_one)
    drawing.append(ball_two)
    drawing.append(ball_three)
    drawing.append(ball_four)
    drawing.append(ball_five)
    drawing.sort()
    drawing.append(mega_ball)

    return drawing

# See https://valottery.com/GamesAndMore/Megamillions/
def calculateWinnings(drawing, tickets):
    winnings = 0
    for ticket in tickets:
        white_matches = 0
        mb_matches = 0
        if ticket[0] == drawing[0]:
            white_matches = white_matches + 1
        if ticket[1] == drawing[1]:
            white_matches = white_matches + 1
        if ticket[2] == drawing[2]:
            white_matches = white_matches + 1
        if ticket[3] == drawing[3]:
            white_matches = white_matches + 1
        if ticket[4] == drawing[4]:
            white_matches = white_matches + 1

        if ticket[5] == drawing[5]:
            mb_matches = mb_matches + 1

        if ( white_matches > 3 or mb_matches > 0):
            #print('You Won Something!')
            
            if (mb_matches == 1):
                if (white_matches == 0):
                    winnings = winnings + 2
                if (white_matches == 1):
                    winnings = winnings + 4
                if (white_matches == 2):
                    winnings = winnings + 10
                if (white_matches == 3):
                    winnings = winnings + 200
                if (white_matches == 4):
                    winnings = winnings + 10000
                if (white_matches == 5):
                    winnings = winnings + JACKPOT
            else:
                if (white_matches == 3):
                    winnings = winnings + 10
                if (white_matches == 4):
                    winnings = winnings + 500
                if (white_matches == 5):
                    winnings = winnings + 1000000

    return winnings

def purchaseLotteryTickets():
    ticket = []
    tickets = []
    for x in range(0, num_tickets):
        ticket = drawMegaMillionNumbersAtRandom()
        tickets.append(ticket)

    return tickets

# Print what was drawn by the house and the tickets you 'bought'
def printNumbers(mega_milly_drawing, tickets):
    print('House Draws:')
    print(
        str(mega_milly_drawing[0]) + ", " 
        + str(mega_milly_drawing[1]) + ", " 
        + str(mega_milly_drawing[2]) + ", " 
        + str(mega_milly_drawing[3]) + ", " 
        + str(mega_milly_drawing[4]) 
        + " Mega Ball: " 
        + str(mega_milly_drawing[5])
    )
    
    print('')
    print('')
    print('Your Tickets:')

    for ticket in tickets:
        print(
            str(ticket[0]) + ", " 
            + str(ticket[1]) + ", " 
            + str(ticket[2]) + ", " 
            + str(ticket[3]) + ", " 
            + str(ticket[4]) 
            + " Mega Ball: " 
            + str(ticket[5])
        )

# Simulate a bunch of drawings and see why the lottery is a mega rip-off
def draw():
    
    num_games_played = 0
    money_spent = 0
    money_won = 0
    total_time = 0

    while True:
        time_start = time.time()

        mega_milly_drawing = drawMegaMillionNumbersAtRandom()

        tickets = purchaseLotteryTickets()

        winnings = calculateWinnings(mega_milly_drawing, tickets)

        num_games_played = num_games_played + 1
        money_spent = money_spent + (num_tickets*2)

        time_end = time.time()
        total_time = total_time + (time_end-time_start)

        if (winnings > 0):
            printNumbers(mega_milly_drawing, tickets)
            print("\r\n   Winning Amount $" + str(winnings) + "\r\n\r\n")

            money_won = money_won + winnings

            print("Total Games Played: " + str(num_games_played))
            print("Total Time: " + str(total_time) + " sec")
            print("Avg Games Per Sec: " + str(round((num_games_played/total_time),0)))
            print("Total Money Spent: $" + str(money_spent))
            print("Total Money Won: $" + str(money_won))

        if (winnings >= JACKPOT or (money_won > money_spent)):
            break

# Run the lottery simulation.  Good luck.  You *WILL* need it...
draw()