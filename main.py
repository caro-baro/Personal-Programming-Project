## Personal Programming Project - Carolina 
from random import randint
fund = 1000
hearts = ['aceofhearts', '2ofhearts', '3ofhearts', '4ofhearts', '5ofhearts', '6ofhearts', '7ofhearts', '8ofhearts', 
          '9ofhearts', '10ofhearts' 'jackofhearts', 'queenofhearts', 'kingofhearts']
spades = ['aceofspades', '2ofspades', '3ofspades', '4ofspades', '5ofspades', '6ofspades', '7ofspades', '8ofspades', 
          '9ofspades', '10ofspades' 'jackofspades', 'queenofspades', 'kingofspades']
clover = ['aceofclover', '2ofclover', '3ofclover', '4ofclover', '5ofclover', '6ofclover', '7ofclover', '8ofclover', 
          '9ofclover', '10ofclover' 'jackofclover', 'queenofclover', 'kingofclover']
user_hand = []
dealer_hand = []
ucard1 = randint(1,10)
ucard2 = randint(1,10)
dcard1= randint(1,10)
newcard = randint(1,10)
game_over = False

user_hand.append(ucard1)
user_hand.append(ucard2)
dealer_hand.append(dcard1)


def hello_to_user():
    print("Hello, we are playing\nBlackjack.")
    
def place_bets(bet):
    print(f"You have: ${fund}")
    bet = int(input("Place your bets:\n"))
    return bet


  
def show_cards(user_hand,dealer_hand):
    print(f"user cards:{user_hand}")
    print(f"dealer cards:{dealer_hand}")
  
def ask_choice():
    choice = input("Hit or Stand?")
    choice = choice.lower()
    return choice

def user_new_card(user_hand):
    user_hand.append(newcard)
    return user_hand

def dealer_new_card(dealer_hand):
    dealer_hand.append(newcard) 
    return dealer_hand
    

def gen_new_card(choice):
    if choice == "hit":
      user_new_card(user_hand)
      return user_hand
    elif choice == "stand":
      dealer_new_card(dealer_hand)
      return dealer_hand

def check_if_over_21(utotal,dtotal):
    if utotal > 21:
        print("dealer wins.")
        game_over = True
    elif dtotal > 21:
        print("user wins.")
        game_over = True
    else:
        game_over = False
    
    return game_over, utotal, dtotal

def check_if_closer_21(utotal, dtotal):
    u = 21- utotal
    d = 21 - dtotal
    if u < d:
        user_wins = True
    elif u > d:
        user_wins = False
    return user_wins


if __name__ == "__main__":
    hello_to_user()
    place_bets(fund)
    while game_over == False:
        show_cards(user_hand,dealer_hand)
        choice = ask_choice()
        gen_new_card(choice)
        show_cards(user_hand,dealer_hand)
        utotal = sum(user_hand)
        dtotal = sum(dealer_hand)
        check_if_over_21(utotal,dtotal)
      #  check_if_closer_21(utotal,dtotal)

        