## Personal Programming Project - Carolina 
from random import randint
fund = 1000
deck = ['4hearts', '6diamonds', '7spades', '2clover', '3hearts', '8spades', '9clover']
user_hand = []
dealer_hand = []
ucard1 = randint(1,10)
ucard2 = randint(1,10)
dcard1= randint(1,10)
newcard = randint(1,10)


def hello_to_user():
    print("Hello, we are playing\nBlackjack.")
    
def place_bets(bet):
    print(f"You have: ${fund}")
    bet = int(input("Place your bets:\n"))
    return bet

def deal_cards():
    user_hand.append(ucard1)
    user_hand.append(ucard2)
    dealer_hand.append(dcard1)
    return user_hand, dealer_hand

  
def show_cards(user_hand,dealer_hand):
    print(f"user cards:{ucard1},{ucard2}")
    print(f"dealer cards:{dcard1}")
  
def ask_choice():
    choice = input("Hit or Stand?")
    choice = choice.lower()
    return choice

def user_new_card(user_hand,dealer_hand):
    user_hand.append(newcard)
    return user_hand

def dealer_new_card(user_hand,dealer_hand):
    dealer_hand.append(newcard) 
    print(dealer_hand)
    return dealer_hand
    

def gen_new_card(user_hand,dealer_hand):
    if choice == "hit":
      user_new_card(user_hand,dealer_hand)
    elif choice == "stand":
      dealer_new_card(user_hand,dealer_hand)





if __name__ == "__main__":
    hello_to_user()
    place_bets(fund)
    show_cards(user_hand,dealer_hand)
    choice = ask_choice()
    gen_new_card(user_hand,dealer_hand)
