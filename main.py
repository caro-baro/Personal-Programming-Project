## Personal Programming Project - Carolina 
import random

fund = 1000
deck = ['🂡', '🂱', '🃁', '🃑',
        '🂢', '🂲', '🃂', '🃒',
        '🂣', '🂳', '🃃', '🃓',
        '🂤', '🂴', '🃄', '🃔',
        '🂥', '🂵', '🃅', '🃕',
        '🂦', '🂶', '🃆', '🃖', 
        '🂧', '🂷', '🃇', '🃗', 
        '🂨', '🂸', '🃈', '🃘',
        '🂩', '🂹', '🃉', '🃙',
        '🂪', '🂺', '🃊', '🃚',
        '🂫', '🂻', '🃋', '🃛',
        '🂬', '🂼', '🃌', '🃜',
        '🂭', '🂽', '🃍', '🃝',
        '🂮', '🂾', '🃎', '🃞']

deck_values =  {'🂡':11, '🂱':11, '🃁':11, '🃑':11,
        '🂢':2, '🂲':2, '🃂':2, '🃒':2,
        '🂣':3, '🂳':3, '🃃':3, '🃓':3,
        '🂤':4, '🂴':4, '🃄':4, '🃔':4,
        '🂥':5, '🂵':5, '🃅':5, '🃕':5,
        '🂦':6, '🂶':6, '🃆':6, '🃖':6, 
        '🂧':7, '🂷':7, '🃇':7, '🃗':7, 
        '🂨':8, '🂸':8, '🃈':8, '🃘':8,
        '🂩':9, '🂹':9, '🃉':9, '🃙':9,
        '🂪':10, '🂺':10, '🃊':10, '🃚':10,
        '🂫':10, '🂻':10, '🃋':10, '🃛':10,
        '🂬':10, '🂼':10, '🃌':10, '🃜':10,
        '🂭':10, '🂽':10, '🃍':10, '🃝':10,
        '🂮':10, '🂾':10, '🃎':10, '🃞':10}

random.shuffle(deck)

ucard1 = deck[0]
ucard2 = deck[1]
dcard1= deck[2]       
user_hand = [ucard1, ucard2]
dealer_hand = [dcard1]
newcard = deck[random.randrange(len(deck))]
game_over = False

def hello_to_user():
  print("hello. we are playing blackjack.")

def place_bets(fund):
  print(f"you have {fund}$ remaining.")
  bet = int(input("Place your bets:"))

def show_initial_cards(user_hand,dealer_hand):
  print(f"user: {user_hand}")
  print(f"dealer: {dealer_hand}🂠")
  
def ask_choice():
    choice = input("hit or stand?")
    choice = choice.lower()
    return choice

def user_new_card(user_hand):
    user_hand.append(deck[-1])
    deck.pop
    return user_hand


def dealer_new_card(dealer_hand):
    dealer_hand.append(deck[-1]) 
    deck.pop
    return dealer_hand



def gen_new_card(choice):
    if choice == "hit" or choice == "h":
      return "h"
    if choice == "stand" or choice == "s":
      return "s"


def calc_utotal(user_hand):
    utotal = 0
    x = 0
    for i in range(len(user_hand)):
       utotal += deck_values[user_hand[x]]
       x +=1
    return utotal

def calc_dtotal(dealer_hand):
    dtotal = 0
    x = 0
    for i in range(len(dealer_hand)):
       dtotal += deck_values[dealer_hand[x]]
       x +=1
    return dtotal
        

def check_if_over_21(utotal,dtotal):
    if utotal > 21:
        game_over = True
        user_wins = False
    elif dtotal > 21:
        game_over = True
        user_wins = False
    else:
        game_over = False
        user_wins = False
    
    return game_over, user_wins


def check_if_closer_21(utotal, dtotal):
    u = 21- utotal
    d = 21 - dtotal
    if u < d:
        user_wins = True
    elif u > d:
        user_wins = False
    return user_wins

def show_cards(new_user, new_dealer):
   print(new_user)
   print(new_dealer)

def check_winner(utotal,dtotal):
   game_over, user_wins = check_if_over_21(utotal,dtotal)
   if game_over == False:
      game_over, user_wins = check_if_closer_21(utotal,dtotal)
   return game_over, user_wins


if __name__ == "__main__":
    user_hand = [ucard1, ucard2]
    dealer_hand = [dcard1]
    hello_to_user()
    place_bets(fund)
    show_initial_cards(user_hand,dealer_hand)    
        
    while game_over == False:
        choice = ask_choice()
        hors = gen_new_card(choice)
        if hors == "h": 
            user_new_card(user_hand)
            show_cards(user_hand, dealer_hand)
            utotal = calc_utotal(user_hand)
            dtotal = calc_dtotal(dealer_hand)
        elif hors == "s":
            dtotal = calc_dtotal(dealer_hand)
            while dtotal <= 17:
                dtotal = calc_dtotal(dealer_hand)
                dealer_new_card(dealer_hand)
            show_cards(user_hand, dealer_hand)
            utotal = calc_utotal(user_hand)
        game_over, user_wins = check_winner(utotal,dtotal)
        




        
    print("game_over.")
    if user_wins == True:
      print("User wins.")
    else:
      print("Dealer wins.")
